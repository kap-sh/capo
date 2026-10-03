"""Generated from Smithy shape ``com.amazonaws.guardduty#GuardDutyAPIService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_guardduty._auth._signers
import capo_guardduty._auth._sigv4
from capo_guardduty._auth._identity import Credentials
from capo_guardduty._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_guardduty._auth._zapros_handler import AuthMiddleware
from capo_guardduty._pagination import resolve_path as _resolve_path
from capo_guardduty._services._aws_config import aws_config
from capo_guardduty._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_guardduty.types.accept_administrator_invitation_request
    import capo_guardduty.types.accept_administrator_invitation_response
    import capo_guardduty.types.accept_invitation_request
    import capo_guardduty.types.accept_invitation_response
    import capo_guardduty.types.account_details
    import capo_guardduty.types.account_id
    import capo_guardduty.types.account_ids
    import capo_guardduty.types.admin_account
    import capo_guardduty.types.archive_findings_request
    import capo_guardduty.types.archive_findings_response
    import capo_guardduty.types.association_id
    import capo_guardduty.types.association_mode
    import capo_guardduty.types.association_summary
    import capo_guardduty.types.auto_enable_members
    import capo_guardduty.types.boolean
    import capo_guardduty.types.client_token
    import capo_guardduty.types.coverage_filter_criteria
    import capo_guardduty.types.coverage_resource
    import capo_guardduty.types.coverage_sort_criteria
    import capo_guardduty.types.coverage_statistics_type_list
    import capo_guardduty.types.create_custom_detection_rule_association_request
    import capo_guardduty.types.create_custom_detection_rule_association_response
    import capo_guardduty.types.create_custom_detection_rule_org_configuration_request
    import capo_guardduty.types.create_custom_detection_rule_org_configuration_response
    import capo_guardduty.types.create_detector_request
    import capo_guardduty.types.create_detector_response
    import capo_guardduty.types.create_filter_request
    import capo_guardduty.types.create_filter_response
    import capo_guardduty.types.create_investigation_request
    import capo_guardduty.types.create_investigation_response
    import capo_guardduty.types.create_ip_set_request
    import capo_guardduty.types.create_ip_set_response
    import capo_guardduty.types.create_malware_protection_plan_request
    import capo_guardduty.types.create_malware_protection_plan_response
    import capo_guardduty.types.create_members_request
    import capo_guardduty.types.create_members_response
    import capo_guardduty.types.create_protected_resource
    import capo_guardduty.types.create_publishing_destination_request
    import capo_guardduty.types.create_publishing_destination_response
    import capo_guardduty.types.create_sample_findings_request
    import capo_guardduty.types.create_sample_findings_response
    import capo_guardduty.types.create_threat_entity_set_request
    import capo_guardduty.types.create_threat_entity_set_response
    import capo_guardduty.types.create_threat_intel_set_request
    import capo_guardduty.types.create_threat_intel_set_response
    import capo_guardduty.types.create_trusted_entity_set_request
    import capo_guardduty.types.create_trusted_entity_set_response
    import capo_guardduty.types.data_source_configurations
    import capo_guardduty.types.decline_invitations_request
    import capo_guardduty.types.decline_invitations_response
    import capo_guardduty.types.delete_custom_detection_rule_association_request
    import capo_guardduty.types.delete_custom_detection_rule_association_response
    import capo_guardduty.types.delete_custom_detection_rule_org_configuration_request
    import capo_guardduty.types.delete_custom_detection_rule_org_configuration_response
    import capo_guardduty.types.delete_detector_request
    import capo_guardduty.types.delete_detector_response
    import capo_guardduty.types.delete_filter_request
    import capo_guardduty.types.delete_filter_response
    import capo_guardduty.types.delete_invitations_request
    import capo_guardduty.types.delete_invitations_response
    import capo_guardduty.types.delete_ip_set_request
    import capo_guardduty.types.delete_ip_set_response
    import capo_guardduty.types.delete_malware_protection_plan_request
    import capo_guardduty.types.delete_members_request
    import capo_guardduty.types.delete_members_response
    import capo_guardduty.types.delete_publishing_destination_request
    import capo_guardduty.types.delete_publishing_destination_response
    import capo_guardduty.types.delete_threat_entity_set_request
    import capo_guardduty.types.delete_threat_entity_set_response
    import capo_guardduty.types.delete_threat_intel_set_request
    import capo_guardduty.types.delete_threat_intel_set_response
    import capo_guardduty.types.delete_trusted_entity_set_request
    import capo_guardduty.types.delete_trusted_entity_set_response
    import capo_guardduty.types.describe_malware_scans_request
    import capo_guardduty.types.describe_malware_scans_response
    import capo_guardduty.types.describe_organization_configuration_request
    import capo_guardduty.types.describe_organization_configuration_response
    import capo_guardduty.types.describe_publishing_destination_request
    import capo_guardduty.types.describe_publishing_destination_response
    import capo_guardduty.types.destination_properties
    import capo_guardduty.types.destination_type
    import capo_guardduty.types.detection_rule_account_ids
    import capo_guardduty.types.detection_rule_configuration_status
    import capo_guardduty.types.detection_rule_filter_list
    import capo_guardduty.types.detection_rule_max_results
    import capo_guardduty.types.detection_rule_org_configuration_summary
    import capo_guardduty.types.detector_feature_configurations
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.disable_organization_admin_account_request
    import capo_guardduty.types.disable_organization_admin_account_response
    import capo_guardduty.types.disassociate_from_administrator_account_request
    import capo_guardduty.types.disassociate_from_administrator_account_response
    import capo_guardduty.types.disassociate_from_master_account_request
    import capo_guardduty.types.disassociate_from_master_account_response
    import capo_guardduty.types.disassociate_members_request
    import capo_guardduty.types.disassociate_members_response
    import capo_guardduty.types.ebs_snapshot_preservation
    import capo_guardduty.types.enable_organization_admin_account_request
    import capo_guardduty.types.enable_organization_admin_account_response
    import capo_guardduty.types.expected_bucket_owner
    import capo_guardduty.types.feedback
    import capo_guardduty.types.filter_action
    import capo_guardduty.types.filter_criteria
    import capo_guardduty.types.filter_description
    import capo_guardduty.types.filter_name
    import capo_guardduty.types.filter_rank
    import capo_guardduty.types.finding_criteria
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.finding_ids
    import capo_guardduty.types.finding_publishing_frequency
    import capo_guardduty.types.finding_statistic_types
    import capo_guardduty.types.finding_types
    import capo_guardduty.types.get_administrator_account_request
    import capo_guardduty.types.get_administrator_account_response
    import capo_guardduty.types.get_coverage_statistics_request
    import capo_guardduty.types.get_coverage_statistics_response
    import capo_guardduty.types.get_custom_detection_rule_association_request
    import capo_guardduty.types.get_custom_detection_rule_association_response
    import capo_guardduty.types.get_custom_detection_rule_org_configuration_request
    import capo_guardduty.types.get_custom_detection_rule_org_configuration_response
    import capo_guardduty.types.get_custom_detection_rule_request
    import capo_guardduty.types.get_custom_detection_rule_response
    import capo_guardduty.types.get_detector_request
    import capo_guardduty.types.get_detector_response
    import capo_guardduty.types.get_filter_request
    import capo_guardduty.types.get_filter_response
    import capo_guardduty.types.get_findings_request
    import capo_guardduty.types.get_findings_response
    import capo_guardduty.types.get_findings_statistics_request
    import capo_guardduty.types.get_findings_statistics_response
    import capo_guardduty.types.get_investigation_request
    import capo_guardduty.types.get_investigation_response
    import capo_guardduty.types.get_invitations_count_request
    import capo_guardduty.types.get_invitations_count_response
    import capo_guardduty.types.get_ip_set_request
    import capo_guardduty.types.get_ip_set_response
    import capo_guardduty.types.get_malware_protection_plan_request
    import capo_guardduty.types.get_malware_protection_plan_response
    import capo_guardduty.types.get_malware_scan_request
    import capo_guardduty.types.get_malware_scan_response
    import capo_guardduty.types.get_malware_scan_settings_request
    import capo_guardduty.types.get_malware_scan_settings_response
    import capo_guardduty.types.get_master_account_request
    import capo_guardduty.types.get_master_account_response
    import capo_guardduty.types.get_member_detectors_request
    import capo_guardduty.types.get_member_detectors_response
    import capo_guardduty.types.get_members_request
    import capo_guardduty.types.get_members_response
    import capo_guardduty.types.get_organization_statistics_response
    import capo_guardduty.types.get_remaining_free_trial_days_request
    import capo_guardduty.types.get_remaining_free_trial_days_response
    import capo_guardduty.types.get_threat_entity_set_request
    import capo_guardduty.types.get_threat_entity_set_response
    import capo_guardduty.types.get_threat_intel_set_request
    import capo_guardduty.types.get_threat_intel_set_response
    import capo_guardduty.types.get_trusted_entity_set_request
    import capo_guardduty.types.get_trusted_entity_set_response
    import capo_guardduty.types.get_usage_statistics_request
    import capo_guardduty.types.get_usage_statistics_response
    import capo_guardduty.types.group_by_type
    import capo_guardduty.types.guard_duty_arn
    import capo_guardduty.types.integer_value_with_max
    import capo_guardduty.types.investigation_id
    import capo_guardduty.types.investigation_sort_criteria
    import capo_guardduty.types.investigation_summary
    import capo_guardduty.types.invitation
    import capo_guardduty.types.invite_members_request
    import capo_guardduty.types.invite_members_response
    import capo_guardduty.types.ip_set_format
    import capo_guardduty.types.list_coverage_request
    import capo_guardduty.types.list_coverage_response
    import capo_guardduty.types.list_custom_detection_rule_associations_request
    import capo_guardduty.types.list_custom_detection_rule_associations_response
    import capo_guardduty.types.list_custom_detection_rule_org_configurations_request
    import capo_guardduty.types.list_custom_detection_rule_org_configurations_response
    import capo_guardduty.types.list_custom_detection_rules_request
    import capo_guardduty.types.list_custom_detection_rules_response
    import capo_guardduty.types.list_detectors_request
    import capo_guardduty.types.list_detectors_response
    import capo_guardduty.types.list_filters_request
    import capo_guardduty.types.list_filters_response
    import capo_guardduty.types.list_findings_request
    import capo_guardduty.types.list_findings_response
    import capo_guardduty.types.list_investigations_request
    import capo_guardduty.types.list_investigations_response
    import capo_guardduty.types.list_invitations_request
    import capo_guardduty.types.list_invitations_response
    import capo_guardduty.types.list_ip_sets_request
    import capo_guardduty.types.list_ip_sets_response
    import capo_guardduty.types.list_malware_protection_plans_request
    import capo_guardduty.types.list_malware_protection_plans_response
    import capo_guardduty.types.list_malware_scans_filter_criteria
    import capo_guardduty.types.list_malware_scans_request
    import capo_guardduty.types.list_malware_scans_response
    import capo_guardduty.types.list_members_request
    import capo_guardduty.types.list_members_response
    import capo_guardduty.types.list_organization_admin_accounts_request
    import capo_guardduty.types.list_organization_admin_accounts_response
    import capo_guardduty.types.list_publishing_destinations_request
    import capo_guardduty.types.list_publishing_destinations_response
    import capo_guardduty.types.list_tags_for_resource_request
    import capo_guardduty.types.list_tags_for_resource_response
    import capo_guardduty.types.list_threat_entity_sets_request
    import capo_guardduty.types.list_threat_entity_sets_response
    import capo_guardduty.types.list_threat_intel_sets_request
    import capo_guardduty.types.list_threat_intel_sets_response
    import capo_guardduty.types.list_trusted_entity_sets_request
    import capo_guardduty.types.list_trusted_entity_sets_response
    import capo_guardduty.types.location
    import capo_guardduty.types.malware_protection_plan_actions
    import capo_guardduty.types.malware_scan
    import capo_guardduty.types.max_results
    import capo_guardduty.types.max_results100
    import capo_guardduty.types.member
    import capo_guardduty.types.member_features_configurations
    import capo_guardduty.types.name
    import capo_guardduty.types.next_token
    import capo_guardduty.types.order_by
    import capo_guardduty.types.organization_data_source_configurations
    import capo_guardduty.types.organization_features_configurations
    import capo_guardduty.types.resource_arn
    import capo_guardduty.types.rule_id
    import capo_guardduty.types.rule_summary
    import capo_guardduty.types.s3_object_for_send_object_malware_scan
    import capo_guardduty.types.scan
    import capo_guardduty.types.scan_resource_criteria
    import capo_guardduty.types.send_object_malware_scan_request
    import capo_guardduty.types.send_object_malware_scan_response
    import capo_guardduty.types.sensitive_string
    import capo_guardduty.types.sort_criteria
    import capo_guardduty.types.start_malware_scan_configuration
    import capo_guardduty.types.start_malware_scan_request
    import capo_guardduty.types.start_malware_scan_response
    import capo_guardduty.types.start_monitoring_members_request
    import capo_guardduty.types.start_monitoring_members_response
    import capo_guardduty.types.stop_monitoring_members_request
    import capo_guardduty.types.stop_monitoring_members_response
    import capo_guardduty.types.string
    import capo_guardduty.types.tag_key_list
    import capo_guardduty.types.tag_map
    import capo_guardduty.types.tag_resource_request
    import capo_guardduty.types.tag_resource_response
    import capo_guardduty.types.threat_entity_set_format
    import capo_guardduty.types.threat_intel_set_format
    import capo_guardduty.types.trigger_prompt
    import capo_guardduty.types.trusted_entity_set_format
    import capo_guardduty.types.unarchive_findings_request
    import capo_guardduty.types.unarchive_findings_response
    import capo_guardduty.types.untag_resource_request
    import capo_guardduty.types.untag_resource_response
    import capo_guardduty.types.update_custom_detection_rule_association_request
    import capo_guardduty.types.update_custom_detection_rule_association_response
    import capo_guardduty.types.update_custom_detection_rule_org_configuration_request
    import capo_guardduty.types.update_custom_detection_rule_org_configuration_response
    import capo_guardduty.types.update_detector_request
    import capo_guardduty.types.update_detector_response
    import capo_guardduty.types.update_filter_request
    import capo_guardduty.types.update_filter_response
    import capo_guardduty.types.update_findings_feedback_request
    import capo_guardduty.types.update_findings_feedback_response
    import capo_guardduty.types.update_ip_set_request
    import capo_guardduty.types.update_ip_set_response
    import capo_guardduty.types.update_malware_protection_plan_request
    import capo_guardduty.types.update_malware_scan_settings_request
    import capo_guardduty.types.update_malware_scan_settings_response
    import capo_guardduty.types.update_member_detectors_request
    import capo_guardduty.types.update_member_detectors_response
    import capo_guardduty.types.update_organization_configuration_request
    import capo_guardduty.types.update_organization_configuration_response
    import capo_guardduty.types.update_protected_resource
    import capo_guardduty.types.update_publishing_destination_request
    import capo_guardduty.types.update_publishing_destination_response
    import capo_guardduty.types.update_threat_entity_set_request
    import capo_guardduty.types.update_threat_entity_set_response
    import capo_guardduty.types.update_threat_intel_set_request
    import capo_guardduty.types.update_threat_intel_set_response
    import capo_guardduty.types.update_trusted_entity_set_request
    import capo_guardduty.types.update_trusted_entity_set_response
    import capo_guardduty.types.usage_criteria
    import capo_guardduty.types.usage_statistic_type


class GuardDutyClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class GuardDutyClient:
    """A client for the ``GuardDuty`` service.

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
        self._config = GuardDutyClientConfig(
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
        self, config_overrides: Optional[GuardDutyClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: GuardDutyClientConfig = config_overrides or {}
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

    def accept_administrator_invitation(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        administrator_id: Optional["capo_guardduty.types.string.String"] = None,
        invitation_id: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse":
        """<p>Accepts the invitation to be a member account and get monitored by a GuardDuty administrator account that sent the invitation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>
            administrator_id: <p>The account ID of the GuardDuty administrator account whose invitation you're accepting.</p>
            invitation_id: <p>The value that is used to validate the administrator account to the member account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.accept_administrator_invitation

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.accept_administrator_invitation.accept_administrator_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest = {
            "detector_id": detector_id
        }
        if administrator_id is not None:
            input_["administrator_id"] = administrator_id
        if invitation_id is not None:
            input_["invitation_id"] = invitation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def accept_invitation(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        master_id: Optional["capo_guardduty.types.string.String"] = None,
        invitation_id: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.accept_invitation_response.AcceptInvitationResponse":
        """<p>Accepts the invitation to be monitored by a GuardDuty administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            master_id: <p>The account ID of the GuardDuty administrator account whose invitation you're accepting.</p>
            invitation_id: <p>The value that is used to validate the administrator account to the member account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.accept_invitation_response.AcceptInvitationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.accept_invitation

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.accept_invitation.accept_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.accept_invitation_request.AcceptInvitationRequest = {
            "detector_id": detector_id
        }
        if master_id is not None:
            input_["master_id"] = master_id
        if invitation_id is not None:
            input_["invitation_id"] = invitation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def archive_findings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_ids: Optional["capo_guardduty.types.finding_ids.FindingIds"] = None,
    ) -> "capo_guardduty.types.archive_findings_response.ArchiveFindingsResponse":
        """<p>Archives GuardDuty findings that are specified by the list of finding IDs.</p> <note> <p>Only the administrator account can archive findings. Member accounts don't have permission to archive findings from their accounts.</p> </note>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose findings you want to archive.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings that you want to archive.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.archive_findings_request.ArchiveFindingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.archive_findings_response.ArchiveFindingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.archive_findings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.archive_findings.archive_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.archive_findings_request.ArchiveFindingsRequest = {
            "detector_id": detector_id
        }
        if finding_ids is not None:
            input_["finding_ids"] = finding_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_custom_detection_rule_association(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        rule_id: Optional["capo_guardduty.types.rule_id.RuleId"] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
    ) -> "capo_guardduty.types.create_custom_detection_rule_association_response.CreateCustomDetectionRuleAssociationResponse":
        """<p>Enables a custom detection rule for your account by creating an association. You specify the rule and the mode in which it operates.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            mode: <p>The rule execution mode. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. Maximum 64 characters.</p>
            tags: <p>The tags to be added to the new custom detection rule association resource.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_custom_detection_rule_association_request.CreateCustomDetectionRuleAssociationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_custom_detection_rule_association_response.CreateCustomDetectionRuleAssociationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_custom_detection_rule_association

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_custom_detection_rule_association.create_custom_detection_rule_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_custom_detection_rule_association_request.CreateCustomDetectionRuleAssociationRequest = {}
        if rule_id is not None:
            input_["rule_id"] = rule_id
        if mode is not None:
            input_["mode"] = mode
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

    def create_custom_detection_rule_org_configuration(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        rule_id: Optional["capo_guardduty.types.rule_id.RuleId"] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
        include_account_ids: Optional[
            "capo_guardduty.types.detection_rule_account_ids.DetectionRuleAccountIds"
        ] = None,
        exclude_account_ids: Optional[
            "capo_guardduty.types.detection_rule_account_ids.DetectionRuleAccountIds"
        ] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
    ) -> "capo_guardduty.types.create_custom_detection_rule_org_configuration_response.CreateCustomDetectionRuleOrgConfigurationResponse":
        """<p>Creates an organization-level configuration that enables a custom detection rule across your organization. This operation is available only to the delegated administrator account.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            mode: <p>The execution mode of the organization configuration. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>
            include_account_ids: <p>The account IDs to include in the organization configuration. Mutually exclusive with <code>ExcludeAccountIds</code>.</p>
            exclude_account_ids: <p>The account IDs to exclude from the organization configuration. Mutually exclusive with <code>IncludeAccountIds</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_custom_detection_rule_org_configuration_request.CreateCustomDetectionRuleOrgConfigurationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_custom_detection_rule_org_configuration_response.CreateCustomDetectionRuleOrgConfigurationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_custom_detection_rule_org_configuration

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_custom_detection_rule_org_configuration.create_custom_detection_rule_org_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_custom_detection_rule_org_configuration_request.CreateCustomDetectionRuleOrgConfigurationRequest = {}
        if rule_id is not None:
            input_["rule_id"] = rule_id
        if mode is not None:
            input_["mode"] = mode
        if include_account_ids is not None:
            input_["include_account_ids"] = include_account_ids
        if exclude_account_ids is not None:
            input_["exclude_account_ids"] = exclude_account_ids
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

    def create_detector(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        enable: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        finding_publishing_frequency: Optional[
            "capo_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
        ] = None,
        data_sources: Optional[
            "capo_guardduty.types.data_source_configurations.DataSourceConfigurations"
        ] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
        features: Optional[
            "capo_guardduty.types.detector_feature_configurations.DetectorFeatureConfigurations"
        ] = None,
    ) -> "capo_guardduty.types.create_detector_response.CreateDetectorResponse":
        """<p>Creates a single GuardDuty detector. A detector is a resource that represents the GuardDuty service. To start using GuardDuty, you must create a detector in each Region where you enable the service. You can have only one detector per account per Region. All data sources are enabled in a new detector by default.</p> <ul> <li> <p>When you don't specify any <code>features</code>, with an exception to <code>RUNTIME_MONITORING</code>, all the optional features are enabled by default.</p> </li> <li> <p>When you specify some of the <code>features</code>, any feature that is not specified in the API call gets enabled by default, with an exception to <code>RUNTIME_MONITORING</code>. </p> </li> </ul> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            enable: <p>A Boolean value that specifies whether the detector is to be enabled.</p>
            client_token: <p>The idempotency token for the create request.</p>
            finding_publishing_frequency: <p>A value that specifies how frequently updated findings are exported.</p>
            data_sources: <p>Describes which data sources will be enabled for the detector.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>
            tags: <p>The tags to be added to a new detector resource.</p>
            features: <p>A list of features that will be configured for the detector.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_detector_request.CreateDetectorRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_detector_response.CreateDetectorResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_detector

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_detector.create_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_detector_request.CreateDetectorRequest = {}
        if enable is not None:
            input_["enable"] = enable
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if finding_publishing_frequency is not None:
            input_["finding_publishing_frequency"] = finding_publishing_frequency
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if tags is not None:
            input_["tags"] = tags
        if features is not None:
            input_["features"] = features

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_filter(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.filter_name.FilterName"] = None,
        description: Optional[
            "capo_guardduty.types.filter_description.FilterDescription"
        ] = None,
        action: Optional["capo_guardduty.types.filter_action.FilterAction"] = None,
        rank: Optional["capo_guardduty.types.filter_rank.FilterRank"] = None,
        finding_criteria: Optional[
            "capo_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
    ) -> "capo_guardduty.types.create_filter_response.CreateFilterResponse":
        """<p>Creates a filter using the specified finding criteria. The maximum number of saved filters per Amazon Web Services account per Region is 100. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_limits.html">Quotas for GuardDuty</a>.</p>

        Args:
            detector_id: <p>The detector ID associated with the GuardDuty account for which you want to create a filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            name: <p>The name of the filter. Valid characters include period (.), underscore (_), dash (-), and alphanumeric characters. A whitespace is considered to be an invalid character.</p>
            description: <p>The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses (<code>{ }</code>, <code>[ ]</code>, and <code>( )</code>), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.</p>
            action: <p>Specifies the action that is to be applied to the findings that match the filter.</p> <p>Default: NOOP</p>
            rank: <p>Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.</p>
            finding_criteria: <p>Represents the criteria to be used in the filter for querying findings. The following fields are available for filtering:</p> <ul> <li> <p>accountId</p> </li> <li> <p>arn</p> </li> <li> <p>associatedAttackSequenceArn</p> </li> <li> <p>confidence</p> </li> <li> <p>createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>id</p> </li> <li> <p>partition</p> </li> <li> <p>region</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.attributes.mfaAuthenticated</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.ec2RoleDelivery</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.invokedBy</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.userName</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sourceIdentity</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.attributes</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.federatedProvider</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.userName</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailArn</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailVersion</p> </li> <li> <p>resource.containerDetails.containerRuntime</p> </li> <li> <p>resource.containerDetails.id</p> </li> <li> <p>resource.containerDetails.image</p> </li> <li> <p>resource.containerDetails.imagePrefix</p> </li> <li> <p>resource.containerDetails.name</p> </li> <li> <p>resource.containerDetails.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.containerDetails.securityContext.privileged</p> </li> <li> <p>resource.containerDetails.volumeMounts.mountPath</p> </li> <li> <p>resource.containerDetails.volumeMounts.name</p> </li> <li> <p>resource.ebsSnapshotDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeType</p> </li> <li> <p>resource.ec2ImageDetails.imageArn</p> </li> <li> <p>resource.ecsClusterDetails.activeServicesCount</p> </li> <li> <p>resource.ecsClusterDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.name</p> </li> <li> <p>resource.ecsClusterDetails.registeredContainerInstancesCount</p> </li> <li> <p>resource.ecsClusterDetails.runningTasksCount</p> </li> <li> <p>resource.ecsClusterDetails.status</p> </li> <li> <p>resource.ecsClusterDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.containerRuntime</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.id</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.image</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.imagePrefix</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.definitionArn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.group</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.launchType</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedBy</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.version</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.hostPath.path</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.name</p> </li> <li> <p>resource.eksClusterDetails.arn</p> </li> <li> <p>resource.eksClusterDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.eksClusterDetails.name</p> </li> <li> <p>resource.eksClusterDetails.status</p> </li> <li> <p>resource.eksClusterDetails.tags.key</p> </li> <li> <p>resource.eksClusterDetails.tags.value</p> </li> <li> <p>resource.eksClusterDetails.vpcId</p> </li> <li> <p>resource.instanceDetails.availabilityZone</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.arn</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageDescription</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.instanceState</p> </li> <li> <p>resource.instanceDetails.instanceType</p> </li> <li> <p>resource.instanceDetails.launchTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.networkInterfaceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.outpostArn</p> </li> <li> <p>resource.instanceDetails.platform</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeId</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeType</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.sessionName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.containerRuntime</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.id</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.imagePrefix</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostIpc</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostNetwork</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostPid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.namespace</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.type</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.hostPath.path</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.name</p> </li> <li> <p>resource.lambdaDetails.description</p> </li> <li> <p>resource.lambdaDetails.functionArn</p> </li> <li> <p>resource.lambdaDetails.functionName</p> </li> <li> <p>resource.lambdaDetails.functionVersion</p> </li> <li> <p>resource.lambdaDetails.lastModifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.lambdaDetails.revisionId</p> </li> <li> <p>resource.lambdaDetails.role</p> </li> <li> <p>resource.lambdaDetails.tags.key</p> </li> <li> <p>resource.lambdaDetails.tags.value</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupId</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupName</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.subnetIds</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceArn</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.name</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbiResourceId</p> </li> <li> <p>resource.rdsDbInstanceDetails.engine</p> </li> <li> <p>resource.rdsDbInstanceDetails.engineVersion</p> </li> <li> <p>resource.rdsDbInstanceDetails.iamDatabaseAuthenticationEnabled</p> </li> <li> <p>resource.rdsDbInstanceDetails.publiclyAccessible</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.vpcSecurityGroupId</p> </li> <li> <p>resource.rdsDbUserDetails.application</p> </li> <li> <p>resource.rdsDbUserDetails.authMethod</p> </li> <li> <p>resource.rdsDbUserDetails.database</p> </li> <li> <p>resource.rdsDbUserDetails.ssl</p> </li> <li> <p>resource.rdsDbUserDetails.user</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupArn</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupResourceId</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engine</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engineVersion</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.key</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.value</p> </li> <li> <p>resource.recoveryPointDetails.backupVaultName</p> </li> <li> <p>resource.recoveryPointDetails.recoveryPointArn</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>resource.s3BucketDetails.arn</p> </li> <li> <p>resource.s3BucketDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.encryptionType</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.kmsMasterKeyArn</p> </li> <li> <p>resource.s3BucketDetails.name</p> </li> <li> <p>resource.s3BucketDetails.owner.id</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.effectivePermission</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.eTag</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.hash</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.key</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.objectArn</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.versionId</p> </li> <li> <p>resource.s3BucketDetails.tags.key</p> </li> <li> <p>resource.s3BucketDetails.tags.value</p> </li> <li> <p>resource.s3BucketDetails.type</p> </li> <li> <p>schemaVersion</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.domainDetails.domain</p> </li> <li> <p>service.action.awsApiCallAction.errorCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.accountId</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.affiliated</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.awsServiceName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.awsApiCallAction.userAgent</p> </li> <li> <p>service.action.dnsRequestAction.blocked</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.dnsRequestAction.protocol</p> </li> <li> <p>service.action.dnsRequestAction.vpcOwnerAccountId</p> </li> <li> <p>service.action.kubernetesApiCallAction.namespace</p> </li> <li> <p>service.action.kubernetesApiCallAction.parameters</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.kubernetesApiCallAction.requestUri</p> </li> <li> <p>service.action.kubernetesApiCallAction.resource</p> </li> <li> <p>service.action.kubernetesApiCallAction.resourceName</p> </li> <li> <p>service.action.kubernetesApiCallAction.sourceIPs</p> </li> <li> <p>service.action.kubernetesApiCallAction.statusCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.subresource</p> </li> <li> <p>service.action.kubernetesApiCallAction.userAgent</p> </li> <li> <p>service.action.kubernetesApiCallAction.verb</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.allowed</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.namespace</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.resource</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.verb</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.name</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefKind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefName</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.uid</p> </li> <li> <p>service.action.kubernetesRoleDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleDetails.name</p> </li> <li> <p>service.action.kubernetesRoleDetails.uid</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.localNetworkInterface</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.portName</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.blocked</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.port</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.application</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.failedLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.successfulLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.user</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.additionalInfo.agentDetails.agentId</p> </li> <li> <p>service.additionalInfo.agentDetails.agentVersion</p> </li> <li> <p>service.additionalInfo.anomalies.anomalousAPIs</p> </li> <li> <p>service.additionalInfo.authenticationMethod</p> </li> <li> <p>service.additionalInfo.averagePacketSizeIn</p> </li> <li> <p>service.additionalInfo.averagePacketSizeOut</p> </li> <li> <p>service.additionalInfo.context</p> </li> <li> <p>service.additionalInfo.domain</p> </li> <li> <p>service.additionalInfo.inBytes</p> </li> <li> <p>service.additionalInfo.localNetworkInterfaceOwner</p> </li> <li> <p>service.additionalInfo.localPort</p> </li> <li> <p>service.additionalInfo.outBytes</p> </li> <li> <p>service.additionalInfo.packetsIn</p> </li> <li> <p>service.additionalInfo.packetsOut</p> </li> <li> <p>service.additionalInfo.policyArn</p> </li> <li> <p>service.additionalInfo.policyName</p> </li> <li> <p>service.additionalInfo.remotePort</p> </li> <li> <p>service.additionalInfo.sample</p> </li> <li> <p>service.additionalInfo.scannedPort</p> </li> <li> <p>service.additionalInfo.threatFileSha256</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.additionalInfo.threatName</p> </li> <li> <p>service.additionalInfo.totalBytesIn</p> </li> <li> <p>service.additionalInfo.totalBytesOut</p> </li> <li> <p>service.additionalInfo.type</p> </li> <li> <p>service.additionalInfo.unusual.asnOrg</p> </li> <li> <p>service.additionalInfo.unusual.port</p> </li> <li> <p>service.additionalInfo.unusualProtocol</p> </li> <li> <p>service.additionalInfo.userAgent.fullUserAgent</p> </li> <li> <p>service.additionalInfo.userAgent.userAgentCategory</p> </li> <li> <p>service.additionalInfo.value</p> </li> <li> <p>service.additionalInfo.vpcOwnerAccountId</p> </li> <li> <p>service.archived</p> </li> <li> <p>service.count</p> </li> <li> <p>service.detection.sequence.actors.id</p> </li> <li> <p>service.detection.sequence.actors.process.name</p> </li> <li> <p>service.detection.sequence.actors.process.path</p> </li> <li> <p>service.detection.sequence.actors.process.sha256</p> </li> <li> <p>service.detection.sequence.actors.session.createdTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.actors.session.issuer</p> </li> <li> <p>service.detection.sequence.actors.session.mfaStatus</p> </li> <li> <p>service.detection.sequence.actors.session.uid</p> </li> <li> <p>service.detection.sequence.actors.user.account.account</p> </li> <li> <p>service.detection.sequence.actors.user.account.uid</p> </li> <li> <p>service.detection.sequence.actors.user.credentialUid</p> </li> <li> <p>service.detection.sequence.actors.user.name</p> </li> <li> <p>service.detection.sequence.actors.user.type</p> </li> <li> <p>service.detection.sequence.actors.user.uid</p> </li> <li> <p>service.detection.sequence.additionalSequenceTypes</p> </li> <li> <p>service.detection.sequence.description</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.name</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.number</p> </li> <li> <p>service.detection.sequence.endpoints.connection.direction</p> </li> <li> <p>service.detection.sequence.endpoints.domain</p> </li> <li> <p>service.detection.sequence.endpoints.id</p> </li> <li> <p>service.detection.sequence.endpoints.ip</p> </li> <li> <p>service.detection.sequence.endpoints.location.city</p> </li> <li> <p>service.detection.sequence.endpoints.location.country</p> </li> <li> <p>service.detection.sequence.endpoints.location.lat</p> </li> <li> <p>service.detection.sequence.endpoints.location.lon</p> </li> <li> <p>service.detection.sequence.endpoints.port</p> </li> <li> <p>service.detection.sequence.resources.accountId</p> </li> <li> <p>service.detection.sequence.resources.cloudPartition</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.principalId</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userName</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userType</p> </li> <li> <p>service.detection.sequence.resources.data.autoscalingAutoScalingGroup.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.cloudformationStack.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.container.image</p> </li> <li> <p>service.detection.sequence.resources.data.container.imageUid</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Image.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.availabilityZone</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.ec2NetworkInterfaceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.arn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.imageDescription</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceState</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.outpostArn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.platform</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.version</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.ipv6Addresses</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateDnsName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateIpAddress</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.publicIp</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.subNetId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Vpc.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.launchType</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.taskDefinitionArn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.arn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.namespace</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.type</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.effectivePermission</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionKeyArn</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionType</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.ownerId</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicReadAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicWriteAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.s3ObjectUids</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.eTag</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.key</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.versionId</p> </li> <li> <p>service.detection.sequence.resources.name</p> </li> <li> <p>service.detection.sequence.resources.region</p> </li> <li> <p>service.detection.sequence.resources.resourceType</p> </li> <li> <p>service.detection.sequence.resources.service</p> </li> <li> <p>service.detection.sequence.resources.tags.key</p> </li> <li> <p>service.detection.sequence.resources.tags.value</p> </li> <li> <p>service.detection.sequence.resources.uid</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.key</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.title</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.actorIds</p> </li> <li> <p>service.detection.sequence.signals.count</p> </li> <li> <p>service.detection.sequence.signals.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.description</p> </li> <li> <p>service.detection.sequence.signals.endpointIds</p> </li> <li> <p>service.detection.sequence.signals.firstSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.lastSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.name</p> </li> <li> <p>service.detection.sequence.signals.resourceUids</p> </li> <li> <p>service.detection.sequence.signals.severity</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.key</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.title</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.type</p> </li> <li> <p>service.detection.sequence.signals.uid</p> </li> <li> <p>service.detection.sequence.signals.updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.uid</p> </li> <li> <p>service.detectorId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanCompletedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.count</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.threatName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.totalGb</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.volumes</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.shortened</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.fileName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.volumeArn</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.name</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.uniqueThreatNameCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatsDetectedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanStartedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanType</p> </li> <li> <p>service.ebsVolumeScanDetails.sources</p> </li> <li> <p>service.ebsVolumeScanDetails.triggerFindingId</p> </li> <li> <p>service.eventFirstSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.eventLastSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatFileSha256</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatListName</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatNames</p> </li> <li> <p>service.featureName</p> </li> <li> <p>service.malwareScanDetails.scanCategory</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.incrementalScanDetails.baselineResourceArn</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.triggerType</p> </li> <li> <p>service.malwareScanDetails.scanId</p> </li> <li> <p>service.malwareScanDetails.scanType</p> </li> <li> <p>service.malwareScanDetails.threats.count</p> </li> <li> <p>service.malwareScanDetails.threats.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.deviceName</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.versionId</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.itemPath</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.resourceArn</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.nestedItemPath</p> </li> <li> <p>service.malwareScanDetails.threats.name</p> </li> <li> <p>service.malwareScanDetails.threats.source</p> </li> <li> <p>service.malwareScanDetails.uniqueThreatCount</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>service.runtimeDetails.context.addressFamily</p> </li> <li> <p>service.runtimeDetails.context.commandLineExample</p> </li> <li> <p>service.runtimeDetails.context.fileOperation</p> </li> <li> <p>service.runtimeDetails.context.filePath</p> </li> <li> <p>service.runtimeDetails.context.fileSystemType</p> </li> <li> <p>service.runtimeDetails.context.flags</p> </li> <li> <p>service.runtimeDetails.context.ianaProtocolNumber</p> </li> <li> <p>service.runtimeDetails.context.ldPreloadValue</p> </li> <li> <p>service.runtimeDetails.context.libraryPath</p> </li> <li> <p>service.runtimeDetails.context.memoryRegions</p> </li> <li> <p>service.runtimeDetails.context.modifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.user</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.moduleFilePath</p> </li> <li> <p>service.runtimeDetails.context.moduleName</p> </li> <li> <p>service.runtimeDetails.context.moduleSha256</p> </li> <li> <p>service.runtimeDetails.context.mountSource</p> </li> <li> <p>service.runtimeDetails.context.mountTarget</p> </li> <li> <p>service.runtimeDetails.context.relatedFilePaths</p> </li> <li> <p>service.runtimeDetails.context.releaseAgentPath</p> </li> <li> <p>service.runtimeDetails.context.runcBinaryPath</p> </li> <li> <p>service.runtimeDetails.context.scriptPath</p> </li> <li> <p>service.runtimeDetails.context.serviceName</p> </li> <li> <p>service.runtimeDetails.context.shellHistoryFilePath</p> </li> <li> <p>service.runtimeDetails.context.socketPath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.user</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.threatFilePath</p> </li> <li> <p>service.runtimeDetails.context.toolCategory</p> </li> <li> <p>service.runtimeDetails.context.toolName</p> </li> <li> <p>service.runtimeDetails.process.euid</p> </li> <li> <p>service.runtimeDetails.process.executablePath</p> </li> <li> <p>service.runtimeDetails.process.executableSha256</p> </li> <li> <p>service.runtimeDetails.process.lineage.euid</p> </li> <li> <p>service.runtimeDetails.process.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.process.lineage.name</p> </li> <li> <p>service.runtimeDetails.process.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.lineage.pid</p> </li> <li> <p>service.runtimeDetails.process.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.lineage.userId</p> </li> <li> <p>service.runtimeDetails.process.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.process.name</p> </li> <li> <p>service.runtimeDetails.process.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.pid</p> </li> <li> <p>service.runtimeDetails.process.pwd</p> </li> <li> <p>service.runtimeDetails.process.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.user</p> </li> <li> <p>service.runtimeDetails.process.userId</p> </li> <li> <p>service.runtimeDetails.process.uuid</p> </li> <li> <p>service.serviceName</p> </li> <li> <p>service.userFeedback</p> </li> <li> <p>severity</p> <p>To configure severity based filters, use the following for the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingCriteria.html">FindingCriteria</a> condition:</p> <ul> <li> <p> <b>Low</b>: <code>["1", "2", "3"]</code> </p> </li> <li> <p> <b>Medium</b>: <code>["4", "5", "6"]</code> </p> </li> <li> <p> <b>High</b>: <code>["7", "8"]</code> </p> </li> <li> <p> <b>Critical</b>: <code>["9", "10"]</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html">Findings severity levels</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> </ul>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new filter resource.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_filter_request.CreateFilterRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_filter_response.CreateFilterResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_filter

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_filter.create_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_filter_request.CreateFilterRequest = {
            "detector_id": detector_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if action is not None:
            input_["action"] = action
        if rank is not None:
            input_["rank"] = rank
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
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

    def create_investigation(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        trigger_prompt: Optional[
            "capo_guardduty.types.trigger_prompt.TriggerPrompt"
        ] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_guardduty.types.create_investigation_response.CreateInvestigationResponse"
    ):
        """<p>This API is currently available as a preview. During the preview, you can initiate up to 10 investigations per account per day, with a total limit of 100 investigations per account. This feature is available in the following Amazon Web Services Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).</p> <p>Initiates a GuardDuty investigation that automatically analyzes security findings, correlates related activity, performs account-level analysis, and produces a structured investigation summary with recommended next steps.</p> <p>Only the administrator account can create an investigation. Member accounts don't have permission to create investigations from their accounts.</p> <p>To use this operation, the <code>AI_ANALYST</code> feature must be enabled on your detector.</p> <p>This feature uses Amazon Bedrock models that leverage Cross-Region Inference (CRIS), which automatically selects the optimal Amazon Web Services Region within your geography to process the investigation analysis and generate the investigation report. This maximizes available compute resources, model availability, and delivers the best customer experience. Your data remains stored only in the Region where the investigation request originates, however, investigation data and summary results may be processed outside that Region. All data is transmitted encrypted across Amazon's secure network. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-investigation.html">GuardDuty Investigation</a>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector for the account in which the investigation is created.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            trigger_prompt: <p>A natural-language description of what to investigate. For example:</p> <ul> <li> <p> <code>"Investigate finding 1ab2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 in account 123456789012"</code> </p> </li> <li> <p> <code>"Analyze findings in account with id 123456789012"</code> </p> </li> <li> <p> <code>"Analyze findings in my organization"</code> </p> </li> </ul>
            client_token: <p>The idempotency token for the create request.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_investigation_request.CreateInvestigationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_investigation_response.CreateInvestigationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_investigation

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_investigation.create_investigation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_investigation_request.CreateInvestigationRequest = {
            "detector_id": detector_id
        }
        if trigger_prompt is not None:
            input_["trigger_prompt"] = trigger_prompt
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

    def create_ip_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        format: Optional["capo_guardduty.types.ip_set_format.IpSetFormat"] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "capo_guardduty.types.create_ip_set_response.CreateIPSetResponse":
        """<p>Creates a new IPSet, which is called a trusted IP list in the console user interface. An IPSet is a list of IP addresses that are trusted for secure communication with Amazon Web Services infrastructure and applications. GuardDuty doesn't generate findings for IP addresses that are included in IPSets. Only users from the administrator account can use this operation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            name: <p>The user-friendly name to identify the IPSet.</p> <p> Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).</p>
            format: <p>The format of the file that contains the IPSet.</p>
            location: <p>The URI of the file that contains the IPSet. </p>
            activate: <p>A Boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new IP set resource.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_ip_set_request.CreateIPSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_ip_set_response.CreateIPSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_ip_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_ip_set.create_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_ip_set_request.CreateIPSetRequest = {
            "detector_id": detector_id
        }
        if name is not None:
            input_["name"] = name
        if format is not None:
            input_["format"] = format
        if location is not None:
            input_["location"] = location
        if activate is not None:
            input_["activate"] = activate
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_malware_protection_plan(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        role: Optional["capo_guardduty.types.string.String"] = None,
        protected_resource: Optional[
            "capo_guardduty.types.create_protected_resource.CreateProtectedResource"
        ] = None,
        actions: Optional[
            "capo_guardduty.types.malware_protection_plan_actions.MalwareProtectionPlanActions"
        ] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
    ) -> "capo_guardduty.types.create_malware_protection_plan_response.CreateMalwareProtectionPlanResponse":
        """<p>Creates a new Malware Protection plan for the protected resource.</p> <p>When you create a Malware Protection plan, the Amazon Web Services service terms for GuardDuty Malware Protection apply. For more information, see <a href="http://aws.amazon.com/service-terms/#87._Amazon_GuardDuty">Amazon Web Services service terms for GuardDuty Malware Protection</a>.</p>

        Args:
            client_token: <p>The idempotency token for the create request.</p>
            role: <p>Amazon Resource Name (ARN) of the IAM role that has the permissions to scan and add tags to the associated protected resource.</p>
            protected_resource: <p>Information about the protected resource that is associated with the created Malware Protection plan. Presently, <code>S3Bucket</code> is the only supported protected resource.</p>
            actions: <p>Information about whether the tags will be added to the S3 object after scanning.</p>
            tags: <p>Tags added to the Malware Protection plan resource. </p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_malware_protection_plan_request.CreateMalwareProtectionPlanRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_malware_protection_plan_response.CreateMalwareProtectionPlanResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_malware_protection_plan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_malware_protection_plan.create_malware_protection_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_malware_protection_plan_request.CreateMalwareProtectionPlanRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if role is not None:
            input_["role"] = role
        if protected_resource is not None:
            input_["protected_resource"] = protected_resource
        if actions is not None:
            input_["actions"] = actions
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_details: Optional[
            "capo_guardduty.types.account_details.AccountDetails"
        ] = None,
    ) -> "capo_guardduty.types.create_members_response.CreateMembersResponse":
        """<p>Creates member accounts of the current Amazon Web Services account by specifying a list of Amazon Web Services account IDs. This step is a prerequisite for managing the associated member accounts either by invitation or through an organization.</p> <p>As a delegated administrator, using <code>CreateMembers</code> will enable GuardDuty in the added member accounts, with the exception of the organization delegated administrator account. A delegated administrator must enable GuardDuty prior to being added as a member.</p> <p>When you use CreateMembers as an Organizations delegated administrator, GuardDuty applies your organization's auto-enable settings to the member accounts in this request, irrespective of the accounts being new or existing members. For more information about the existing auto-enable settings for your organization, see <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html">DescribeOrganizationConfiguration</a>.</p> <p>If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a> API. </p> <p>When the member accounts added through Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to associate member accounts.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_details: <p>A list of account ID and email address pairs of the accounts that you want to associate with the GuardDuty administrator account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_members_request.CreateMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_members_response.CreateMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_members.create_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_members_request.CreateMembersRequest = {
            "detector_id": detector_id
        }
        if account_details is not None:
            input_["account_details"] = account_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_publishing_destination(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        destination_type: Optional[
            "capo_guardduty.types.destination_type.DestinationType"
        ] = None,
        destination_properties: Optional[
            "capo_guardduty.types.destination_properties.DestinationProperties"
        ] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
    ) -> "capo_guardduty.types.create_publishing_destination_response.CreatePublishingDestinationResponse":
        """<p>Creates a publishing destination where you can export your GuardDuty findings. Before you start exporting the findings, the destination resource must exist.</p>

        Args:
            detector_id: <p>The ID of the GuardDuty detector associated with the publishing destination.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            destination_type: <p>The type of resource for the publishing destination. Currently only Amazon S3 buckets are supported.</p>
            destination_properties: <p>The properties of the publishing destination, including the ARNs for the destination and the KMS key used for encryption.</p>
            client_token: <p>The idempotency token for the request.</p>
            tags: <p>The tags to be added to a new publishing destination resource.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_publishing_destination_request.CreatePublishingDestinationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_publishing_destination_response.CreatePublishingDestinationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_publishing_destination

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_publishing_destination.create_publishing_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_publishing_destination_request.CreatePublishingDestinationRequest = {
            "detector_id": detector_id
        }
        if destination_type is not None:
            input_["destination_type"] = destination_type
        if destination_properties is not None:
            input_["destination_properties"] = destination_properties
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

    def create_sample_findings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_types: Optional[
            "capo_guardduty.types.finding_types.FindingTypes"
        ] = None,
    ) -> "capo_guardduty.types.create_sample_findings_response.CreateSampleFindingsResponse":
        """<p>Generates sample findings of types specified by the list of finding types. If 'NULL' is specified for <code>findingTypes</code>, the API generates sample findings of all supported finding types.</p>

        Args:
            detector_id: <p>The ID of the detector for which you need to create sample findings.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_types: <p>The types of sample findings to generate.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_sample_findings_request.CreateSampleFindingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_sample_findings_response.CreateSampleFindingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_sample_findings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_sample_findings.create_sample_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_sample_findings_request.CreateSampleFindingsRequest = {
            "detector_id": detector_id
        }
        if finding_types is not None:
            input_["finding_types"] = finding_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_threat_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        format: Optional[
            "capo_guardduty.types.threat_entity_set_format.ThreatEntitySetFormat"
        ] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
    ) -> "capo_guardduty.types.create_threat_entity_set_response.CreateThreatEntitySetResponse":
        """<p>Creates a new threat entity set. In a threat entity set, you can provide known malicious threat entities for your Amazon Web Services environment. GuardDuty generates findings based on the entries in the threat entity sets. Only users of the administrator account can manage entity sets, which automatically apply to member accounts.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create a threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            name: <p>A user-friendly name to identify the threat entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            format: <p>The format of the file that contains the threat entity set.</p>
            location: <p>The URI of the file that contains the threat entity set. The format of the <code>Location</code> URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html">Format of location URL under Step 2: Adding trusted or threat intelligence data</a> in the <i>Amazon GuardDuty User Guide</i>.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty should start using the uploaded threat entity set to generate findings.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new threat entity set resource.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_threat_entity_set_request.CreateThreatEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_threat_entity_set_response.CreateThreatEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_threat_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_threat_entity_set.create_threat_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_threat_entity_set_request.CreateThreatEntitySetRequest = {
            "detector_id": detector_id
        }
        if name is not None:
            input_["name"] = name
        if format is not None:
            input_["format"] = format
        if location is not None:
            input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        if activate is not None:
            input_["activate"] = activate
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

    def create_threat_intel_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        format: Optional[
            "capo_guardduty.types.threat_intel_set_format.ThreatIntelSetFormat"
        ] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "capo_guardduty.types.create_threat_intel_set_response.CreateThreatIntelSetResponse":
        """<p>Creates a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty generates findings based on ThreatIntelSets. Only users of the administrator account can use this operation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create a <code>threatIntelSet</code>.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            name: <p>A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.</p>
            format: <p>The format of the file that contains the ThreatIntelSet.</p>
            location: <p>The URI of the file that contains the ThreatIntelSet. </p>
            activate: <p>A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new threat list resource.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_threat_intel_set_request.CreateThreatIntelSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_threat_intel_set_response.CreateThreatIntelSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_threat_intel_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_threat_intel_set.create_threat_intel_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_threat_intel_set_request.CreateThreatIntelSetRequest = {
            "detector_id": detector_id
        }
        if name is not None:
            input_["name"] = name
        if format is not None:
            input_["format"] = format
        if location is not None:
            input_["location"] = location
        if activate is not None:
            input_["activate"] = activate
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_trusted_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        format: Optional[
            "capo_guardduty.types.trusted_entity_set_format.TrustedEntitySetFormat"
        ] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        tags: Optional["capo_guardduty.types.tag_map.TagMap"] = None,
    ) -> "capo_guardduty.types.create_trusted_entity_set_response.CreateTrustedEntitySetResponse":
        """<p>Creates a new trusted entity set. In the trusted entity set, you can provide IP addresses and domains that you believe are secure for communication in your Amazon Web Services environment. GuardDuty will not generate findings for the entries that are specified in a trusted entity set. At any given time, you can have only one trusted entity set. </p> <p>Only users of the administrator account can manage the entity sets, which automatically apply to member accounts.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create a trusted entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            name: <p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            format: <p>The format of the file that contains the trusted entity set.</p>
            location: <p>The URI of the file that contains the threat entity set. The format of the <code>Location</code> URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html">Format of location URL under Step 2: Adding trusted or threat intelligence data</a> in the <i>Amazon GuardDuty User Guide</i>.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty is to start using the uploaded trusted entity set.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new trusted entity set resource.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.create_trusted_entity_set_request.CreateTrustedEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.create_trusted_entity_set_response.CreateTrustedEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.create_trusted_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.create_trusted_entity_set.create_trusted_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.create_trusted_entity_set_request.CreateTrustedEntitySetRequest = {
            "detector_id": detector_id
        }
        if name is not None:
            input_["name"] = name
        if format is not None:
            input_["format"] = format
        if location is not None:
            input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        if activate is not None:
            input_["activate"] = activate
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

    def decline_invitations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> "capo_guardduty.types.decline_invitations_response.DeclineInvitationsResponse":
        """<p>Declines invitations sent to the current member account by Amazon Web Services accounts specified by their account IDs.</p>

        Args:
            account_ids: <p>A list of account IDs of the Amazon Web Services accounts that sent invitations to the current member account that you want to decline invitations from.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.decline_invitations_request.DeclineInvitationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.decline_invitations_response.DeclineInvitationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.decline_invitations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.decline_invitations.decline_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.decline_invitations_request.DeclineInvitationsRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_detection_rule_association(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        association_id: "capo_guardduty.types.association_id.AssociationId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_custom_detection_rule_association_response.DeleteCustomDetectionRuleAssociationResponse":
        """<p>Disables a custom detection rule by deleting its association. This operation is idempotent.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            association_id: <p>The unique identifier for the association to delete.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_custom_detection_rule_association_request.DeleteCustomDetectionRuleAssociationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_custom_detection_rule_association_response.DeleteCustomDetectionRuleAssociationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_custom_detection_rule_association

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_custom_detection_rule_association.delete_custom_detection_rule_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_custom_detection_rule_association_request.DeleteCustomDetectionRuleAssociationRequest = {
            "rule_id": rule_id,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_detection_rule_org_configuration(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
    ) -> "capo_guardduty.types.delete_custom_detection_rule_org_configuration_response.DeleteCustomDetectionRuleOrgConfigurationResponse":
        """<p>Deletes the organization-level configuration for a custom detection rule. This operation is available only to the delegated administrator account.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            mode: <p>The execution mode of the organization configuration to delete. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_custom_detection_rule_org_configuration_request.DeleteCustomDetectionRuleOrgConfigurationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_custom_detection_rule_org_configuration_response.DeleteCustomDetectionRuleOrgConfigurationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_custom_detection_rule_org_configuration

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_custom_detection_rule_org_configuration.delete_custom_detection_rule_org_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_custom_detection_rule_org_configuration_request.DeleteCustomDetectionRuleOrgConfigurationRequest = {
            "rule_id": rule_id
        }
        if mode is not None:
            input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_detector(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_detector_response.DeleteDetectorResponse":
        """<p>Deletes an Amazon GuardDuty detector that is specified by the detector ID.</p>

        Args:
            detector_id: <p>The unique ID of the detector that you want to delete.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_detector_request.DeleteDetectorRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_detector_response.DeleteDetectorResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_detector

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_detector.delete_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_detector_request.DeleteDetectorRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_filter(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        filter_name: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_filter_response.DeleteFilterResponse":
        """<p>Deletes the filter specified by the filter name.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            filter_name: <p>The name of the filter that you want to delete.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_filter_request.DeleteFilterRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_filter_response.DeleteFilterResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_filter

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_filter.delete_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_filter_request.DeleteFilterRequest = {
            "detector_id": detector_id,
            "filter_name": filter_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_invitations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> "capo_guardduty.types.delete_invitations_response.DeleteInvitationsResponse":
        """<p>Deletes invitations sent to the current member account by Amazon Web Services accounts specified by their account IDs.</p>

        Args:
            account_ids: <p>A list of account IDs of the Amazon Web Services accounts that sent invitations to the current member account that you want to delete invitations from.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_invitations_request.DeleteInvitationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_invitations_response.DeleteInvitationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_invitations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_invitations.delete_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_invitations_request.DeleteInvitationsRequest = {}
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_ip_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        ip_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_ip_set_response.DeleteIPSetResponse":
        """<p>Deletes the IPSet specified by the <code>ipSetId</code>. IPSets are called trusted IP lists in the console user interface.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            ip_set_id: <p>The unique ID of the IPSet to delete.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_ip_set_request.DeleteIPSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_ip_set_response.DeleteIPSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_ip_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_ip_set.delete_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_ip_set_request.DeleteIPSetRequest = {
            "detector_id": detector_id,
            "ip_set_id": ip_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_malware_protection_plan(
        self,
        malware_protection_plan_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> None:
        """<p>Deletes the Malware Protection plan ID associated with the Malware Protection plan resource. Use this API only when you no longer want to protect the resource associated with this Malware Protection plan ID.</p>

        Args:
            malware_protection_plan_id: <p>A unique identifier associated with Malware Protection plan resource.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_malware_protection_plan_request.DeleteMalwareProtectionPlanRequest]",
        ) -> OperationResponse[None]:
            import capo_guardduty._operations.guard_duty_api_service.delete_malware_protection_plan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_malware_protection_plan.delete_malware_protection_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_malware_protection_plan_request.DeleteMalwareProtectionPlanRequest = {
            "malware_protection_plan_id": malware_protection_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> "capo_guardduty.types.delete_members_response.DeleteMembersResponse":
        """<p>Deletes GuardDuty member accounts (to the current GuardDuty administrator account) specified by the account IDs.</p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to disable GuardDuty for a member account in your organization.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account whose members you want to delete.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts that you want to delete.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_members_request.DeleteMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_members_response.DeleteMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_members.delete_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_members_request.DeleteMembersRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_publishing_destination(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        destination_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_publishing_destination_response.DeletePublishingDestinationResponse":
        """<p>Deletes the publishing definition with the specified <code>destinationId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the publishing destination to delete.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            destination_id: <p>The ID of the publishing destination to delete.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_publishing_destination_request.DeletePublishingDestinationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_publishing_destination_response.DeletePublishingDestinationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_publishing_destination

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_publishing_destination.delete_publishing_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_publishing_destination_request.DeletePublishingDestinationRequest = {
            "detector_id": detector_id,
            "destination_id": destination_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_threat_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        threat_entity_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_threat_entity_set_response.DeleteThreatEntitySetResponse":
        """<p>Deletes the threat entity set that is associated with the specified <code>threatEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the threat entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            threat_entity_set_id: <p>The unique ID that helps GuardDuty identify which threat entity set needs to be deleted.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_threat_entity_set_request.DeleteThreatEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_threat_entity_set_response.DeleteThreatEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_threat_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_threat_entity_set.delete_threat_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_threat_entity_set_request.DeleteThreatEntitySetRequest = {
            "detector_id": detector_id,
            "threat_entity_set_id": threat_entity_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_threat_intel_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        threat_intel_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_threat_intel_set_response.DeleteThreatIntelSetResponse":
        """<p>Deletes the ThreatIntelSet specified by the ThreatIntelSet ID.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            threat_intel_set_id: <p>The unique ID of the threatIntelSet that you want to delete.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_threat_intel_set_request.DeleteThreatIntelSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_threat_intel_set_response.DeleteThreatIntelSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_threat_intel_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_threat_intel_set.delete_threat_intel_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_threat_intel_set_request.DeleteThreatIntelSetRequest = {
            "detector_id": detector_id,
            "threat_intel_set_id": threat_intel_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_trusted_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        trusted_entity_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.delete_trusted_entity_set_response.DeleteTrustedEntitySetResponse":
        """<p>Deletes the trusted entity set that is associated with the specified <code>trustedEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the trusted entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            trusted_entity_set_id: <p>The unique ID that helps GuardDuty identify which trusted entity set needs to be deleted.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.delete_trusted_entity_set_request.DeleteTrustedEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.delete_trusted_entity_set_response.DeleteTrustedEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.delete_trusted_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.delete_trusted_entity_set.delete_trusted_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.delete_trusted_entity_set_request.DeleteTrustedEntitySetRequest = {
            "detector_id": detector_id,
            "trusted_entity_set_id": trusted_entity_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_malware_scans(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        max_results: Optional[
            "capo_guardduty.types.integer_value_with_max.IntegerValueWithMax"
        ] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "capo_guardduty.types.describe_malware_scans_response.DescribeMalwareScansResponse":
        """<p>Returns a list of malware scans. Each member account can view the malware scans for their own accounts. An administrator can view the malware scans for all the member accounts.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that the request is associated with.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            filter_criteria: <p>Represents the criteria to be used in the filter for describing scan entries.</p>
            sort_criteria: <p>Represents the criteria used for sorting scan entries. The <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SortCriteria.html#guardduty-Type-SortCriteria-attributeName"> <code>attributeName</code> </a> is required and it must be <code>scanStartTime</code>.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.describe_malware_scans_request.DescribeMalwareScansRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.describe_malware_scans_response.DescribeMalwareScansResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.describe_malware_scans

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.describe_malware_scans.describe_malware_scans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.describe_malware_scans_request.DescribeMalwareScansRequest = {
            "detector_id": detector_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_malware_scans(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        max_results: Optional[
            "capo_guardduty.types.integer_value_with_max.IntegerValueWithMax"
        ] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "Iterator[capo_guardduty.types.scan.Scan]":
        _token = next_token
        while True:
            _response = self.describe_malware_scans(
                detector_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("scans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_organization_configuration(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Returns information about the account selected as the delegated administrator for GuardDuty.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The detector ID of the delegated administrator for which you need to retrieve the information.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill <code>nextToken</code> in the request with the value of <code>NextToken</code> from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.describe_organization_configuration

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.describe_organization_configuration.describe_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {
            "detector_id": detector_id
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

    def iter_describe_organization_configuration(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse]":
        _token = next_token
        while True:
            _response = self.describe_organization_configuration(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_publishing_destination(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        destination_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.describe_publishing_destination_response.DescribePublishingDestinationResponse":
        """<p>Returns information about the publishing destination specified by the provided <code>destinationId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the publishing destination to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            destination_id: <p>The ID of the publishing destination to retrieve.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.describe_publishing_destination_request.DescribePublishingDestinationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.describe_publishing_destination_response.DescribePublishingDestinationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.describe_publishing_destination

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.describe_publishing_destination.describe_publishing_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.describe_publishing_destination_request.DescribePublishingDestinationRequest = {
            "detector_id": detector_id,
            "destination_id": destination_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_organization_admin_account(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        admin_account_id: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse":
        """<p>Removes the existing GuardDuty delegated administrator of the organization. Only the organization's management account can run this API operation.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services Account ID for the organizations account to be disabled as a GuardDuty delegated administrator.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.disable_organization_admin_account

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.disable_organization_admin_account.disable_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest = {}
        if admin_account_id is not None:
            input_["admin_account_id"] = admin_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_from_administrator_account(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse":
        """<p>Disassociates the current GuardDuty member account from its administrator account.</p> <p>When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html">CreateMembers</a> API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a> API. </p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to disable GuardDuty in a member account.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.disassociate_from_administrator_account

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.disassociate_from_administrator_account.disassociate_from_administrator_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_from_master_account(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse":
        """<p>Disassociates the current GuardDuty member account from its administrator account.</p> <p>When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html">CreateMembers</a> API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a> API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.disassociate_from_master_account

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.disassociate_from_master_account.disassociate_from_master_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> (
        "capo_guardduty.types.disassociate_members_response.DisassociateMembersResponse"
    ):
        """<p>Disassociates GuardDuty member accounts (from the current administrator account) specified by the account IDs.</p> <p>When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html">CreateMembers</a> API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a> API. </p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to disassociate a member account before removing them from your organization.</p> <p>If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a> API. </p> <p>When the member accounts added through Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account whose members you want to disassociate from the administrator account.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts that you want to disassociate from the administrator account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.disassociate_members_request.DisassociateMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.disassociate_members_response.DisassociateMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.disassociate_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.disassociate_members.disassociate_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.disassociate_members_request.DisassociateMembersRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_organization_admin_account(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        admin_account_id: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse":
        """<p>Designates an Amazon Web Services account within the organization as your GuardDuty delegated administrator. Only the organization's management account can run this API operation.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account ID for the organization account to be enabled as a GuardDuty delegated administrator.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.enable_organization_admin_account

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.enable_organization_admin_account.enable_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {}
        if admin_account_id is not None:
            input_["admin_account_id"] = admin_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_administrator_account(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_administrator_account_response.GetAdministratorAccountResponse":
        """<p>Provides the details of the GuardDuty administrator account associated with the current GuardDuty member account.</p> <p>Based on the type of account that runs this API, the following list shows how the API behavior varies:</p> <ul> <li> <p>When the GuardDuty administrator account runs this API, it will return success (<code>HTTP 200</code>) but no content.</p> </li> <li> <p>When a member account runs this API, it will return the details of the GuardDuty administrator account that is associated with this calling member account.</p> </li> <li> <p>When an individual account (not associated with an organization) runs this API, it will return success (<code>HTTP 200</code>) but no content.</p> </li> </ul>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_administrator_account_request.GetAdministratorAccountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_administrator_account_response.GetAdministratorAccountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_administrator_account

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_administrator_account.get_administrator_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_administrator_account_request.GetAdministratorAccountRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_coverage_statistics(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        statistics_type: Optional[
            "capo_guardduty.types.coverage_statistics_type_list.CoverageStatisticsTypeList"
        ] = None,
    ) -> "capo_guardduty.types.get_coverage_statistics_response.GetCoverageStatisticsResponse":
        """<p>Retrieves aggregated statistics for your account. If you are a GuardDuty administrator, you can retrieve the statistics for all the resources associated with the active member accounts in your organization who have enabled Runtime Monitoring and have the GuardDuty security agent running on their resources.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            filter_criteria: <p>Represents the criteria used to filter the coverage statistics.</p>
            statistics_type: <p>Represents the statistics type used to aggregate the coverage details.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_coverage_statistics_request.GetCoverageStatisticsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_coverage_statistics_response.GetCoverageStatisticsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_coverage_statistics

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_coverage_statistics.get_coverage_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_coverage_statistics_request.GetCoverageStatisticsRequest = {
            "detector_id": detector_id
        }
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if statistics_type is not None:
            input_["statistics_type"] = statistics_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_custom_detection_rule(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_custom_detection_rule_response.GetCustomDetectionRuleResponse":
        """<p>Returns details for a custom detection rule in GuardDuty, including its detection logic.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_custom_detection_rule_request.GetCustomDetectionRuleRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_custom_detection_rule_response.GetCustomDetectionRuleResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_custom_detection_rule

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_custom_detection_rule.get_custom_detection_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_custom_detection_rule_request.GetCustomDetectionRuleRequest = {
            "rule_id": rule_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_custom_detection_rule_association(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        association_id: "capo_guardduty.types.association_id.AssociationId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_custom_detection_rule_association_response.GetCustomDetectionRuleAssociationResponse":
        """<p>Returns details for a custom detection rule association.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            association_id: <p>The unique identifier for the association.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_custom_detection_rule_association_request.GetCustomDetectionRuleAssociationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_custom_detection_rule_association_response.GetCustomDetectionRuleAssociationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_custom_detection_rule_association

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_custom_detection_rule_association.get_custom_detection_rule_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_custom_detection_rule_association_request.GetCustomDetectionRuleAssociationRequest = {
            "rule_id": rule_id,
            "association_id": association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_custom_detection_rule_org_configuration(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
    ) -> "capo_guardduty.types.get_custom_detection_rule_org_configuration_response.GetCustomDetectionRuleOrgConfigurationResponse":
        """<p>Returns the organization-level configuration for a custom detection rule.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            mode: <p>The execution mode of the organization configuration to retrieve. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_custom_detection_rule_org_configuration_request.GetCustomDetectionRuleOrgConfigurationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_custom_detection_rule_org_configuration_response.GetCustomDetectionRuleOrgConfigurationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_custom_detection_rule_org_configuration

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_custom_detection_rule_org_configuration.get_custom_detection_rule_org_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_custom_detection_rule_org_configuration_request.GetCustomDetectionRuleOrgConfigurationRequest = {
            "rule_id": rule_id
        }
        if mode is not None:
            input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_detector(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_detector_response.GetDetectorResponse":
        """<p>Retrieves a GuardDuty detector specified by the detectorId.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that you want to get.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_detector_request.GetDetectorRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_detector_response.GetDetectorResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_detector

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_detector.get_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_detector_request.GetDetectorRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_filter(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        filter_name: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_filter_response.GetFilterResponse":
        """<p>Returns the details of the filter specified by the filter name.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with this filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            filter_name: <p>The name of the filter you want to get.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_filter_request.GetFilterRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_filter_response.GetFilterResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_filter

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_filter.get_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_filter_request.GetFilterRequest = {
            "detector_id": detector_id,
            "filter_name": filter_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_findings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_ids: Optional["capo_guardduty.types.finding_ids.FindingIds"] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "capo_guardduty.types.get_findings_response.GetFindingsResponse":
        """<p>Describes Amazon GuardDuty findings specified by finding IDs.</p>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings that you want to retrieve.</p>
            sort_criteria: <p>Represents the criteria used for sorting findings.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_findings_request.GetFindingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_findings_response.GetFindingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_findings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_findings.get_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_findings_request.GetFindingsRequest = {
            "detector_id": detector_id
        }
        if finding_ids is not None:
            input_["finding_ids"] = finding_ids
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_findings_statistics(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_statistic_types: Optional[
            "capo_guardduty.types.finding_statistic_types.FindingStatisticTypes"
        ] = None,
        finding_criteria: Optional[
            "capo_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        group_by: Optional["capo_guardduty.types.group_by_type.GroupByType"] = None,
        order_by: Optional["capo_guardduty.types.order_by.OrderBy"] = None,
        max_results: Optional[
            "capo_guardduty.types.max_results100.MaxResults100"
        ] = None,
    ) -> "capo_guardduty.types.get_findings_statistics_response.GetFindingsStatisticsResponse":
        """<p>Lists GuardDuty findings statistics for the specified detector ID.</p> <p>You must provide either <code>findingStatisticTypes</code> or <code>groupBy</code> parameter, and not both. You can use the <code>maxResults</code> and <code>orderBy</code> parameters only when using <code>groupBy</code>.</p> <p>There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The ID of the detector whose findings statistics you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_statistic_types: <p>The types of finding statistics to retrieve.</p>
            finding_criteria: <p>Represents the criteria that is used for querying findings.</p>
            group_by: <p>Displays the findings statistics grouped by one of the listed valid values.</p>
            order_by: <p>Displays the sorted findings in the requested order. The default value of <code>orderBy</code> is <code>DESC</code>.</p> <p>You can use this parameter only with the <code>groupBy</code> parameter.</p>
            max_results: <p>The maximum number of results to be returned in the response. The default value is 25.</p> <p>You can use this parameter only with the <code>groupBy</code> parameter.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_findings_statistics_request.GetFindingsStatisticsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_findings_statistics_response.GetFindingsStatisticsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_findings_statistics

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_findings_statistics.get_findings_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_findings_statistics_request.GetFindingsStatisticsRequest = {
            "detector_id": detector_id
        }
        if finding_statistic_types is not None:
            input_["finding_statistic_types"] = finding_statistic_types
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        if group_by is not None:
            input_["group_by"] = group_by
        if order_by is not None:
            input_["order_by"] = order_by
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_investigation(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        investigation_id: "capo_guardduty.types.investigation_id.InvestigationId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_investigation_response.GetInvestigationResponse":
        """<p>This API is currently available as a preview. This feature is available in the following Amazon Web Services Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).</p> <p>Retrieves the results and status of a specific GuardDuty investigation.</p> <p>An administrator account can retrieve any investigation within the organization. Member accounts can only retrieve investigations that belong to them.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with the investigation.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            investigation_id: <p>The unique identifier of the investigation to retrieve.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_investigation_request.GetInvestigationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_investigation_response.GetInvestigationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_investigation

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_investigation.get_investigation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_investigation_request.GetInvestigationRequest = {
            "detector_id": detector_id,
            "investigation_id": investigation_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_invitations_count(
        self, *, config_overrides: Optional[GuardDutyClientConfig] = None
    ) -> "capo_guardduty.types.get_invitations_count_response.GetInvitationsCountResponse":
        """<p>Returns the count of all GuardDuty membership invitations that were sent to the current member account except the currently accepted invitation.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_invitations_count_request.GetInvitationsCountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_invitations_count_response.GetInvitationsCountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_invitations_count

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_invitations_count.get_invitations_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_invitations_count_request.GetInvitationsCountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ip_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        ip_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_ip_set_response.GetIPSetResponse":
        """<p>Retrieves the IPSet specified by the <code>ipSetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            ip_set_id: <p>The unique ID of the IPSet to retrieve.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_ip_set_request.GetIPSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_ip_set_response.GetIPSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_ip_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_ip_set.get_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_ip_set_request.GetIPSetRequest = {
            "detector_id": detector_id,
            "ip_set_id": ip_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_malware_protection_plan(
        self,
        malware_protection_plan_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_malware_protection_plan_response.GetMalwareProtectionPlanResponse":
        """<p>Retrieves the Malware Protection plan details associated with a Malware Protection plan ID.</p>

        Args:
            malware_protection_plan_id: <p>A unique identifier associated with Malware Protection plan resource.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_malware_protection_plan_request.GetMalwareProtectionPlanRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_malware_protection_plan_response.GetMalwareProtectionPlanResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_malware_protection_plan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_malware_protection_plan.get_malware_protection_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_malware_protection_plan_request.GetMalwareProtectionPlanRequest = {
            "malware_protection_plan_id": malware_protection_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_malware_scan(
        self,
        scan_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_malware_scan_response.GetMalwareScanResponse":
        """<p>Retrieves the detailed information for a specific malware scan. Each member account can view the malware scan details for their own account. An administrator can view malware scan details for all accounts in the organization.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            scan_id: <p>A unique identifier that gets generated when you invoke the API without any error. Each malware scan has a corresponding scan ID. Using this scan ID, you can monitor the status of your malware scan.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_malware_scan_request.GetMalwareScanRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_malware_scan_response.GetMalwareScanResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_malware_scan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_malware_scan.get_malware_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_malware_scan_request.GetMalwareScanRequest = {
            "scan_id": scan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_malware_scan_settings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_malware_scan_settings_response.GetMalwareScanSettingsResponse":
        """<p>Returns the details of the malware scan settings.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with this scan.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_malware_scan_settings_request.GetMalwareScanSettingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_malware_scan_settings_response.GetMalwareScanSettingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_malware_scan_settings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_malware_scan_settings.get_malware_scan_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_malware_scan_settings_request.GetMalwareScanSettingsRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_master_account(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_master_account_response.GetMasterAccountResponse":
        """<p>Provides the details for the GuardDuty administrator account associated with the current GuardDuty member account.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_master_account_request.GetMasterAccountRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_master_account_response.GetMasterAccountResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_master_account

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_master_account.get_master_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_master_account_request.GetMasterAccountRequest = {
            "detector_id": detector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_member_detectors(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> (
        "capo_guardduty.types.get_member_detectors_response.GetMemberDetectorsResponse"
    ):
        """<p>Describes which data sources are enabled for the member account's detector.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The detector ID for the administrator account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of member account IDs.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_member_detectors_request.GetMemberDetectorsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_member_detectors_response.GetMemberDetectorsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_member_detectors

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_member_detectors.get_member_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_member_detectors_request.GetMemberDetectorsRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> "capo_guardduty.types.get_members_response.GetMembersResponse":
        """<p>Retrieves GuardDuty member accounts (of the current GuardDuty administrator account) specified by the account IDs.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account whose members you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts that you want to describe.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_members_request.GetMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_members_response.GetMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_members.get_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_members_request.GetMembersRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_organization_statistics(
        self, *, config_overrides: Optional[GuardDutyClientConfig] = None
    ) -> "capo_guardduty.types.get_organization_statistics_response.GetOrganizationStatisticsResponse":
        """<p>Retrieves how many active member accounts have each feature enabled within GuardDuty. Only a delegated GuardDuty administrator of an organization can run this API.</p> <p>When you create a new organization, it might take up to 24 hours to generate the statistics for the entire organization.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_organization_statistics_response.GetOrganizationStatisticsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_organization_statistics

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_organization_statistics.get_organization_statistics(
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

    def get_remaining_free_trial_days(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        account_ids: "capo_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_remaining_free_trial_days_response.GetRemainingFreeTrialDaysResponse":
        """<p>Provides the number of days left for each data source used in the free trial period.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of account identifiers of the GuardDuty member account.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_remaining_free_trial_days_request.GetRemainingFreeTrialDaysRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_remaining_free_trial_days_response.GetRemainingFreeTrialDaysResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_remaining_free_trial_days

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_remaining_free_trial_days.get_remaining_free_trial_days(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_remaining_free_trial_days_request.GetRemainingFreeTrialDaysRequest = {
            "detector_id": detector_id,
            "account_ids": account_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_threat_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        threat_entity_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> (
        "capo_guardduty.types.get_threat_entity_set_response.GetThreatEntitySetResponse"
    ):
        """<p>Retrieves the threat entity set associated with the specified <code>threatEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the threat entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            threat_entity_set_id: <p>The unique ID that helps GuardDuty identify the threat entity set.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_threat_entity_set_request.GetThreatEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_threat_entity_set_response.GetThreatEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_threat_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_threat_entity_set.get_threat_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_threat_entity_set_request.GetThreatEntitySetRequest = {
            "detector_id": detector_id,
            "threat_entity_set_id": threat_entity_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_threat_intel_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        threat_intel_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_threat_intel_set_response.GetThreatIntelSetResponse":
        """<p>Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            threat_intel_set_id: <p>The unique ID of the threatIntelSet that you want to get.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_threat_intel_set_request.GetThreatIntelSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_threat_intel_set_response.GetThreatIntelSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_threat_intel_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_threat_intel_set.get_threat_intel_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_threat_intel_set_request.GetThreatIntelSetRequest = {
            "detector_id": detector_id,
            "threat_intel_set_id": threat_intel_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_trusted_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        trusted_entity_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.get_trusted_entity_set_response.GetTrustedEntitySetResponse":
        """<p>Retrieves the trusted entity set associated with the specified <code>trustedEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with this trusted entity set.</p>
            trusted_entity_set_id: <p>The unique ID that helps GuardDuty identify the trusted entity set.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_trusted_entity_set_request.GetTrustedEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_trusted_entity_set_response.GetTrustedEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_trusted_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_trusted_entity_set.get_trusted_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_trusted_entity_set_request.GetTrustedEntitySetRequest = {
            "detector_id": detector_id,
            "trusted_entity_set_id": trusted_entity_set_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_usage_statistics(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        usage_statistic_type: Optional[
            "capo_guardduty.types.usage_statistic_type.UsageStatisticType"
        ] = None,
        usage_criteria: Optional[
            "capo_guardduty.types.usage_criteria.UsageCriteria"
        ] = None,
        unit: Optional["capo_guardduty.types.string.String"] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> (
        "capo_guardduty.types.get_usage_statistics_response.GetUsageStatisticsResponse"
    ):
        """<p>Lists Amazon GuardDuty usage statistics over the last 30 days for the specified detector ID. For newly enabled detectors or data sources, the cost returned will include only the usage so far under 30 days. This may differ from the cost metrics in the console, which project usage over 30 days to provide a monthly cost estimate. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/monitoring_costs.html#usage-calculations">Understanding How Usage Costs are Calculated</a>.</p>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose usage statistics you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            usage_statistic_type: <p>The type of usage statistics to retrieve.</p>
            usage_criteria: <p>Represents the criteria used for querying usage.</p>
            unit: <p>The currency unit you would like to view your usage statistics in. Current valid values are USD.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.get_usage_statistics_request.GetUsageStatisticsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.get_usage_statistics_response.GetUsageStatisticsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.get_usage_statistics

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.get_usage_statistics.get_usage_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.get_usage_statistics_request.GetUsageStatisticsRequest = {
            "detector_id": detector_id
        }
        if usage_statistic_type is not None:
            input_["usage_statistic_type"] = usage_statistic_type
        if usage_criteria is not None:
            input_["usage_criteria"] = usage_criteria
        if unit is not None:
            input_["unit"] = unit
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

    def iter_get_usage_statistics(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        usage_statistic_type: Optional[
            "capo_guardduty.types.usage_statistic_type.UsageStatisticType"
        ] = None,
        usage_criteria: Optional[
            "capo_guardduty.types.usage_criteria.UsageCriteria"
        ] = None,
        unit: Optional["capo_guardduty.types.string.String"] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.get_usage_statistics_response.GetUsageStatisticsResponse]":
        _token = next_token
        while True:
            _response = self.get_usage_statistics(
                detector_id,
                config_overrides=config_overrides,
                usage_statistic_type=usage_statistic_type,
                usage_criteria=usage_criteria,
                unit=unit,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def invite_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
        disable_email_notification: Optional[
            "capo_guardduty.types.boolean.Boolean"
        ] = None,
        message: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.invite_members_response.InviteMembersResponse":
        """<p>Invites Amazon Web Services accounts to become members of an organization administered by the Amazon Web Services account that invokes this API. If you are using Amazon Web Services Organizations to manage your GuardDuty environment, this step is not needed. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html">Managing accounts with organizations</a>.</p> <p>To invite Amazon Web Services accounts, the first step is to ensure that GuardDuty has been enabled in the potential member accounts. You can now invoke this API to add accounts by invitation. The invited accounts can either accept or decline the invitation from their GuardDuty accounts. Each invited Amazon Web Services account can choose to accept the invitation from only one Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html">Managing GuardDuty accounts by invitation</a>.</p> <p>After the invite has been accepted and you choose to disassociate a member account (by using <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateMembers.html">DisassociateMembers</a>) from your account, the details of the member account obtained by invoking <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html">CreateMembers</a>, including the associated email addresses, will be retained. This is done so that you can invoke InviteMembers without the need to invoke <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html">CreateMembers</a> again. To remove the details associated with a member account, you must also invoke <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a>. </p> <p>If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html">DeleteMembers</a> API. </p> <p>When the member accounts added through Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account with which you want to invite members.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the accounts that you want to invite to GuardDuty as members.</p>
            disable_email_notification: <p>A Boolean value that specifies whether you want to disable email notification to the accounts that you are inviting to GuardDuty as members.</p>
            message: <p>The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.invite_members_request.InviteMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.invite_members_response.InviteMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.invite_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.invite_members.invite_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.invite_members_request.InviteMembersRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if disable_email_notification is not None:
            input_["disable_email_notification"] = disable_email_notification
        if message is not None:
            input_["message"] = message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_coverage(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.coverage_sort_criteria.CoverageSortCriteria"
        ] = None,
    ) -> "capo_guardduty.types.list_coverage_response.ListCoverageResponse":
        """<p>Lists coverage details for your GuardDuty account. If you're a GuardDuty administrator, you can retrieve all resources associated with the active member accounts in your organization.</p> <p>Make sure the accounts have Runtime Monitoring enabled and GuardDuty agent running on their resources.</p>

        Args:
            detector_id: <p>The unique ID of the detector whose coverage details you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filter_criteria: <p>Represents the criteria used to filter the coverage details.</p>
            sort_criteria: <p>Represents the criteria used to sort the coverage details.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_coverage_request.ListCoverageRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_coverage_response.ListCoverageResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_coverage

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_coverage.list_coverage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_coverage_request.ListCoverageRequest = {
            "detector_id": detector_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_coverage(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.coverage_sort_criteria.CoverageSortCriteria"
        ] = None,
    ) -> "Iterator[capo_guardduty.types.coverage_resource.CoverageResource]":
        _token = next_token
        while True:
            _response = self.list_coverage(
                detector_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_detection_rule_associations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional[
            "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
        ] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        rule_id: Optional["capo_guardduty.types.rule_id.RuleId"] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
    ) -> "capo_guardduty.types.list_custom_detection_rule_associations_response.ListCustomDetectionRuleAssociationsResponse":
        """<p>Returns all custom detection rule associations for your account. You can filter by rule ID and mode.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.</p>
            next_token: <p>A pagination token from a previous response. Use this token to retrieve the next page of results.</p>
            rule_id: <p>The unique identifier for the custom detection rule to filter associations by.</p>
            mode: <p>The rule execution mode to filter associations by.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_custom_detection_rule_associations_request.ListCustomDetectionRuleAssociationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_custom_detection_rule_associations_response.ListCustomDetectionRuleAssociationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_custom_detection_rule_associations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_custom_detection_rule_associations.list_custom_detection_rule_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_custom_detection_rule_associations_request.ListCustomDetectionRuleAssociationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if rule_id is not None:
            input_["rule_id"] = rule_id
        if mode is not None:
            input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_custom_detection_rule_associations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional[
            "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
        ] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        rule_id: Optional["capo_guardduty.types.rule_id.RuleId"] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
    ) -> "Iterator[capo_guardduty.types.association_summary.AssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_custom_detection_rule_associations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                rule_id=rule_id,
                mode=mode,
            )
            _page = _resolve_path(_response, ("rule_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_detection_rule_org_configurations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional[
            "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
        ] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        status: Optional[
            "capo_guardduty.types.detection_rule_configuration_status.DetectionRuleConfigurationStatus"
        ] = None,
    ) -> "capo_guardduty.types.list_custom_detection_rule_org_configurations_response.ListCustomDetectionRuleOrgConfigurationsResponse":
        """<p>Returns all organization-level configurations for custom detection rules. You can filter the results by status.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.</p>
            next_token: <p>A pagination token from a previous response. Use this token to retrieve the next page of results.</p>
            status: <p>The configuration status to filter by.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_custom_detection_rule_org_configurations_request.ListCustomDetectionRuleOrgConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_custom_detection_rule_org_configurations_response.ListCustomDetectionRuleOrgConfigurationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_custom_detection_rule_org_configurations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_custom_detection_rule_org_configurations.list_custom_detection_rule_org_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_custom_detection_rule_org_configurations_request.ListCustomDetectionRuleOrgConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_custom_detection_rule_org_configurations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional[
            "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
        ] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        status: Optional[
            "capo_guardduty.types.detection_rule_configuration_status.DetectionRuleConfigurationStatus"
        ] = None,
    ) -> "Iterator[capo_guardduty.types.detection_rule_org_configuration_summary.DetectionRuleOrgConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_custom_detection_rule_org_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_custom_detection_rules(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional[
            "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
        ] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        filters: Optional[
            "capo_guardduty.types.detection_rule_filter_list.DetectionRuleFilterList"
        ] = None,
    ) -> "capo_guardduty.types.list_custom_detection_rules_response.ListCustomDetectionRulesResponse":
        """<p>Returns all available custom detection rules in GuardDuty. You can filter the results by data source, severity, tactic, technique, and service.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single page. Minimum value of 1, maximum value of 100.</p>
            next_token: <p>A pagination token from a previous response. Use this token to retrieve the next page of results.</p>
            filters: <p>A list of filter criteria to apply when listing custom detection rules.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_custom_detection_rules_request.ListCustomDetectionRulesRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_custom_detection_rules_response.ListCustomDetectionRulesResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_custom_detection_rules

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_custom_detection_rules.list_custom_detection_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_custom_detection_rules_request.ListCustomDetectionRulesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_custom_detection_rules(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional[
            "capo_guardduty.types.detection_rule_max_results.DetectionRuleMaxResults"
        ] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        filters: Optional[
            "capo_guardduty.types.detection_rule_filter_list.DetectionRuleFilterList"
        ] = None,
    ) -> "Iterator[capo_guardduty.types.rule_summary.RuleSummary]":
        _token = next_token
        while True:
            _response = self.list_custom_detection_rules(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_detectors(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_detectors_response.ListDetectorsResponse":
        """<p>Lists detectorIds of all the existing Amazon GuardDuty detector resources.</p>

        Args:
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_detectors_request.ListDetectorsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_detectors_response.ListDetectorsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_detectors

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_detectors.list_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_detectors_request.ListDetectorsRequest = {}
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

    def iter_list_detectors(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.detector_id.DetectorId]":
        _token = next_token
        while True:
            _response = self.list_detectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("detector_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_filters(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_filters_response.ListFiltersResponse":
        """<p>Returns a paginated list of the current filters.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_filters_request.ListFiltersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_filters_response.ListFiltersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_filters

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_filters.list_filters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_filters_request.ListFiltersRequest = {
            "detector_id": detector_id
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

    def iter_list_filters(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.filter_name.FilterName]":
        _token = next_token
        while True:
            _response = self.list_filters(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("filter_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_findings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_criteria: Optional[
            "capo_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_findings_response.ListFindingsResponse":
        """<p>Lists GuardDuty findings for the specified detector ID.</p> <p>There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose findings you want to list.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_criteria: <p>Represents the criteria used for querying findings. Valid values include:</p> <ul> <li> <p>JSON field name</p> </li> <li> <p>accountId</p> </li> <li> <p>region</p> </li> <li> <p>confidence</p> </li> <li> <p>id</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.archived</p> <p>When this attribute is set to 'true', only archived findings are listed. When it's set to 'false', only unarchived findings are listed. When this attribute is not set, all existing findings are listed.</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>severity</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format: 1486685375000</p> </li> </ul>
            sort_criteria: <p>Represents the criteria used for sorting findings.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_findings_request.ListFindingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_findings_response.ListFindingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_findings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_findings.list_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_findings_request.ListFindingsRequest = {
            "detector_id": detector_id
        }
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
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

    def iter_list_findings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_criteria: Optional[
            "capo_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.finding_id.FindingId]":
        _token = next_token
        while True:
            _response = self.list_findings(
                detector_id,
                config_overrides=config_overrides,
                finding_criteria=finding_criteria,
                sort_criteria=sort_criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("finding_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_investigations(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.investigation_sort_criteria.InvestigationSortCriteria"
        ] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.next_token.NextToken"] = None,
    ) -> "capo_guardduty.types.list_investigations_response.ListInvestigationsResponse":
        """<p>This API is currently available as a preview. This feature is available in the following Amazon Web Services Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Stockholm), and Asia Pacific (Tokyo).</p> <p>Returns a list of investigations associated with the specified GuardDuty detector.</p> <p>An administrator account sees all investigations across the organization. Member accounts see only the investigations that belong to them.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector whose investigations you want to list.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            sort_criteria: <p>Represents the criteria used for sorting investigations.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_investigations_request.ListInvestigationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_investigations_response.ListInvestigationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_investigations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_investigations.list_investigations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_investigations_request.ListInvestigationsRequest = {
            "detector_id": detector_id
        }
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
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

    def iter_list_investigations(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.investigation_sort_criteria.InvestigationSortCriteria"
        ] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_guardduty.types.investigation_summary.InvestigationSummary]":
        _token = next_token
        while True:
            _response = self.list_investigations(
                detector_id,
                config_overrides=config_overrides,
                sort_criteria=sort_criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("investigations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_invitations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_invitations_response.ListInvitationsResponse":
        """<p>Lists all GuardDuty membership invitations that were sent to the current Amazon Web Services account.</p>

        Args:
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_invitations_request.ListInvitationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_invitations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_invitations.list_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_invitations_request.ListInvitationsRequest = {}
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

    def iter_list_invitations(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.invitation.Invitation]":
        _token = next_token
        while True:
            _response = self.list_invitations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("invitations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_ip_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_ip_sets_response.ListIPSetsResponse":
        """<p>Lists the IPSets of the GuardDuty service specified by the detector ID. If you use this operation from a member account, the IPSets returned are the IPSets from the associated administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_ip_sets_request.ListIPSetsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_ip_sets_response.ListIPSetsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_ip_sets

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_ip_sets.list_ip_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_ip_sets_request.ListIPSetsRequest = {
            "detector_id": detector_id
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

    def iter_list_ip_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_ip_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ip_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_malware_protection_plans(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_malware_protection_plans_response.ListMalwareProtectionPlansResponse":
        """<p>Lists the Malware Protection plan IDs associated with the protected resources in your Amazon Web Services account.</p>

        Args:
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of <code>NextToken</code> from the previous response to continue listing data. The default page size is 100 plans.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_malware_protection_plans_request.ListMalwareProtectionPlansRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_malware_protection_plans_response.ListMalwareProtectionPlansResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_malware_protection_plans

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_malware_protection_plans.list_malware_protection_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_malware_protection_plans_request.ListMalwareProtectionPlansRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_malware_scans(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.list_malware_scans_filter_criteria.ListMalwareScansFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "capo_guardduty.types.list_malware_scans_response.ListMalwareScansResponse":
        """<p>Returns a list of malware scans. Each member account can view the malware scans for their own accounts. An administrator can view the malware scans for all of its members' accounts.</p>

        Args:
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing results.</p>
            filter_criteria: <p>Represents the criteria used to filter the malware scan entries.</p>
            sort_criteria: <p>Represents the criteria used for sorting malware scan entries.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_malware_scans_request.ListMalwareScansRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_malware_scans_response.ListMalwareScansResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_malware_scans

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_malware_scans.list_malware_scans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_malware_scans_request.ListMalwareScansRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_malware_scans(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        filter_criteria: Optional[
            "capo_guardduty.types.list_malware_scans_filter_criteria.ListMalwareScansFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "capo_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "Iterator[capo_guardduty.types.malware_scan.MalwareScan]":
        _token = next_token
        while True:
            _response = self.list_malware_scans(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("scans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        only_associated: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_members_response.ListMembersResponse":
        """<p>Lists details about all member accounts for the current GuardDuty administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the member.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
            only_associated: <p>Specifies whether to only return associated members or to return all members (including members who haven't been invited yet or have been disassociated). Member accounts must have been previously associated with the GuardDuty administrator account using <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html"> <code>Create Members</code> </a>. </p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_members_request.ListMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_members_response.ListMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_members_request.ListMembersRequest = {
            "detector_id": detector_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if only_associated is not None:
            input_["only_associated"] = only_associated

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
        only_associated: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.member.Member]":
        _token = next_token
        while True:
            _response = self.list_members(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                only_associated=only_associated,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Lists the accounts designated as GuardDuty delegated administrators. Only the organization's management account can run this API operation.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_organization_admin_accounts

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_organization_admin_accounts.list_organization_admin_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}
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

    def iter_list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.admin_account.AdminAccount]":
        _token = next_token
        while True:
            _response = self.list_organization_admin_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_publishing_destinations(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_publishing_destinations_response.ListPublishingDestinationsResponse":
        """<p>Returns a list of publishing destinations associated with the specified <code>detectorId</code>.</p>

        Args:
            detector_id: <p>The detector ID for which you want to retrieve the publishing destination.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_publishing_destinations_request.ListPublishingDestinationsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_publishing_destinations_response.ListPublishingDestinationsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_publishing_destinations

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_publishing_destinations.list_publishing_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_publishing_destinations_request.ListPublishingDestinationsRequest = {
            "detector_id": detector_id
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

    def iter_list_publishing_destinations(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.list_publishing_destinations_response.ListPublishingDestinationsResponse]":
        _token = next_token
        while True:
            _response = self.list_publishing_destinations(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_guardduty.types.guard_duty_arn.GuardDutyArn",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource. Tagging is currently supported for detectors, finding filters, IP sets, threat intel sets, and publishing destination, with a limit of 50 tags per resource. When invoked, this operation returns all assigned tags for a given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the given GuardDuty resource. </p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_tags_for_resource

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_threat_entity_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_threat_entity_sets_response.ListThreatEntitySetsResponse":
        """<p>Lists the threat entity sets associated with the specified GuardDuty detector ID. If you use this operation from a member account, the threat entity sets that are returned as a response, belong to the administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector that is associated with this threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_threat_entity_sets_request.ListThreatEntitySetsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_threat_entity_sets_response.ListThreatEntitySetsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_threat_entity_sets

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_threat_entity_sets.list_threat_entity_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_threat_entity_sets_request.ListThreatEntitySetsRequest = {
            "detector_id": detector_id
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

    def iter_list_threat_entity_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_threat_entity_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_entity_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_threat_intel_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_threat_intel_sets_response.ListThreatIntelSetsResponse":
        """<p>Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID. If you use this operation from a member account, the ThreatIntelSets associated with the administrator account are returned.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter to paginate results in the response. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_threat_intel_sets_request.ListThreatIntelSetsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_threat_intel_sets_response.ListThreatIntelSetsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_threat_intel_sets

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_threat_intel_sets.list_threat_intel_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_threat_intel_sets_request.ListThreatIntelSetsRequest = {
            "detector_id": detector_id
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

    def iter_list_threat_intel_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_threat_intel_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_intel_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_trusted_entity_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "capo_guardduty.types.list_trusted_entity_sets_response.ListTrustedEntitySetsResponse":
        """<p>Lists the trusted entity sets associated with the specified GuardDuty detector ID. If you use this operation from a member account, the trusted entity sets that are returned as a response, belong to the administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector that is associated with this threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.list_trusted_entity_sets_request.ListTrustedEntitySetsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.list_trusted_entity_sets_response.ListTrustedEntitySetsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.list_trusted_entity_sets

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.list_trusted_entity_sets.list_trusted_entity_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.list_trusted_entity_sets_request.ListTrustedEntitySetsRequest = {
            "detector_id": detector_id
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

    def iter_list_trusted_entity_sets(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        max_results: Optional["capo_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_guardduty.types.string.String"] = None,
    ) -> "Iterator[capo_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_trusted_entity_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("trusted_entity_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def send_object_malware_scan(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        s3_object: Optional[
            "capo_guardduty.types.s3_object_for_send_object_malware_scan.S3ObjectForSendObjectMalwareScan"
        ] = None,
    ) -> "capo_guardduty.types.send_object_malware_scan_response.SendObjectMalwareScanResponse":
        """<p>Initiates a malware scan for a specific S3 object. This API allows you to perform on-demand malware scanning of individual objects in S3 buckets that have Malware Protection for S3 enabled.</p> <p>When you use this API, the Amazon Web Services service terms for GuardDuty Malware Protection apply. For more information, see <a href="http://aws.amazon.com/service-terms/#87._Amazon_GuardDuty">Amazon Web Services service terms for GuardDuty Malware Protection</a>.</p>

        Args:
            s3_object: <p>The S3 object information for the object you want to scan. The bucket must have a Malware Protection plan configured to use this API.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.send_object_malware_scan_request.SendObjectMalwareScanRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.send_object_malware_scan_response.SendObjectMalwareScanResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.send_object_malware_scan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.send_object_malware_scan.send_object_malware_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.send_object_malware_scan_request.SendObjectMalwareScanRequest = {}
        if s3_object is not None:
            input_["s3_object"] = s3_object

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_malware_scan(
        self,
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        resource_arn: Optional["capo_guardduty.types.resource_arn.ResourceArn"] = None,
        client_token: Optional["capo_guardduty.types.client_token.ClientToken"] = None,
        scan_configuration: Optional[
            "capo_guardduty.types.start_malware_scan_configuration.StartMalwareScanConfiguration"
        ] = None,
    ) -> "capo_guardduty.types.start_malware_scan_response.StartMalwareScanResponse":
        """<p>Initiates the malware scan. Invoking this API will automatically create the <a href="https://docs.aws.amazon.com/guardduty/latest/ug/slr-permissions-malware-protection.html">Service-linked role</a> in the corresponding account if the resourceArn belongs to an EC2 instance.</p> <p>When the malware scan starts, you can use the associated scan ID to track the status of the scan. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMalwareScans.html">ListMalwareScans</a> and <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareScan.html">GetMalwareScan</a>.</p> <p>When you use this API, the Amazon Web Services service terms for GuardDuty Malware Protection apply. For more information, see <a href="http://aws.amazon.com/service-terms/#87._Amazon_GuardDuty">Amazon Web Services service terms for GuardDuty Malware Protection</a>.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource for which you invoked the API.</p>
            client_token: <p>The idempotency token for the create request.</p>
            scan_configuration: <p>Contains information about the configuration to be used for the malware scan.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.start_malware_scan_request.StartMalwareScanRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.start_malware_scan_response.StartMalwareScanResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.start_malware_scan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.start_malware_scan.start_malware_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.start_malware_scan_request.StartMalwareScanRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scan_configuration is not None:
            input_["scan_configuration"] = scan_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_monitoring_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> "capo_guardduty.types.start_monitoring_members_response.StartMonitoringMembersResponse":
        """<p>Turns on GuardDuty monitoring of the specified member accounts. Use this operation to restart monitoring of accounts that you stopped monitoring with the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_StopMonitoringMembers.html">StopMonitoringMembers</a> operation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty administrator account associated with the member accounts to monitor.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts to start monitoring.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.start_monitoring_members_request.StartMonitoringMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.start_monitoring_members_response.StartMonitoringMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.start_monitoring_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.start_monitoring_members.start_monitoring_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.start_monitoring_members_request.StartMonitoringMembersRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_monitoring_members(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
    ) -> "capo_guardduty.types.stop_monitoring_members_response.StopMonitoringMembersResponse":
        """<p>Stops GuardDuty monitoring for the specified member accounts. Use the <code>StartMonitoringMembers</code> operation to restart monitoring for those accounts.</p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to stop monitoring the member accounts in your organization.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the GuardDuty administrator account that is monitoring member accounts.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs for the member accounts to stop monitoring.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.stop_monitoring_members_request.StopMonitoringMembersRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.stop_monitoring_members_response.StopMonitoringMembersResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.stop_monitoring_members

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.stop_monitoring_members.stop_monitoring_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.stop_monitoring_members_request.StopMonitoringMembersRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_guardduty.types.guard_duty_arn.GuardDutyArn",
        tags: "capo_guardduty.types.tag_map.TagMap",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
    ) -> "capo_guardduty.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the GuardDuty resource to apply a tag to.</p>
            tags: <p>The tags to be added to a resource.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.tag_resource

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.tag_resource_request.TagResourceRequest = {
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

    def unarchive_findings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_ids: Optional["capo_guardduty.types.finding_ids.FindingIds"] = None,
    ) -> "capo_guardduty.types.unarchive_findings_response.UnarchiveFindingsResponse":
        """<p>Unarchives GuardDuty findings specified by the <code>findingIds</code>.</p>

        Args:
            detector_id: <p>The ID of the detector associated with the findings to unarchive.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings to unarchive.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.unarchive_findings_request.UnarchiveFindingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.unarchive_findings_response.UnarchiveFindingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.unarchive_findings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.unarchive_findings.unarchive_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.unarchive_findings_request.UnarchiveFindingsRequest = {
            "detector_id": detector_id
        }
        if finding_ids is not None:
            input_["finding_ids"] = finding_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_guardduty.types.guard_duty_arn.GuardDutyArn",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        tag_keys: Optional["capo_guardduty.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_guardduty.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource to remove tags from.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.untag_resource

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_custom_detection_rule_association(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        association_id: "capo_guardduty.types.association_id.AssociationId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
    ) -> "capo_guardduty.types.update_custom_detection_rule_association_response.UpdateCustomDetectionRuleAssociationResponse":
        """<p>Updates the mode of an existing custom detection rule association.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            association_id: <p>The unique identifier for the association to update.</p>
            mode: <p>The rule execution mode. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_custom_detection_rule_association_request.UpdateCustomDetectionRuleAssociationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_custom_detection_rule_association_response.UpdateCustomDetectionRuleAssociationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_custom_detection_rule_association

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_custom_detection_rule_association.update_custom_detection_rule_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_custom_detection_rule_association_request.UpdateCustomDetectionRuleAssociationRequest = {
            "rule_id": rule_id,
            "association_id": association_id,
        }
        if mode is not None:
            input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_custom_detection_rule_org_configuration(
        self,
        rule_id: "capo_guardduty.types.rule_id.RuleId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        mode: Optional["capo_guardduty.types.association_mode.AssociationMode"] = None,
        include_account_ids: Optional[
            "capo_guardduty.types.detection_rule_account_ids.DetectionRuleAccountIds"
        ] = None,
        exclude_account_ids: Optional[
            "capo_guardduty.types.detection_rule_account_ids.DetectionRuleAccountIds"
        ] = None,
    ) -> "capo_guardduty.types.update_custom_detection_rule_org_configuration_response.UpdateCustomDetectionRuleOrgConfigurationResponse":
        """<p>Updates the organization-level configuration for a custom detection rule, including the mode and include/exclude account lists.</p>

        Args:
            rule_id: <p>The unique identifier for the custom detection rule.</p>
            mode: <p>The execution mode of the organization configuration. Valid values: <code>LIVE</code> | <code>DRY_RUN</code>.</p>
            include_account_ids: <p>The account IDs to include in the organization configuration. Mutually exclusive with <code>ExcludeAccountIds</code>.</p>
            exclude_account_ids: <p>The account IDs to exclude from the organization configuration. Mutually exclusive with <code>IncludeAccountIds</code>.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.conflict_exception.ConflictException: <p>A request conflict exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_custom_detection_rule_org_configuration_request.UpdateCustomDetectionRuleOrgConfigurationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_custom_detection_rule_org_configuration_response.UpdateCustomDetectionRuleOrgConfigurationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_custom_detection_rule_org_configuration

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_custom_detection_rule_org_configuration.update_custom_detection_rule_org_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_custom_detection_rule_org_configuration_request.UpdateCustomDetectionRuleOrgConfigurationRequest = {
            "rule_id": rule_id
        }
        if mode is not None:
            input_["mode"] = mode
        if include_account_ids is not None:
            input_["include_account_ids"] = include_account_ids
        if exclude_account_ids is not None:
            input_["exclude_account_ids"] = exclude_account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_detector(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        enable: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        finding_publishing_frequency: Optional[
            "capo_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
        ] = None,
        data_sources: Optional[
            "capo_guardduty.types.data_source_configurations.DataSourceConfigurations"
        ] = None,
        features: Optional[
            "capo_guardduty.types.detector_feature_configurations.DetectorFeatureConfigurations"
        ] = None,
    ) -> "capo_guardduty.types.update_detector_response.UpdateDetectorResponse":
        """<p>Updates the GuardDuty detector specified by the detector ID.</p> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            enable: <p>Specifies whether the detector is enabled or not enabled.</p>
            finding_publishing_frequency: <p>An enum value that specifies how frequently findings are exported, such as to CloudWatch Events.</p>
            data_sources: <p>Describes which data sources will be updated.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>
            features: <p>Provides the features that will be updated for the detector.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_detector_request.UpdateDetectorRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_detector_response.UpdateDetectorResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_detector

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_detector.update_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_detector_request.UpdateDetectorRequest = {
            "detector_id": detector_id
        }
        if enable is not None:
            input_["enable"] = enable
        if finding_publishing_frequency is not None:
            input_["finding_publishing_frequency"] = finding_publishing_frequency
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if features is not None:
            input_["features"] = features

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_filter(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        filter_name: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        description: Optional[
            "capo_guardduty.types.filter_description.FilterDescription"
        ] = None,
        action: Optional["capo_guardduty.types.filter_action.FilterAction"] = None,
        rank: Optional["capo_guardduty.types.filter_rank.FilterRank"] = None,
        finding_criteria: Optional[
            "capo_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
    ) -> "capo_guardduty.types.update_filter_response.UpdateFilterResponse":
        """<p>Updates the filter specified by the filter name.</p>

        Args:
            detector_id: <p>The unique ID of the detector that specifies the GuardDuty service where you want to update a filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            filter_name: <p>The name of the filter.</p>
            description: <p>The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses (<code>{ }</code>, <code>[ ]</code>, and <code>( )</code>), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.</p>
            action: <p>Specifies the action that is to be applied to the findings that match the filter.</p> <p>Default: NOOP</p>
            rank: <p>Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.</p>
            finding_criteria: <p>Represents the criteria to be used in the filter for querying findings. The following fields are available for filtering:</p> <ul> <li> <p>accountId</p> </li> <li> <p>arn</p> </li> <li> <p>associatedAttackSequenceArn</p> </li> <li> <p>confidence</p> </li> <li> <p>createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>id</p> </li> <li> <p>partition</p> </li> <li> <p>region</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.attributes.mfaAuthenticated</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.ec2RoleDelivery</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.invokedBy</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.userName</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sourceIdentity</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.attributes</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.federatedProvider</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.userName</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailArn</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailVersion</p> </li> <li> <p>resource.containerDetails.containerRuntime</p> </li> <li> <p>resource.containerDetails.id</p> </li> <li> <p>resource.containerDetails.image</p> </li> <li> <p>resource.containerDetails.imagePrefix</p> </li> <li> <p>resource.containerDetails.name</p> </li> <li> <p>resource.containerDetails.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.containerDetails.securityContext.privileged</p> </li> <li> <p>resource.containerDetails.volumeMounts.mountPath</p> </li> <li> <p>resource.containerDetails.volumeMounts.name</p> </li> <li> <p>resource.ebsSnapshotDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeType</p> </li> <li> <p>resource.ec2ImageDetails.imageArn</p> </li> <li> <p>resource.ecsClusterDetails.activeServicesCount</p> </li> <li> <p>resource.ecsClusterDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.name</p> </li> <li> <p>resource.ecsClusterDetails.registeredContainerInstancesCount</p> </li> <li> <p>resource.ecsClusterDetails.runningTasksCount</p> </li> <li> <p>resource.ecsClusterDetails.status</p> </li> <li> <p>resource.ecsClusterDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.containerRuntime</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.id</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.image</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.imagePrefix</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.definitionArn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.group</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.launchType</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedBy</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.version</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.hostPath.path</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.name</p> </li> <li> <p>resource.eksClusterDetails.arn</p> </li> <li> <p>resource.eksClusterDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.eksClusterDetails.name</p> </li> <li> <p>resource.eksClusterDetails.status</p> </li> <li> <p>resource.eksClusterDetails.tags.key</p> </li> <li> <p>resource.eksClusterDetails.tags.value</p> </li> <li> <p>resource.eksClusterDetails.vpcId</p> </li> <li> <p>resource.instanceDetails.availabilityZone</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.arn</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageDescription</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.instanceState</p> </li> <li> <p>resource.instanceDetails.instanceType</p> </li> <li> <p>resource.instanceDetails.launchTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.networkInterfaceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.outpostArn</p> </li> <li> <p>resource.instanceDetails.platform</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeId</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeType</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.sessionName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.containerRuntime</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.id</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.imagePrefix</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostIpc</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostNetwork</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostPid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.namespace</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.type</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.hostPath.path</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.name</p> </li> <li> <p>resource.lambdaDetails.description</p> </li> <li> <p>resource.lambdaDetails.functionArn</p> </li> <li> <p>resource.lambdaDetails.functionName</p> </li> <li> <p>resource.lambdaDetails.functionVersion</p> </li> <li> <p>resource.lambdaDetails.lastModifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.lambdaDetails.revisionId</p> </li> <li> <p>resource.lambdaDetails.role</p> </li> <li> <p>resource.lambdaDetails.tags.key</p> </li> <li> <p>resource.lambdaDetails.tags.value</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupId</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupName</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.subnetIds</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceArn</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.name</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbiResourceId</p> </li> <li> <p>resource.rdsDbInstanceDetails.engine</p> </li> <li> <p>resource.rdsDbInstanceDetails.engineVersion</p> </li> <li> <p>resource.rdsDbInstanceDetails.iamDatabaseAuthenticationEnabled</p> </li> <li> <p>resource.rdsDbInstanceDetails.publiclyAccessible</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.vpcSecurityGroupId</p> </li> <li> <p>resource.rdsDbUserDetails.application</p> </li> <li> <p>resource.rdsDbUserDetails.authMethod</p> </li> <li> <p>resource.rdsDbUserDetails.database</p> </li> <li> <p>resource.rdsDbUserDetails.ssl</p> </li> <li> <p>resource.rdsDbUserDetails.user</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupArn</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupResourceId</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engine</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engineVersion</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.key</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.value</p> </li> <li> <p>resource.recoveryPointDetails.backupVaultName</p> </li> <li> <p>resource.recoveryPointDetails.recoveryPointArn</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>resource.s3BucketDetails.arn</p> </li> <li> <p>resource.s3BucketDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.encryptionType</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.kmsMasterKeyArn</p> </li> <li> <p>resource.s3BucketDetails.name</p> </li> <li> <p>resource.s3BucketDetails.owner.id</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.effectivePermission</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.eTag</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.hash</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.key</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.objectArn</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.versionId</p> </li> <li> <p>resource.s3BucketDetails.tags.key</p> </li> <li> <p>resource.s3BucketDetails.tags.value</p> </li> <li> <p>resource.s3BucketDetails.type</p> </li> <li> <p>schemaVersion</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.domainDetails.domain</p> </li> <li> <p>service.action.awsApiCallAction.errorCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.accountId</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.affiliated</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.awsServiceName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.awsApiCallAction.userAgent</p> </li> <li> <p>service.action.dnsRequestAction.blocked</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.dnsRequestAction.protocol</p> </li> <li> <p>service.action.dnsRequestAction.vpcOwnerAccountId</p> </li> <li> <p>service.action.kubernetesApiCallAction.namespace</p> </li> <li> <p>service.action.kubernetesApiCallAction.parameters</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.kubernetesApiCallAction.requestUri</p> </li> <li> <p>service.action.kubernetesApiCallAction.resource</p> </li> <li> <p>service.action.kubernetesApiCallAction.resourceName</p> </li> <li> <p>service.action.kubernetesApiCallAction.sourceIPs</p> </li> <li> <p>service.action.kubernetesApiCallAction.statusCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.subresource</p> </li> <li> <p>service.action.kubernetesApiCallAction.userAgent</p> </li> <li> <p>service.action.kubernetesApiCallAction.verb</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.allowed</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.namespace</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.resource</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.verb</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.name</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefKind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefName</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.uid</p> </li> <li> <p>service.action.kubernetesRoleDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleDetails.name</p> </li> <li> <p>service.action.kubernetesRoleDetails.uid</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.localNetworkInterface</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.portName</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.blocked</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.port</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.application</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.failedLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.successfulLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.user</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.additionalInfo.agentDetails.agentId</p> </li> <li> <p>service.additionalInfo.agentDetails.agentVersion</p> </li> <li> <p>service.additionalInfo.anomalies.anomalousAPIs</p> </li> <li> <p>service.additionalInfo.authenticationMethod</p> </li> <li> <p>service.additionalInfo.averagePacketSizeIn</p> </li> <li> <p>service.additionalInfo.averagePacketSizeOut</p> </li> <li> <p>service.additionalInfo.context</p> </li> <li> <p>service.additionalInfo.domain</p> </li> <li> <p>service.additionalInfo.inBytes</p> </li> <li> <p>service.additionalInfo.localNetworkInterfaceOwner</p> </li> <li> <p>service.additionalInfo.localPort</p> </li> <li> <p>service.additionalInfo.outBytes</p> </li> <li> <p>service.additionalInfo.packetsIn</p> </li> <li> <p>service.additionalInfo.packetsOut</p> </li> <li> <p>service.additionalInfo.policyArn</p> </li> <li> <p>service.additionalInfo.policyName</p> </li> <li> <p>service.additionalInfo.remotePort</p> </li> <li> <p>service.additionalInfo.sample</p> </li> <li> <p>service.additionalInfo.scannedPort</p> </li> <li> <p>service.additionalInfo.threatFileSha256</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.additionalInfo.threatName</p> </li> <li> <p>service.additionalInfo.totalBytesIn</p> </li> <li> <p>service.additionalInfo.totalBytesOut</p> </li> <li> <p>service.additionalInfo.type</p> </li> <li> <p>service.additionalInfo.unusual.asnOrg</p> </li> <li> <p>service.additionalInfo.unusual.port</p> </li> <li> <p>service.additionalInfo.unusualProtocol</p> </li> <li> <p>service.additionalInfo.userAgent.fullUserAgent</p> </li> <li> <p>service.additionalInfo.userAgent.userAgentCategory</p> </li> <li> <p>service.additionalInfo.value</p> </li> <li> <p>service.additionalInfo.vpcOwnerAccountId</p> </li> <li> <p>service.archived</p> </li> <li> <p>service.count</p> </li> <li> <p>service.detection.sequence.actors.id</p> </li> <li> <p>service.detection.sequence.actors.process.name</p> </li> <li> <p>service.detection.sequence.actors.process.path</p> </li> <li> <p>service.detection.sequence.actors.process.sha256</p> </li> <li> <p>service.detection.sequence.actors.session.createdTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.actors.session.issuer</p> </li> <li> <p>service.detection.sequence.actors.session.mfaStatus</p> </li> <li> <p>service.detection.sequence.actors.session.uid</p> </li> <li> <p>service.detection.sequence.actors.user.account.account</p> </li> <li> <p>service.detection.sequence.actors.user.account.uid</p> </li> <li> <p>service.detection.sequence.actors.user.credentialUid</p> </li> <li> <p>service.detection.sequence.actors.user.name</p> </li> <li> <p>service.detection.sequence.actors.user.type</p> </li> <li> <p>service.detection.sequence.actors.user.uid</p> </li> <li> <p>service.detection.sequence.additionalSequenceTypes</p> </li> <li> <p>service.detection.sequence.description</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.name</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.number</p> </li> <li> <p>service.detection.sequence.endpoints.connection.direction</p> </li> <li> <p>service.detection.sequence.endpoints.domain</p> </li> <li> <p>service.detection.sequence.endpoints.id</p> </li> <li> <p>service.detection.sequence.endpoints.ip</p> </li> <li> <p>service.detection.sequence.endpoints.location.city</p> </li> <li> <p>service.detection.sequence.endpoints.location.country</p> </li> <li> <p>service.detection.sequence.endpoints.location.lat</p> </li> <li> <p>service.detection.sequence.endpoints.location.lon</p> </li> <li> <p>service.detection.sequence.endpoints.port</p> </li> <li> <p>service.detection.sequence.resources.accountId</p> </li> <li> <p>service.detection.sequence.resources.cloudPartition</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.principalId</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userName</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userType</p> </li> <li> <p>service.detection.sequence.resources.data.autoscalingAutoScalingGroup.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.cloudformationStack.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.container.image</p> </li> <li> <p>service.detection.sequence.resources.data.container.imageUid</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Image.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.availabilityZone</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.ec2NetworkInterfaceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.arn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.imageDescription</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceState</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.outpostArn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.platform</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.version</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.ipv6Addresses</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateDnsName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateIpAddress</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.publicIp</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.subNetId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Vpc.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.launchType</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.taskDefinitionArn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.arn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.namespace</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.type</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.effectivePermission</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionKeyArn</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionType</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.ownerId</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicReadAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicWriteAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.s3ObjectUids</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.eTag</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.key</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.versionId</p> </li> <li> <p>service.detection.sequence.resources.name</p> </li> <li> <p>service.detection.sequence.resources.region</p> </li> <li> <p>service.detection.sequence.resources.resourceType</p> </li> <li> <p>service.detection.sequence.resources.service</p> </li> <li> <p>service.detection.sequence.resources.tags.key</p> </li> <li> <p>service.detection.sequence.resources.tags.value</p> </li> <li> <p>service.detection.sequence.resources.uid</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.key</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.title</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.actorIds</p> </li> <li> <p>service.detection.sequence.signals.count</p> </li> <li> <p>service.detection.sequence.signals.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.description</p> </li> <li> <p>service.detection.sequence.signals.endpointIds</p> </li> <li> <p>service.detection.sequence.signals.firstSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.lastSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.name</p> </li> <li> <p>service.detection.sequence.signals.resourceUids</p> </li> <li> <p>service.detection.sequence.signals.severity</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.key</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.title</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.type</p> </li> <li> <p>service.detection.sequence.signals.uid</p> </li> <li> <p>service.detection.sequence.signals.updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.uid</p> </li> <li> <p>service.detectorId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanCompletedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.count</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.threatName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.totalGb</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.volumes</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.shortened</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.fileName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.volumeArn</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.name</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.uniqueThreatNameCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatsDetectedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanStartedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanType</p> </li> <li> <p>service.ebsVolumeScanDetails.sources</p> </li> <li> <p>service.ebsVolumeScanDetails.triggerFindingId</p> </li> <li> <p>service.eventFirstSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.eventLastSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatFileSha256</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatListName</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatNames</p> </li> <li> <p>service.featureName</p> </li> <li> <p>service.malwareScanDetails.scanCategory</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.incrementalScanDetails.baselineResourceArn</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.triggerType</p> </li> <li> <p>service.malwareScanDetails.scanId</p> </li> <li> <p>service.malwareScanDetails.scanType</p> </li> <li> <p>service.malwareScanDetails.threats.count</p> </li> <li> <p>service.malwareScanDetails.threats.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.deviceName</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.versionId</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.itemPath</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.resourceArn</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.nestedItemPath</p> </li> <li> <p>service.malwareScanDetails.threats.name</p> </li> <li> <p>service.malwareScanDetails.threats.source</p> </li> <li> <p>service.malwareScanDetails.uniqueThreatCount</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>service.runtimeDetails.context.addressFamily</p> </li> <li> <p>service.runtimeDetails.context.commandLineExample</p> </li> <li> <p>service.runtimeDetails.context.fileOperation</p> </li> <li> <p>service.runtimeDetails.context.filePath</p> </li> <li> <p>service.runtimeDetails.context.fileSystemType</p> </li> <li> <p>service.runtimeDetails.context.flags</p> </li> <li> <p>service.runtimeDetails.context.ianaProtocolNumber</p> </li> <li> <p>service.runtimeDetails.context.ldPreloadValue</p> </li> <li> <p>service.runtimeDetails.context.libraryPath</p> </li> <li> <p>service.runtimeDetails.context.memoryRegions</p> </li> <li> <p>service.runtimeDetails.context.modifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.user</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.moduleFilePath</p> </li> <li> <p>service.runtimeDetails.context.moduleName</p> </li> <li> <p>service.runtimeDetails.context.moduleSha256</p> </li> <li> <p>service.runtimeDetails.context.mountSource</p> </li> <li> <p>service.runtimeDetails.context.mountTarget</p> </li> <li> <p>service.runtimeDetails.context.relatedFilePaths</p> </li> <li> <p>service.runtimeDetails.context.releaseAgentPath</p> </li> <li> <p>service.runtimeDetails.context.runcBinaryPath</p> </li> <li> <p>service.runtimeDetails.context.scriptPath</p> </li> <li> <p>service.runtimeDetails.context.serviceName</p> </li> <li> <p>service.runtimeDetails.context.shellHistoryFilePath</p> </li> <li> <p>service.runtimeDetails.context.socketPath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.user</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.threatFilePath</p> </li> <li> <p>service.runtimeDetails.context.toolCategory</p> </li> <li> <p>service.runtimeDetails.context.toolName</p> </li> <li> <p>service.runtimeDetails.process.euid</p> </li> <li> <p>service.runtimeDetails.process.executablePath</p> </li> <li> <p>service.runtimeDetails.process.executableSha256</p> </li> <li> <p>service.runtimeDetails.process.lineage.euid</p> </li> <li> <p>service.runtimeDetails.process.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.process.lineage.name</p> </li> <li> <p>service.runtimeDetails.process.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.lineage.pid</p> </li> <li> <p>service.runtimeDetails.process.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.lineage.userId</p> </li> <li> <p>service.runtimeDetails.process.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.process.name</p> </li> <li> <p>service.runtimeDetails.process.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.pid</p> </li> <li> <p>service.runtimeDetails.process.pwd</p> </li> <li> <p>service.runtimeDetails.process.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.user</p> </li> <li> <p>service.runtimeDetails.process.userId</p> </li> <li> <p>service.runtimeDetails.process.uuid</p> </li> <li> <p>service.serviceName</p> </li> <li> <p>service.userFeedback</p> </li> <li> <p>severity</p> <p>To configure severity based filters, use the following for the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingCriteria.html">FindingCriteria</a> condition:</p> <ul> <li> <p> <b>Low</b>: <code>["1", "2", "3"]</code> </p> </li> <li> <p> <b>Medium</b>: <code>["4", "5", "6"]</code> </p> </li> <li> <p> <b>High</b>: <code>["7", "8"]</code> </p> </li> <li> <p> <b>Critical</b>: <code>["9", "10"]</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html">Findings severity levels</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> </ul>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_filter_request.UpdateFilterRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_filter_response.UpdateFilterResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_filter

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_filter.update_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_filter_request.UpdateFilterRequest = {
            "detector_id": detector_id,
            "filter_name": filter_name,
        }
        if description is not None:
            input_["description"] = description
        if action is not None:
            input_["action"] = action
        if rank is not None:
            input_["rank"] = rank
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_findings_feedback(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        finding_ids: Optional["capo_guardduty.types.finding_ids.FindingIds"] = None,
        feedback: Optional["capo_guardduty.types.feedback.Feedback"] = None,
        comments: Optional[
            "capo_guardduty.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "capo_guardduty.types.update_findings_feedback_response.UpdateFindingsFeedbackResponse":
        """<p>Marks the specified GuardDuty findings as useful or not useful.</p>

        Args:
            detector_id: <p>The ID of the detector that is associated with the findings for which you want to update the feedback.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings that you want to mark as useful or not useful.</p>
            feedback: <p>The feedback for the finding.</p>
            comments: <p>Additional feedback about the GuardDuty findings.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_findings_feedback_request.UpdateFindingsFeedbackRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_findings_feedback_response.UpdateFindingsFeedbackResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_findings_feedback

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_findings_feedback.update_findings_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_findings_feedback_request.UpdateFindingsFeedbackRequest = {
            "detector_id": detector_id
        }
        if finding_ids is not None:
            input_["finding_ids"] = finding_ids
        if feedback is not None:
            input_["feedback"] = feedback
        if comments is not None:
            input_["comments"] = comments

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_ip_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        ip_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "capo_guardduty.types.update_ip_set_response.UpdateIPSetResponse":
        """<p>Updates the IPSet specified by the IPSet ID.</p>

        Args:
            detector_id: <p>The detectorID that specifies the GuardDuty service whose IPSet you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            ip_set_id: <p>The unique ID that specifies the IPSet that you want to update.</p>
            name: <p>The unique ID that specifies the IPSet that you want to update.</p>
            location: <p>The updated URI of the file that contains the IPSet. </p>
            activate: <p>The updated Boolean value that specifies whether the IPSet is active or not.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_ip_set_request.UpdateIPSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_ip_set_response.UpdateIPSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_ip_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_ip_set.update_ip_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_ip_set_request.UpdateIPSetRequest = {
            "detector_id": detector_id,
            "ip_set_id": ip_set_id,
        }
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if activate is not None:
            input_["activate"] = activate
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_malware_protection_plan(
        self,
        malware_protection_plan_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        role: Optional["capo_guardduty.types.string.String"] = None,
        actions: Optional[
            "capo_guardduty.types.malware_protection_plan_actions.MalwareProtectionPlanActions"
        ] = None,
        protected_resource: Optional[
            "capo_guardduty.types.update_protected_resource.UpdateProtectedResource"
        ] = None,
    ) -> None:
        """<p>Updates an existing Malware Protection plan resource.</p>

        Args:
            malware_protection_plan_id: <p>A unique identifier associated with the Malware Protection plan.</p>
            role: <p>Amazon Resource Name (ARN) of the IAM role with permissions to scan and add tags to the associated protected resource.</p>
            actions: <p>Information about whether the tags will be added to the S3 object after scanning.</p>
            protected_resource: <p>Information about the protected resource that is associated with the created Malware Protection plan. Presently, <code>S3Bucket</code> is the only supported protected resource.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_malware_protection_plan_request.UpdateMalwareProtectionPlanRequest]",
        ) -> OperationResponse[None]:
            import capo_guardduty._operations.guard_duty_api_service.update_malware_protection_plan

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_malware_protection_plan.update_malware_protection_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_malware_protection_plan_request.UpdateMalwareProtectionPlanRequest = {
            "malware_protection_plan_id": malware_protection_plan_id
        }
        if role is not None:
            input_["role"] = role
        if actions is not None:
            input_["actions"] = actions
        if protected_resource is not None:
            input_["protected_resource"] = protected_resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_malware_scan_settings(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        scan_resource_criteria: Optional[
            "capo_guardduty.types.scan_resource_criteria.ScanResourceCriteria"
        ] = None,
        ebs_snapshot_preservation: Optional[
            "capo_guardduty.types.ebs_snapshot_preservation.EbsSnapshotPreservation"
        ] = None,
    ) -> "capo_guardduty.types.update_malware_scan_settings_response.UpdateMalwareScanSettingsResponse":
        """<p>Updates the malware scan settings.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that specifies the GuardDuty service where you want to update scan settings.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            scan_resource_criteria: <p>Represents the criteria to be used in the filter for selecting resources to scan.</p>
            ebs_snapshot_preservation: <p>An enum value representing possible snapshot preservation settings.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_malware_scan_settings_request.UpdateMalwareScanSettingsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_malware_scan_settings_response.UpdateMalwareScanSettingsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_malware_scan_settings

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_malware_scan_settings.update_malware_scan_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_malware_scan_settings_request.UpdateMalwareScanSettingsRequest = {
            "detector_id": detector_id
        }
        if scan_resource_criteria is not None:
            input_["scan_resource_criteria"] = scan_resource_criteria
        if ebs_snapshot_preservation is not None:
            input_["ebs_snapshot_preservation"] = ebs_snapshot_preservation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_member_detectors(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        account_ids: Optional["capo_guardduty.types.account_ids.AccountIds"] = None,
        data_sources: Optional[
            "capo_guardduty.types.data_source_configurations.DataSourceConfigurations"
        ] = None,
        features: Optional[
            "capo_guardduty.types.member_features_configurations.MemberFeaturesConfigurations"
        ] = None,
    ) -> "capo_guardduty.types.update_member_detectors_response.UpdateMemberDetectorsResponse":
        """<p>Contains information on member accounts to be updated.</p> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The detector ID of the administrator account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            account_ids: <p>A list of member account IDs to be updated.</p>
            data_sources: <p>Describes which data sources will be updated.</p>
            features: <p>A list of features that will be updated for the specified member accounts.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_member_detectors_request.UpdateMemberDetectorsRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_member_detectors_response.UpdateMemberDetectorsResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_member_detectors

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_member_detectors.update_member_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_member_detectors_request.UpdateMemberDetectorsRequest = {
            "detector_id": detector_id
        }
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if features is not None:
            input_["features"] = features

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_organization_configuration(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        auto_enable: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        data_sources: Optional[
            "capo_guardduty.types.organization_data_source_configurations.OrganizationDataSourceConfigurations"
        ] = None,
        features: Optional[
            "capo_guardduty.types.organization_features_configurations.OrganizationFeaturesConfigurations"
        ] = None,
        auto_enable_organization_members: Optional[
            "capo_guardduty.types.auto_enable_members.AutoEnableMembers"
        ] = None,
    ) -> "capo_guardduty.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse":
        """<p>Configures the delegated administrator account with the provided values. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>, but not both. </p> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The ID of the detector that configures the delegated administrator.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            auto_enable: <p>Represents whether to automatically enable member accounts in the organization. This applies to only new member accounts, not the existing member accounts. When a new account joins the organization, the chosen features will be enabled for them by default.</p> <p>Even though this is still supported, we recommend using <code>AutoEnableOrganizationMembers</code> to achieve the similar results. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>.</p>
            data_sources: <p>Describes which data sources will be updated.</p>
            features: <p>A list of features that will be configured for the organization.</p>
            auto_enable_organization_members: <p>Indicates the auto-enablement configuration of GuardDuty for the member accounts in the organization. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>. </p> <p>Use one of the following configuration values for <code>autoEnableOrganizationMembers</code>:</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have GuardDuty enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have GuardDuty enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> <p>It may take up to 24 hours to update the configuration for all the member accounts.</p> </li> <li> <p> <code>NONE</code>: Indicates that GuardDuty will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually.</p> <p>When you update the auto-enable setting from <code>ALL</code> or <code>NEW</code> to <code>NONE</code>, this action doesn't disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.</p> </li> </ul>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_organization_configuration

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_organization_configuration.update_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {
            "detector_id": detector_id
        }
        if auto_enable is not None:
            input_["auto_enable"] = auto_enable
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if features is not None:
            input_["features"] = features
        if auto_enable_organization_members is not None:
            input_["auto_enable_organization_members"] = (
                auto_enable_organization_members
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_publishing_destination(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        destination_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        destination_properties: Optional[
            "capo_guardduty.types.destination_properties.DestinationProperties"
        ] = None,
    ) -> "capo_guardduty.types.update_publishing_destination_response.UpdatePublishingDestinationResponse":
        """<p>Updates information about the publishing destination specified by the <code>destinationId</code>.</p>

        Args:
            detector_id: <p>The ID of the detector associated with the publishing destinations to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            destination_id: <p>The ID of the publishing destination to update.</p>
            destination_properties: <p>A <code>DestinationProperties</code> object that includes the <code>DestinationArn</code> and <code>KmsKeyArn</code> of the publishing destination.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_publishing_destination_request.UpdatePublishingDestinationRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_publishing_destination_response.UpdatePublishingDestinationResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_publishing_destination

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_publishing_destination.update_publishing_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_publishing_destination_request.UpdatePublishingDestinationRequest = {
            "detector_id": detector_id,
            "destination_id": destination_id,
        }
        if destination_properties is not None:
            input_["destination_properties"] = destination_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_threat_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        threat_entity_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
    ) -> "capo_guardduty.types.update_threat_entity_set_response.UpdateThreatEntitySetResponse":
        """<p>Updates the threat entity set associated with the specified <code>threatEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with the threat entity set that you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            threat_entity_set_id: <p>The ID returned by GuardDuty after updating the threat entity set resource.</p>
            name: <p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            location: <p>The URI of the file that contains the trusted entity set.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty is to start using this updated threat entity set. After you update an entity set, you will need to activate it again. It might take up to 15 minutes for the updated entity set to be effective.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_threat_entity_set_request.UpdateThreatEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_threat_entity_set_response.UpdateThreatEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_threat_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_threat_entity_set.update_threat_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_threat_entity_set_request.UpdateThreatEntitySetRequest = {
            "detector_id": detector_id,
            "threat_entity_set_id": threat_entity_set_id,
        }
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        if activate is not None:
            input_["activate"] = activate

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_threat_intel_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        threat_intel_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "capo_guardduty.types.update_threat_intel_set_response.UpdateThreatIntelSetResponse":
        """<p>Updates the ThreatIntelSet specified by the ThreatIntelSet ID.</p>

        Args:
            detector_id: <p>The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            threat_intel_set_id: <p>The unique ID that specifies the ThreatIntelSet that you want to update.</p>
            name: <p>The unique ID that specifies the ThreatIntelSet that you want to update.</p>
            location: <p>The updated URI of the file that contains the ThreateIntelSet.</p>
            activate: <p>The updated Boolean value that specifies whether the ThreateIntelSet is active or not.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>

        Raises:
            capo_guardduty.errors.access_denied_exception.AccessDeniedException: <p>An access denied exception object.</p>
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_threat_intel_set_request.UpdateThreatIntelSetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_threat_intel_set_response.UpdateThreatIntelSetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_threat_intel_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_threat_intel_set.update_threat_intel_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_threat_intel_set_request.UpdateThreatIntelSetRequest = {
            "detector_id": detector_id,
            "threat_intel_set_id": threat_intel_set_id,
        }
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if activate is not None:
            input_["activate"] = activate
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_trusted_entity_set(
        self,
        detector_id: "capo_guardduty.types.detector_id.DetectorId",
        trusted_entity_set_id: "capo_guardduty.types.string.String",
        *,
        config_overrides: Optional[GuardDutyClientConfig] = None,
        name: Optional["capo_guardduty.types.name.Name"] = None,
        location: Optional["capo_guardduty.types.location.Location"] = None,
        expected_bucket_owner: Optional[
            "capo_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        activate: Optional["capo_guardduty.types.boolean.Boolean"] = None,
    ) -> "capo_guardduty.types.update_trusted_entity_set_response.UpdateTrustedEntitySetResponse":
        """<p>Updates the trusted entity set associated with the specified <code>trustedEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with the threat entity set that you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>
            trusted_entity_set_id: <p>The ID returned by GuardDuty after updating the trusted entity set resource.</p>
            name: <p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            location: <p>The URI of the file that contains the trusted entity set.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty is to start using this updated trusted entity set. After you update an entity set, you will need to activate it again. It might take up to 15 minutes for the updated entity set to be effective.</p>

        Raises:
            capo_guardduty.errors.bad_request_exception.BadRequestException: <p>A bad request exception object.</p>
            capo_guardduty.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error exception object.</p>
            capo_guardduty.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_guardduty.types.update_trusted_entity_set_request.UpdateTrustedEntitySetRequest]",
        ) -> OperationResponse[
            "capo_guardduty.types.update_trusted_entity_set_response.UpdateTrustedEntitySetResponse"
        ]:
            import capo_guardduty._operations.guard_duty_api_service.update_trusted_entity_set

            output, http_response = (
                capo_guardduty._operations.guard_duty_api_service.update_trusted_entity_set.update_trusted_entity_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_guardduty.types.update_trusted_entity_set_request.UpdateTrustedEntitySetRequest = {
            "detector_id": detector_id,
            "trusted_entity_set_id": trusted_entity_set_id,
        }
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        if activate is not None:
            input_["activate"] = activate

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
