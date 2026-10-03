"""Generated from Smithy shape ``com.amazonaws.backup#CryoControllerUserManager``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_backup._auth._signers
import capo_backup._auth._sigv4
from capo_backup._auth._identity import Credentials
from capo_backup._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_backup._auth._zapros_handler import AuthMiddleware
from capo_backup._pagination import resolve_path as _resolve_path
from capo_backup._services._aws_config import aws_config
from capo_backup._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_backup.types.access_point_arn
    import capo_backup.types.access_point_metadata_map
    import capo_backup.types.access_point_name
    import capo_backup.types.access_point_policy
    import capo_backup.types.account_id
    import capo_backup.types.aggregation_period
    import capo_backup.types.arn
    import capo_backup.types.associate_backup_vault_mpa_approval_team_input
    import capo_backup.types.backup_job
    import capo_backup.types.backup_job_state
    import capo_backup.types.backup_job_status
    import capo_backup.types.backup_options
    import capo_backup.types.backup_plan_input
    import capo_backup.types.backup_plan_templates_list_member
    import capo_backup.types.backup_plans_list_member
    import capo_backup.types.backup_selection
    import capo_backup.types.backup_selections_list_member
    import capo_backup.types.backup_vault_events
    import capo_backup.types.backup_vault_list_member
    import capo_backup.types.backup_vault_name
    import capo_backup.types.boolean
    import capo_backup.types.boolean2
    import capo_backup.types.cancel_legal_hold_input
    import capo_backup.types.cancel_legal_hold_output
    import capo_backup.types.copy_job
    import capo_backup.types.copy_job_state
    import capo_backup.types.copy_job_status
    import capo_backup.types.create_backup_access_point_request
    import capo_backup.types.create_backup_access_point_response
    import capo_backup.types.create_backup_plan_input
    import capo_backup.types.create_backup_plan_output
    import capo_backup.types.create_backup_selection_input
    import capo_backup.types.create_backup_selection_output
    import capo_backup.types.create_backup_vault_input
    import capo_backup.types.create_backup_vault_output
    import capo_backup.types.create_framework_input
    import capo_backup.types.create_framework_output
    import capo_backup.types.create_legal_hold_input
    import capo_backup.types.create_legal_hold_output
    import capo_backup.types.create_logically_air_gapped_backup_vault_input
    import capo_backup.types.create_logically_air_gapped_backup_vault_output
    import capo_backup.types.create_report_plan_input
    import capo_backup.types.create_report_plan_output
    import capo_backup.types.create_restore_access_backup_vault_input
    import capo_backup.types.create_restore_access_backup_vault_output
    import capo_backup.types.create_restore_testing_plan_input
    import capo_backup.types.create_restore_testing_plan_output
    import capo_backup.types.create_restore_testing_selection_input
    import capo_backup.types.create_restore_testing_selection_output
    import capo_backup.types.create_tiering_configuration_input
    import capo_backup.types.create_tiering_configuration_output
    import capo_backup.types.creator_request_id
    import capo_backup.types.delete_backup_access_point_input
    import capo_backup.types.delete_backup_plan_input
    import capo_backup.types.delete_backup_plan_output
    import capo_backup.types.delete_backup_selection_input
    import capo_backup.types.delete_backup_vault_access_policy_input
    import capo_backup.types.delete_backup_vault_input
    import capo_backup.types.delete_backup_vault_lock_configuration_input
    import capo_backup.types.delete_backup_vault_notifications_input
    import capo_backup.types.delete_framework_input
    import capo_backup.types.delete_recovery_point_input
    import capo_backup.types.delete_report_plan_input
    import capo_backup.types.delete_restore_testing_plan_input
    import capo_backup.types.delete_restore_testing_selection_input
    import capo_backup.types.delete_tiering_configuration_input
    import capo_backup.types.delete_tiering_configuration_output
    import capo_backup.types.describe_backup_access_point_input
    import capo_backup.types.describe_backup_access_point_response
    import capo_backup.types.describe_backup_job_input
    import capo_backup.types.describe_backup_job_output
    import capo_backup.types.describe_backup_vault_input
    import capo_backup.types.describe_backup_vault_output
    import capo_backup.types.describe_copy_job_input
    import capo_backup.types.describe_copy_job_output
    import capo_backup.types.describe_framework_input
    import capo_backup.types.describe_framework_output
    import capo_backup.types.describe_global_settings_input
    import capo_backup.types.describe_global_settings_output
    import capo_backup.types.describe_protected_resource_input
    import capo_backup.types.describe_protected_resource_output
    import capo_backup.types.describe_recovery_point_input
    import capo_backup.types.describe_recovery_point_output
    import capo_backup.types.describe_region_settings_input
    import capo_backup.types.describe_region_settings_output
    import capo_backup.types.describe_report_job_input
    import capo_backup.types.describe_report_job_output
    import capo_backup.types.describe_report_plan_input
    import capo_backup.types.describe_report_plan_output
    import capo_backup.types.describe_restore_job_input
    import capo_backup.types.describe_restore_job_output
    import capo_backup.types.describe_scan_job_input
    import capo_backup.types.describe_scan_job_output
    import capo_backup.types.disassociate_backup_vault_mpa_approval_team_input
    import capo_backup.types.disassociate_recovery_point_from_parent_input
    import capo_backup.types.disassociate_recovery_point_input
    import capo_backup.types.export_backup_plan_template_input
    import capo_backup.types.export_backup_plan_template_output
    import capo_backup.types.framework_controls
    import capo_backup.types.framework_description
    import capo_backup.types.framework_name
    import capo_backup.types.get_backup_plan_from_json_input
    import capo_backup.types.get_backup_plan_from_json_output
    import capo_backup.types.get_backup_plan_from_template_input
    import capo_backup.types.get_backup_plan_from_template_output
    import capo_backup.types.get_backup_plan_input
    import capo_backup.types.get_backup_plan_output
    import capo_backup.types.get_backup_selection_input
    import capo_backup.types.get_backup_selection_output
    import capo_backup.types.get_backup_vault_access_policy_input
    import capo_backup.types.get_backup_vault_access_policy_output
    import capo_backup.types.get_backup_vault_notifications_input
    import capo_backup.types.get_backup_vault_notifications_output
    import capo_backup.types.get_legal_hold_input
    import capo_backup.types.get_legal_hold_output
    import capo_backup.types.get_pitr_malware_scan_results_input
    import capo_backup.types.get_pitr_malware_scan_results_output
    import capo_backup.types.get_recovery_point_index_details_input
    import capo_backup.types.get_recovery_point_index_details_output
    import capo_backup.types.get_recovery_point_restore_metadata_input
    import capo_backup.types.get_recovery_point_restore_metadata_output
    import capo_backup.types.get_restore_job_metadata_input
    import capo_backup.types.get_restore_job_metadata_output
    import capo_backup.types.get_restore_testing_inferred_metadata_input
    import capo_backup.types.get_restore_testing_inferred_metadata_output
    import capo_backup.types.get_restore_testing_plan_input
    import capo_backup.types.get_restore_testing_plan_output
    import capo_backup.types.get_restore_testing_selection_input
    import capo_backup.types.get_restore_testing_selection_output
    import capo_backup.types.get_supported_resource_types_output
    import capo_backup.types.get_tiering_configuration_input
    import capo_backup.types.get_tiering_configuration_output
    import capo_backup.types.global_settings
    import capo_backup.types.iam_policy
    import capo_backup.types.iam_role_arn
    import capo_backup.types.index
    import capo_backup.types.index_status
    import capo_backup.types.indexed_recovery_point
    import capo_backup.types.legal_hold
    import capo_backup.types.lifecycle
    import capo_backup.types.list_access_points_member
    import capo_backup.types.list_backup_access_points_by_recovery_point_request
    import capo_backup.types.list_backup_access_points_by_recovery_point_request_max_results_integer
    import capo_backup.types.list_backup_access_points_by_recovery_point_response
    import capo_backup.types.list_backup_access_points_by_resource_request
    import capo_backup.types.list_backup_access_points_by_resource_request_max_results_integer
    import capo_backup.types.list_backup_access_points_by_resource_response
    import capo_backup.types.list_backup_access_points_request
    import capo_backup.types.list_backup_access_points_request_max_results_integer
    import capo_backup.types.list_backup_access_points_response
    import capo_backup.types.list_backup_job_summaries_input
    import capo_backup.types.list_backup_job_summaries_output
    import capo_backup.types.list_backup_jobs_input
    import capo_backup.types.list_backup_jobs_output
    import capo_backup.types.list_backup_plan_templates_input
    import capo_backup.types.list_backup_plan_templates_output
    import capo_backup.types.list_backup_plan_versions_input
    import capo_backup.types.list_backup_plan_versions_output
    import capo_backup.types.list_backup_plans_input
    import capo_backup.types.list_backup_plans_output
    import capo_backup.types.list_backup_selections_input
    import capo_backup.types.list_backup_selections_output
    import capo_backup.types.list_backup_vaults_input
    import capo_backup.types.list_backup_vaults_output
    import capo_backup.types.list_copy_job_summaries_input
    import capo_backup.types.list_copy_job_summaries_output
    import capo_backup.types.list_copy_jobs_input
    import capo_backup.types.list_copy_jobs_output
    import capo_backup.types.list_frameworks_input
    import capo_backup.types.list_frameworks_output
    import capo_backup.types.list_indexed_recovery_points_input
    import capo_backup.types.list_indexed_recovery_points_output
    import capo_backup.types.list_legal_holds_input
    import capo_backup.types.list_legal_holds_output
    import capo_backup.types.list_protected_resources_by_backup_vault_input
    import capo_backup.types.list_protected_resources_by_backup_vault_output
    import capo_backup.types.list_protected_resources_input
    import capo_backup.types.list_protected_resources_output
    import capo_backup.types.list_recovery_points_by_backup_vault_input
    import capo_backup.types.list_recovery_points_by_backup_vault_output
    import capo_backup.types.list_recovery_points_by_legal_hold_input
    import capo_backup.types.list_recovery_points_by_legal_hold_output
    import capo_backup.types.list_recovery_points_by_resource_input
    import capo_backup.types.list_recovery_points_by_resource_output
    import capo_backup.types.list_report_jobs_input
    import capo_backup.types.list_report_jobs_output
    import capo_backup.types.list_report_plans_input
    import capo_backup.types.list_report_plans_output
    import capo_backup.types.list_restore_access_backup_vaults_input
    import capo_backup.types.list_restore_access_backup_vaults_output
    import capo_backup.types.list_restore_job_summaries_input
    import capo_backup.types.list_restore_job_summaries_output
    import capo_backup.types.list_restore_jobs_by_protected_resource_input
    import capo_backup.types.list_restore_jobs_by_protected_resource_output
    import capo_backup.types.list_restore_jobs_input
    import capo_backup.types.list_restore_jobs_output
    import capo_backup.types.list_restore_testing_plans_input
    import capo_backup.types.list_restore_testing_plans_input_max_results_integer
    import capo_backup.types.list_restore_testing_plans_output
    import capo_backup.types.list_restore_testing_selections_input
    import capo_backup.types.list_restore_testing_selections_input_max_results_integer
    import capo_backup.types.list_restore_testing_selections_output
    import capo_backup.types.list_scan_job_summaries_input
    import capo_backup.types.list_scan_job_summaries_output
    import capo_backup.types.list_scan_jobs_input
    import capo_backup.types.list_scan_jobs_input_max_results_integer
    import capo_backup.types.list_scan_jobs_output
    import capo_backup.types.list_tags_input
    import capo_backup.types.list_tags_output
    import capo_backup.types.list_tiering_configurations_input
    import capo_backup.types.list_tiering_configurations_output
    import capo_backup.types.long
    import capo_backup.types.malware_scanner
    import capo_backup.types.max_framework_inputs
    import capo_backup.types.max_results
    import capo_backup.types.max_scheduled_runs_preview
    import capo_backup.types.message_category
    import capo_backup.types.metadata
    import capo_backup.types.protected_resource
    import capo_backup.types.put_backup_vault_access_policy_input
    import capo_backup.types.put_backup_vault_lock_configuration_input
    import capo_backup.types.put_backup_vault_notifications_input
    import capo_backup.types.put_restore_validation_result_input
    import capo_backup.types.recovery_point_arn
    import capo_backup.types.recovery_point_by_backup_vault
    import capo_backup.types.recovery_point_by_resource
    import capo_backup.types.recovery_point_member
    import capo_backup.types.recovery_point_selection
    import capo_backup.types.report_delivery_channel
    import capo_backup.types.report_job_id
    import capo_backup.types.report_plan_description
    import capo_backup.types.report_plan_name
    import capo_backup.types.report_setting
    import capo_backup.types.requester_comment
    import capo_backup.types.resource_arn
    import capo_backup.types.resource_type
    import capo_backup.types.resource_type_management_preference
    import capo_backup.types.resource_type_opt_in_preference
    import capo_backup.types.restore_access_backup_vault_list_member
    import capo_backup.types.restore_job_id
    import capo_backup.types.restore_job_state
    import capo_backup.types.restore_job_status
    import capo_backup.types.restore_jobs_list_member
    import capo_backup.types.restore_testing_plan_for_create
    import capo_backup.types.restore_testing_plan_for_list
    import capo_backup.types.restore_testing_plan_for_update
    import capo_backup.types.restore_testing_selection_for_create
    import capo_backup.types.restore_testing_selection_for_list
    import capo_backup.types.restore_testing_selection_for_update
    import capo_backup.types.restore_validation_status
    import capo_backup.types.revoke_restore_access_backup_vault_input
    import capo_backup.types.scan_job
    import capo_backup.types.scan_job_status
    import capo_backup.types.scan_job_summary
    import capo_backup.types.scan_mode
    import capo_backup.types.scan_resource_type
    import capo_backup.types.scan_result_status
    import capo_backup.types.scan_state
    import capo_backup.types.sensitive_string_map
    import capo_backup.types.start_backup_job_input
    import capo_backup.types.start_backup_job_output
    import capo_backup.types.start_copy_job_input
    import capo_backup.types.start_copy_job_output
    import capo_backup.types.start_report_job_input
    import capo_backup.types.start_report_job_output
    import capo_backup.types.start_restore_job_input
    import capo_backup.types.start_restore_job_output
    import capo_backup.types.start_scan_job_input
    import capo_backup.types.start_scan_job_output
    import capo_backup.types.stop_backup_job_input
    import capo_backup.types.string
    import capo_backup.types.string_map
    import capo_backup.types.tag_key_list
    import capo_backup.types.tag_map
    import capo_backup.types.tag_resource_input
    import capo_backup.types.tags
    import capo_backup.types.tiering_configuration_input_for_create
    import capo_backup.types.tiering_configuration_input_for_update
    import capo_backup.types.tiering_configuration_name
    import capo_backup.types.tiering_configurations_list_member
    import capo_backup.types.timestamp
    import capo_backup.types.untag_resource_input
    import capo_backup.types.update_backup_plan_input
    import capo_backup.types.update_backup_plan_output
    import capo_backup.types.update_framework_input
    import capo_backup.types.update_framework_output
    import capo_backup.types.update_global_settings_input
    import capo_backup.types.update_recovery_point_index_settings_input
    import capo_backup.types.update_recovery_point_index_settings_output
    import capo_backup.types.update_recovery_point_lifecycle_input
    import capo_backup.types.update_recovery_point_lifecycle_output
    import capo_backup.types.update_region_settings_input
    import capo_backup.types.update_report_plan_input
    import capo_backup.types.update_report_plan_output
    import capo_backup.types.update_restore_testing_plan_input
    import capo_backup.types.update_restore_testing_plan_output
    import capo_backup.types.update_restore_testing_selection_input
    import capo_backup.types.update_restore_testing_selection_output
    import capo_backup.types.update_tiering_configuration_input
    import capo_backup.types.update_tiering_configuration_output
    import capo_backup.types.vault_type
    import capo_backup.types.window_minutes


class BackupClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BackupClient:
    """A client for the ``Backup`` service.

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
        self._config = BackupClientConfig(
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
        self, config_overrides: Optional[BackupClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BackupClientConfig = config_overrides or {}
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

    def associate_backup_vault_mpa_approval_team(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        mpa_approval_team_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        requester_comment: Optional[
            "capo_backup.types.requester_comment.RequesterComment"
        ] = None,
    ) -> None:
        """<p>Associates an MPA approval team with a backup vault.</p>

        Args:
            backup_vault_name: <p>The name of the backup vault to associate with the MPA approval team.</p>
            mpa_approval_team_arn: <p>The Amazon Resource Name (ARN) of the MPA approval team to associate with the backup vault.</p>
            requester_comment: <p>A comment provided by the requester explaining the association request.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.associate_backup_vault_mpa_approval_team_input.AssociateBackupVaultMpaApprovalTeamInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.associate_backup_vault_mpa_approval_team

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.associate_backup_vault_mpa_approval_team.associate_backup_vault_mpa_approval_team(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.associate_backup_vault_mpa_approval_team_input.AssociateBackupVaultMpaApprovalTeamInput = {
            "backup_vault_name": backup_vault_name,
            "mpa_approval_team_arn": mpa_approval_team_arn,
        }
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_legal_hold(
        self,
        legal_hold_id: "capo_backup.types.string.string",
        cancel_description: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        retain_record_in_days: Optional["capo_backup.types.long.Long"] = None,
    ) -> "capo_backup.types.cancel_legal_hold_output.CancelLegalHoldOutput":
        """<p>Removes the specified legal hold on a recovery point. This action can only be performed by a user with sufficient permissions.</p>

        Args:
            legal_hold_id: <p>The ID of the legal hold.</p>
            cancel_description: <p>A string the describes the reason for removing the legal hold.</p>
            retain_record_in_days: <p>The integer amount, in days, after which to remove legal hold.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>Backup is already performing an action on this recovery point. It can't perform the action you requested until the first action finishes. Try again later.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.cancel_legal_hold_input.CancelLegalHoldInput]",
        ) -> OperationResponse[
            "capo_backup.types.cancel_legal_hold_output.CancelLegalHoldOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.cancel_legal_hold

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.cancel_legal_hold.cancel_legal_hold(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.cancel_legal_hold_input.CancelLegalHoldInput = {
            "legal_hold_id": legal_hold_id,
            "cancel_description": cancel_description,
        }
        if retain_record_in_days is not None:
            input_["retain_record_in_days"] = retain_record_in_days

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backup_access_point(
        self,
        name: "capo_backup.types.access_point_name.AccessPointName",
        recovery_point_arn: "capo_backup.types.recovery_point_arn.RecoveryPointArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        access_point_metadata: Optional[
            "capo_backup.types.access_point_metadata_map.AccessPointMetadataMap"
        ] = None,
        access_point_policy: Optional[
            "capo_backup.types.access_point_policy.AccessPointPolicy"
        ] = None,
        tags: Optional["capo_backup.types.tag_map.TagMap"] = None,
    ) -> "capo_backup.types.create_backup_access_point_response.CreateBackupAccessPointResponse":
        """<p>Creates a backup access point for an Amazon S3 recovery point. A backup access point provides on-demand, read-only access to the backup data in a recovery point through an Amazon S3 access point, without initiating a restore.</p> <p>While a backup access point is active for a recovery point, Backup pauses lifecycle transitions and blocks deletion of that recovery point.</p>

        Args:
            access_point_metadata: <p>Metadata for the backup access point. For continuous (point-in-time) recovery points, you must include an <code>AccessPointInTime</code> timestamp (in format <code>2021-11-27T03:30:27Z</code>). The access point provides access to the content present in the backup at that specific time. You can specify any time within the continuous backup's retention period, up to the latest restorable time. For snapshot recovery points, do not include <code>AccessPointInTime</code>.</p>
            access_point_policy: <p>An optional resource-based policy, in JSON format, to apply to the underlying Amazon S3 access point. The policy controls how backup data can be accessed through the access point. If you do not specify a policy, access is governed by the caller's IAM permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html">Configuring IAM policies for using access points</a> in the <i>Amazon S3 User Guide</i>.</p>
            name: <p>The name of the backup access point. This name is shared with the Amazon S3 access point namespace. It must be unique within your account and Region and cannot conflict with an existing Amazon S3 access point. For more information about access point naming, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.html">Access points naming rules, restrictions, and limitations</a> in the <i>Amazon S3 User Guide</i>.</p>
            recovery_point_arn: <p>The Amazon Resource Name (ARN) of the recovery point for which to create the backup access point. The recovery point must be an Amazon S3 recovery point in the <code>AVAILABLE</code>, <code>STOPPED</code>, or <code>COMPLETED</code> state.</p>
            tags: <p>The tags to assign to the backup access point.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_backup_access_point_request.CreateBackupAccessPointRequest]",
        ) -> OperationResponse[
            "capo_backup.types.create_backup_access_point_response.CreateBackupAccessPointResponse"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_backup_access_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_backup_access_point.create_backup_access_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_backup_access_point_request.CreateBackupAccessPointRequest = {
            "name": name,
            "recovery_point_arn": recovery_point_arn,
        }
        if access_point_metadata is not None:
            input_["access_point_metadata"] = access_point_metadata
        if access_point_policy is not None:
            input_["access_point_policy"] = access_point_policy
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backup_plan(
        self,
        backup_plan: "capo_backup.types.backup_plan_input.BackupPlanInput",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_plan_tags: Optional["capo_backup.types.tags.Tags"] = None,
        creator_request_id: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.create_backup_plan_output.CreateBackupPlanOutput":
        """<p>Creates a backup plan using a backup plan name and backup rules. A backup plan is a document that contains information that Backup uses to schedule tasks that create recovery points for resources.</p> <p>If you call <code>CreateBackupPlan</code> with a plan that already exists, you receive an <code>AlreadyExistsException</code> exception.</p>

        Args:
            backup_plan: <p>The body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>
            backup_plan_tags: <p>The tags to assign to the backup plan.</p>
            creator_request_id: <p>Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a <code>CreatorRequestId</code> that matches an existing backup plan, that plan is returned. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_backup_plan_input.CreateBackupPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_backup_plan_output.CreateBackupPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_backup_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_backup_plan.create_backup_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_backup_plan_input.CreateBackupPlanInput = {
            "backup_plan": backup_plan
        }
        if backup_plan_tags is not None:
            input_["backup_plan_tags"] = backup_plan_tags
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backup_selection(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        backup_selection: "capo_backup.types.backup_selection.BackupSelection",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        creator_request_id: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.create_backup_selection_output.CreateBackupSelectionOutput":
        """<p>Creates a JSON document that specifies a set of resources to assign to a backup plan. For examples, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-json">Assigning resources programmatically</a>. </p>

        Args:
            backup_plan_id: <p>The ID of the backup plan.</p>
            backup_selection: <p>The body of a request to assign a set of resources to a backup plan.</p>
            creator_request_id: <p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_backup_selection_input.CreateBackupSelectionInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_backup_selection_output.CreateBackupSelectionOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_backup_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_backup_selection.create_backup_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_backup_selection_input.CreateBackupSelectionInput = {
            "backup_plan_id": backup_plan_id,
            "backup_selection": backup_selection,
        }
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_tags: Optional["capo_backup.types.tags.Tags"] = None,
        encryption_key_arn: Optional["capo_backup.types.arn.ARN"] = None,
        creator_request_id: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.create_backup_vault_output.CreateBackupVaultOutput":
        """<p>Creates a logical container where backups are stored. A <code>CreateBackupVault</code> request includes a name, optionally one or more resource tags, an encryption key, and a request ID.</p> <note> <p>Do not include sensitive data, such as passport numbers, in the name of a backup vault.</p> </note>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of letters, numbers, and hyphens.</p>
            backup_vault_tags: <p>The tags to assign to the backup vault.</p>
            encryption_key_arn: <p>The server-side encryption key that is used to protect your backups; for example, <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p>
            creator_request_id: <p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_backup_vault_input.CreateBackupVaultInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_backup_vault_output.CreateBackupVaultOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_backup_vault.create_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_backup_vault_input.CreateBackupVaultInput = {
            "backup_vault_name": backup_vault_name
        }
        if backup_vault_tags is not None:
            input_["backup_vault_tags"] = backup_vault_tags
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_framework(
        self,
        framework_name: "capo_backup.types.framework_name.FrameworkName",
        framework_controls: "capo_backup.types.framework_controls.FrameworkControls",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        framework_description: Optional[
            "capo_backup.types.framework_description.FrameworkDescription"
        ] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
        framework_tags: Optional["capo_backup.types.string_map.stringMap"] = None,
    ) -> "capo_backup.types.create_framework_output.CreateFrameworkOutput":
        """<p>Creates a framework with one or more controls. A framework is a collection of controls that you can use to evaluate your backup practices. By using pre-built customizable controls to define your policies, you can evaluate whether your backup practices comply with your policies and which resources are not yet in compliance.</p>

        Args:
            framework_name: <p>The unique name of the framework. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>
            framework_description: <p>An optional description of the framework with a maximum of 1,024 characters.</p>
            framework_controls: <p>The controls that make up the framework. Each control in the list has a name, input parameters, and scope.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>CreateFrameworkInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>
            framework_tags: <p>The tags to assign to the framework.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_framework_input.CreateFrameworkInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_framework_output.CreateFrameworkOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_framework

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_framework.create_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_framework_input.CreateFrameworkInput = {
            "framework_name": framework_name,
            "framework_controls": framework_controls,
        }
        if framework_description is not None:
            input_["framework_description"] = framework_description
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if framework_tags is not None:
            input_["framework_tags"] = framework_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_legal_hold(
        self,
        title: "capo_backup.types.string.string",
        description: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
        recovery_point_selection: Optional[
            "capo_backup.types.recovery_point_selection.RecoveryPointSelection"
        ] = None,
        tags: Optional["capo_backup.types.tags.Tags"] = None,
    ) -> "capo_backup.types.create_legal_hold_output.CreateLegalHoldOutput":
        """<p>Creates a legal hold on a recovery point (backup). A legal hold is a restraint on altering or deleting a backup until an authorized user cancels the legal hold. Any actions to delete or disassociate a recovery point will fail with an error if one or more active legal holds are on the recovery point.</p>

        Args:
            title: <p>The title of the legal hold.</p>
            description: <p>The description of the legal hold.</p>
            idempotency_token: <p>This is a user-chosen string used to distinguish between otherwise identical calls. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>
            recovery_point_selection: <p>The criteria to assign a set of resources, such as resource types or backup vaults.</p>
            tags: <p>Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_legal_hold_input.CreateLegalHoldInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_legal_hold_output.CreateLegalHoldOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_legal_hold

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_legal_hold.create_legal_hold(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_legal_hold_input.CreateLegalHoldInput = {
            "title": title,
            "description": description,
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if recovery_point_selection is not None:
            input_["recovery_point_selection"] = recovery_point_selection
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_logically_air_gapped_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        min_retention_days: "capo_backup.types.long.Long",
        max_retention_days: "capo_backup.types.long.Long",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_tags: Optional["capo_backup.types.tags.Tags"] = None,
        creator_request_id: Optional["capo_backup.types.string.string"] = None,
        encryption_key_arn: Optional["capo_backup.types.arn.ARN"] = None,
    ) -> "capo_backup.types.create_logically_air_gapped_backup_vault_output.CreateLogicallyAirGappedBackupVaultOutput":
        """<p>Creates a logical container to where backups may be copied.</p> <p>This request includes a name, the Region, the maximum number of retention days, the minimum number of retention days, and optionally can include tags and a creator request ID.</p> <note> <p>Do not include sensitive data, such as passport numbers, in the name of a backup vault.</p> </note>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Logically air-gapped backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>
            backup_vault_tags: <p>The tags to assign to the vault.</p>
            creator_request_id: <p>The ID of the creation request.</p> <p>This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>
            min_retention_days: <p>This setting specifies the minimum retention period that the vault retains its recovery points.</p> <p>The minimum value accepted is 7 days.</p>
            max_retention_days: <p>The maximum retention period that the vault retains its recovery points.</p>
            encryption_key_arn: <p>The ARN of the customer-managed KMS key to use for encrypting the logically air-gapped backup vault. If not specified, the vault will be encrypted with an Amazon Web Services-owned key managed by Amazon Web Services Backup.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_logically_air_gapped_backup_vault_input.CreateLogicallyAirGappedBackupVaultInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_logically_air_gapped_backup_vault_output.CreateLogicallyAirGappedBackupVaultOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_logically_air_gapped_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_logically_air_gapped_backup_vault.create_logically_air_gapped_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_logically_air_gapped_backup_vault_input.CreateLogicallyAirGappedBackupVaultInput = {
            "backup_vault_name": backup_vault_name,
            "min_retention_days": min_retention_days,
            "max_retention_days": max_retention_days,
        }
        if backup_vault_tags is not None:
            input_["backup_vault_tags"] = backup_vault_tags
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_report_plan(
        self,
        report_plan_name: "capo_backup.types.report_plan_name.ReportPlanName",
        report_delivery_channel: "capo_backup.types.report_delivery_channel.ReportDeliveryChannel",
        report_setting: "capo_backup.types.report_setting.ReportSetting",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        report_plan_description: Optional[
            "capo_backup.types.report_plan_description.ReportPlanDescription"
        ] = None,
        report_plan_tags: Optional["capo_backup.types.string_map.stringMap"] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.create_report_plan_output.CreateReportPlanOutput":
        """<p>Creates a report plan. A report plan is a document that contains information about the contents of the report and where Backup will deliver it.</p> <p>If you call <code>CreateReportPlan</code> with a plan that already exists, you receive an <code>AlreadyExistsException</code> exception.</p>

        Args:
            report_plan_name: <p>The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>
            report_plan_description: <p>An optional description of the report plan with a maximum of 1,024 characters.</p>
            report_delivery_channel: <p>A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</p>
            report_setting: <p>Identifies the report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT </code> </p> <p>If the report template is <code>RESOURCE_COMPLIANCE_REPORT</code> or <code>CONTROL_COMPLIANCE_REPORT</code>, this API resource also describes the report coverage by Amazon Web Services Regions and frameworks.</p>
            report_plan_tags: <p>The tags to assign to the report plan.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>CreateReportPlanInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_report_plan_input.CreateReportPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_report_plan_output.CreateReportPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_report_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_report_plan.create_report_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_report_plan_input.CreateReportPlanInput = {
            "report_plan_name": report_plan_name,
            "report_delivery_channel": report_delivery_channel,
            "report_setting": report_setting,
        }
        if report_plan_description is not None:
            input_["report_plan_description"] = report_plan_description
        if report_plan_tags is not None:
            input_["report_plan_tags"] = report_plan_tags
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_restore_access_backup_vault(
        self,
        source_backup_vault_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_name: Optional[
            "capo_backup.types.backup_vault_name.BackupVaultName"
        ] = None,
        backup_vault_tags: Optional["capo_backup.types.tags.Tags"] = None,
        creator_request_id: Optional["capo_backup.types.string.string"] = None,
        requester_comment: Optional[
            "capo_backup.types.requester_comment.RequesterComment"
        ] = None,
    ) -> "capo_backup.types.create_restore_access_backup_vault_output.CreateRestoreAccessBackupVaultOutput":
        """<p>Creates a restore access backup vault that provides temporary access to recovery points in a logically air-gapped backup vault, subject to MPA approval.</p>

        Args:
            source_backup_vault_arn: <p>The ARN of the source backup vault containing the recovery points to which temporary access is requested.</p>
            backup_vault_name: <p>The name of the backup vault to associate with an MPA approval team.</p>
            backup_vault_tags: <p>Optional tags to assign to the restore access backup vault.</p>
            creator_request_id: <p>A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.</p>
            requester_comment: <p>A comment explaining the reason for requesting restore access to the backup vault.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_restore_access_backup_vault_input.CreateRestoreAccessBackupVaultInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_restore_access_backup_vault_output.CreateRestoreAccessBackupVaultOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_restore_access_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_restore_access_backup_vault.create_restore_access_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_restore_access_backup_vault_input.CreateRestoreAccessBackupVaultInput = {
            "source_backup_vault_arn": source_backup_vault_arn
        }
        if backup_vault_name is not None:
            input_["backup_vault_name"] = backup_vault_name
        if backup_vault_tags is not None:
            input_["backup_vault_tags"] = backup_vault_tags
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_restore_testing_plan(
        self,
        restore_testing_plan: "capo_backup.types.restore_testing_plan_for_create.RestoreTestingPlanForCreate",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        creator_request_id: Optional[str] = None,
        tags: Optional[
            "capo_backup.types.sensitive_string_map.SensitiveStringMap"
        ] = None,
    ) -> "capo_backup.types.create_restore_testing_plan_output.CreateRestoreTestingPlanOutput":
        """<p>Creates a restore testing plan.</p> <p>The first of two steps to create a restore testing plan. After this request is successful, finish the procedure using CreateRestoreTestingSelection.</p>

        Args:
            creator_request_id: <p>This is a unique string that identifies the request and allows failed requests to be retriedwithout the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>
            restore_testing_plan: <p>A restore testing plan must contain a unique <code>RestoreTestingPlanName</code> string you create and must contain a <code>ScheduleExpression</code> cron. You may optionally include a <code>StartWindowHours</code> integer and a <code>CreatorRequestId</code> string.</p> <p>The <code>RestoreTestingPlanName</code> is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>
            tags: <p>The tags to assign to the restore testing plan.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_restore_testing_plan_input.CreateRestoreTestingPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_restore_testing_plan_output.CreateRestoreTestingPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_restore_testing_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_restore_testing_plan.create_restore_testing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_restore_testing_plan_input.CreateRestoreTestingPlanInput = {
            "restore_testing_plan": restore_testing_plan
        }
        if creator_request_id is not None:
            input_["creator_request_id"] = creator_request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_restore_testing_selection(
        self,
        restore_testing_plan_name: str,
        restore_testing_selection: "capo_backup.types.restore_testing_selection_for_create.RestoreTestingSelectionForCreate",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        creator_request_id: Optional[str] = None,
    ) -> "capo_backup.types.create_restore_testing_selection_output.CreateRestoreTestingSelectionOutput":
        """<p>This request can be sent after CreateRestoreTestingPlan request returns successfully. This is the second part of creating a resource testing plan, and it must be completed sequentially.</p> <p>This consists of <code>RestoreTestingSelectionName</code>, <code>ProtectedResourceType</code>, and one of the following:</p> <ul> <li> <p> <code>ProtectedResourceArns</code> </p> </li> <li> <p> <code>ProtectedResourceConditions</code> </p> </li> </ul> <p>Each protected resource type can have one single value.</p> <p>A restore testing selection can include a wildcard value ("*") for <code>ProtectedResourceArns</code> along with <code>ProtectedResourceConditions</code>. Alternatively, you can include up to 30 specific protected resource ARNs in <code>ProtectedResourceArns</code>.</p> <p>Cannot select by both protected resource types AND specific ARNs. Request will fail if both are included.</p>

        Args:
            creator_request_id: <p>This is an optional unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>
            restore_testing_plan_name: <p>Input the restore testing plan name that was returned from the related CreateRestoreTestingPlan request.</p>
            restore_testing_selection: <p>This consists of <code>RestoreTestingSelectionName</code>, <code>ProtectedResourceType</code>, and one of the following:</p> <ul> <li> <p> <code>ProtectedResourceArns</code> </p> </li> <li> <p> <code>ProtectedResourceConditions</code> </p> </li> </ul> <p>Each protected resource type can have one single value.</p> <p>A restore testing selection can include a wildcard value ("*") for <code>ProtectedResourceArns</code> along with <code>ProtectedResourceConditions</code>. Alternatively, you can include up to 30 specific protected resource ARNs in <code>ProtectedResourceArns</code>.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_restore_testing_selection_input.CreateRestoreTestingSelectionInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_restore_testing_selection_output.CreateRestoreTestingSelectionOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_restore_testing_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_restore_testing_selection.create_restore_testing_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_restore_testing_selection_input.CreateRestoreTestingSelectionInput = {
            "restore_testing_plan_name": restore_testing_plan_name,
            "restore_testing_selection": restore_testing_selection,
        }
        if creator_request_id is not None:
            input_["creator_request_id"] = creator_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tiering_configuration(
        self,
        tiering_configuration: "capo_backup.types.tiering_configuration_input_for_create.TieringConfigurationInputForCreate",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        tiering_configuration_tags: Optional["capo_backup.types.tags.Tags"] = None,
        creator_request_id: Optional[
            "capo_backup.types.creator_request_id.CreatorRequestId"
        ] = None,
    ) -> "capo_backup.types.create_tiering_configuration_output.CreateTieringConfigurationOutput":
        """<p>Creates a tiering configuration.</p> <p>A tiering configuration enables automatic movement of backup data to a lower-cost storage tier based on the age of backed-up objects in the backup vault.</p> <p>Each vault can only have one vault-specific tiering configuration, in addition to any global configuration that applies to all vaults.</p>

        Args:
            tiering_configuration: <p>A tiering configuration must contain a unique <code>TieringConfigurationName</code> string you create and must contain a <code>BackupVaultName</code> and <code>ResourceSelection</code>. You may optionally include a <code>CreatorRequestId</code> string.</p> <p>The <code>TieringConfigurationName</code> is a unique string that is the name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>
            tiering_configuration_tags: <p>The tags to assign to the tiering configuration.</p>
            creator_request_id: <p>This is a unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.create_tiering_configuration_input.CreateTieringConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup.types.create_tiering_configuration_output.CreateTieringConfigurationOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.create_tiering_configuration

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.create_tiering_configuration.create_tiering_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.create_tiering_configuration_input.CreateTieringConfigurationInput = {
            "tiering_configuration": tiering_configuration
        }
        if tiering_configuration_tags is not None:
            input_["tiering_configuration_tags"] = tiering_configuration_tags
        if creator_request_id is None:
            creator_request_id = str(uuid.uuid4())
        input_["creator_request_id"] = creator_request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_access_point(
        self,
        access_point_arn: "capo_backup.types.access_point_arn.AccessPointArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes a backup access point. This deletes the underlying Amazon S3 access point and, if no other backup access points remain for the recovery point, resumes lifecycle transitions for that recovery point.</p> <p>Always delete backup access points using this operation rather than deleting the underlying Amazon S3 access point directly.</p>

        Args:
            access_point_arn: <p>The Amazon Resource Name (ARN) of the backup access point to delete.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_access_point_input.DeleteBackupAccessPointInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_access_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_access_point.delete_backup_access_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_access_point_input.DeleteBackupAccessPointInput = {
            "access_point_arn": access_point_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_plan(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.delete_backup_plan_output.DeleteBackupPlanOutput":
        """<p>Deletes a backup plan. A backup plan can only be deleted after all associated selections of resources have been deleted. Deleting a backup plan deletes the current version of a backup plan. Previous versions, if any, will still exist.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_plan_input.DeleteBackupPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.delete_backup_plan_output.DeleteBackupPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_plan.delete_backup_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_plan_input.DeleteBackupPlanInput = {
            "backup_plan_id": backup_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_selection(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        selection_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource selection associated with a backup plan that is specified by the <code>SelectionId</code>.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>
            selection_id: <p>Uniquely identifies the body of a request to assign a set of resources to a backup plan.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_selection_input.DeleteBackupSelectionInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_selection.delete_backup_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_selection_input.DeleteBackupSelectionInput = {
            "backup_plan_id": backup_plan_id,
            "selection_id": selection_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the backup vault identified by its name. A vault can be deleted only if it is empty.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_vault_input.DeleteBackupVaultInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_vault.delete_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_vault_input.DeleteBackupVaultInput = {
            "backup_vault_name": backup_vault_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_vault_access_policy(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the policy document that manages permissions on a backup vault.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_vault_access_policy_input.DeleteBackupVaultAccessPolicyInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_vault_access_policy

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_vault_access_policy.delete_backup_vault_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_vault_access_policy_input.DeleteBackupVaultAccessPolicyInput = {
            "backup_vault_name": backup_vault_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_vault_lock_configuration(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes Backup Vault Lock from a backup vault specified by a backup vault name.</p> <p>If the Vault Lock configuration is immutable, then you cannot delete Vault Lock using API operations, and you will receive an <code>InvalidRequestException</code> if you attempt to do so. For more information, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html">Vault Lock</a> in the <i>Backup Developer Guide</i>.</p>

        Args:
            backup_vault_name: <p>The name of the backup vault from which to delete Backup Vault Lock.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_vault_lock_configuration_input.DeleteBackupVaultLockConfigurationInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_vault_lock_configuration

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_vault_lock_configuration.delete_backup_vault_lock_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_vault_lock_configuration_input.DeleteBackupVaultLockConfigurationInput = {
            "backup_vault_name": backup_vault_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup_vault_notifications(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes event notifications for the specified backup vault.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_backup_vault_notifications_input.DeleteBackupVaultNotificationsInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_backup_vault_notifications

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_backup_vault_notifications.delete_backup_vault_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_backup_vault_notifications_input.DeleteBackupVaultNotificationsInput = {
            "backup_vault_name": backup_vault_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_framework(
        self,
        framework_name: "capo_backup.types.framework_name.FrameworkName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the framework specified by a framework name.</p>

        Args:
            framework_name: <p>The unique name of a framework.</p>

        Raises:
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_framework_input.DeleteFrameworkInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_framework

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_framework.delete_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_framework_input.DeleteFrameworkInput = {
            "framework_name": framework_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recovery_point(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the recovery point specified by a recovery point ID.</p> <p>If the recovery point ID belongs to a continuous backup, calling this endpoint deletes the existing continuous backup and stops future continuous backup.</p> <p>When an IAM role's permissions are insufficient to call this API, the service sends back an HTTP 200 response with an empty HTTP body, but the recovery point is not deleted. Instead, it enters an <code>EXPIRED</code> state.</p> <p> <code>EXPIRED</code> recovery points can be deleted with this API once the IAM role has the <code>iam:CreateServiceLinkedRole</code> action. To learn more about adding this role, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/deleting-backups.html#deleting-backups-troubleshooting"> Troubleshooting manual deletions</a>.</p> <p>If the user or role is deleted or the permission within the role is removed, the deletion will not be successful and will enter an <code>EXPIRED</code> state.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>Backup is already performing an action on this recovery point. It can't perform the action you requested until the first action finishes. Try again later.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_recovery_point_input.DeleteRecoveryPointInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_recovery_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_recovery_point.delete_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_recovery_point_input.DeleteRecoveryPointInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_report_plan(
        self,
        report_plan_name: "capo_backup.types.report_plan_name.ReportPlanName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the report plan specified by a report plan name.</p>

        Args:
            report_plan_name: <p>The unique name of a report plan.</p>

        Raises:
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_report_plan_input.DeleteReportPlanInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_report_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_report_plan.delete_report_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_report_plan_input.DeleteReportPlanInput = {
            "report_plan_name": report_plan_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_restore_testing_plan(
        self,
        restore_testing_plan_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>This request deletes the specified restore testing plan.</p> <p>Deletion can only successfully occur if all associated restore testing selections are deleted first.</p>

        Args:
            restore_testing_plan_name: <p>Required unique name of the restore testing plan you wish to delete.</p>

        Raises:
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_restore_testing_plan_input.DeleteRestoreTestingPlanInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_restore_testing_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_restore_testing_plan.delete_restore_testing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_restore_testing_plan_input.DeleteRestoreTestingPlanInput = {
            "restore_testing_plan_name": restore_testing_plan_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_restore_testing_selection(
        self,
        restore_testing_plan_name: str,
        restore_testing_selection_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Input the Restore Testing Plan name and Restore Testing Selection name.</p> <p>All testing selections associated with a restore testing plan must be deleted before the restore testing plan can be deleted.</p>

        Args:
            restore_testing_plan_name: <p>Required unique name of the restore testing plan that contains the restore testing selection you wish to delete.</p>
            restore_testing_selection_name: <p>Required unique name of the restore testing selection you wish to delete.</p>

        Raises:
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_restore_testing_selection_input.DeleteRestoreTestingSelectionInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.delete_restore_testing_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_restore_testing_selection.delete_restore_testing_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_restore_testing_selection_input.DeleteRestoreTestingSelectionInput = {
            "restore_testing_plan_name": restore_testing_plan_name,
            "restore_testing_selection_name": restore_testing_selection_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tiering_configuration(
        self,
        tiering_configuration_name: "capo_backup.types.tiering_configuration_name.TieringConfigurationName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.delete_tiering_configuration_output.DeleteTieringConfigurationOutput":
        """<p>Deletes the tiering configuration specified by a tiering configuration name.</p>

        Args:
            tiering_configuration_name: <p>The unique name of a tiering configuration.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.delete_tiering_configuration_input.DeleteTieringConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup.types.delete_tiering_configuration_output.DeleteTieringConfigurationOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.delete_tiering_configuration

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.delete_tiering_configuration.delete_tiering_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.delete_tiering_configuration_input.DeleteTieringConfigurationInput = {
            "tiering_configuration_name": tiering_configuration_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_backup_access_point(
        self,
        access_point_arn: "capo_backup.types.access_point_arn.AccessPointArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_backup_access_point_response.DescribeBackupAccessPointResponse":
        """<p>Returns metadata about a backup access point, including its status and the details of the underlying Amazon S3 access point.</p> <p>After a backup access point reaches the <code>AVAILABLE</code> status, use this operation to retrieve the Amazon S3 access point ARN and alias that you need to read the backup data.</p>

        Args:
            access_point_arn: <p>The Amazon Resource Name (ARN) of the backup access point to describe.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_backup_access_point_input.DescribeBackupAccessPointInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_backup_access_point_response.DescribeBackupAccessPointResponse"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_backup_access_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_backup_access_point.describe_backup_access_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_backup_access_point_input.DescribeBackupAccessPointInput = {
            "access_point_arn": access_point_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_backup_job(
        self,
        backup_job_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_backup_job_output.DescribeBackupJobOutput":
        """<p>Returns backup job details for the specified <code>BackupJobId</code>.</p>

        Args:
            backup_job_id: <p>Uniquely identifies a request to Backup to back up a resource.</p>

        Raises:
            capo_backup.errors.dependency_failure_exception.DependencyFailureException: <p>A dependent Amazon Web Services service or resource returned an error to the Backup service, and the action cannot be completed.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_backup_job_input.DescribeBackupJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_backup_job_output.DescribeBackupJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_backup_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_backup_job.describe_backup_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_backup_job_input.DescribeBackupJobInput = {
            "backup_job_id": backup_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.describe_backup_vault_output.DescribeBackupVaultOutput":
        """<p>Returns metadata about a backup vault specified by its name.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            backup_vault_account_id: <p>The account ID of the specified backup vault.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_backup_vault_input.DescribeBackupVaultInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_backup_vault_output.DescribeBackupVaultOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_backup_vault.describe_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_backup_vault_input.DescribeBackupVaultInput = {
            "backup_vault_name": backup_vault_name
        }
        if backup_vault_account_id is not None:
            input_["backup_vault_account_id"] = backup_vault_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_copy_job(
        self,
        copy_job_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_copy_job_output.DescribeCopyJobOutput":
        """<p>Returns metadata associated with creating a copy of a resource.</p>

        Args:
            copy_job_id: <p>Uniquely identifies a copy job.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_copy_job_input.DescribeCopyJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_copy_job_output.DescribeCopyJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_copy_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_copy_job.describe_copy_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_copy_job_input.DescribeCopyJobInput = {
            "copy_job_id": copy_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_framework(
        self,
        framework_name: "capo_backup.types.framework_name.FrameworkName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_framework_output.DescribeFrameworkOutput":
        """<p>Returns the framework details for the specified <code>FrameworkName</code>.</p>

        Args:
            framework_name: <p>The unique name of a framework.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_framework_input.DescribeFrameworkInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_framework_output.DescribeFrameworkOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_framework

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_framework.describe_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_framework_input.DescribeFrameworkInput = {
            "framework_name": framework_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_global_settings(
        self, *, config_overrides: Optional[BackupClientConfig] = None
    ) -> (
        "capo_backup.types.describe_global_settings_output.DescribeGlobalSettingsOutput"
    ):
        """<p>Describes whether the Amazon Web Services account has enabled different cross-account management options, including cross-account backup, multi-party approval, and delegated administrator. Returns an error if the account is not a member of an Organizations organization. Example: <code>describe-global-settings --region us-west-2</code> </p>

        Raises:
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_global_settings_input.DescribeGlobalSettingsInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_global_settings_output.DescribeGlobalSettingsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_global_settings

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_global_settings.describe_global_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_global_settings_input.DescribeGlobalSettingsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_protected_resource(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_protected_resource_output.DescribeProtectedResourceOutput":
        """<p>Returns information about a saved resource, including the last time it was backed up, its Amazon Resource Name (ARN), and the Amazon Web Services service type of the saved resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_protected_resource_input.DescribeProtectedResourceInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_protected_resource_output.DescribeProtectedResourceOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_protected_resource

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_protected_resource.describe_protected_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_protected_resource_input.DescribeProtectedResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_recovery_point(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[
            "capo_backup.types.account_id.AccountId"
        ] = None,
    ) -> "capo_backup.types.describe_recovery_point_output.DescribeRecoveryPointOutput":
        """<p>Returns metadata associated with a recovery point, including ID, status, encryption, and lifecycle.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>
            backup_vault_account_id: <p>The account ID of the specified backup vault.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_recovery_point_input.DescribeRecoveryPointInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_recovery_point_output.DescribeRecoveryPointOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_recovery_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_recovery_point.describe_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_recovery_point_input.DescribeRecoveryPointInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }
        if backup_vault_account_id is not None:
            input_["backup_vault_account_id"] = backup_vault_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_region_settings(
        self, *, config_overrides: Optional[BackupClientConfig] = None
    ) -> (
        "capo_backup.types.describe_region_settings_output.DescribeRegionSettingsOutput"
    ):
        """<p>Returns the current service opt-in settings for the Region. If service opt-in is enabled for a service, Backup tries to protect that service's resources in this Region, when the resource is included in an on-demand backup or scheduled backup plan. Otherwise, Backup does not try to protect that service's resources in this Region.</p>

        Raises:
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_region_settings_input.DescribeRegionSettingsInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_region_settings_output.DescribeRegionSettingsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_region_settings

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_region_settings.describe_region_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_region_settings_input.DescribeRegionSettingsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_report_job(
        self,
        report_job_id: "capo_backup.types.report_job_id.ReportJobId",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_report_job_output.DescribeReportJobOutput":
        """<p>Returns the details associated with creating a report as specified by its <code>ReportJobId</code>.</p>

        Args:
            report_job_id: <p>The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited.</p>

        Raises:
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_report_job_input.DescribeReportJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_report_job_output.DescribeReportJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_report_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_report_job.describe_report_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_report_job_input.DescribeReportJobInput = {
            "report_job_id": report_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_report_plan(
        self,
        report_plan_name: "capo_backup.types.report_plan_name.ReportPlanName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_report_plan_output.DescribeReportPlanOutput":
        """<p>Returns a list of all report plans for an Amazon Web Services account and Amazon Web Services Region.</p>

        Args:
            report_plan_name: <p>The unique name of a report plan.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_report_plan_input.DescribeReportPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_report_plan_output.DescribeReportPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_report_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_report_plan.describe_report_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_report_plan_input.DescribeReportPlanInput = {
            "report_plan_name": report_plan_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_restore_job(
        self,
        restore_job_id: "capo_backup.types.restore_job_id.RestoreJobId",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.describe_restore_job_output.DescribeRestoreJobOutput":
        """<p>Returns metadata associated with a restore job that is specified by a job ID.</p>

        Args:
            restore_job_id: <p>Uniquely identifies the job that restores a recovery point.</p>

        Raises:
            capo_backup.errors.dependency_failure_exception.DependencyFailureException: <p>A dependent Amazon Web Services service or resource returned an error to the Backup service, and the action cannot be completed.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_restore_job_input.DescribeRestoreJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_restore_job_output.DescribeRestoreJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_restore_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_restore_job.describe_restore_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_restore_job_input.DescribeRestoreJobInput = {
            "restore_job_id": restore_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scan_job(
        self, scan_job_id: str, *, config_overrides: Optional[BackupClientConfig] = None
    ) -> "capo_backup.types.describe_scan_job_output.DescribeScanJobOutput":
        """<p>Returns scan job details for the specified ScanJobID.</p>

        Args:
            scan_job_id: <p>Uniquely identifies a request to Backup to scan a resource.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.describe_scan_job_input.DescribeScanJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.describe_scan_job_output.DescribeScanJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.describe_scan_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.describe_scan_job.describe_scan_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.describe_scan_job_input.DescribeScanJobInput = {
            "scan_job_id": scan_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_backup_vault_mpa_approval_team(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        requester_comment: Optional[
            "capo_backup.types.requester_comment.RequesterComment"
        ] = None,
    ) -> None:
        """<p>Removes the association between an MPA approval team and a backup vault, disabling the MPA approval workflow for restore operations.</p>

        Args:
            backup_vault_name: <p>The name of the backup vault from which to disassociate the MPA approval team.</p>
            requester_comment: <p>An optional comment explaining the reason for disassociating the MPA approval team from the backup vault.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.disassociate_backup_vault_mpa_approval_team_input.DisassociateBackupVaultMpaApprovalTeamInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.disassociate_backup_vault_mpa_approval_team

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.disassociate_backup_vault_mpa_approval_team.disassociate_backup_vault_mpa_approval_team(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.disassociate_backup_vault_mpa_approval_team_input.DisassociateBackupVaultMpaApprovalTeamInput = {
            "backup_vault_name": backup_vault_name
        }
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_recovery_point(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified continuous backup recovery point from Backup and releases control of that continuous backup to the source service, such as Amazon RDS. The source service will continue to create and retain continuous backups using the lifecycle that you specified in your original backup plan.</p> <p>Does not support snapshot backup recovery points.</p>

        Args:
            backup_vault_name: <p>The unique name of an Backup vault.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an Backup recovery point.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>Backup is already performing an action on this recovery point. It can't perform the action you requested until the first action finishes. Try again later.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.disassociate_recovery_point_input.DisassociateRecoveryPointInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.disassociate_recovery_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.disassociate_recovery_point.disassociate_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.disassociate_recovery_point_input.DisassociateRecoveryPointInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_recovery_point_from_parent(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>This action to a specific child (nested) recovery point removes the relationship between the specified recovery point and its parent (composite) recovery point.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where the child (nested) recovery point is stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            recovery_point_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the child (nested) recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.</code> </p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.disassociate_recovery_point_from_parent_input.DisassociateRecoveryPointFromParentInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.disassociate_recovery_point_from_parent

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.disassociate_recovery_point_from_parent.disassociate_recovery_point_from_parent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.disassociate_recovery_point_from_parent_input.DisassociateRecoveryPointFromParentInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_backup_plan_template(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.export_backup_plan_template_output.ExportBackupPlanTemplateOutput":
        """<p>Returns the backup plan that is specified by the plan ID as a backup template.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.export_backup_plan_template_input.ExportBackupPlanTemplateInput]",
        ) -> OperationResponse[
            "capo_backup.types.export_backup_plan_template_output.ExportBackupPlanTemplateOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.export_backup_plan_template

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.export_backup_plan_template.export_backup_plan_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.export_backup_plan_template_input.ExportBackupPlanTemplateInput = {
            "backup_plan_id": backup_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backup_plan(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        version_id: Optional["capo_backup.types.string.string"] = None,
        max_scheduled_runs_preview: Optional[
            "capo_backup.types.max_scheduled_runs_preview.MaxScheduledRunsPreview"
        ] = None,
    ) -> "capo_backup.types.get_backup_plan_output.GetBackupPlanOutput":
        """<p>Returns <code>BackupPlan</code> details for the specified <code>BackupPlanId</code>. The details are the body of a backup plan in JSON format, in addition to plan metadata.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>
            version_id: <p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>
            max_scheduled_runs_preview: <p>Number of future scheduled backup runs to preview. When set to 0 (default), no scheduled runs preview is included in the response. Valid range is 0-10.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_backup_plan_input.GetBackupPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_backup_plan_output.GetBackupPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_backup_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_backup_plan.get_backup_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_backup_plan_input.GetBackupPlanInput = {
            "backup_plan_id": backup_plan_id
        }
        if version_id is not None:
            input_["version_id"] = version_id
        if max_scheduled_runs_preview is not None:
            input_["max_scheduled_runs_preview"] = max_scheduled_runs_preview

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backup_plan_from_json(
        self,
        backup_plan_template_json: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> (
        "capo_backup.types.get_backup_plan_from_json_output.GetBackupPlanFromJSONOutput"
    ):
        """<p>Returns a valid JSON document specifying a backup plan or an error.</p>

        Args:
            backup_plan_template_json: <p>A customer-supplied backup plan document in JSON format.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_backup_plan_from_json_input.GetBackupPlanFromJSONInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_backup_plan_from_json_output.GetBackupPlanFromJSONOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_backup_plan_from_json

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_backup_plan_from_json.get_backup_plan_from_json(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_backup_plan_from_json_input.GetBackupPlanFromJSONInput = {
            "backup_plan_template_json": backup_plan_template_json
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backup_plan_from_template(
        self,
        backup_plan_template_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_backup_plan_from_template_output.GetBackupPlanFromTemplateOutput":
        """<p>Returns the template specified by its <code>templateId</code> as a backup plan.</p>

        Args:
            backup_plan_template_id: <p>Uniquely identifies a stored backup plan template.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_backup_plan_from_template_input.GetBackupPlanFromTemplateInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_backup_plan_from_template_output.GetBackupPlanFromTemplateOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_backup_plan_from_template

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_backup_plan_from_template.get_backup_plan_from_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_backup_plan_from_template_input.GetBackupPlanFromTemplateInput = {
            "backup_plan_template_id": backup_plan_template_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backup_selection(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        selection_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_backup_selection_output.GetBackupSelectionOutput":
        """<p>Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>
            selection_id: <p>Uniquely identifies the body of a request to assign a set of resources to a backup plan.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_backup_selection_input.GetBackupSelectionInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_backup_selection_output.GetBackupSelectionOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_backup_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_backup_selection.get_backup_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_backup_selection_input.GetBackupSelectionInput = {
            "backup_plan_id": backup_plan_id,
            "selection_id": selection_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backup_vault_access_policy(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_backup_vault_access_policy_output.GetBackupVaultAccessPolicyOutput":
        """<p>Returns the access policy document that is associated with the named backup vault.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_backup_vault_access_policy_input.GetBackupVaultAccessPolicyInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_backup_vault_access_policy_output.GetBackupVaultAccessPolicyOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_backup_vault_access_policy

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_backup_vault_access_policy.get_backup_vault_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_backup_vault_access_policy_input.GetBackupVaultAccessPolicyInput = {
            "backup_vault_name": backup_vault_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backup_vault_notifications(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_backup_vault_notifications_output.GetBackupVaultNotificationsOutput":
        """<p>Returns event notifications for the specified backup vault.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_backup_vault_notifications_input.GetBackupVaultNotificationsInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_backup_vault_notifications_output.GetBackupVaultNotificationsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_backup_vault_notifications

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_backup_vault_notifications.get_backup_vault_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_backup_vault_notifications_input.GetBackupVaultNotificationsInput = {
            "backup_vault_name": backup_vault_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_legal_hold(
        self,
        legal_hold_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_legal_hold_output.GetLegalHoldOutput":
        """<p>This action returns details for a specified legal hold. The details are the body of a legal hold in JSON format, in addition to metadata.</p>

        Args:
            legal_hold_id: <p>The ID of the legal hold.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_legal_hold_input.GetLegalHoldInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_legal_hold_output.GetLegalHoldOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_legal_hold

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_legal_hold.get_legal_hold(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_legal_hold_input.GetLegalHoldInput = {
            "legal_hold_id": legal_hold_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_pitr_malware_scan_results(
        self,
        recovery_point_arn: str,
        backup_vault_name: str,
        scan_end_time: datetime.datetime,
        malware_scanner: "capo_backup.types.malware_scanner.MalwareScanner",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_pitr_malware_scan_results_output.GetPITRMalwareScanResultsOutput":
        """<p>Returns the malware scan results for a specified point in time within a continuous (point-in-time recovery) backup.</p>

        Args:
            recovery_point_arn: <p>An ARN that uniquely identifies the target recovery point for scanning; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            scan_end_time: <p>The point in time within the continuous backup to examine for malware scan results.</p>
            malware_scanner: <p>The scanning engine used for the corresponding scan job. Currently only <code>GUARDDUTY</code> is supported.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_pitr_malware_scan_results_input.GetPITRMalwareScanResultsInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_pitr_malware_scan_results_output.GetPITRMalwareScanResultsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_pitr_malware_scan_results

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_pitr_malware_scan_results.get_pitr_malware_scan_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_pitr_malware_scan_results_input.GetPITRMalwareScanResultsInput = {
            "recovery_point_arn": recovery_point_arn,
            "backup_vault_name": backup_vault_name,
            "scan_end_time": scan_end_time,
            "malware_scanner": malware_scanner,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recovery_point_index_details(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_recovery_point_index_details_output.GetRecoveryPointIndexDetailsOutput":
        """<p>This operation returns the metadata and details specific to the backup index associated with the specified recovery point.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p> <p>Accepted characters include lowercase letters, numbers, and hyphens.</p>
            recovery_point_arn: <p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_recovery_point_index_details_input.GetRecoveryPointIndexDetailsInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_recovery_point_index_details_output.GetRecoveryPointIndexDetailsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_recovery_point_index_details

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_recovery_point_index_details.get_recovery_point_index_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_recovery_point_index_details_input.GetRecoveryPointIndexDetailsInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recovery_point_restore_metadata(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[
            "capo_backup.types.account_id.AccountId"
        ] = None,
    ) -> "capo_backup.types.get_recovery_point_restore_metadata_output.GetRecoveryPointRestoreMetadataOutput":
        """<p>Returns a set of metadata key-value pairs that were used to create the backup.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>
            backup_vault_account_id: <p>The account ID of the specified backup vault.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_recovery_point_restore_metadata_input.GetRecoveryPointRestoreMetadataInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_recovery_point_restore_metadata_output.GetRecoveryPointRestoreMetadataOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_recovery_point_restore_metadata

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_recovery_point_restore_metadata.get_recovery_point_restore_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_recovery_point_restore_metadata_input.GetRecoveryPointRestoreMetadataInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }
        if backup_vault_account_id is not None:
            input_["backup_vault_account_id"] = backup_vault_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_restore_job_metadata(
        self,
        restore_job_id: "capo_backup.types.restore_job_id.RestoreJobId",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> (
        "capo_backup.types.get_restore_job_metadata_output.GetRestoreJobMetadataOutput"
    ):
        """<p>This request returns the metadata for the specified restore job.</p>

        Args:
            restore_job_id: <p>This is a unique identifier of a restore job within Backup.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_restore_job_metadata_input.GetRestoreJobMetadataInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_restore_job_metadata_output.GetRestoreJobMetadataOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_restore_job_metadata

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_restore_job_metadata.get_restore_job_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_restore_job_metadata_input.GetRestoreJobMetadataInput = {
            "restore_job_id": restore_job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_restore_testing_inferred_metadata(
        self,
        backup_vault_name: str,
        recovery_point_arn: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[str] = None,
    ) -> "capo_backup.types.get_restore_testing_inferred_metadata_output.GetRestoreTestingInferredMetadataOutput":
        """<p>This request returns the minimal required set of metadata needed to start a restore job with secure default settings. <code>BackupVaultName</code> and <code>RecoveryPointArn</code> are required parameters. <code>BackupVaultAccountId</code> is an optional parameter.</p>

        Args:
            backup_vault_account_id: <p>The account ID of the specified backup vault.</p>
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web ServicesRegion where they are created. They consist of letters, numbers, and hyphens.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>. </p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_restore_testing_inferred_metadata_input.GetRestoreTestingInferredMetadataInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_restore_testing_inferred_metadata_output.GetRestoreTestingInferredMetadataOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_restore_testing_inferred_metadata

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_restore_testing_inferred_metadata.get_restore_testing_inferred_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_restore_testing_inferred_metadata_input.GetRestoreTestingInferredMetadataInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }
        if backup_vault_account_id is not None:
            input_["backup_vault_account_id"] = backup_vault_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_restore_testing_plan(
        self,
        restore_testing_plan_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> (
        "capo_backup.types.get_restore_testing_plan_output.GetRestoreTestingPlanOutput"
    ):
        """<p>Returns <code>RestoreTestingPlan</code> details for the specified <code>RestoreTestingPlanName</code>. The details are the body of a restore testing plan in JSON format, in addition to plan metadata.</p>

        Args:
            restore_testing_plan_name: <p>Required unique name of the restore testing plan.</p>

        Raises:
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_restore_testing_plan_input.GetRestoreTestingPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_restore_testing_plan_output.GetRestoreTestingPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_restore_testing_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_restore_testing_plan.get_restore_testing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_restore_testing_plan_input.GetRestoreTestingPlanInput = {
            "restore_testing_plan_name": restore_testing_plan_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_restore_testing_selection(
        self,
        restore_testing_plan_name: str,
        restore_testing_selection_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_restore_testing_selection_output.GetRestoreTestingSelectionOutput":
        """<p>Returns RestoreTestingSelection, which displays resources and elements of the restore testing plan.</p>

        Args:
            restore_testing_plan_name: <p>Required unique name of the restore testing plan.</p>
            restore_testing_selection_name: <p>Required unique name of the restore testing selection.</p>

        Raises:
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_restore_testing_selection_input.GetRestoreTestingSelectionInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_restore_testing_selection_output.GetRestoreTestingSelectionOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_restore_testing_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_restore_testing_selection.get_restore_testing_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_restore_testing_selection_input.GetRestoreTestingSelectionInput = {
            "restore_testing_plan_name": restore_testing_plan_name,
            "restore_testing_selection_name": restore_testing_selection_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_supported_resource_types(
        self, *, config_overrides: Optional[BackupClientConfig] = None
    ) -> "capo_backup.types.get_supported_resource_types_output.GetSupportedResourceTypesOutput":
        """<p>Returns the Amazon Web Services resource types supported by Backup.</p>

        Raises:
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_backup.types.get_supported_resource_types_output.GetSupportedResourceTypesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_supported_resource_types

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_supported_resource_types.get_supported_resource_types(
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

    def get_tiering_configuration(
        self,
        tiering_configuration_name: "capo_backup.types.tiering_configuration_name.TieringConfigurationName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.get_tiering_configuration_output.GetTieringConfigurationOutput":
        """<p>Returns <code>TieringConfiguration</code> details for the specified <code>TieringConfigurationName</code>. The details are the body of a tiering configuration in JSON format, in addition to configuration metadata.</p>

        Args:
            tiering_configuration_name: <p>The unique name of a tiering configuration.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.get_tiering_configuration_input.GetTieringConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup.types.get_tiering_configuration_output.GetTieringConfigurationOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.get_tiering_configuration

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.get_tiering_configuration.get_tiering_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.get_tiering_configuration_input.GetTieringConfigurationInput = {
            "tiering_configuration_name": tiering_configuration_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_backup_access_points(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_backup_access_points_request_max_results_integer.ListBackupAccessPointsRequestMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_backup.types.list_backup_access_points_response.ListBackupAccessPointsResponse":
        """<p>Returns a list of the backup access points in your account and Region.</p>

        Args:
            max_results: <p>The maximum number of items to be returned.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_access_points_request.ListBackupAccessPointsRequest]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_access_points_response.ListBackupAccessPointsResponse"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_access_points

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_access_points.list_backup_access_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_access_points_request.ListBackupAccessPointsRequest = {}
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

    def iter_list_backup_access_points(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_backup_access_points_request_max_results_integer.ListBackupAccessPointsRequestMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_backup.types.list_access_points_member.ListAccessPointsMember]":
        _token = next_token
        while True:
            _response = self.list_backup_access_points(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("backup_access_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_access_points_by_recovery_point(
        self,
        recovery_point_arn: "capo_backup.types.recovery_point_arn.RecoveryPointArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_backup_access_points_by_recovery_point_request_max_results_integer.ListBackupAccessPointsByRecoveryPointRequestMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_backup.types.list_backup_access_points_by_recovery_point_response.ListBackupAccessPointsByRecoveryPointResponse":
        """<p>Returns the backup access points associated with the specified recovery point.</p> <p>If you own the recovery point and have shared it with other accounts, the response includes backup access points created by those accounts.</p>

        Args:
            max_results: <p>The maximum number of items to be returned.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            recovery_point_arn: <p>The Amazon Resource Name (ARN) of the recovery point whose backup access points you want to list.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_access_points_by_recovery_point_request.ListBackupAccessPointsByRecoveryPointRequest]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_access_points_by_recovery_point_response.ListBackupAccessPointsByRecoveryPointResponse"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_access_points_by_recovery_point

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_access_points_by_recovery_point.list_backup_access_points_by_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_access_points_by_recovery_point_request.ListBackupAccessPointsByRecoveryPointRequest = {
            "recovery_point_arn": recovery_point_arn
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

    def iter_list_backup_access_points_by_recovery_point(
        self,
        recovery_point_arn: "capo_backup.types.recovery_point_arn.RecoveryPointArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_backup_access_points_by_recovery_point_request_max_results_integer.ListBackupAccessPointsByRecoveryPointRequestMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_backup.types.list_access_points_member.ListAccessPointsMember]":
        _token = next_token
        while True:
            _response = self.list_backup_access_points_by_recovery_point(
                recovery_point_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("backup_access_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_access_points_by_resource(
        self,
        resource_arn: "capo_backup.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_backup_access_points_by_resource_request_max_results_integer.ListBackupAccessPointsByResourceRequestMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_backup.types.list_backup_access_points_by_resource_response.ListBackupAccessPointsByResourceResponse":
        """<p>Returns the backup access points associated with the specified resource, such as an Amazon S3 bucket.</p>

        Args:
            max_results: <p>The maximum number of items to be returned.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose backup access points you want to list.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_access_points_by_resource_request.ListBackupAccessPointsByResourceRequest]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_access_points_by_resource_response.ListBackupAccessPointsByResourceResponse"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_access_points_by_resource

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_access_points_by_resource.list_backup_access_points_by_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_access_points_by_resource_request.ListBackupAccessPointsByResourceRequest = {
            "resource_arn": resource_arn
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

    def iter_list_backup_access_points_by_resource(
        self,
        resource_arn: "capo_backup.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_backup_access_points_by_resource_request_max_results_integer.ListBackupAccessPointsByResourceRequestMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_backup.types.list_access_points_member.ListAccessPointsMember]":
        _token = next_token
        while True:
            _response = self.list_backup_access_points_by_resource(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("backup_access_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_state: Optional["capo_backup.types.backup_job_state.BackupJobState"] = None,
        by_backup_vault_name: Optional[
            "capo_backup.types.backup_vault_name.BackupVaultName"
        ] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        by_complete_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_complete_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_parent_job_id: Optional["capo_backup.types.string.string"] = None,
        by_message_category: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput":
        """<p>Returns a list of existing backup jobs for an authenticated account for the last 30 days. For a longer period of time, consider using these <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">monitoring tools</a>.</p>

        Args:
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>
            by_resource_arn: <p>Returns only backup jobs that match the specified resource Amazon Resource Name (ARN).</p>
            by_state: <p>Returns only backup jobs that are in the specified state.</p> <p> <code>Completed with issues</code> is a status found only in the Backup console. For API, this status refers to jobs with a state of <code>COMPLETED</code> and a <code>MessageCategory</code> with a value other than <code>SUCCESS</code>; that is, the status is completed but comes with a status message.</p> <p>To obtain the job count for <code>Completed with issues</code>, run two GET requests, and subtract the second, smaller number:</p> <p>GET /backup-jobs/?state=COMPLETED</p> <p>GET /backup-jobs/?messageCategory=SUCCESS&state=COMPLETED</p>
            by_backup_vault_name: <p>Returns only backup jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            by_created_before: <p>Returns only backup jobs that were created before the specified date.</p>
            by_created_after: <p>Returns only backup jobs that were created after the specified date.</p>
            by_resource_type: <p>Returns only backup jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>
            by_account_id: <p>The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.</p> <p>If used from an Organizations management account, passing <code>*</code> returns all jobs across the organization.</p>
            by_complete_after: <p>Returns only backup jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_complete_before: <p>Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_parent_job_id: <p>This is a filter to list child (nested) jobs based on parent job ID.</p>
            by_message_category: <p>This is an optional parameter that can be used to filter out jobs with a MessageCategory which matches the value you input.</p> <p>Example strings may include <code>AccessDenied</code>, <code>SUCCESS</code>, <code>AGGREGATE_ALL</code>, and <code>InvalidParameters</code>.</p> <p>View <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> </p> <p>The wildcard () returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_jobs_input.ListBackupJobsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_jobs_output.ListBackupJobsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_jobs

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_jobs.list_backup_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_jobs_input.ListBackupJobsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if by_resource_arn is not None:
            input_["by_resource_arn"] = by_resource_arn
        if by_state is not None:
            input_["by_state"] = by_state
        if by_backup_vault_name is not None:
            input_["by_backup_vault_name"] = by_backup_vault_name
        if by_created_before is not None:
            input_["by_created_before"] = by_created_before
        if by_created_after is not None:
            input_["by_created_after"] = by_created_after
        if by_resource_type is not None:
            input_["by_resource_type"] = by_resource_type
        if by_account_id is not None:
            input_["by_account_id"] = by_account_id
        if by_complete_after is not None:
            input_["by_complete_after"] = by_complete_after
        if by_complete_before is not None:
            input_["by_complete_before"] = by_complete_before
        if by_parent_job_id is not None:
            input_["by_parent_job_id"] = by_parent_job_id
        if by_message_category is not None:
            input_["by_message_category"] = by_message_category

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_backup_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_state: Optional["capo_backup.types.backup_job_state.BackupJobState"] = None,
        by_backup_vault_name: Optional[
            "capo_backup.types.backup_vault_name.BackupVaultName"
        ] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        by_complete_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_complete_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_parent_job_id: Optional["capo_backup.types.string.string"] = None,
        by_message_category: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.backup_job.BackupJob]":
        _token = next_token
        while True:
            _response = self.list_backup_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                by_resource_arn=by_resource_arn,
                by_state=by_state,
                by_backup_vault_name=by_backup_vault_name,
                by_created_before=by_created_before,
                by_created_after=by_created_after,
                by_resource_type=by_resource_type,
                by_account_id=by_account_id,
                by_complete_after=by_complete_after,
                by_complete_before=by_complete_before,
                by_parent_job_id=by_parent_job_id,
                by_message_category=by_message_category,
            )
            _page = _resolve_path(_response, ("backup_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        state: Optional["capo_backup.types.backup_job_status.BackupJobStatus"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        message_category: Optional[
            "capo_backup.types.message_category.MessageCategory"
        ] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_backup_job_summaries_output.ListBackupJobSummariesOutput":
        """<p>This is a request for a summary of backup jobs created or running within the most recent 14 days. You can include parameters AccountID, State, ResourceType, MessageCategory, AggregationPeriod, MaxResults, or NextToken to filter results.</p> <p>This request returns a summary that contains Region, Account, State, ResourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.</p>

        Args:
            account_id: <p>Returns the job count for the specified account.</p> <p>If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestor's account will be returned.</p> <p>Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts from all accounts within the authenticated organization, then returns the sum.</p>
            state: <p>This parameter returns the job count for jobs with the specified state.</p> <p>The the value ANY returns count of all states.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all states and returns the sum.</p> <p> <code>Completed with issues</code> is a status found only in the Backup console. For API, this status refers to jobs with a state of <code>COMPLETED</code> and a <code>MessageCategory</code> with a value other than <code>SUCCESS</code>; that is, the status is completed but comes with a status message. To obtain the job count for <code>Completed with issues</code>, run two GET requests, and subtract the second, smaller number:</p> <p>GET /audit/backup-job-summaries?AggregationPeriod=FOURTEEN_DAYS&State=COMPLETED</p> <p>GET /audit/backup-job-summaries?AggregationPeriod=FOURTEEN_DAYS&MessageCategory=SUCCESS&State=COMPLETED</p>
            resource_type: <p>Returns the job count for the specified resource type. Use request <code>GetSupportedResourceTypes</code> to obtain strings for supported resource types.</p> <p>The the value ANY returns count of all resource types.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all resource types and returns the sum.</p> <p>The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>
            message_category: <p>This parameter returns the job count for the specified message category.</p> <p>Example accepted strings include <code>AccessDenied</code>, <code>Success</code>, and <code>InvalidParameters</code>. See <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of accepted MessageCategory strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>
            aggregation_period: <p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code> - The daily job count for the prior 14 days.</p> </li> <li> <p> <code>SEVEN_DAYS</code> - The aggregated job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code> - The aggregated job count for prior 14 days.</p> </li> </ul>
            max_results: <p>The maximum number of items to be returned.</p> <p>The value is an integer. Range of accepted values is from 1 to 500.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_job_summaries_input.ListBackupJobSummariesInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_job_summaries_output.ListBackupJobSummariesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_job_summaries

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_job_summaries.list_backup_job_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_job_summaries_input.ListBackupJobSummariesInput = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if state is not None:
            input_["state"] = state
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if message_category is not None:
            input_["message_category"] = message_category
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
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

    def iter_list_backup_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        state: Optional["capo_backup.types.backup_job_status.BackupJobStatus"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        message_category: Optional[
            "capo_backup.types.message_category.MessageCategory"
        ] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.list_backup_job_summaries_output.ListBackupJobSummariesOutput]":
        _token = next_token
        while True:
            _response = self.list_backup_job_summaries(
                config_overrides=config_overrides,
                account_id=account_id,
                state=state,
                resource_type=resource_type,
                message_category=message_category,
                aggregation_period=aggregation_period,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_plans(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        include_deleted: Optional["capo_backup.types.boolean.Boolean"] = None,
    ) -> "capo_backup.types.list_backup_plans_output.ListBackupPlansOutput":
        """<p>Lists the active backup plans for the account.</p>

        Args:
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>
            include_deleted: <p>A Boolean value with a default value of <code>FALSE</code> that returns deleted backup plans when set to <code>TRUE</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_plans_input.ListBackupPlansInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_plans_output.ListBackupPlansOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_plans

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_plans.list_backup_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_plans_input.ListBackupPlansInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_deleted is not None:
            input_["include_deleted"] = include_deleted

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_backup_plans(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        include_deleted: Optional["capo_backup.types.boolean.Boolean"] = None,
    ) -> "Iterator[capo_backup.types.backup_plans_list_member.BackupPlansListMember]":
        _token = next_token
        while True:
            _response = self.list_backup_plans(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                include_deleted=include_deleted,
            )
            _page = _resolve_path(_response, ("backup_plans_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_plan_templates(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_backup_plan_templates_output.ListBackupPlanTemplatesOutput":
        """<p>Lists the backup plan templates.</p>

        Args:
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_plan_templates_input.ListBackupPlanTemplatesInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_plan_templates_output.ListBackupPlanTemplatesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_plan_templates

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_plan_templates.list_backup_plan_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_plan_templates_input.ListBackupPlanTemplatesInput = {}
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

    def iter_list_backup_plan_templates(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.backup_plan_templates_list_member.BackupPlanTemplatesListMember]":
        _token = next_token
        while True:
            _response = self.list_backup_plan_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("backup_plan_templates_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_plan_versions(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_backup_plan_versions_output.ListBackupPlanVersionsOutput":
        """<p>Returns version metadata of your backup plans, including Amazon Resource Names (ARNs), backup plan IDs, creation and deletion dates, plan names, and version IDs.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_plan_versions_input.ListBackupPlanVersionsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_plan_versions_output.ListBackupPlanVersionsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_plan_versions

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_plan_versions.list_backup_plan_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_plan_versions_input.ListBackupPlanVersionsInput = {
            "backup_plan_id": backup_plan_id
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

    def iter_list_backup_plan_versions(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.backup_plans_list_member.BackupPlansListMember]":
        _token = next_token
        while True:
            _response = self.list_backup_plan_versions(
                backup_plan_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("backup_plan_versions_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_selections(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_backup_selections_output.ListBackupSelectionsOutput":
        """<p>Returns an array containing metadata of the resources associated with the target backup plan.</p>

        Args:
            backup_plan_id: <p>Uniquely identifies a backup plan.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_selections_input.ListBackupSelectionsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_selections_output.ListBackupSelectionsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_selections

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_selections.list_backup_selections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_selections_input.ListBackupSelectionsInput = {
            "backup_plan_id": backup_plan_id
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

    def iter_list_backup_selections(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.backup_selections_list_member.BackupSelectionsListMember]":
        _token = next_token
        while True:
            _response = self.list_backup_selections(
                backup_plan_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("backup_selections_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_backup_vaults(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_vault_type: Optional["capo_backup.types.vault_type.VaultType"] = None,
        by_shared: Optional["capo_backup.types.boolean2.Boolean2"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_backup_vaults_output.ListBackupVaultsOutput":
        """<p>Returns a list of recovery point storage containers along with information about them.</p>

        Args:
            by_vault_type: <p>This parameter will sort the list of vaults by vault type.</p>
            by_shared: <p>This parameter will sort the list of vaults by shared vaults.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_backup_vaults_input.ListBackupVaultsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_backup_vaults_output.ListBackupVaultsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_backup_vaults

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_backup_vaults.list_backup_vaults(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_backup_vaults_input.ListBackupVaultsInput = {}
        if by_vault_type is not None:
            input_["by_vault_type"] = by_vault_type
        if by_shared is not None:
            input_["by_shared"] = by_shared
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

    def iter_list_backup_vaults(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_vault_type: Optional["capo_backup.types.vault_type.VaultType"] = None,
        by_shared: Optional["capo_backup.types.boolean2.Boolean2"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.backup_vault_list_member.BackupVaultListMember]":
        _token = next_token
        while True:
            _response = self.list_backup_vaults(
                config_overrides=config_overrides,
                by_vault_type=by_vault_type,
                by_shared=by_shared,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("backup_vault_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_copy_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_state: Optional["capo_backup.types.copy_job_state.CopyJobState"] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_destination_vault_arn: Optional["capo_backup.types.string.string"] = None,
        by_account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        by_complete_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_complete_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_parent_job_id: Optional["capo_backup.types.string.string"] = None,
        by_message_category: Optional["capo_backup.types.string.string"] = None,
        by_source_recovery_point_arn: Optional[
            "capo_backup.types.string.string"
        ] = None,
    ) -> "capo_backup.types.list_copy_jobs_output.ListCopyJobsOutput":
        """<p>Returns metadata about your copy jobs.</p>

        Args:
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return MaxResults number of items, NextToken allows you to return more items in your list starting at the location pointed to by the next token. </p>
            max_results: <p>The maximum number of items to be returned.</p>
            by_resource_arn: <p>Returns only copy jobs that match the specified resource Amazon Resource Name (ARN). </p>
            by_state: <p>Returns only copy jobs that are in the specified state.</p>
            by_created_before: <p>Returns only copy jobs that were created before the specified date.</p>
            by_created_after: <p>Returns only copy jobs that were created after the specified date.</p>
            by_resource_type: <p>Returns only backup jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>
            by_destination_vault_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a source backup vault to copy from; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>. </p>
            by_account_id: <p>The account ID to list the jobs from. Returns only copy jobs associated with the specified account ID.</p>
            by_complete_before: <p>Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_complete_after: <p>Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_parent_job_id: <p>This is a filter to list child (nested) jobs based on parent job ID.</p>
            by_message_category: <p>This is an optional parameter that can be used to filter out jobs with a MessageCategory which matches the value you input.</p> <p>Example strings may include <code>AccessDenied</code>, <code>SUCCESS</code>, <code>AGGREGATE_ALL</code>, and <code>INVALIDPARAMETERS</code>.</p> <p>View <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of accepted strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>
            by_source_recovery_point_arn: <p>Filters copy jobs by the specified source recovery point ARN.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_copy_jobs_input.ListCopyJobsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_copy_jobs_output.ListCopyJobsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_copy_jobs

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_copy_jobs.list_copy_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_copy_jobs_input.ListCopyJobsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if by_resource_arn is not None:
            input_["by_resource_arn"] = by_resource_arn
        if by_state is not None:
            input_["by_state"] = by_state
        if by_created_before is not None:
            input_["by_created_before"] = by_created_before
        if by_created_after is not None:
            input_["by_created_after"] = by_created_after
        if by_resource_type is not None:
            input_["by_resource_type"] = by_resource_type
        if by_destination_vault_arn is not None:
            input_["by_destination_vault_arn"] = by_destination_vault_arn
        if by_account_id is not None:
            input_["by_account_id"] = by_account_id
        if by_complete_before is not None:
            input_["by_complete_before"] = by_complete_before
        if by_complete_after is not None:
            input_["by_complete_after"] = by_complete_after
        if by_parent_job_id is not None:
            input_["by_parent_job_id"] = by_parent_job_id
        if by_message_category is not None:
            input_["by_message_category"] = by_message_category
        if by_source_recovery_point_arn is not None:
            input_["by_source_recovery_point_arn"] = by_source_recovery_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_copy_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_state: Optional["capo_backup.types.copy_job_state.CopyJobState"] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_destination_vault_arn: Optional["capo_backup.types.string.string"] = None,
        by_account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        by_complete_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_complete_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_parent_job_id: Optional["capo_backup.types.string.string"] = None,
        by_message_category: Optional["capo_backup.types.string.string"] = None,
        by_source_recovery_point_arn: Optional[
            "capo_backup.types.string.string"
        ] = None,
    ) -> "Iterator[capo_backup.types.copy_job.CopyJob]":
        _token = next_token
        while True:
            _response = self.list_copy_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                by_resource_arn=by_resource_arn,
                by_state=by_state,
                by_created_before=by_created_before,
                by_created_after=by_created_after,
                by_resource_type=by_resource_type,
                by_destination_vault_arn=by_destination_vault_arn,
                by_account_id=by_account_id,
                by_complete_before=by_complete_before,
                by_complete_after=by_complete_after,
                by_parent_job_id=by_parent_job_id,
                by_message_category=by_message_category,
                by_source_recovery_point_arn=by_source_recovery_point_arn,
            )
            _page = _resolve_path(_response, ("copy_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_copy_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        state: Optional["capo_backup.types.copy_job_status.CopyJobStatus"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        message_category: Optional[
            "capo_backup.types.message_category.MessageCategory"
        ] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_copy_job_summaries_output.ListCopyJobSummariesOutput":
        """<p>This request obtains a list of copy jobs created or running within the the most recent 14 days. You can include parameters AccountID, State, ResourceType, MessageCategory, AggregationPeriod, MaxResults, or NextToken to filter results.</p> <p>This request returns a summary that contains Region, Account, State, RestourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.</p>

        Args:
            account_id: <p>Returns the job count for the specified account.</p> <p>If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestor's account will be returned.</p> <p>Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts from all accounts within the authenticated organization, then returns the sum.</p>
            state: <p>This parameter returns the job count for jobs with the specified state.</p> <p>The the value ANY returns count of all states.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all states and returns the sum.</p>
            resource_type: <p>Returns the job count for the specified resource type. Use request <code>GetSupportedResourceTypes</code> to obtain strings for supported resource types.</p> <p>The the value ANY returns count of all resource types.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all resource types and returns the sum.</p> <p>The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>
            message_category: <p>This parameter returns the job count for the specified message category.</p> <p>Example accepted strings include <code>AccessDenied</code>, <code>Success</code>, and <code>InvalidParameters</code>. See <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of accepted MessageCategory strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum.</p>
            aggregation_period: <p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code> - The daily job count for the prior 14 days.</p> </li> <li> <p> <code>SEVEN_DAYS</code> - The aggregated job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code> - The aggregated job count for prior 14 days.</p> </li> </ul>
            max_results: <p>This parameter sets the maximum number of items to be returned.</p> <p>The value is an integer. Range of accepted values is from 1 to 500.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_copy_job_summaries_input.ListCopyJobSummariesInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_copy_job_summaries_output.ListCopyJobSummariesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_copy_job_summaries

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_copy_job_summaries.list_copy_job_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_copy_job_summaries_input.ListCopyJobSummariesInput = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if state is not None:
            input_["state"] = state
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if message_category is not None:
            input_["message_category"] = message_category
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
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

    def iter_list_copy_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        state: Optional["capo_backup.types.copy_job_status.CopyJobStatus"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        message_category: Optional[
            "capo_backup.types.message_category.MessageCategory"
        ] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.list_copy_job_summaries_output.ListCopyJobSummariesOutput]":
        _token = next_token
        while True:
            _response = self.list_copy_job_summaries(
                config_overrides=config_overrides,
                account_id=account_id,
                state=state,
                resource_type=resource_type,
                message_category=message_category,
                aggregation_period=aggregation_period,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_frameworks(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.max_framework_inputs.MaxFrameworkInputs"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_frameworks_output.ListFrameworksOutput":
        """<p>Returns a list of all frameworks for an Amazon Web Services account and Amazon Web Services Region.</p>

        Args:
            max_results: <p>The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_frameworks_input.ListFrameworksInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_frameworks_output.ListFrameworksOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_frameworks

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_frameworks.list_frameworks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_frameworks_input.ListFrameworksInput = {}
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

    def iter_list_frameworks(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.max_framework_inputs.MaxFrameworkInputs"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.list_frameworks_output.ListFrameworksOutput]":
        _token = next_token
        while True:
            _response = self.list_frameworks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_indexed_recovery_points(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        source_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        index_status: Optional["capo_backup.types.index_status.IndexStatus"] = None,
    ) -> "capo_backup.types.list_indexed_recovery_points_output.ListIndexedRecoveryPointsOutput":
        """<p>This operation returns a list of recovery points that have an associated index, belonging to the specified account.</p> <p>Optional parameters you can include are: MaxResults; NextToken; SourceResourceArns; CreatedBefore; CreatedAfter; and ResourceType.</p>

        Args:
            next_token: <p>The next item following a partial list of returned recovery points.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of indexed recovery points, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>
            source_resource_arn: <p>A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.</p>
            created_before: <p>Returns only indexed recovery points that were created before the specified date.</p>
            created_after: <p>Returns only indexed recovery points that were created after the specified date.</p>
            resource_type: <p>Returns a list of indexed recovery points for the specified resource type(s).</p> <p>Accepted values include:</p> <ul> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul>
            index_status: <p>Include this parameter to filter the returned list by the indicated statuses.</p> <p>Accepted values: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_indexed_recovery_points_input.ListIndexedRecoveryPointsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_indexed_recovery_points_output.ListIndexedRecoveryPointsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_indexed_recovery_points

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_indexed_recovery_points.list_indexed_recovery_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_indexed_recovery_points_input.ListIndexedRecoveryPointsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if source_resource_arn is not None:
            input_["source_resource_arn"] = source_resource_arn
        if created_before is not None:
            input_["created_before"] = created_before
        if created_after is not None:
            input_["created_after"] = created_after
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if index_status is not None:
            input_["index_status"] = index_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_indexed_recovery_points(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        source_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        index_status: Optional["capo_backup.types.index_status.IndexStatus"] = None,
    ) -> "Iterator[capo_backup.types.indexed_recovery_point.IndexedRecoveryPoint]":
        _token = next_token
        while True:
            _response = self.list_indexed_recovery_points(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                source_resource_arn=source_resource_arn,
                created_before=created_before,
                created_after=created_after,
                resource_type=resource_type,
                index_status=index_status,
            )
            _page = _resolve_path(_response, ("indexed_recovery_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_legal_holds(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_legal_holds_output.ListLegalHoldsOutput":
        """<p>This action returns metadata about active and previous legal holds.</p>

        Args:
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_legal_holds_input.ListLegalHoldsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_legal_holds_output.ListLegalHoldsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_legal_holds

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_legal_holds.list_legal_holds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_legal_holds_input.ListLegalHoldsInput = {}
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

    def iter_list_legal_holds(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.legal_hold.LegalHold]":
        _token = next_token
        while True:
            _response = self.list_legal_holds(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("legal_holds",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_protected_resources(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_backup.types.list_protected_resources_output.ListProtectedResourcesOutput"
    ):
        """<p>Returns an array of resources with recovery points created by Backup (regardless of the recovery point's <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeRecoveryPoint.html#Backup-DescribeRecoveryPoint-response-Status">status</a>), including the time the resource was saved, an Amazon Resource Name (ARN) of the resource, and a resource type.</p>

        Args:
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_protected_resources_input.ListProtectedResourcesInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_protected_resources_output.ListProtectedResourcesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_protected_resources

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_protected_resources.list_protected_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_protected_resources_input.ListProtectedResourcesInput = {}
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

    def iter_list_protected_resources(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.protected_resource.ProtectedResource]":
        _token = next_token
        while True:
            _response = self.list_protected_resources(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_protected_resources_by_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[
            "capo_backup.types.account_id.AccountId"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_protected_resources_by_backup_vault_output.ListProtectedResourcesByBackupVaultOutput":
        """<p>This request lists the protected resources corresponding to each backup vault.</p>

        Args:
            backup_vault_name: <p>The list of protected resources by backup vault within the vault(s) you specify by name.</p>
            backup_vault_account_id: <p>The list of protected resources by backup vault within the vault(s) you specify by account ID.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_protected_resources_by_backup_vault_input.ListProtectedResourcesByBackupVaultInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_protected_resources_by_backup_vault_output.ListProtectedResourcesByBackupVaultOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_protected_resources_by_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_protected_resources_by_backup_vault.list_protected_resources_by_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_protected_resources_by_backup_vault_input.ListProtectedResourcesByBackupVaultInput = {
            "backup_vault_name": backup_vault_name
        }
        if backup_vault_account_id is not None:
            input_["backup_vault_account_id"] = backup_vault_account_id
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

    def iter_list_protected_resources_by_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[
            "capo_backup.types.account_id.AccountId"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.protected_resource.ProtectedResource]":
        _token = next_token
        while True:
            _response = self.list_protected_resources_by_backup_vault(
                backup_vault_name,
                config_overrides=config_overrides,
                backup_vault_account_id=backup_vault_account_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recovery_points_by_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[
            "capo_backup.types.account_id.AccountId"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_backup_plan_id: Optional["capo_backup.types.string.string"] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_parent_recovery_point_arn: Optional["capo_backup.types.arn.ARN"] = None,
    ) -> "capo_backup.types.list_recovery_points_by_backup_vault_output.ListRecoveryPointsByBackupVaultOutput":
        """<p>Returns detailed information about the recovery points stored in a backup vault.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <note> <p>Backup vault name might not be available when a supported service creates the backup.</p> </note>
            backup_vault_account_id: <p>This parameter will sort the list of recovery points by account ID.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>
            by_resource_arn: <p>Returns only recovery points that match the specified resource Amazon Resource Name (ARN).</p>
            by_resource_type: <p>Returns only recovery points that match the specified resource type(s):</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>
            by_backup_plan_id: <p>Returns only recovery points that match the specified backup plan ID.</p>
            by_created_before: <p>Returns only recovery points that were created before the specified timestamp.</p>
            by_created_after: <p>Returns only recovery points that were created after the specified timestamp.</p>
            by_parent_recovery_point_arn: <p>This returns only recovery points that match the specified parent (composite) recovery point Amazon Resource Name (ARN).</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_recovery_points_by_backup_vault_input.ListRecoveryPointsByBackupVaultInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_recovery_points_by_backup_vault_output.ListRecoveryPointsByBackupVaultOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_recovery_points_by_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_recovery_points_by_backup_vault.list_recovery_points_by_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_recovery_points_by_backup_vault_input.ListRecoveryPointsByBackupVaultInput = {
            "backup_vault_name": backup_vault_name
        }
        if backup_vault_account_id is not None:
            input_["backup_vault_account_id"] = backup_vault_account_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if by_resource_arn is not None:
            input_["by_resource_arn"] = by_resource_arn
        if by_resource_type is not None:
            input_["by_resource_type"] = by_resource_type
        if by_backup_plan_id is not None:
            input_["by_backup_plan_id"] = by_backup_plan_id
        if by_created_before is not None:
            input_["by_created_before"] = by_created_before
        if by_created_after is not None:
            input_["by_created_after"] = by_created_after
        if by_parent_recovery_point_arn is not None:
            input_["by_parent_recovery_point_arn"] = by_parent_recovery_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recovery_points_by_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        backup_vault_account_id: Optional[
            "capo_backup.types.account_id.AccountId"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_resource_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_backup_plan_id: Optional["capo_backup.types.string.string"] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_parent_recovery_point_arn: Optional["capo_backup.types.arn.ARN"] = None,
    ) -> "Iterator[capo_backup.types.recovery_point_by_backup_vault.RecoveryPointByBackupVault]":
        _token = next_token
        while True:
            _response = self.list_recovery_points_by_backup_vault(
                backup_vault_name,
                config_overrides=config_overrides,
                backup_vault_account_id=backup_vault_account_id,
                next_token=_token,
                max_results=max_results,
                by_resource_arn=by_resource_arn,
                by_resource_type=by_resource_type,
                by_backup_plan_id=by_backup_plan_id,
                by_created_before=by_created_before,
                by_created_after=by_created_after,
                by_parent_recovery_point_arn=by_parent_recovery_point_arn,
            )
            _page = _resolve_path(_response, ("recovery_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recovery_points_by_legal_hold(
        self,
        legal_hold_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_recovery_points_by_legal_hold_output.ListRecoveryPointsByLegalHoldOutput":
        """<p>This action returns recovery point ARNs (Amazon Resource Names) of the specified legal hold.</p>

        Args:
            legal_hold_id: <p>The ID of the legal hold.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_recovery_points_by_legal_hold_input.ListRecoveryPointsByLegalHoldInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_recovery_points_by_legal_hold_output.ListRecoveryPointsByLegalHoldOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_recovery_points_by_legal_hold

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_recovery_points_by_legal_hold.list_recovery_points_by_legal_hold(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_recovery_points_by_legal_hold_input.ListRecoveryPointsByLegalHoldInput = {
            "legal_hold_id": legal_hold_id
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

    def iter_list_recovery_points_by_legal_hold(
        self,
        legal_hold_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.recovery_point_member.RecoveryPointMember]":
        _token = next_token
        while True:
            _response = self.list_recovery_points_by_legal_hold(
                legal_hold_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recovery_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recovery_points_by_resource(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        managed_by_aws_backup_only: Optional[
            "capo_backup.types.boolean2.Boolean2"
        ] = None,
    ) -> "capo_backup.types.list_recovery_points_by_resource_output.ListRecoveryPointsByResourceOutput":
        """<p>The information about the recovery points of the type specified by a resource Amazon Resource Name (ARN).</p> <note> <p>For Amazon EFS and Amazon EC2, this action only lists recovery points created by Backup.</p> </note>

        Args:
            resource_arn: <p>An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p> <note> <p>Amazon RDS requires a value of at least 20.</p> </note>
            managed_by_aws_backup_only: <p>This attribute filters recovery points based on ownership.</p> <p>If this is set to <code>TRUE</code>, the response will contain recovery points associated with the selected resources that are managed by Backup.</p> <p>If this is set to <code>FALSE</code>, the response will contain all recovery points associated with the selected resource, except for EBS snapshots copied within the same Region and account.</p> <p>Type: Boolean</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_recovery_points_by_resource_input.ListRecoveryPointsByResourceInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_recovery_points_by_resource_output.ListRecoveryPointsByResourceOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_recovery_points_by_resource

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_recovery_points_by_resource.list_recovery_points_by_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_recovery_points_by_resource_input.ListRecoveryPointsByResourceInput = {
            "resource_arn": resource_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if managed_by_aws_backup_only is not None:
            input_["managed_by_aws_backup_only"] = managed_by_aws_backup_only

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recovery_points_by_resource(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        managed_by_aws_backup_only: Optional[
            "capo_backup.types.boolean2.Boolean2"
        ] = None,
    ) -> (
        "Iterator[capo_backup.types.recovery_point_by_resource.RecoveryPointByResource]"
    ):
        _token = next_token
        while True:
            _response = self.list_recovery_points_by_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                managed_by_aws_backup_only=managed_by_aws_backup_only,
            )
            _page = _resolve_path(_response, ("recovery_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_report_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_report_plan_name: Optional[
            "capo_backup.types.report_plan_name.ReportPlanName"
        ] = None,
        by_creation_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_creation_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_status: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_report_jobs_output.ListReportJobsOutput":
        """<p>Returns details about your report jobs.</p>

        Args:
            by_report_plan_name: <p>Returns only report jobs with the specified report plan name.</p>
            by_creation_before: <p>Returns only report jobs that were created before the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.</p>
            by_creation_after: <p>Returns only report jobs that were created after the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.</p>
            by_status: <p>Returns only report jobs that are in the specified status. The statuses are:</p> <p> <code>CREATED | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_ISSUES</code> </p> <p> Please note that only scanning jobs finish with state completed with issues. For backup jobs this is a console interpretation of a job that finishes in completed state and has a status message.</p>
            max_results: <p>The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_report_jobs_input.ListReportJobsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_report_jobs_output.ListReportJobsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_report_jobs

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_report_jobs.list_report_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_report_jobs_input.ListReportJobsInput = {}
        if by_report_plan_name is not None:
            input_["by_report_plan_name"] = by_report_plan_name
        if by_creation_before is not None:
            input_["by_creation_before"] = by_creation_before
        if by_creation_after is not None:
            input_["by_creation_after"] = by_creation_after
        if by_status is not None:
            input_["by_status"] = by_status
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

    def iter_list_report_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_report_plan_name: Optional[
            "capo_backup.types.report_plan_name.ReportPlanName"
        ] = None,
        by_creation_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_creation_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_status: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.list_report_jobs_output.ListReportJobsOutput]":
        _token = next_token
        while True:
            _response = self.list_report_jobs(
                config_overrides=config_overrides,
                by_report_plan_name=by_report_plan_name,
                by_creation_before=by_creation_before,
                by_creation_after=by_creation_after,
                by_status=by_status,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_report_plans(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_report_plans_output.ListReportPlansOutput":
        """<p>Returns a list of your report plans. For detailed information about a single report plan, use <code>DescribeReportPlan</code>.</p>

        Args:
            max_results: <p>The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_report_plans_input.ListReportPlansInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_report_plans_output.ListReportPlansOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_report_plans

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_report_plans.list_report_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_report_plans_input.ListReportPlansInput = {}
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

    def iter_list_report_plans(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.list_report_plans_output.ListReportPlansOutput]":
        _token = next_token
        while True:
            _response = self.list_report_plans(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_restore_access_backup_vaults(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput":
        """<p>Returns a list of restore access backup vaults associated with a specified backup vault.</p>

        Args:
            backup_vault_name: <p>The name of the backup vault for which to list associated restore access backup vaults.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of items to return in the response.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_restore_access_backup_vaults_input.ListRestoreAccessBackupVaultsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_restore_access_backup_vaults_output.ListRestoreAccessBackupVaultsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_restore_access_backup_vaults

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_restore_access_backup_vaults.list_restore_access_backup_vaults(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_restore_access_backup_vaults_input.ListRestoreAccessBackupVaultsInput = {
            "backup_vault_name": backup_vault_name
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

    def iter_list_restore_access_backup_vaults(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.restore_access_backup_vault_list_member.RestoreAccessBackupVaultListMember]":
        _token = next_token
        while True:
            _response = self.list_restore_access_backup_vaults(
                backup_vault_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("restore_access_backup_vaults",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_restore_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_status: Optional[
            "capo_backup.types.restore_job_status.RestoreJobStatus"
        ] = None,
        by_complete_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_complete_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_restore_testing_plan_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_parent_job_id: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_restore_jobs_output.ListRestoreJobsOutput":
        """<p>Returns a list of jobs that Backup initiated to restore a saved resource, including details about the recovery process.</p>

        Args:
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>
            by_account_id: <p>The account ID to list the jobs from. Returns only restore jobs associated with the specified account ID.</p>
            by_resource_type: <p>Include this parameter to return only restore jobs for the specified resources:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>CloudFormation</code> for CloudFormation</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> for Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> for Amazon Redshift</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> <li> <p> <code>SAP HANA on Amazon EC2</code> for SAP HANA databases on Amazon Elastic Compute Cloud instances</p> </li> <li> <p> <code>Storage Gateway</code> for Storage Gateway</p> </li> <li> <p> <code>Timestream</code> for Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> for VMware virtual machines</p> </li> </ul>
            by_created_before: <p>Returns only restore jobs that were created before the specified date.</p>
            by_created_after: <p>Returns only restore jobs that were created after the specified date.</p>
            by_status: <p>Returns only restore jobs associated with the specified job status.</p>
            by_complete_before: <p>Returns only copy jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_complete_after: <p>Returns only copy jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_restore_testing_plan_arn: <p>This returns only restore testing jobs that match the specified resource Amazon Resource Name (ARN).</p>
            by_parent_job_id: <p>This is a filter to list child (nested) restore jobs based on parent restore job ID.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_restore_jobs_input.ListRestoreJobsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_restore_jobs_output.ListRestoreJobsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_restore_jobs

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_restore_jobs.list_restore_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_restore_jobs_input.ListRestoreJobsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if by_account_id is not None:
            input_["by_account_id"] = by_account_id
        if by_resource_type is not None:
            input_["by_resource_type"] = by_resource_type
        if by_created_before is not None:
            input_["by_created_before"] = by_created_before
        if by_created_after is not None:
            input_["by_created_after"] = by_created_after
        if by_status is not None:
            input_["by_status"] = by_status
        if by_complete_before is not None:
            input_["by_complete_before"] = by_complete_before
        if by_complete_after is not None:
            input_["by_complete_after"] = by_complete_after
        if by_restore_testing_plan_arn is not None:
            input_["by_restore_testing_plan_arn"] = by_restore_testing_plan_arn
        if by_parent_job_id is not None:
            input_["by_parent_job_id"] = by_parent_job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_restore_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        by_account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        by_resource_type: Optional[
            "capo_backup.types.resource_type.ResourceType"
        ] = None,
        by_created_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_created_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_status: Optional[
            "capo_backup.types.restore_job_status.RestoreJobStatus"
        ] = None,
        by_complete_before: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_complete_after: Optional["capo_backup.types.timestamp.timestamp"] = None,
        by_restore_testing_plan_arn: Optional["capo_backup.types.arn.ARN"] = None,
        by_parent_job_id: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.restore_jobs_list_member.RestoreJobsListMember]":
        _token = next_token
        while True:
            _response = self.list_restore_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                by_account_id=by_account_id,
                by_resource_type=by_resource_type,
                by_created_before=by_created_before,
                by_created_after=by_created_after,
                by_status=by_status,
                by_complete_before=by_complete_before,
                by_complete_after=by_complete_after,
                by_restore_testing_plan_arn=by_restore_testing_plan_arn,
                by_parent_job_id=by_parent_job_id,
            )
            _page = _resolve_path(_response, ("restore_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_restore_jobs_by_protected_resource(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_status: Optional[
            "capo_backup.types.restore_job_status.RestoreJobStatus"
        ] = None,
        by_recovery_point_creation_date_after: Optional[
            "capo_backup.types.timestamp.timestamp"
        ] = None,
        by_recovery_point_creation_date_before: Optional[
            "capo_backup.types.timestamp.timestamp"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_restore_jobs_by_protected_resource_output.ListRestoreJobsByProtectedResourceOutput":
        """<p>This returns restore jobs that contain the specified protected resource.</p> <p>You must include <code>ResourceArn</code>. You can optionally include <code>NextToken</code>, <code>ByStatus</code>, <code>MaxResults</code>, <code>ByRecoveryPointCreationDateAfter</code> , and <code>ByRecoveryPointCreationDateBefore</code>.</p>

        Args:
            resource_arn: <p>Returns only restore jobs that match the specified resource Amazon Resource Name (ARN).</p>
            by_status: <p>Returns only restore jobs associated with the specified job status.</p>
            by_recovery_point_creation_date_after: <p>Returns only restore jobs of recovery points that were created after the specified date.</p>
            by_recovery_point_creation_date_before: <p>Returns only restore jobs of recovery points that were created before the specified date.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request ismade to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_restore_jobs_by_protected_resource_input.ListRestoreJobsByProtectedResourceInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_restore_jobs_by_protected_resource_output.ListRestoreJobsByProtectedResourceOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_restore_jobs_by_protected_resource

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_restore_jobs_by_protected_resource.list_restore_jobs_by_protected_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_restore_jobs_by_protected_resource_input.ListRestoreJobsByProtectedResourceInput = {
            "resource_arn": resource_arn
        }
        if by_status is not None:
            input_["by_status"] = by_status
        if by_recovery_point_creation_date_after is not None:
            input_["by_recovery_point_creation_date_after"] = (
                by_recovery_point_creation_date_after
            )
        if by_recovery_point_creation_date_before is not None:
            input_["by_recovery_point_creation_date_before"] = (
                by_recovery_point_creation_date_before
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

    def iter_list_restore_jobs_by_protected_resource(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_status: Optional[
            "capo_backup.types.restore_job_status.RestoreJobStatus"
        ] = None,
        by_recovery_point_creation_date_after: Optional[
            "capo_backup.types.timestamp.timestamp"
        ] = None,
        by_recovery_point_creation_date_before: Optional[
            "capo_backup.types.timestamp.timestamp"
        ] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.restore_jobs_list_member.RestoreJobsListMember]":
        _token = next_token
        while True:
            _response = self.list_restore_jobs_by_protected_resource(
                resource_arn,
                config_overrides=config_overrides,
                by_status=by_status,
                by_recovery_point_creation_date_after=by_recovery_point_creation_date_after,
                by_recovery_point_creation_date_before=by_recovery_point_creation_date_before,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("restore_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_restore_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        state: Optional["capo_backup.types.restore_job_state.RestoreJobState"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_restore_job_summaries_output.ListRestoreJobSummariesOutput":
        """<p>This request obtains a summary of restore jobs created or running within the the most recent 14 days. You can include parameters AccountID, State, ResourceType, AggregationPeriod, MaxResults, or NextToken to filter results.</p> <p>This request returns a summary that contains Region, Account, State, RestourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.</p>

        Args:
            account_id: <p>Returns the job count for the specified account.</p> <p>If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestor's account will be returned.</p> <p>Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts from all accounts within the authenticated organization, then returns the sum.</p>
            state: <p>This parameter returns the job count for jobs with the specified state.</p> <p>The the value ANY returns count of all states.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all states and returns the sum.</p>
            resource_type: <p>Returns the job count for the specified resource type. Use request <code>GetSupportedResourceTypes</code> to obtain strings for supported resource types.</p> <p>The the value ANY returns count of all resource types.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all resource types and returns the sum.</p> <p>The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>
            aggregation_period: <p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code> - The daily job count for the prior 14 days.</p> </li> <li> <p> <code>SEVEN_DAYS</code> - The aggregated job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code> - The aggregated job count for prior 14 days.</p> </li> </ul>
            max_results: <p>This parameter sets the maximum number of items to be returned.</p> <p>The value is an integer. Range of accepted values is from 1 to 500.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_restore_job_summaries_input.ListRestoreJobSummariesInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_restore_job_summaries_output.ListRestoreJobSummariesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_restore_job_summaries

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_restore_job_summaries.list_restore_job_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_restore_job_summaries_input.ListRestoreJobSummariesInput = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if state is not None:
            input_["state"] = state
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
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

    def iter_list_restore_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        state: Optional["capo_backup.types.restore_job_state.RestoreJobState"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.list_restore_job_summaries_output.ListRestoreJobSummariesOutput]":
        _token = next_token
        while True:
            _response = self.list_restore_job_summaries(
                config_overrides=config_overrides,
                account_id=account_id,
                state=state,
                resource_type=resource_type,
                aggregation_period=aggregation_period,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_restore_testing_plans(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_restore_testing_plans_input_max_results_integer.ListRestoreTestingPlansInputMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_backup.types.list_restore_testing_plans_output.ListRestoreTestingPlansOutput":
        """<p>Returns a list of restore testing plans.</p>

        Args:
            max_results: <p>The maximum number of items to be returned.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the nexttoken.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_restore_testing_plans_input.ListRestoreTestingPlansInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_restore_testing_plans_output.ListRestoreTestingPlansOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_restore_testing_plans

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_restore_testing_plans.list_restore_testing_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_restore_testing_plans_input.ListRestoreTestingPlansInput = {}
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

    def iter_list_restore_testing_plans(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_restore_testing_plans_input_max_results_integer.ListRestoreTestingPlansInputMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_backup.types.restore_testing_plan_for_list.RestoreTestingPlanForList]":
        _token = next_token
        while True:
            _response = self.list_restore_testing_plans(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("restore_testing_plans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_restore_testing_selections(
        self,
        restore_testing_plan_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_restore_testing_selections_input_max_results_integer.ListRestoreTestingSelectionsInputMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_backup.types.list_restore_testing_selections_output.ListRestoreTestingSelectionsOutput":
        """<p>Returns a list of restore testing selections. Can be filtered by <code>MaxResults</code> and <code>RestoreTestingPlanName</code>.</p>

        Args:
            max_results: <p>The maximum number of items to be returned.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the nexttoken.</p>
            restore_testing_plan_name: <p>Returns restore testing selections by the specified restore testing plan name.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_restore_testing_selections_input.ListRestoreTestingSelectionsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_restore_testing_selections_output.ListRestoreTestingSelectionsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_restore_testing_selections

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_restore_testing_selections.list_restore_testing_selections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_restore_testing_selections_input.ListRestoreTestingSelectionsInput = {
            "restore_testing_plan_name": restore_testing_plan_name
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

    def iter_list_restore_testing_selections(
        self,
        restore_testing_plan_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional[
            "capo_backup.types.list_restore_testing_selections_input_max_results_integer.ListRestoreTestingSelectionsInputMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_backup.types.restore_testing_selection_for_list.RestoreTestingSelectionForList]":
        _token = next_token
        while True:
            _response = self.list_restore_testing_selections(
                restore_testing_plan_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("restore_testing_selections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scan_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_account_id: Optional[str] = None,
        by_backup_vault_name: Optional[str] = None,
        by_complete_after: Optional[datetime.datetime] = None,
        by_complete_before: Optional[datetime.datetime] = None,
        by_malware_scanner: Optional[
            "capo_backup.types.malware_scanner.MalwareScanner"
        ] = None,
        by_recovery_point_arn: Optional[str] = None,
        by_resource_arn: Optional[str] = None,
        by_resource_type: Optional[
            "capo_backup.types.scan_resource_type.ScanResourceType"
        ] = None,
        by_scan_result_status: Optional[
            "capo_backup.types.scan_result_status.ScanResultStatus"
        ] = None,
        by_state: Optional["capo_backup.types.scan_state.ScanState"] = None,
        max_results: Optional[
            "capo_backup.types.list_scan_jobs_input_max_results_integer.ListScanJobsInputMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_backup.types.list_scan_jobs_output.ListScanJobsOutput":
        r"""<p>Returns a list of existing scan jobs for an authenticated account for the last 30 days.</p>

        Args:
            by_account_id: <p>The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.</p> <p>If used from an Amazon Web Services Organizations management account, passing <code>*</code> returns all jobs across the organization.</p> <p>Pattern: <code>^[0-9]{12}$</code> </p>
            by_backup_vault_name: <p>Returns only scan jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <p>Pattern: <code>^[a-zA-Z0-9\-\_\.]{2,50}$</code> </p>
            by_complete_after: <p>Returns only scan jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_complete_before: <p>Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).</p>
            by_malware_scanner: <p>Returns only the scan jobs for the specified malware scanner. Currently only supports <code>GUARDDUTY</code>.</p>
            by_recovery_point_arn: <p>Returns only the scan jobs that are ran against the specified recovery point.</p>
            by_resource_arn: <p>Returns only scan jobs that match the specified resource Amazon Resource Name (ARN).</p>
            by_resource_type: <p>Returns restore testing selections by the specified restore testing plan name.</p> <ul> <li> <p> <code>EBS</code>for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code>for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>S3</code>for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul> <p>Pattern: <code>^[a-zA-Z0-9\-\_\.]{1,50}$</code> </p>
            by_scan_result_status: <p>Returns only the scan jobs for the specified scan results:</p> <ul> <li> <p> <code>THREATS_FOUND</code> </p> </li> <li> <p> <code>NO_THREATS_FOUND</code> </p> </li> </ul>
            by_state: <p>Returns only the scan jobs for the specified scanning job state.</p>
            max_results: <p>The maximum number of items to be returned.</p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_scan_jobs_input.ListScanJobsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_scan_jobs_output.ListScanJobsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_scan_jobs

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_scan_jobs.list_scan_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_scan_jobs_input.ListScanJobsInput = {}
        if by_account_id is not None:
            input_["by_account_id"] = by_account_id
        if by_backup_vault_name is not None:
            input_["by_backup_vault_name"] = by_backup_vault_name
        if by_complete_after is not None:
            input_["by_complete_after"] = by_complete_after
        if by_complete_before is not None:
            input_["by_complete_before"] = by_complete_before
        if by_malware_scanner is not None:
            input_["by_malware_scanner"] = by_malware_scanner
        if by_recovery_point_arn is not None:
            input_["by_recovery_point_arn"] = by_recovery_point_arn
        if by_resource_arn is not None:
            input_["by_resource_arn"] = by_resource_arn
        if by_resource_type is not None:
            input_["by_resource_type"] = by_resource_type
        if by_scan_result_status is not None:
            input_["by_scan_result_status"] = by_scan_result_status
        if by_state is not None:
            input_["by_state"] = by_state
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

    def iter_list_scan_jobs(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        by_account_id: Optional[str] = None,
        by_backup_vault_name: Optional[str] = None,
        by_complete_after: Optional[datetime.datetime] = None,
        by_complete_before: Optional[datetime.datetime] = None,
        by_malware_scanner: Optional[
            "capo_backup.types.malware_scanner.MalwareScanner"
        ] = None,
        by_recovery_point_arn: Optional[str] = None,
        by_resource_arn: Optional[str] = None,
        by_resource_type: Optional[
            "capo_backup.types.scan_resource_type.ScanResourceType"
        ] = None,
        by_scan_result_status: Optional[
            "capo_backup.types.scan_result_status.ScanResultStatus"
        ] = None,
        by_state: Optional["capo_backup.types.scan_state.ScanState"] = None,
        max_results: Optional[
            "capo_backup.types.list_scan_jobs_input_max_results_integer.ListScanJobsInputMaxResultsInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_backup.types.scan_job.ScanJob]":
        _token = next_token
        while True:
            _response = self.list_scan_jobs(
                config_overrides=config_overrides,
                by_account_id=by_account_id,
                by_backup_vault_name=by_backup_vault_name,
                by_complete_after=by_complete_after,
                by_complete_before=by_complete_before,
                by_malware_scanner=by_malware_scanner,
                by_recovery_point_arn=by_recovery_point_arn,
                by_resource_arn=by_resource_arn,
                by_resource_type=by_resource_type,
                by_scan_result_status=by_scan_result_status,
                by_state=by_state,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scan_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scan_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        malware_scanner: Optional[
            "capo_backup.types.malware_scanner.MalwareScanner"
        ] = None,
        scan_result_status: Optional[
            "capo_backup.types.scan_result_status.ScanResultStatus"
        ] = None,
        state: Optional["capo_backup.types.scan_job_status.ScanJobStatus"] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput":
        """<p>This is a request for a summary of scan jobs created or running within the most recent 14 days.</p>

        Args:
            account_id: <p>Returns the job count for the specified account.</p> <p>If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestor's account will be returned.</p> <p>Root, admin, and delegated administrator accounts can use the value <code>ANY</code> to return job counts from every account in the organization.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts from all accounts within the authenticated organization, then returns the sum.</p>
            resource_type: <p>Returns the job count for the specified resource type. Use request <code>GetSupportedResourceTypes</code> to obtain strings for supported resource types.</p> <p>The the value <code>ANY</code> returns count of all resource types.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all resource types and returns the sum.</p>
            malware_scanner: <p>Returns only the scan jobs for the specified malware scanner. Currently the only MalwareScanner is <code>GUARDDUTY</code>. But the field also supports <code>ANY</code>, and <code>AGGREGATE_ALL</code>.</p>
            scan_result_status: <p>Returns only the scan jobs for the specified scan results.</p>
            state: <p>Returns only the scan jobs for the specified scanning job state.</p>
            aggregation_period: <p>The period for the returned results.</p> <ul> <li> <p> <code>ONE_DAY</code>The daily job count for the prior 1 day.</p> </li> <li> <p> <code>SEVEN_DAYS</code>The daily job count for the prior 7 days.</p> </li> <li> <p> <code>FOURTEEN_DAYS</code>The daily job count for the prior 14 days.</p> </li> </ul>
            max_results: <p>The maximum number of items to be returned.</p> <p>The value is an integer. Range of accepted values is from 1 to 500.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_scan_job_summaries_input.ListScanJobSummariesInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_scan_job_summaries_output.ListScanJobSummariesOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_scan_job_summaries

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_scan_job_summaries.list_scan_job_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_scan_job_summaries_input.ListScanJobSummariesInput = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if malware_scanner is not None:
            input_["malware_scanner"] = malware_scanner
        if scan_result_status is not None:
            input_["scan_result_status"] = scan_result_status
        if state is not None:
            input_["state"] = state
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
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

    def iter_list_scan_job_summaries(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        account_id: Optional["capo_backup.types.account_id.AccountId"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        malware_scanner: Optional[
            "capo_backup.types.malware_scanner.MalwareScanner"
        ] = None,
        scan_result_status: Optional[
            "capo_backup.types.scan_result_status.ScanResultStatus"
        ] = None,
        state: Optional["capo_backup.types.scan_job_status.ScanJobStatus"] = None,
        aggregation_period: Optional[
            "capo_backup.types.aggregation_period.AggregationPeriod"
        ] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.scan_job_summary.ScanJobSummary]":
        _token = next_token
        while True:
            _response = self.list_scan_job_summaries(
                config_overrides=config_overrides,
                account_id=account_id,
                resource_type=resource_type,
                malware_scanner=malware_scanner,
                scan_result_status=scan_result_status,
                state=state,
                aggregation_period=aggregation_period,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scan_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "capo_backup.types.list_tags_output.ListTagsOutput":
        """<p>Returns the tags assigned to the resource, such as a target recovery point, backup plan, or backup vault.</p> <p>This operation returns results depending on the resource type used in the value for <code>resourceArn</code>. For example, recovery points of Amazon DynamoDB with Advanced Settings have an ARN (Amazon Resource Name) that begins with <code>arn:aws:backup</code>. Recovery points (backups) of DynamoDB without Advanced Settings enabled have an ARN that begins with <code>arn:aws:dynamodb</code>.</p> <p>When this operation is called and when you include values of <code>resourceArn</code> that have an ARN other than <code>arn:aws:backup</code>, it may return one of the exceptions listed below. To prevent this exception, include only values representing resource types that are fully managed by Backup. These have an ARN that begins <code>arn:aws:backup</code> and they are noted in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the type of resource. Valid targets for <code>ListTags</code> are recovery points, backup plans, and backup vaults.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of items to be returned.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_tags_input.ListTagsInput]",
        ) -> OperationResponse["capo_backup.types.list_tags_output.ListTagsOutput"]:
            import capo_backup._operations.cryo_controller_user_manager.list_tags

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_tags_input.ListTagsInput = {
            "resource_arn": resource_arn
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

    def iter_list_tags(
        self,
        resource_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_backup.types.list_tags_output.ListTagsOutput]":
        _token = next_token
        while True:
            _response = self.list_tags(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tiering_configurations(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.list_tiering_configurations_output.ListTieringConfigurationsOutput":
        """<p>Returns a list of tiering configurations.</p>

        Args:
            max_results: <p>The maximum number of items to be returned.</p>
            next_token: <p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.list_tiering_configurations_input.ListTieringConfigurationsInput]",
        ) -> OperationResponse[
            "capo_backup.types.list_tiering_configurations_output.ListTieringConfigurationsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.list_tiering_configurations

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.list_tiering_configurations.list_tiering_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.list_tiering_configurations_input.ListTieringConfigurationsInput = {}
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

    def iter_list_tiering_configurations(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        max_results: Optional["capo_backup.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "Iterator[capo_backup.types.tiering_configurations_list_member.TieringConfigurationsListMember]":
        _token = next_token
        while True:
            _response = self.list_tiering_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tiering_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_backup_vault_access_policy(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        policy: Optional["capo_backup.types.iam_policy.IAMPolicy"] = None,
    ) -> None:
        """<p>Sets a resource-based policy that is used to manage access permissions on the target backup vault. Requires a backup vault name and an access policy document in JSON format.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            policy: <p>The backup vault access policy document in JSON format.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.put_backup_vault_access_policy_input.PutBackupVaultAccessPolicyInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.put_backup_vault_access_policy

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.put_backup_vault_access_policy.put_backup_vault_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.put_backup_vault_access_policy_input.PutBackupVaultAccessPolicyInput = {
            "backup_vault_name": backup_vault_name
        }
        if policy is not None:
            input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_backup_vault_lock_configuration(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        min_retention_days: Optional["capo_backup.types.long.Long"] = None,
        max_retention_days: Optional["capo_backup.types.long.Long"] = None,
        changeable_for_days: Optional["capo_backup.types.long.Long"] = None,
    ) -> None:
        """<p>Applies Backup Vault Lock to a backup vault, preventing attempts to delete any recovery point stored in or created in a backup vault. Vault Lock also prevents attempts to update the lifecycle policy that controls the retention period of any recovery point currently stored in a backup vault. If specified, Vault Lock enforces a minimum and maximum retention period for future backup and copy jobs that target a backup vault.</p> <note> <p>Backup Vault Lock has been assessed by Cohasset Associates for use in environments that are subject to SEC 17a-4, CFTC, and FINRA regulations. For more information about how Backup Vault Lock relates to these regulations, see the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/samples/cohassetreport.zip">Cohasset Associates Compliance Assessment.</a> </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html">Backup Vault Lock</a>.</p>

        Args:
            backup_vault_name: <p>The Backup Vault Lock configuration that specifies the name of the backup vault it protects.</p>
            min_retention_days: <p>The Backup Vault Lock configuration that specifies the minimum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to retain certain data for at least seven years (2555 days).</p> <p>This parameter is required when a vault lock is created through CloudFormation; otherwise, this parameter is optional. If this parameter is not specified, Vault Lock will not enforce a minimum retention period.</p> <p>If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. The shortest minimum retention period you can specify is 1 day. Recovery points already saved in the vault prior to Vault Lock are not affected.</p>
            max_retention_days: <p>The Backup Vault Lock configuration that specifies the maximum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to destroy certain data after retaining it for four years (1460 days).</p> <p>If this parameter is not included, Vault Lock does not enforce a maximum retention period on the recovery points in the vault. If this parameter is included without a value, Vault Lock will not enforce a maximum retention period.</p> <p>If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. The longest maximum retention period you can specify is 36500 days (approximately 100 years). Recovery points already saved in the vault prior to Vault Lock are not affected.</p>
            changeable_for_days: <p>The Backup Vault Lock configuration that specifies the number of days before the lock date. For example, setting <code>ChangeableForDays</code> to 30 on Jan. 1, 2022 at 8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC.</p> <p>Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Therefore, you must set <code>ChangeableForDays</code> to 3 or greater.</p> <p>The maximum value you can specify is 36,500 days (approximately 100 years).</p> <p>Before the lock date, you can delete Vault Lock from the vault using <code>DeleteBackupVaultLockConfiguration</code> or change the Vault Lock configuration using <code>PutBackupVaultLockConfiguration</code>. On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted.</p> <p>If this parameter is not specified, you can delete Vault Lock from the vault using <code>DeleteBackupVaultLockConfiguration</code> or change the Vault Lock configuration using <code>PutBackupVaultLockConfiguration</code> at any time.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.put_backup_vault_lock_configuration_input.PutBackupVaultLockConfigurationInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.put_backup_vault_lock_configuration

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.put_backup_vault_lock_configuration.put_backup_vault_lock_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.put_backup_vault_lock_configuration_input.PutBackupVaultLockConfigurationInput = {
            "backup_vault_name": backup_vault_name
        }
        if min_retention_days is not None:
            input_["min_retention_days"] = min_retention_days
        if max_retention_days is not None:
            input_["max_retention_days"] = max_retention_days
        if changeable_for_days is not None:
            input_["changeable_for_days"] = changeable_for_days

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_backup_vault_notifications(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        sns_topic_arn: "capo_backup.types.arn.ARN",
        backup_vault_events: "capo_backup.types.backup_vault_events.BackupVaultEvents",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Turns on notifications on a backup vault for the specified topic and events.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            sns_topic_arn: <p>The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for example, <code>arn:aws:sns:us-west-2:111122223333:MyVaultTopic</code>.</p>
            backup_vault_events: <p>An array of events that indicate the status of jobs to back up resources to the backup vault. For the list of supported events, common use cases, and code samples, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html">Notification options with Backup</a>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.put_backup_vault_notifications_input.PutBackupVaultNotificationsInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.put_backup_vault_notifications

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.put_backup_vault_notifications.put_backup_vault_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.put_backup_vault_notifications_input.PutBackupVaultNotificationsInput = {
            "backup_vault_name": backup_vault_name,
            "sns_topic_arn": sns_topic_arn,
            "backup_vault_events": backup_vault_events,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_restore_validation_result(
        self,
        restore_job_id: "capo_backup.types.restore_job_id.RestoreJobId",
        validation_status: "capo_backup.types.restore_validation_status.RestoreValidationStatus",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        validation_status_message: Optional["capo_backup.types.string.string"] = None,
    ) -> None:
        """<p>This request allows you to send your independent self-run restore test validation results. <code>RestoreJobId</code> and <code>ValidationStatus</code> are required. Optionally, you can input a <code>ValidationStatusMessage</code>.</p>

        Args:
            restore_job_id: <p>This is a unique identifier of a restore job within Backup.</p>
            validation_status: <p>The status of your restore validation.</p>
            validation_status_message: <p>This is an optional message string you can input to describe the validation status for the restore test validation.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.put_restore_validation_result_input.PutRestoreValidationResultInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.put_restore_validation_result

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.put_restore_validation_result.put_restore_validation_result(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.put_restore_validation_result_input.PutRestoreValidationResultInput = {
            "restore_job_id": restore_job_id,
            "validation_status": validation_status,
        }
        if validation_status_message is not None:
            input_["validation_status_message"] = validation_status_message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def revoke_restore_access_backup_vault(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        restore_access_backup_vault_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        requester_comment: Optional[
            "capo_backup.types.requester_comment.RequesterComment"
        ] = None,
    ) -> None:
        """<p>Revokes access to a restore access backup vault, removing the ability to restore from its recovery points and permanently deleting the vault.</p>

        Args:
            backup_vault_name: <p>The name of the source backup vault associated with the restore access backup vault to be revoked.</p>
            restore_access_backup_vault_arn: <p>The ARN of the restore access backup vault to revoke.</p>
            requester_comment: <p>A comment explaining the reason for revoking access to the restore access backup vault.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.revoke_restore_access_backup_vault_input.RevokeRestoreAccessBackupVaultInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.revoke_restore_access_backup_vault

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.revoke_restore_access_backup_vault.revoke_restore_access_backup_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.revoke_restore_access_backup_vault_input.RevokeRestoreAccessBackupVaultInput = {
            "backup_vault_name": backup_vault_name,
            "restore_access_backup_vault_arn": restore_access_backup_vault_arn,
        }
        if requester_comment is not None:
            input_["requester_comment"] = requester_comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_backup_job(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        resource_arn: "capo_backup.types.arn.ARN",
        iam_role_arn: "capo_backup.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        logically_air_gapped_backup_vault_arn: Optional[
            "capo_backup.types.arn.ARN"
        ] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
        start_window_minutes: Optional[
            "capo_backup.types.window_minutes.WindowMinutes"
        ] = None,
        complete_window_minutes: Optional[
            "capo_backup.types.window_minutes.WindowMinutes"
        ] = None,
        lifecycle: Optional["capo_backup.types.lifecycle.Lifecycle"] = None,
        recovery_point_tags: Optional["capo_backup.types.tags.Tags"] = None,
        backup_options: Optional[
            "capo_backup.types.backup_options.BackupOptions"
        ] = None,
        index: Optional["capo_backup.types.index.Index"] = None,
    ) -> "capo_backup.types.start_backup_job_output.StartBackupJobOutput":
        """<p>Starts an on-demand backup job for the specified resource.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            logically_air_gapped_backup_vault_arn: <p>The ARN of a logically air-gapped vault. ARN must be in the same account and Region. If provided, supported fully managed resources back up directly to logically air-gapped vault, while other supported resources create a temporary (billable) snapshot in backup vault, then copy it to logically air-gapped vault. Unsupported resources only back up to the specified backup vault.</p>
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>
            iam_role_arn: <p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartBackupJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>
            start_window_minutes: <p>A value in minutes after a backup is scheduled before a job will be canceled if it doesn't start successfully. This value is optional, and the default is 8 hours. If this value is included, it must be at least 60 minutes to avoid errors.</p> <p>This parameter has a maximum value of 100 years (52,560,000 minutes).</p> <p>During the start window, the backup job status remains in <code>CREATED</code> status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to <code>RUNNING</code>) or until the job status changes to <code>EXPIRED</code> (which is expected to occur when the start window time is over).</p>
            complete_window_minutes: <p>A value in minutes during which a successfully started backup must complete, or else Backup will cancel the job. This value is optional. This value begins counting down from when the backup was scheduled. It does not add additional time for <code>StartWindowMinutes</code>, or if the backup started later than scheduled.</p> <p>Like <code>StartWindowMinutes</code>, this parameter has a maximum value of 100 years (52,560,000 minutes).</p>
            lifecycle: <p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup will transition and expire backups automatically according to the lifecycle that you define. </p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. </p> <p>Resource types that can transition to cold storage are listed in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p> <p>This parameter has a maximum value of 100 years (36,500 days).</p>
            recovery_point_tags: <p>The tags to assign to the resources.</p>
            backup_options: <p>The backup option for a selected resource. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.</p> <p>Valid values: Set to <code>"WindowsVSS":"enabled"</code> to enable the <code>WindowsVSS</code> backup option and create a Windows VSS backup. Set to <code>"WindowsVSS""disabled"</code> to create a regular backup. The <code>WindowsVSS</code> option is not enabled by default.</p>
            index: <p>Include this parameter to enable index creation if your backup job has a resource type that supports backup indexes.</p> <p>Resource types that support backup indexes include:</p> <ul> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul> <p>Index can have 1 of 2 possible values, either <code>ENABLED</code> or <code>DISABLED</code>.</p> <p>To create a backup index for an eligible <code>ACTIVE</code> recovery point that does not yet have a backup index, set value to <code>ENABLED</code>.</p> <p>To delete a backup index, set value to <code>DISABLED</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.start_backup_job_input.StartBackupJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.start_backup_job_output.StartBackupJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.start_backup_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.start_backup_job.start_backup_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.start_backup_job_input.StartBackupJobInput = {
            "backup_vault_name": backup_vault_name,
            "resource_arn": resource_arn,
            "iam_role_arn": iam_role_arn,
        }
        if logically_air_gapped_backup_vault_arn is not None:
            input_["logically_air_gapped_backup_vault_arn"] = (
                logically_air_gapped_backup_vault_arn
            )
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if start_window_minutes is not None:
            input_["start_window_minutes"] = start_window_minutes
        if complete_window_minutes is not None:
            input_["complete_window_minutes"] = complete_window_minutes
        if lifecycle is not None:
            input_["lifecycle"] = lifecycle
        if recovery_point_tags is not None:
            input_["recovery_point_tags"] = recovery_point_tags
        if backup_options is not None:
            input_["backup_options"] = backup_options
        if index is not None:
            input_["index"] = index

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_copy_job(
        self,
        recovery_point_arn: "capo_backup.types.arn.ARN",
        source_backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        destination_backup_vault_arn: "capo_backup.types.arn.ARN",
        iam_role_arn: "capo_backup.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
        lifecycle: Optional["capo_backup.types.lifecycle.Lifecycle"] = None,
    ) -> "capo_backup.types.start_copy_job_output.StartCopyJobOutput":
        """<p>Starts a job to create a one-time copy of the specified resource.</p> <p>Does not support continuous backups.</p> <p>See <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/recov-point-create-a-copy.html#backup-copy-retry">Copy job retry</a> for information on how Backup retries copy job operations.</p>

        Args:
            recovery_point_arn: <p>An ARN that uniquely identifies a recovery point to use for the copy job; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45. </p>
            source_backup_vault_name: <p>The name of a logical source container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            destination_backup_vault_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a destination backup vault to copy to; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>
            iam_role_arn: <p>Specifies the IAM role ARN used to copy the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartCopyJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.start_copy_job_input.StartCopyJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.start_copy_job_output.StartCopyJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.start_copy_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.start_copy_job.start_copy_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.start_copy_job_input.StartCopyJobInput = {
            "recovery_point_arn": recovery_point_arn,
            "source_backup_vault_name": source_backup_vault_name,
            "destination_backup_vault_arn": destination_backup_vault_arn,
            "iam_role_arn": iam_role_arn,
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if lifecycle is not None:
            input_["lifecycle"] = lifecycle

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_report_job(
        self,
        report_plan_name: "capo_backup.types.report_plan_name.ReportPlanName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.start_report_job_output.StartReportJobOutput":
        """<p>Starts an on-demand report job for the specified report plan.</p>

        Args:
            report_plan_name: <p>The unique name of a report plan.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartReportJobInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.start_report_job_input.StartReportJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.start_report_job_output.StartReportJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.start_report_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.start_report_job.start_report_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.start_report_job_input.StartReportJobInput = {
            "report_plan_name": report_plan_name
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_restore_job(
        self,
        recovery_point_arn: "capo_backup.types.arn.ARN",
        metadata: "capo_backup.types.metadata.Metadata",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        iam_role_arn: Optional["capo_backup.types.iam_role_arn.IAMRoleArn"] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
        resource_type: Optional["capo_backup.types.resource_type.ResourceType"] = None,
        copy_source_tags_to_restored_resource: Optional[
            "capo_backup.types.boolean2.Boolean2"
        ] = None,
    ) -> "capo_backup.types.start_restore_job_output.StartRestoreJobOutput":
        """<p>Recovers the saved resource identified by an Amazon Resource Name (ARN).</p>

        Args:
            recovery_point_arn: <p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>
            metadata: <p>A set of metadata key-value pairs.</p> <p>You can get configuration metadata about a resource at the time it was backed up by calling <code>GetRecoveryPointRestoreMetadata</code>. However, values in addition to those provided by <code>GetRecoveryPointRestoreMetadata</code> might be required to restore a resource. For example, you might need to provide a new resource name if the original already exists.</p> <p>For more information about the metadata for each resource, see the following:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-aur.html#aur-restore-cli">Metadata for Amazon Aurora</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-docdb.html#docdb-restore-cli">Metadata for Amazon DocumentDB</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-application-stacks.html#restoring-cfn-cli">Metadata for CloudFormation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-dynamodb.html#ddb-restore-cli">Metadata for Amazon DynamoDB</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ebs.html#ebs-restore-cli"> Metadata for Amazon EBS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ec2.html#restoring-ec2-cli">Metadata for Amazon EC2</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-efs.html#efs-restore-cli">Metadata for Amazon EFS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-eks.html#eks-restore-backup-section">Metadata for Amazon EKS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-fsx.html#fsx-restore-cli">Metadata for Amazon FSx</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-nep.html#nep-restore-cli">Metadata for Amazon Neptune</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-rds.html#rds-restore-cli">Metadata for Amazon RDS</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-restores.html#redshift-restore-api">Metadata for Amazon Redshift</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html#restoring-sgw-cli">Metadata for Storage Gateway</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html#s3-restore-cli">Metadata for Amazon S3</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/timestream-restore.html#timestream-restore-api">Metadata for Amazon Timestream</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-vm.html#vm-restore-cli">Metadata for virtual machines</a> </p> </li> </ul>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Backup uses to create the target resource; for example: <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartRestoreJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>
            resource_type: <p>Starts a job to restore a recovery point for one of the following resources:</p> <ul> <li> <p> <code>Aurora</code> - Amazon Aurora</p> </li> <li> <p> <code>DocumentDB</code> - Amazon DocumentDB</p> </li> <li> <p> <code>CloudFormation</code> - CloudFormation</p> </li> <li> <p> <code>DynamoDB</code> - Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> - Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> - Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> - Amazon Elastic File System</p> </li> <li> <p> <code>EKS</code> - Amazon Elastic Kubernetes Service</p> </li> <li> <p> <code>FSx</code> - Amazon FSx</p> </li> <li> <p> <code>Neptune</code> - Amazon Neptune</p> </li> <li> <p> <code>RDS</code> - Amazon Relational Database Service</p> </li> <li> <p> <code>Redshift</code> - Amazon Redshift</p> </li> <li> <p> <code>Storage Gateway</code> - Storage Gateway</p> </li> <li> <p> <code>S3</code> - Amazon Simple Storage Service</p> </li> <li> <p> <code>Timestream</code> - Amazon Timestream</p> </li> <li> <p> <code>VirtualMachine</code> - Virtual machines</p> </li> </ul>
            copy_source_tags_to_restored_resource: <p>This is an optional parameter. If this equals <code>True</code>, tags included in the backup will be copied to the restored resource.</p> <p>This can only be applied to backups created through Backup.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.start_restore_job_input.StartRestoreJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.start_restore_job_output.StartRestoreJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.start_restore_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.start_restore_job.start_restore_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.start_restore_job_input.StartRestoreJobInput = {
            "recovery_point_arn": recovery_point_arn,
            "metadata": metadata,
        }
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if copy_source_tags_to_restored_resource is not None:
            input_["copy_source_tags_to_restored_resource"] = (
                copy_source_tags_to_restored_resource
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_scan_job(
        self,
        backup_vault_name: str,
        iam_role_arn: str,
        malware_scanner: "capo_backup.types.malware_scanner.MalwareScanner",
        recovery_point_arn: str,
        scan_mode: "capo_backup.types.scan_mode.ScanMode",
        scanner_role_arn: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        continuous_scan_end_time: Optional[datetime.datetime] = None,
        idempotency_token: Optional[str] = None,
        scan_base_recovery_point_arn: Optional[str] = None,
    ) -> "capo_backup.types.start_scan_job_output.StartScanJobOutput":
        r"""<p>Starts scanning jobs for specific resources.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p> <p>Pattern: <code>^[a-zA-Z0-9\-\_]{2,50}$</code> </p>
            continuous_scan_end_time: <p>The point in time the scan job will scan up to for a continuous backup.</p>
            iam_role_arn: <p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartScanJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>
            malware_scanner: <p>Specifies the malware scanner used during the scan job. Currently only supports <code>GUARDDUTY</code>.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point. This is your target recovery point for a full scan. If you are running an incremental scan, this will be your a recovery point which has been created after your base recovery point selection.</p>
            scan_base_recovery_point_arn: <p>An ARN that uniquely identifies the base recovery point to be used for incremental scanning.</p>
            scan_mode: <p>Specifies the scan type use for the scan job.</p> <p>Includes:</p> <ul> <li> <p> <code>FULL_SCAN</code> will scan the entire data lineage within the backup.</p> </li> <li> <p> <code>INCREMENTAL_SCAN</code> will scan the data difference between the target recovery point and base recovery point ARN.</p> </li> </ul>
            scanner_role_arn: <p>Specified the IAM scanner role ARN.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.start_scan_job_input.StartScanJobInput]",
        ) -> OperationResponse[
            "capo_backup.types.start_scan_job_output.StartScanJobOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.start_scan_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.start_scan_job.start_scan_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.start_scan_job_input.StartScanJobInput = {
            "backup_vault_name": backup_vault_name,
            "iam_role_arn": iam_role_arn,
            "malware_scanner": malware_scanner,
            "recovery_point_arn": recovery_point_arn,
            "scan_mode": scan_mode,
            "scanner_role_arn": scanner_role_arn,
        }
        if continuous_scan_end_time is not None:
            input_["continuous_scan_end_time"] = continuous_scan_end_time
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if scan_base_recovery_point_arn is not None:
            input_["scan_base_recovery_point_arn"] = scan_base_recovery_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_backup_job(
        self,
        backup_job_id: "capo_backup.types.string.string",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Attempts to cancel a job to create a one-time backup of a resource.</p> <p>This action is not supported for the following services:</p> <ul> <li> <p>Amazon Aurora</p> </li> <li> <p>Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p>Amazon FSx for Lustre</p> </li> <li> <p>Amazon FSx for NetApp ONTAP</p> </li> <li> <p>Amazon FSx for OpenZFS</p> </li> <li> <p>Amazon FSx for Windows File Server</p> </li> <li> <p>Amazon Neptune</p> </li> <li> <p>SAP HANA databases on Amazon EC2 instances</p> </li> <li> <p>Amazon RDS</p> </li> </ul>

        Args:
            backup_job_id: <p>Uniquely identifies a request to Backup to back up a resource.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.stop_backup_job_input.StopBackupJobInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.stop_backup_job

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.stop_backup_job.stop_backup_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.stop_backup_job_input.StopBackupJobInput = {
            "backup_job_id": backup_job_id
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
        resource_arn: "capo_backup.types.arn.ARN",
        tags: "capo_backup.types.tags.Tags",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Assigns a set of key-value pairs to a resource.</p>

        Args:
            resource_arn: <p>The ARN that uniquely identifies the resource.</p>
            tags: <p>Key-value pairs that are used to help organize your resources. You can assign your own metadata to the resources you create. For clarity, this is the structure to assign tags: <code>[{"Key":"string","Value":"string"}]</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.tag_resource

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_backup.types.arn.ARN",
        tag_key_list: "capo_backup.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> None:
        """<p>Removes a set of key-value pairs from a recovery point, backup plan, or backup vault identified by an Amazon Resource Name (ARN)</p> <p>This API is not supported for recovery points for resource types including Aurora, Amazon DocumentDB. Amazon EBS, Amazon FSx, Neptune, and Amazon RDS.</p>

        Args:
            resource_arn: <p>An ARN that uniquely identifies a resource. The format of the ARN depends on the type of the tagged resource.</p> <p>ARNs that do not include <code>backup</code> are incompatible with tagging. <code>TagResource</code> and <code>UntagResource</code> with invalid ARNs will result in an error. Acceptable ARN content can include <code>arn:aws:backup:us-east</code>. Invalid ARN content may look like <code>arn:aws:ec2:us-east</code>.</p>
            tag_key_list: <p>The keys to identify which key-value tags to remove from a resource.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.untag_resource

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_key_list": tag_key_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_backup_plan(
        self,
        backup_plan_id: "capo_backup.types.string.string",
        backup_plan: "capo_backup.types.backup_plan_input.BackupPlanInput",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.update_backup_plan_output.UpdateBackupPlanOutput":
        """<p>Updates the specified backup plan. The new version is uniquely identified by its ID.</p>

        Args:
            backup_plan_id: <p>The ID of the backup plan.</p>
            backup_plan: <p>The body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_backup_plan_input.UpdateBackupPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_backup_plan_output.UpdateBackupPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_backup_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_backup_plan.update_backup_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_backup_plan_input.UpdateBackupPlanInput = {
            "backup_plan_id": backup_plan_id,
            "backup_plan": backup_plan,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_framework(
        self,
        framework_name: "capo_backup.types.framework_name.FrameworkName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        framework_description: Optional[
            "capo_backup.types.framework_description.FrameworkDescription"
        ] = None,
        framework_controls: Optional[
            "capo_backup.types.framework_controls.FrameworkControls"
        ] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.update_framework_output.UpdateFrameworkOutput":
        """<p>Updates the specified framework.</p>

        Args:
            framework_name: <p>The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>
            framework_description: <p>An optional description of the framework with a maximum 1,024 characters.</p>
            framework_controls: <p>The controls that make up the framework. Each control in the list has a name, input parameters, and scope.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>UpdateFrameworkInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_framework_input.UpdateFrameworkInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_framework_output.UpdateFrameworkOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_framework

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_framework.update_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_framework_input.UpdateFrameworkInput = {
            "framework_name": framework_name
        }
        if framework_description is not None:
            input_["framework_description"] = framework_description
        if framework_controls is not None:
            input_["framework_controls"] = framework_controls
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_global_settings(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        global_settings: Optional[
            "capo_backup.types.global_settings.GlobalSettings"
        ] = None,
    ) -> None:
        """<p>Updates whether the Amazon Web Services account has enabled different cross-account management options, including cross-account backup, multi-party approval, and delegated administrator. Returns an error if the account is not an Organizations management account. Use the <code>DescribeGlobalSettings</code> API to determine the current settings.</p>

        Args:
            global_settings: <p>Inputs can include:</p> <p>A value for <code>isCrossAccountBackupEnabled</code>. Values can be true or false. Example: <code>update-global-settings --global-settings isCrossAccountBackupEnabled=false</code>.</p> <p>A value for Multi-party approval, styled as <code>isMpaEnabled</code>. Values can be true or false. Example: <code>update-global-settings --global-settings isMpaEnabled=false</code>.</p> <p>A value for Backup Service-Linked Role creation, styled as <code>isDelegatedAdministratorEnabled</code>. Values can be true or false. Example: <code>update-global-settings --global-settings isDelegatedAdministratorEnabled=false</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_global_settings_input.UpdateGlobalSettingsInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.update_global_settings

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_global_settings.update_global_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_global_settings_input.UpdateGlobalSettingsInput = {}
        if global_settings is not None:
            input_["global_settings"] = global_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_recovery_point_index_settings(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        index: "capo_backup.types.index.Index",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        iam_role_arn: Optional["capo_backup.types.iam_role_arn.IAMRoleArn"] = None,
    ) -> "capo_backup.types.update_recovery_point_index_settings_output.UpdateRecoveryPointIndexSettingsOutput":
        """<p>This operation updates the settings of a recovery point index.</p> <p>Required: BackupVaultName, RecoveryPointArn, and IAMRoleArn</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p> <p>Accepted characters include lowercase letters, numbers, and hyphens.</p>
            recovery_point_arn: <p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>
            iam_role_arn: <p>This specifies the IAM role ARN used for this operation.</p> <p>For example, arn:aws:iam::123456789012:role/S3Access</p>
            index: <p>Index can have 1 of 2 possible values, either <code>ENABLED</code> or <code>DISABLED</code>.</p> <p>To create a backup index for an eligible <code>ACTIVE</code> recovery point that does not yet have a backup index, set value to <code>ENABLED</code>.</p> <p>To delete a backup index, set value to <code>DISABLED</code>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_recovery_point_index_settings_input.UpdateRecoveryPointIndexSettingsInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_recovery_point_index_settings_output.UpdateRecoveryPointIndexSettingsOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_recovery_point_index_settings

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_recovery_point_index_settings.update_recovery_point_index_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_recovery_point_index_settings_input.UpdateRecoveryPointIndexSettingsInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
            "index": index,
        }
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_recovery_point_lifecycle(
        self,
        backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName",
        recovery_point_arn: "capo_backup.types.arn.ARN",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        lifecycle: Optional["capo_backup.types.lifecycle.Lifecycle"] = None,
    ) -> "capo_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput":
        """<p>Sets the transition lifecycle of a recovery point.</p> <p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.</p> <p>Resource types that can transition to cold storage are listed in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.</p> <important> <p>If your lifecycle currently uses the parameters <code>DeleteAfterDays</code> and <code>MoveToColdStorageAfterDays</code>, include these parameters and their values when you call this operation. Not including them may result in your plan updating with null values.</p> </important> <p>This operation does not support continuous backups.</p>

        Args:
            backup_vault_name: <p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>
            recovery_point_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>
            lifecycle: <p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define. </p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. </p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_recovery_point_lifecycle_input.UpdateRecoveryPointLifecycleInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_recovery_point_lifecycle_output.UpdateRecoveryPointLifecycleOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_recovery_point_lifecycle

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_recovery_point_lifecycle.update_recovery_point_lifecycle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_recovery_point_lifecycle_input.UpdateRecoveryPointLifecycleInput = {
            "backup_vault_name": backup_vault_name,
            "recovery_point_arn": recovery_point_arn,
        }
        if lifecycle is not None:
            input_["lifecycle"] = lifecycle

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_region_settings(
        self,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        resource_type_opt_in_preference: Optional[
            "capo_backup.types.resource_type_opt_in_preference.ResourceTypeOptInPreference"
        ] = None,
        resource_type_management_preference: Optional[
            "capo_backup.types.resource_type_management_preference.ResourceTypeManagementPreference"
        ] = None,
    ) -> None:
        """<p>Updates the current service opt-in settings for the Region.</p> <p>Use the <code>DescribeRegionSettings</code> API to determine the resource types that are supported.</p>

        Args:
            resource_type_opt_in_preference: <p>Updates the list of services along with the opt-in preferences for the Region.</p> <p>If resource assignments are only based on tags, then service opt-in settings are applied. If a resource type is explicitly assigned to a backup plan, such as Amazon S3, Amazon EC2, or Amazon RDS, it will be included in the backup even if the opt-in is not enabled for that particular service. If both a resource type and tags are specified in a resource assignment, the resource type specified in the backup plan takes priority over the tag condition. Service opt-in settings are disregarded in this situation.</p>
            resource_type_management_preference: <p>Enables or disables full Backup management of backups for a resource type. To enable full Backup management for DynamoDB along with <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html"> Backup's advanced DynamoDB backup features</a>, follow the procedure to <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html#advanced-ddb-backup-enable-cli"> enable advanced DynamoDB backup programmatically</a>.</p>

        Raises:
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_region_settings_input.UpdateRegionSettingsInput]",
        ) -> OperationResponse[None]:
            import capo_backup._operations.cryo_controller_user_manager.update_region_settings

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_region_settings.update_region_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_region_settings_input.UpdateRegionSettingsInput = {}
        if resource_type_opt_in_preference is not None:
            input_["resource_type_opt_in_preference"] = resource_type_opt_in_preference
        if resource_type_management_preference is not None:
            input_["resource_type_management_preference"] = (
                resource_type_management_preference
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_report_plan(
        self,
        report_plan_name: "capo_backup.types.report_plan_name.ReportPlanName",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
        report_plan_description: Optional[
            "capo_backup.types.report_plan_description.ReportPlanDescription"
        ] = None,
        report_delivery_channel: Optional[
            "capo_backup.types.report_delivery_channel.ReportDeliveryChannel"
        ] = None,
        report_setting: Optional[
            "capo_backup.types.report_setting.ReportSetting"
        ] = None,
        idempotency_token: Optional["capo_backup.types.string.string"] = None,
    ) -> "capo_backup.types.update_report_plan_output.UpdateReportPlanOutput":
        """<p>Updates the specified report plan.</p>

        Args:
            report_plan_name: <p>The unique name of the report plan. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>
            report_plan_description: <p>An optional description of the report plan with a maximum 1,024 characters.</p>
            report_delivery_channel: <p>The information about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</p>
            report_setting: <p>The report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT</code> </p> <p>If the report template is <code>RESOURCE_COMPLIANCE_REPORT</code> or <code>CONTROL_COMPLIANCE_REPORT</code>, this API resource also describes the report coverage by Amazon Web Services Regions and frameworks.</p>
            idempotency_token: <p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>UpdateReportPlanInput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>

        Raises:
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_report_plan_input.UpdateReportPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_report_plan_output.UpdateReportPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_report_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_report_plan.update_report_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_report_plan_input.UpdateReportPlanInput = {
            "report_plan_name": report_plan_name
        }
        if report_plan_description is not None:
            input_["report_plan_description"] = report_plan_description
        if report_delivery_channel is not None:
            input_["report_delivery_channel"] = report_delivery_channel
        if report_setting is not None:
            input_["report_setting"] = report_setting
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_restore_testing_plan(
        self,
        restore_testing_plan: "capo_backup.types.restore_testing_plan_for_update.RestoreTestingPlanForUpdate",
        restore_testing_plan_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.update_restore_testing_plan_output.UpdateRestoreTestingPlanOutput":
        """<p>This request will send changes to your specified restore testing plan. <code>RestoreTestingPlanName</code> cannot be updated after it is created.</p> <p> <code>RecoveryPointSelection</code> can contain:</p> <ul> <li> <p> <code>Algorithm</code> </p> </li> <li> <p> <code>ExcludeVaults</code> </p> </li> <li> <p> <code>IncludeVaults</code> </p> </li> <li> <p> <code>RecoveryPointTypes</code> </p> </li> <li> <p> <code>SelectionWindowDays</code> </p> </li> </ul>

        Args:
            restore_testing_plan: <p>Specifies the body of a restore testing plan.</p>
            restore_testing_plan_name: <p>The name of the restore testing plan name.</p>

        Raises:
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_restore_testing_plan_input.UpdateRestoreTestingPlanInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_restore_testing_plan_output.UpdateRestoreTestingPlanOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_restore_testing_plan

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_restore_testing_plan.update_restore_testing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_restore_testing_plan_input.UpdateRestoreTestingPlanInput = {
            "restore_testing_plan": restore_testing_plan,
            "restore_testing_plan_name": restore_testing_plan_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_restore_testing_selection(
        self,
        restore_testing_plan_name: str,
        restore_testing_selection: "capo_backup.types.restore_testing_selection_for_update.RestoreTestingSelectionForUpdate",
        restore_testing_selection_name: str,
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.update_restore_testing_selection_output.UpdateRestoreTestingSelectionOutput":
        """<p>Updates the specified restore testing selection.</p> <p>Most elements except the <code>RestoreTestingSelectionName</code> can be updated with this request.</p> <p>You can use either protected resource ARNs or conditions, but not both.</p>

        Args:
            restore_testing_plan_name: <p>The restore testing plan name is required to update the indicated testing plan.</p>
            restore_testing_selection: <p>To update your restore testing selection, you can use either protected resource ARNs or conditions, but not both. That is, if your selection has <code>ProtectedResourceArns</code>, requesting an update with the parameter <code>ProtectedResourceConditions</code> will be unsuccessful.</p>
            restore_testing_selection_name: <p>The required restore testing selection name of the restore testing selection you wish to update.</p>

        Raises:
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_restore_testing_selection_input.UpdateRestoreTestingSelectionInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_restore_testing_selection_output.UpdateRestoreTestingSelectionOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_restore_testing_selection

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_restore_testing_selection.update_restore_testing_selection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_restore_testing_selection_input.UpdateRestoreTestingSelectionInput = {
            "restore_testing_plan_name": restore_testing_plan_name,
            "restore_testing_selection": restore_testing_selection,
            "restore_testing_selection_name": restore_testing_selection_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_tiering_configuration(
        self,
        tiering_configuration_name: "capo_backup.types.tiering_configuration_name.TieringConfigurationName",
        tiering_configuration: "capo_backup.types.tiering_configuration_input_for_update.TieringConfigurationInputForUpdate",
        *,
        config_overrides: Optional[BackupClientConfig] = None,
    ) -> "capo_backup.types.update_tiering_configuration_output.UpdateTieringConfigurationOutput":
        """<p>This request will send changes to your specified tiering configuration. <code>TieringConfigurationName</code> cannot be updated after it is created.</p> <p> <code>ResourceSelection</code> can contain:</p> <ul> <li> <p> <code>Resources</code> </p> </li> <li> <p> <code>TieringDownSettingsInDays</code> </p> </li> <li> <p> <code>ResourceType</code> </p> </li> </ul>

        Args:
            tiering_configuration_name: <p>The name of a tiering configuration to update.</p>
            tiering_configuration: <p>Specifies the body of a tiering configuration.</p>

        Raises:
            capo_backup.errors.already_exists_exception.AlreadyExistsException: <p>The required resource already exists.</p>
            capo_backup.errors.conflict_exception.ConflictException: <p>Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.</p>
            capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Indicates that something is wrong with a parameter's value. For example, the value is out of range.</p>
            capo_backup.errors.limit_exceeded_exception.LimitExceededException: <p>A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.</p>
            capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Indicates that a required parameter is missing.</p>
            capo_backup.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action doesn't exist.</p>
            capo_backup.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request failed due to a temporary failure of the server.</p>
            capo_backup.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup.types.update_tiering_configuration_input.UpdateTieringConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup.types.update_tiering_configuration_output.UpdateTieringConfigurationOutput"
        ]:
            import capo_backup._operations.cryo_controller_user_manager.update_tiering_configuration

            output, http_response = (
                capo_backup._operations.cryo_controller_user_manager.update_tiering_configuration.update_tiering_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup.types.update_tiering_configuration_input.UpdateTieringConfigurationInput = {
            "tiering_configuration_name": tiering_configuration_name,
            "tiering_configuration": tiering_configuration,
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
