"""Generated from Smithy shape ``com.amazonaws.auditmanager#BedrockAssessmentManagerLambda``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_auditmanager._auth._signers
import capo_auditmanager._auth._sigv4
from capo_auditmanager._auth._identity import Credentials
from capo_auditmanager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_auditmanager._auth._zapros_handler import AuthMiddleware
from capo_auditmanager._pagination import resolve_path as _resolve_path
from capo_auditmanager._services._aws_config import aws_config
from capo_auditmanager._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_auditmanager.types.account_id
    import capo_auditmanager.types.action_plan_instructions
    import capo_auditmanager.types.action_plan_title
    import capo_auditmanager.types.assessment_description
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.assessment_report_description
    import capo_auditmanager.types.assessment_report_name
    import capo_auditmanager.types.assessment_reports_destination
    import capo_auditmanager.types.assessment_status
    import capo_auditmanager.types.associate_assessment_report_evidence_folder_request
    import capo_auditmanager.types.associate_assessment_report_evidence_folder_response
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.batch_associate_assessment_report_evidence_request
    import capo_auditmanager.types.batch_associate_assessment_report_evidence_response
    import capo_auditmanager.types.batch_create_delegation_by_assessment_request
    import capo_auditmanager.types.batch_create_delegation_by_assessment_response
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_request
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_response
    import capo_auditmanager.types.batch_disassociate_assessment_report_evidence_request
    import capo_auditmanager.types.batch_disassociate_assessment_report_evidence_response
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_request
    import capo_auditmanager.types.batch_import_evidence_to_assessment_control_response
    import capo_auditmanager.types.boolean
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.control_catalog_id
    import capo_auditmanager.types.control_comment_body
    import capo_auditmanager.types.control_description
    import capo_auditmanager.types.control_domain_id
    import capo_auditmanager.types.control_mapping_sources
    import capo_auditmanager.types.control_name
    import capo_auditmanager.types.control_set_id
    import capo_auditmanager.types.control_set_status
    import capo_auditmanager.types.control_status
    import capo_auditmanager.types.control_type
    import capo_auditmanager.types.create_assessment_framework_control_sets
    import capo_auditmanager.types.create_assessment_framework_request
    import capo_auditmanager.types.create_assessment_framework_response
    import capo_auditmanager.types.create_assessment_report_request
    import capo_auditmanager.types.create_assessment_report_response
    import capo_auditmanager.types.create_assessment_request
    import capo_auditmanager.types.create_assessment_response
    import capo_auditmanager.types.create_control_mapping_sources
    import capo_auditmanager.types.create_control_request
    import capo_auditmanager.types.create_control_response
    import capo_auditmanager.types.create_delegation_requests
    import capo_auditmanager.types.data_source_type
    import capo_auditmanager.types.default_export_destination
    import capo_auditmanager.types.delegation_comment
    import capo_auditmanager.types.delegation_ids
    import capo_auditmanager.types.delete_assessment_framework_request
    import capo_auditmanager.types.delete_assessment_framework_response
    import capo_auditmanager.types.delete_assessment_framework_share_request
    import capo_auditmanager.types.delete_assessment_framework_share_response
    import capo_auditmanager.types.delete_assessment_report_request
    import capo_auditmanager.types.delete_assessment_report_response
    import capo_auditmanager.types.delete_assessment_request
    import capo_auditmanager.types.delete_assessment_response
    import capo_auditmanager.types.delete_control_request
    import capo_auditmanager.types.delete_control_response
    import capo_auditmanager.types.deregister_account_request
    import capo_auditmanager.types.deregister_account_response
    import capo_auditmanager.types.deregister_organization_admin_account_request
    import capo_auditmanager.types.deregister_organization_admin_account_response
    import capo_auditmanager.types.deregistration_policy
    import capo_auditmanager.types.disassociate_assessment_report_evidence_folder_request
    import capo_auditmanager.types.disassociate_assessment_report_evidence_folder_response
    import capo_auditmanager.types.evidence_ids
    import capo_auditmanager.types.framework_description
    import capo_auditmanager.types.framework_name
    import capo_auditmanager.types.framework_type
    import capo_auditmanager.types.get_account_status_request
    import capo_auditmanager.types.get_account_status_response
    import capo_auditmanager.types.get_assessment_framework_request
    import capo_auditmanager.types.get_assessment_framework_response
    import capo_auditmanager.types.get_assessment_report_url_request
    import capo_auditmanager.types.get_assessment_report_url_response
    import capo_auditmanager.types.get_assessment_request
    import capo_auditmanager.types.get_assessment_response
    import capo_auditmanager.types.get_change_logs_request
    import capo_auditmanager.types.get_change_logs_response
    import capo_auditmanager.types.get_control_request
    import capo_auditmanager.types.get_control_response
    import capo_auditmanager.types.get_delegations_request
    import capo_auditmanager.types.get_delegations_response
    import capo_auditmanager.types.get_evidence_by_evidence_folder_request
    import capo_auditmanager.types.get_evidence_by_evidence_folder_response
    import capo_auditmanager.types.get_evidence_file_upload_url_request
    import capo_auditmanager.types.get_evidence_file_upload_url_response
    import capo_auditmanager.types.get_evidence_folder_request
    import capo_auditmanager.types.get_evidence_folder_response
    import capo_auditmanager.types.get_evidence_folders_by_assessment_control_request
    import capo_auditmanager.types.get_evidence_folders_by_assessment_control_response
    import capo_auditmanager.types.get_evidence_folders_by_assessment_request
    import capo_auditmanager.types.get_evidence_folders_by_assessment_response
    import capo_auditmanager.types.get_evidence_request
    import capo_auditmanager.types.get_evidence_response
    import capo_auditmanager.types.get_insights_by_assessment_request
    import capo_auditmanager.types.get_insights_by_assessment_response
    import capo_auditmanager.types.get_insights_request
    import capo_auditmanager.types.get_insights_response
    import capo_auditmanager.types.get_organization_admin_account_request
    import capo_auditmanager.types.get_organization_admin_account_response
    import capo_auditmanager.types.get_services_in_scope_request
    import capo_auditmanager.types.get_services_in_scope_response
    import capo_auditmanager.types.get_settings_request
    import capo_auditmanager.types.get_settings_response
    import capo_auditmanager.types.kms_key
    import capo_auditmanager.types.list_assessment_control_insights_by_control_domain_request
    import capo_auditmanager.types.list_assessment_control_insights_by_control_domain_response
    import capo_auditmanager.types.list_assessment_framework_share_requests_request
    import capo_auditmanager.types.list_assessment_framework_share_requests_response
    import capo_auditmanager.types.list_assessment_frameworks_request
    import capo_auditmanager.types.list_assessment_frameworks_response
    import capo_auditmanager.types.list_assessment_reports_request
    import capo_auditmanager.types.list_assessment_reports_response
    import capo_auditmanager.types.list_assessments_request
    import capo_auditmanager.types.list_assessments_response
    import capo_auditmanager.types.list_control_domain_insights_by_assessment_request
    import capo_auditmanager.types.list_control_domain_insights_by_assessment_response
    import capo_auditmanager.types.list_control_domain_insights_request
    import capo_auditmanager.types.list_control_domain_insights_response
    import capo_auditmanager.types.list_control_insights_by_control_domain_request
    import capo_auditmanager.types.list_control_insights_by_control_domain_response
    import capo_auditmanager.types.list_controls_request
    import capo_auditmanager.types.list_controls_response
    import capo_auditmanager.types.list_keywords_for_data_source_request
    import capo_auditmanager.types.list_keywords_for_data_source_response
    import capo_auditmanager.types.list_notifications_request
    import capo_auditmanager.types.list_notifications_response
    import capo_auditmanager.types.list_tags_for_resource_request
    import capo_auditmanager.types.list_tags_for_resource_response
    import capo_auditmanager.types.manual_evidence_list
    import capo_auditmanager.types.manual_evidence_local_file_name
    import capo_auditmanager.types.max_results
    import capo_auditmanager.types.query_statement
    import capo_auditmanager.types.region
    import capo_auditmanager.types.register_account_request
    import capo_auditmanager.types.register_account_response
    import capo_auditmanager.types.register_organization_admin_account_request
    import capo_auditmanager.types.register_organization_admin_account_response
    import capo_auditmanager.types.roles
    import capo_auditmanager.types.s3_url
    import capo_auditmanager.types.scope
    import capo_auditmanager.types.setting_attribute
    import capo_auditmanager.types.share_request_action
    import capo_auditmanager.types.share_request_comment
    import capo_auditmanager.types.share_request_type
    import capo_auditmanager.types.sns_arn
    import capo_auditmanager.types.start_assessment_framework_share_request
    import capo_auditmanager.types.start_assessment_framework_share_response
    import capo_auditmanager.types.string
    import capo_auditmanager.types.tag_key_list
    import capo_auditmanager.types.tag_map
    import capo_auditmanager.types.tag_resource_request
    import capo_auditmanager.types.tag_resource_response
    import capo_auditmanager.types.testing_information
    import capo_auditmanager.types.token
    import capo_auditmanager.types.untag_resource_request
    import capo_auditmanager.types.untag_resource_response
    import capo_auditmanager.types.update_assessment_control_request
    import capo_auditmanager.types.update_assessment_control_response
    import capo_auditmanager.types.update_assessment_control_set_status_request
    import capo_auditmanager.types.update_assessment_control_set_status_response
    import capo_auditmanager.types.update_assessment_framework_control_sets
    import capo_auditmanager.types.update_assessment_framework_request
    import capo_auditmanager.types.update_assessment_framework_response
    import capo_auditmanager.types.update_assessment_framework_share_request
    import capo_auditmanager.types.update_assessment_framework_share_response
    import capo_auditmanager.types.update_assessment_request
    import capo_auditmanager.types.update_assessment_response
    import capo_auditmanager.types.update_assessment_status_request
    import capo_auditmanager.types.update_assessment_status_response
    import capo_auditmanager.types.update_control_request
    import capo_auditmanager.types.update_control_response
    import capo_auditmanager.types.update_settings_request
    import capo_auditmanager.types.update_settings_response
    import capo_auditmanager.types.uuid
    import capo_auditmanager.types.validate_assessment_report_integrity_request
    import capo_auditmanager.types.validate_assessment_report_integrity_response


class AuditManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AuditManagerClient:
    """A client for the ``AuditManager`` service.

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
        self._config = AuditManagerClientConfig(
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
        self, config_overrides: Optional[AuditManagerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AuditManagerClientConfig = config_overrides or {}
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

    def associate_assessment_report_evidence_folder(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.associate_assessment_report_evidence_folder_response.AssociateAssessmentReportEvidenceFolderResponse":
        """<p> Associates an evidence folder to an assessment report in an Audit Manager assessment. </p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>
            evidence_folder_id: <p> The identifier for the folder that the evidence is stored in. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.associate_assessment_report_evidence_folder_request.AssociateAssessmentReportEvidenceFolderRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.associate_assessment_report_evidence_folder_response.AssociateAssessmentReportEvidenceFolderResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.associate_assessment_report_evidence_folder

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.associate_assessment_report_evidence_folder.associate_assessment_report_evidence_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.associate_assessment_report_evidence_folder_request.AssociateAssessmentReportEvidenceFolderRequest = {
            "assessment_id": assessment_id,
            "evidence_folder_id": evidence_folder_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_associate_assessment_report_evidence(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        evidence_ids: "capo_auditmanager.types.evidence_ids.EvidenceIds",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.batch_associate_assessment_report_evidence_response.BatchAssociateAssessmentReportEvidenceResponse":
        """<p> Associates a list of evidence to an assessment report in an Audit Manager assessment. </p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>
            evidence_folder_id: <p> The identifier for the folder that the evidence is stored in. </p>
            evidence_ids: <p> The list of evidence identifiers. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.batch_associate_assessment_report_evidence_request.BatchAssociateAssessmentReportEvidenceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.batch_associate_assessment_report_evidence_response.BatchAssociateAssessmentReportEvidenceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_associate_assessment_report_evidence

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_associate_assessment_report_evidence.batch_associate_assessment_report_evidence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.batch_associate_assessment_report_evidence_request.BatchAssociateAssessmentReportEvidenceRequest = {
            "assessment_id": assessment_id,
            "evidence_folder_id": evidence_folder_id,
            "evidence_ids": evidence_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_create_delegation_by_assessment(
        self,
        create_delegation_requests: "capo_auditmanager.types.create_delegation_requests.CreateDelegationRequests",
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.batch_create_delegation_by_assessment_response.BatchCreateDelegationByAssessmentResponse":
        """<p> Creates a batch of delegations for an assessment in Audit Manager. </p>

        Args:
            create_delegation_requests: <p> The API request to batch create delegations in Audit Manager. </p>
            assessment_id: <p> The identifier for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.batch_create_delegation_by_assessment_request.BatchCreateDelegationByAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.batch_create_delegation_by_assessment_response.BatchCreateDelegationByAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_create_delegation_by_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_create_delegation_by_assessment.batch_create_delegation_by_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.batch_create_delegation_by_assessment_request.BatchCreateDelegationByAssessmentRequest = {
            "create_delegation_requests": create_delegation_requests,
            "assessment_id": assessment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_delegation_by_assessment(
        self,
        delegation_ids: "capo_auditmanager.types.delegation_ids.DelegationIds",
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.batch_delete_delegation_by_assessment_response.BatchDeleteDelegationByAssessmentResponse":
        """<p> Deletes a batch of delegations for an assessment in Audit Manager. </p>

        Args:
            delegation_ids: <p> The identifiers for the delegations. </p>
            assessment_id: <p> The identifier for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.batch_delete_delegation_by_assessment_request.BatchDeleteDelegationByAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.batch_delete_delegation_by_assessment_response.BatchDeleteDelegationByAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_delete_delegation_by_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_delete_delegation_by_assessment.batch_delete_delegation_by_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.batch_delete_delegation_by_assessment_request.BatchDeleteDelegationByAssessmentRequest = {
            "delegation_ids": delegation_ids,
            "assessment_id": assessment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_disassociate_assessment_report_evidence(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        evidence_ids: "capo_auditmanager.types.evidence_ids.EvidenceIds",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.batch_disassociate_assessment_report_evidence_response.BatchDisassociateAssessmentReportEvidenceResponse":
        """<p> Disassociates a list of evidence from an assessment report in Audit Manager. </p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>
            evidence_folder_id: <p> The identifier for the folder that the evidence is stored in. </p>
            evidence_ids: <p> The list of evidence identifiers. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.batch_disassociate_assessment_report_evidence_request.BatchDisassociateAssessmentReportEvidenceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.batch_disassociate_assessment_report_evidence_response.BatchDisassociateAssessmentReportEvidenceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_disassociate_assessment_report_evidence

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_disassociate_assessment_report_evidence.batch_disassociate_assessment_report_evidence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.batch_disassociate_assessment_report_evidence_request.BatchDisassociateAssessmentReportEvidenceRequest = {
            "assessment_id": assessment_id,
            "evidence_folder_id": evidence_folder_id,
            "evidence_ids": evidence_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_import_evidence_to_assessment_control(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        control_id: "capo_auditmanager.types.uuid.UUID",
        manual_evidence: "capo_auditmanager.types.manual_evidence_list.ManualEvidenceList",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.batch_import_evidence_to_assessment_control_response.BatchImportEvidenceToAssessmentControlResponse":
        """<p>Adds one or more pieces of evidence to a control in an Audit Manager assessment. </p> <p>You can import manual evidence from any S3 bucket by specifying the S3 URI of the object. You can also upload a file from your browser, or enter plain text in response to a risk assessment question. </p> <p>The following restrictions apply to this action:</p> <ul> <li> <p> <code>manualEvidence</code> can be only one of the following: <code>evidenceFileName</code>, <code>s3ResourcePath</code>, or <code>textResponse</code> </p> </li> <li> <p>Maximum size of an individual evidence file: 100 MB</p> </li> <li> <p>Number of daily manual evidence uploads per control: 100</p> </li> <li> <p>Supported file formats: See <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files">Supported file types for manual evidence</a> in the <i>Audit Manager User Guide</i> </p> </li> </ul> <p>For more information about Audit Manager service restrictions, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>
            control_set_id: <p> The identifier for the control set. </p>
            control_id: <p> The identifier for the control. </p>
            manual_evidence: <p> The list of manual evidence objects. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.batch_import_evidence_to_assessment_control_request.BatchImportEvidenceToAssessmentControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.batch_import_evidence_to_assessment_control_response.BatchImportEvidenceToAssessmentControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_import_evidence_to_assessment_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.batch_import_evidence_to_assessment_control.batch_import_evidence_to_assessment_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.batch_import_evidence_to_assessment_control_request.BatchImportEvidenceToAssessmentControlRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "control_id": control_id,
            "manual_evidence": manual_evidence,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_assessment(
        self,
        name: "capo_auditmanager.types.assessment_name.AssessmentName",
        assessment_reports_destination: "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination",
        scope: "capo_auditmanager.types.scope.Scope",
        roles: "capo_auditmanager.types.roles.Roles",
        framework_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        description: Optional[
            "capo_auditmanager.types.assessment_description.AssessmentDescription"
        ] = None,
        tags: Optional["capo_auditmanager.types.tag_map.TagMap"] = None,
    ) -> "capo_auditmanager.types.create_assessment_response.CreateAssessmentResponse":
        """<p> Creates an assessment in Audit Manager. </p>

        Args:
            name: <p> The name of the assessment to be created. </p>
            description: <p> The optional description of the assessment to be created. </p>
            assessment_reports_destination: <p> The assessment report storage destination for the assessment that's being created. </p>
            roles: <p> The list of roles for the assessment. </p>
            framework_id: <p> The identifier for the framework that the assessment will be created from. </p>
            tags: <p> The tags that are associated with the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.create_assessment_request.CreateAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.create_assessment_response.CreateAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_assessment.create_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.create_assessment_request.CreateAssessmentRequest = {
            "name": name,
            "assessment_reports_destination": assessment_reports_destination,
            "scope": scope,
            "roles": roles,
            "framework_id": framework_id,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_assessment_framework(
        self,
        name: "capo_auditmanager.types.framework_name.FrameworkName",
        control_sets: "capo_auditmanager.types.create_assessment_framework_control_sets.CreateAssessmentFrameworkControlSets",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        description: Optional[
            "capo_auditmanager.types.framework_description.FrameworkDescription"
        ] = None,
        compliance_type: Optional[
            "capo_auditmanager.types.compliance_type.ComplianceType"
        ] = None,
        tags: Optional["capo_auditmanager.types.tag_map.TagMap"] = None,
    ) -> "capo_auditmanager.types.create_assessment_framework_response.CreateAssessmentFrameworkResponse":
        """<p> Creates a custom framework in Audit Manager. </p>

        Args:
            name: <p> The name of the new custom framework. </p>
            description: <p> An optional description for the new custom framework. </p>
            compliance_type: <p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>
            control_sets: <p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>
            tags: <p> The tags that are associated with the framework. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.create_assessment_framework_request.CreateAssessmentFrameworkRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.create_assessment_framework_response.CreateAssessmentFrameworkResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_assessment_framework

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_assessment_framework.create_assessment_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.create_assessment_framework_request.CreateAssessmentFrameworkRequest = {
            "name": name,
            "control_sets": control_sets,
        }
        if description is not None:
            input_["description"] = description
        if compliance_type is not None:
            input_["compliance_type"] = compliance_type
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_assessment_report(
        self,
        name: "capo_auditmanager.types.assessment_report_name.AssessmentReportName",
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        description: Optional[
            "capo_auditmanager.types.assessment_report_description.AssessmentReportDescription"
        ] = None,
        query_statement: Optional[
            "capo_auditmanager.types.query_statement.QueryStatement"
        ] = None,
    ) -> "capo_auditmanager.types.create_assessment_report_response.CreateAssessmentReportResponse":
        """<p> Creates an assessment report for the specified assessment. </p>

        Args:
            name: <p> The name of the new assessment report. </p>
            description: <p> The description of the assessment report. </p>
            assessment_id: <p> The identifier for the assessment. </p>
            query_statement: <p>A SQL statement that represents an evidence finder query.</p> <p>Provide this parameter when you want to generate an assessment report from the results of an evidence finder search query. When you use this parameter, Audit Manager generates a one-time report using only the evidence from the query output. This report does not include any assessment evidence that was manually <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#generate-assessment-report-include-evidence">added to a report using the console</a>, or <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchAssociateAssessmentReportEvidence.html">associated with a report using the API</a>. </p> <p>To use this parameter, the <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_EvidenceFinderEnablement.html#auditmanager-Type-EvidenceFinderEnablement-enablementStatus">enablementStatus</a> of evidence finder must be <code>ENABLED</code>. </p> <p> For examples and help resolving <code>queryStatement</code> validation exceptions, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-issues.html#querystatement-exceptions">Troubleshooting evidence finder issues</a> in the <i>Audit Manager User Guide.</i> </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.create_assessment_report_request.CreateAssessmentReportRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.create_assessment_report_response.CreateAssessmentReportResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_assessment_report

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_assessment_report.create_assessment_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.create_assessment_report_request.CreateAssessmentReportRequest = {
            "name": name,
            "assessment_id": assessment_id,
        }
        if description is not None:
            input_["description"] = description
        if query_statement is not None:
            input_["query_statement"] = query_statement

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_control(
        self,
        name: "capo_auditmanager.types.control_name.ControlName",
        control_mapping_sources: "capo_auditmanager.types.create_control_mapping_sources.CreateControlMappingSources",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        description: Optional[
            "capo_auditmanager.types.control_description.ControlDescription"
        ] = None,
        testing_information: Optional[
            "capo_auditmanager.types.testing_information.TestingInformation"
        ] = None,
        action_plan_title: Optional[
            "capo_auditmanager.types.action_plan_title.ActionPlanTitle"
        ] = None,
        action_plan_instructions: Optional[
            "capo_auditmanager.types.action_plan_instructions.ActionPlanInstructions"
        ] = None,
        tags: Optional["capo_auditmanager.types.tag_map.TagMap"] = None,
    ) -> "capo_auditmanager.types.create_control_response.CreateControlResponse":
        """<p> Creates a new custom control in Audit Manager. </p>

        Args:
            name: <p> The name of the control. </p>
            description: <p> The description of the control. </p>
            testing_information: <p> The steps to follow to determine if the control is satisfied. </p>
            action_plan_title: <p> The title of the action plan for remediating the control. </p>
            action_plan_instructions: <p> The recommended actions to carry out if the control isn't fulfilled. </p>
            control_mapping_sources: <p> The data mapping sources for the control. </p>
            tags: <p> The tags that are associated with the control. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.create_control_request.CreateControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.create_control_response.CreateControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.create_control.create_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.create_control_request.CreateControlRequest = {
            "name": name,
            "control_mapping_sources": control_mapping_sources,
        }
        if description is not None:
            input_["description"] = description
        if testing_information is not None:
            input_["testing_information"] = testing_information
        if action_plan_title is not None:
            input_["action_plan_title"] = action_plan_title
        if action_plan_instructions is not None:
            input_["action_plan_instructions"] = action_plan_instructions
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.delete_assessment_response.DeleteAssessmentResponse":
        """<p> Deletes an assessment in Audit Manager. </p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.delete_assessment_request.DeleteAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.delete_assessment_response.DeleteAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment.delete_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.delete_assessment_request.DeleteAssessmentRequest = {
            "assessment_id": assessment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment_framework(
        self,
        framework_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.delete_assessment_framework_response.DeleteAssessmentFrameworkResponse":
        """<p> Deletes a custom framework in Audit Manager. </p>

        Args:
            framework_id: <p> The identifier for the custom framework. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.delete_assessment_framework_request.DeleteAssessmentFrameworkRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.delete_assessment_framework_response.DeleteAssessmentFrameworkResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment_framework

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment_framework.delete_assessment_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.delete_assessment_framework_request.DeleteAssessmentFrameworkRequest = {
            "framework_id": framework_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment_framework_share(
        self,
        request_id: "capo_auditmanager.types.uuid.UUID",
        request_type: "capo_auditmanager.types.share_request_type.ShareRequestType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.delete_assessment_framework_share_response.DeleteAssessmentFrameworkShareResponse":
        """<p> Deletes a share request for a custom framework in Audit Manager. </p>

        Args:
            request_id: <p>The unique identifier for the share request to be deleted.</p>
            request_type: <p>Specifies whether the share request is a sent request or a received request.</p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.delete_assessment_framework_share_request.DeleteAssessmentFrameworkShareRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.delete_assessment_framework_share_response.DeleteAssessmentFrameworkShareResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment_framework_share

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment_framework_share.delete_assessment_framework_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.delete_assessment_framework_share_request.DeleteAssessmentFrameworkShareRequest = {
            "request_id": request_id,
            "request_type": request_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_assessment_report(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        assessment_report_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.delete_assessment_report_response.DeleteAssessmentReportResponse":
        """<p>Deletes an assessment report in Audit Manager. </p> <p>When you run the <code>DeleteAssessmentReport</code> operation, Audit Manager attempts to delete the following data:</p> <ol> <li> <p>The specified assessment report that’s stored in your S3 bucket</p> </li> <li> <p>The associated metadata that’s stored in Audit Manager</p> </li> </ol> <p>If Audit Manager can’t access the assessment report in your S3 bucket, the report isn’t deleted. In this event, the <code>DeleteAssessmentReport</code> operation doesn’t fail. Instead, it proceeds to delete the associated metadata only. You must then delete the assessment report from the S3 bucket yourself. </p> <p>This scenario happens when Audit Manager receives a <code>403 (Forbidden)</code> or <code>404 (Not Found)</code> error from Amazon S3. To avoid this, make sure that your S3 bucket is available, and that you configured the correct permissions for Audit Manager to delete resources in your S3 bucket. For an example permissions policy that you can use, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#full-administrator-access-assessment-report-destination">Assessment report destination permissions</a> in the <i>Audit Manager User Guide</i>. For information about the issues that could cause a <code>403 (Forbidden)</code> or <code>404 (Not Found</code>) error from Amazon S3, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#ErrorCodeList">List of Error Codes</a> in the <i>Amazon Simple Storage Service API Reference</i>. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            assessment_report_id: <p> The unique identifier for the assessment report. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.delete_assessment_report_request.DeleteAssessmentReportRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.delete_assessment_report_response.DeleteAssessmentReportResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment_report

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_assessment_report.delete_assessment_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.delete_assessment_report_request.DeleteAssessmentReportRequest = {
            "assessment_id": assessment_id,
            "assessment_report_id": assessment_report_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_control(
        self,
        control_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.delete_control_response.DeleteControlResponse":
        """<p> Deletes a custom control in Audit Manager. </p> <important> <p>When you invoke this operation, the custom control is deleted from any frameworks or assessments that it’s currently part of. As a result, Audit Manager will stop collecting evidence for that custom control in all of your assessments. This includes assessments that you previously created before you deleted the custom control.</p> </important>

        Args:
            control_id: <p> The unique identifier for the control. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.delete_control_request.DeleteControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.delete_control_response.DeleteControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.delete_control.delete_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.delete_control_request.DeleteControlRequest = {
            "control_id": control_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_account(
        self, *, config_overrides: Optional[AuditManagerClientConfig] = None
    ) -> (
        "capo_auditmanager.types.deregister_account_response.DeregisterAccountResponse"
    ):
        """<p> Deregisters an account in Audit Manager. </p> <note> <p>Before you deregister, you can use the <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html">UpdateSettings</a> API operation to set your preferred data retention policy. By default, Audit Manager retains your data. If you want to delete your data, you can use the <code>DeregistrationPolicy</code> attribute to request the deletion of your data. </p> <p>For more information about data retention, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/data-protection.html">Data Protection</a> in the <i>Audit Manager User Guide</i>. </p> </note>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.deregister_account_request.DeregisterAccountRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.deregister_account_response.DeregisterAccountResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.deregister_account

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.deregister_account.deregister_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.deregister_account_request.DeregisterAccountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_organization_admin_account(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        admin_account_id: Optional[
            "capo_auditmanager.types.account_id.AccountId"
        ] = None,
    ) -> "capo_auditmanager.types.deregister_organization_admin_account_response.DeregisterOrganizationAdminAccountResponse":
        """<p>Removes the specified Amazon Web Services account as a delegated administrator for Audit Manager. </p> <p>When you remove a delegated administrator from your Audit Manager settings, you continue to have access to the evidence that you previously collected under that account. This is also the case when you deregister a delegated administrator from Organizations. However, Audit Manager stops collecting and attaching evidence to that delegated administrator account moving forward.</p> <important> <p>Keep in mind the following cleanup task if you use evidence finder:</p> <p>Before you use your management account to remove a delegated administrator, make sure that the current delegated administrator account signs in to Audit Manager and disables evidence finder first. Disabling evidence finder automatically deletes the event data store that was created in their account when they enabled evidence finder. If this task isn’t completed, the event data store remains in their account. In this case, we recommend that the original delegated administrator goes to CloudTrail Lake and manually <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-eds-disable-termination.html">deletes the event data store</a>.</p> <p>This cleanup task is necessary to ensure that you don't end up with multiple event data stores. Audit Manager ignores an unused event data store after you remove or change a delegated administrator account. However, the unused event data store continues to incur storage costs from CloudTrail Lake if you don't delete it.</p> </important> <p>When you deregister a delegated administrator account for Audit Manager, the data for that account isn’t deleted. If you want to delete resource data for a delegated administrator account, you must perform that task separately before you deregister the account. Either, you can do this in the Audit Manager console. Or, you can use one of the delete API operations that are provided by Audit Manager. </p> <p>To delete your Audit Manager resource data, see the following instructions: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessment.html">DeleteAssessment</a> (see also: <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-assessment.html">Deleting an assessment</a> in the <i>Audit Manager User Guide</i>)</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html">DeleteAssessmentFramework</a> (see also: <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-custom-framework.html">Deleting a custom framework</a> in the <i>Audit Manager User Guide</i>)</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFrameworkShare.html">DeleteAssessmentFrameworkShare</a> (see also: <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/deleting-shared-framework-requests.html">Deleting a share request</a> in the <i>Audit Manager User Guide</i>)</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html">DeleteAssessmentReport</a> (see also: <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#delete-assessment-report-steps">Deleting an assessment report</a> in the <i>Audit Manager User Guide</i>)</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteControl.html">DeleteControl</a> (see also: <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/delete-controls.html">Deleting a custom control</a> in the <i>Audit Manager User Guide</i>)</p> </li> </ul> <p>At this time, Audit Manager doesn't provide an option to delete evidence for a specific delegated administrator. Instead, when your management account deregisters Audit Manager, we perform a cleanup for the current delegated administrator account at the time of deregistration.</p>

        Args:
            admin_account_id: <p> The identifier for the administrator account. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.deregister_organization_admin_account_request.DeregisterOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.deregister_organization_admin_account_response.DeregisterOrganizationAdminAccountResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.deregister_organization_admin_account

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.deregister_organization_admin_account.deregister_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.deregister_organization_admin_account_request.DeregisterOrganizationAdminAccountRequest = {}
        if admin_account_id is not None:
            input_["admin_account_id"] = admin_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_assessment_report_evidence_folder(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.disassociate_assessment_report_evidence_folder_response.DisassociateAssessmentReportEvidenceFolderResponse":
        """<p> Disassociates an evidence folder from the specified assessment report in Audit Manager. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            evidence_folder_id: <p> The unique identifier for the folder that the evidence is stored in. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.disassociate_assessment_report_evidence_folder_request.DisassociateAssessmentReportEvidenceFolderRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.disassociate_assessment_report_evidence_folder_response.DisassociateAssessmentReportEvidenceFolderResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.disassociate_assessment_report_evidence_folder

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.disassociate_assessment_report_evidence_folder.disassociate_assessment_report_evidence_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.disassociate_assessment_report_evidence_folder_request.DisassociateAssessmentReportEvidenceFolderRequest = {
            "assessment_id": assessment_id,
            "evidence_folder_id": evidence_folder_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_status(
        self, *, config_overrides: Optional[AuditManagerClientConfig] = None
    ) -> "capo_auditmanager.types.get_account_status_response.GetAccountStatusResponse":
        """<p> Gets the registration status of an account in Audit Manager. </p>

        Raises:
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_account_status_request.GetAccountStatusRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_account_status_response.GetAccountStatusResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_account_status

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_account_status.get_account_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_account_status_request.GetAccountStatusRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_assessment_response.GetAssessmentResponse":
        """<p>Gets information about a specified assessment. </p>

        Args:
            assessment_id: <p>The unique identifier for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_assessment_request.GetAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_assessment_response.GetAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_assessment.get_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_assessment_request.GetAssessmentRequest = {
            "assessment_id": assessment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_assessment_framework(
        self,
        framework_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_assessment_framework_response.GetAssessmentFrameworkResponse":
        """<p>Gets information about a specified framework.</p>

        Args:
            framework_id: <p> The identifier for the framework. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_assessment_framework_request.GetAssessmentFrameworkRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_assessment_framework_response.GetAssessmentFrameworkResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_assessment_framework

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_assessment_framework.get_assessment_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_assessment_framework_request.GetAssessmentFrameworkRequest = {
            "framework_id": framework_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_assessment_report_url(
        self,
        assessment_report_id: "capo_auditmanager.types.uuid.UUID",
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_assessment_report_url_response.GetAssessmentReportUrlResponse":
        """<p> Gets the URL of an assessment report in Audit Manager. </p>

        Args:
            assessment_report_id: <p> The unique identifier for the assessment report. </p>
            assessment_id: <p> The unique identifier for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_assessment_report_url_request.GetAssessmentReportUrlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_assessment_report_url_response.GetAssessmentReportUrlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_assessment_report_url

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_assessment_report_url.get_assessment_report_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_assessment_report_url_request.GetAssessmentReportUrlRequest = {
            "assessment_report_id": assessment_report_id,
            "assessment_id": assessment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_change_logs(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        control_set_id: Optional[
            "capo_auditmanager.types.control_set_id.ControlSetId"
        ] = None,
        control_id: Optional["capo_auditmanager.types.uuid.UUID"] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.get_change_logs_response.GetChangeLogsResponse":
        """<p> Gets a list of changelogs from Audit Manager. </p>

        Args:
            assessment_id: <p>The unique identifier for the assessment. </p>
            control_set_id: <p> The unique identifier for the control set. </p>
            control_id: <p> The unique identifier for the control. </p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p>Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_change_logs_request.GetChangeLogsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_change_logs_response.GetChangeLogsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_change_logs

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_change_logs.get_change_logs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_change_logs_request.GetChangeLogsRequest = {
            "assessment_id": assessment_id
        }
        if control_set_id is not None:
            input_["control_set_id"] = control_set_id
        if control_id is not None:
            input_["control_id"] = control_id
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

    def iter_get_change_logs(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        control_set_id: Optional[
            "capo_auditmanager.types.control_set_id.ControlSetId"
        ] = None,
        control_id: Optional["capo_auditmanager.types.uuid.UUID"] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.get_change_logs_response.GetChangeLogsResponse]":
        _token = next_token
        while True:
            _response = self.get_change_logs(
                assessment_id,
                config_overrides=config_overrides,
                control_set_id=control_set_id,
                control_id=control_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_control(
        self,
        control_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_control_response.GetControlResponse":
        """<p> Gets information about a specified control.</p>

        Args:
            control_id: <p> The identifier for the control. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_control_request.GetControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_control_response.GetControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_control.get_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_control_request.GetControlRequest = {
            "control_id": control_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_delegations(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.get_delegations_response.GetDelegationsResponse":
        """<p> Gets a list of delegations from an audit owner to a delegate. </p>

        Args:
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_delegations_request.GetDelegationsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_delegations_response.GetDelegationsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_delegations

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_delegations.get_delegations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_delegations_request.GetDelegationsRequest = {}
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

    def iter_get_delegations(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.get_delegations_response.GetDelegationsResponse]":
        _token = next_token
        while True:
            _response = self.get_delegations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_evidence(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        evidence_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_evidence_response.GetEvidenceResponse":
        """<p> Gets information about a specified evidence item.</p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            control_set_id: <p> The unique identifier for the control set. </p>
            evidence_folder_id: <p> The unique identifier for the folder that the evidence is stored in. </p>
            evidence_id: <p> The unique identifier for the evidence. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_evidence_request.GetEvidenceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_evidence_response.GetEvidenceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence.get_evidence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_evidence_request.GetEvidenceRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "evidence_folder_id": evidence_folder_id,
            "evidence_id": evidence_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_evidence_by_evidence_folder(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.get_evidence_by_evidence_folder_response.GetEvidenceByEvidenceFolderResponse":
        """<p> Gets all evidence from a specified evidence folder in Audit Manager. </p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>
            control_set_id: <p> The identifier for the control set. </p>
            evidence_folder_id: <p> The unique identifier for the folder that the evidence is stored in. </p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_evidence_by_evidence_folder_request.GetEvidenceByEvidenceFolderRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_evidence_by_evidence_folder_response.GetEvidenceByEvidenceFolderResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_by_evidence_folder

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_by_evidence_folder.get_evidence_by_evidence_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_evidence_by_evidence_folder_request.GetEvidenceByEvidenceFolderRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "evidence_folder_id": evidence_folder_id,
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

    def iter_get_evidence_by_evidence_folder(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.get_evidence_by_evidence_folder_response.GetEvidenceByEvidenceFolderResponse]":
        _token = next_token
        while True:
            _response = self.get_evidence_by_evidence_folder(
                assessment_id,
                control_set_id,
                evidence_folder_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_evidence_file_upload_url(
        self,
        file_name: "capo_auditmanager.types.manual_evidence_local_file_name.ManualEvidenceLocalFileName",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_evidence_file_upload_url_response.GetEvidenceFileUploadUrlResponse":
        """<p>Creates a presigned Amazon S3 URL that can be used to upload a file as manual evidence. For instructions on how to use this operation, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#how-to-upload-manual-evidence-files">Upload a file from your browser </a> in the <i>Audit Manager User Guide</i>.</p> <p>The following restrictions apply to this operation:</p> <ul> <li> <p>Maximum size of an individual evidence file: 100 MB</p> </li> <li> <p>Number of daily manual evidence uploads per control: 100</p> </li> <li> <p>Supported file formats: See <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files">Supported file types for manual evidence</a> in the <i>Audit Manager User Guide</i> </p> </li> </ul> <p>For more information about Audit Manager service restrictions, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>

        Args:
            file_name: <p>The file that you want to upload. For a list of supported file formats, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files">Supported file types for manual evidence</a> in the <i>Audit Manager User Guide</i>.</p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_evidence_file_upload_url_request.GetEvidenceFileUploadUrlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_evidence_file_upload_url_response.GetEvidenceFileUploadUrlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_file_upload_url

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_file_upload_url.get_evidence_file_upload_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_evidence_file_upload_url_request.GetEvidenceFileUploadUrlRequest = {
            "file_name": file_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_evidence_folder(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        evidence_folder_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> (
        "capo_auditmanager.types.get_evidence_folder_response.GetEvidenceFolderResponse"
    ):
        """<p> Gets an evidence folder from a specified assessment in Audit Manager. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            control_set_id: <p> The unique identifier for the control set. </p>
            evidence_folder_id: <p> The unique identifier for the folder that the evidence is stored in. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_evidence_folder_request.GetEvidenceFolderRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_evidence_folder_response.GetEvidenceFolderResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_folder

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_folder.get_evidence_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_evidence_folder_request.GetEvidenceFolderRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "evidence_folder_id": evidence_folder_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_evidence_folders_by_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.get_evidence_folders_by_assessment_response.GetEvidenceFoldersByAssessmentResponse":
        """<p> Gets the evidence folders from a specified assessment in Audit Manager. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_evidence_folders_by_assessment_request.GetEvidenceFoldersByAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_evidence_folders_by_assessment_response.GetEvidenceFoldersByAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_folders_by_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_folders_by_assessment.get_evidence_folders_by_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_evidence_folders_by_assessment_request.GetEvidenceFoldersByAssessmentRequest = {
            "assessment_id": assessment_id
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

    def iter_get_evidence_folders_by_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.get_evidence_folders_by_assessment_response.GetEvidenceFoldersByAssessmentResponse]":
        _token = next_token
        while True:
            _response = self.get_evidence_folders_by_assessment(
                assessment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_evidence_folders_by_assessment_control(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        control_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.get_evidence_folders_by_assessment_control_response.GetEvidenceFoldersByAssessmentControlResponse":
        """<p> Gets a list of evidence folders that are associated with a specified control in an Audit Manager assessment. </p>

        Args:
            assessment_id: <p> The identifier for the assessment. </p>
            control_set_id: <p> The identifier for the control set. </p>
            control_id: <p> The identifier for the control. </p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_evidence_folders_by_assessment_control_request.GetEvidenceFoldersByAssessmentControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_evidence_folders_by_assessment_control_response.GetEvidenceFoldersByAssessmentControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_folders_by_assessment_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_evidence_folders_by_assessment_control.get_evidence_folders_by_assessment_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_evidence_folders_by_assessment_control_request.GetEvidenceFoldersByAssessmentControlRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "control_id": control_id,
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

    def iter_get_evidence_folders_by_assessment_control(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        control_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.get_evidence_folders_by_assessment_control_response.GetEvidenceFoldersByAssessmentControlResponse]":
        _token = next_token
        while True:
            _response = self.get_evidence_folders_by_assessment_control(
                assessment_id,
                control_set_id,
                control_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_insights(
        self, *, config_overrides: Optional[AuditManagerClientConfig] = None
    ) -> "capo_auditmanager.types.get_insights_response.GetInsightsResponse":
        """<p>Gets the latest analytics data for all your current active assessments. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_insights_request.GetInsightsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_insights_response.GetInsightsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_insights

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_insights.get_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_insights_request.GetInsightsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_insights_by_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_insights_by_assessment_response.GetInsightsByAssessmentResponse":
        """<p>Gets the latest analytics data for a specific active assessment. </p>

        Args:
            assessment_id: <p>The unique identifier for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_insights_by_assessment_request.GetInsightsByAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_insights_by_assessment_response.GetInsightsByAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_insights_by_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_insights_by_assessment.get_insights_by_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_insights_by_assessment_request.GetInsightsByAssessmentRequest = {
            "assessment_id": assessment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_organization_admin_account(
        self, *, config_overrides: Optional[AuditManagerClientConfig] = None
    ) -> "capo_auditmanager.types.get_organization_admin_account_response.GetOrganizationAdminAccountResponse":
        """<p> Gets the name of the delegated Amazon Web Services administrator account for a specified organization. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_organization_admin_account_request.GetOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_organization_admin_account_response.GetOrganizationAdminAccountResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_organization_admin_account

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_organization_admin_account.get_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_organization_admin_account_request.GetOrganizationAdminAccountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_services_in_scope(
        self, *, config_overrides: Optional[AuditManagerClientConfig] = None
    ) -> "capo_auditmanager.types.get_services_in_scope_response.GetServicesInScopeResponse":
        """<p>Gets a list of the Amazon Web Services services from which Audit Manager can collect evidence. </p> <p>Audit Manager defines which Amazon Web Services services are in scope for an assessment. Audit Manager infers this scope by examining the assessment’s controls and their data sources, and then mapping this information to one or more of the corresponding Amazon Web Services services that are in this list.</p> <note> <p>For information about why it's no longer possible to specify services in scope manually, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-collection-issues.html#unable-to-edit-services">I can't edit the services in scope for my assessment</a> in the <i>Troubleshooting</i> section of the Audit Manager user guide.</p> </note>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_services_in_scope_request.GetServicesInScopeRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_services_in_scope_response.GetServicesInScopeResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_services_in_scope

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_services_in_scope.get_services_in_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_services_in_scope_request.GetServicesInScopeRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_settings(
        self,
        attribute: "capo_auditmanager.types.setting_attribute.SettingAttribute",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.get_settings_response.GetSettingsResponse":
        """<p> Gets the settings for a specified Amazon Web Services account. </p>

        Args:
            attribute: <p> The list of setting attribute enum values. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.get_settings_request.GetSettingsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.get_settings_response.GetSettingsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_settings

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.get_settings.get_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.get_settings_request.GetSettingsRequest = {
            "attribute": attribute
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_assessment_control_insights_by_control_domain(
        self,
        control_domain_id: "capo_auditmanager.types.control_domain_id.ControlDomainId",
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_assessment_control_insights_by_control_domain_response.ListAssessmentControlInsightsByControlDomainResponse":
        """<p>Lists the latest analytics data for controls within a specific control domain and a specific active assessment.</p> <note> <p>Control insights are listed only if the control belongs to the control domain and assessment that was specified. Moreover, the control must have collected evidence on the <code>lastUpdated</code> date of <code>controlInsightsByAssessment</code>. If neither of these conditions are met, no data is listed for that control. </p> </note>

        Args:
            control_domain_id: <p>The unique identifier for the control domain. </p> <p>Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p>
            assessment_id: <p>The unique identifier for the active assessment. </p>
            next_token: <p>The pagination token that's used to fetch the next set of results. </p>
            max_results: <p>Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_assessment_control_insights_by_control_domain_request.ListAssessmentControlInsightsByControlDomainRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_assessment_control_insights_by_control_domain_response.ListAssessmentControlInsightsByControlDomainResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_control_insights_by_control_domain

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_control_insights_by_control_domain.list_assessment_control_insights_by_control_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_assessment_control_insights_by_control_domain_request.ListAssessmentControlInsightsByControlDomainRequest = {
            "control_domain_id": control_domain_id,
            "assessment_id": assessment_id,
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

    def iter_list_assessment_control_insights_by_control_domain(
        self,
        control_domain_id: "capo_auditmanager.types.control_domain_id.ControlDomainId",
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_assessment_control_insights_by_control_domain_response.ListAssessmentControlInsightsByControlDomainResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_control_insights_by_control_domain(
                control_domain_id,
                assessment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessment_frameworks(
        self,
        framework_type: "capo_auditmanager.types.framework_type.FrameworkType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_assessment_frameworks_response.ListAssessmentFrameworksResponse":
        """<p> Returns a list of the frameworks that are available in the Audit Manager framework library. </p>

        Args:
            framework_type: <p> The type of framework, such as a standard framework or a custom framework. </p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_assessment_frameworks_request.ListAssessmentFrameworksRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_assessment_frameworks_response.ListAssessmentFrameworksResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_frameworks

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_frameworks.list_assessment_frameworks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_assessment_frameworks_request.ListAssessmentFrameworksRequest = {
            "framework_type": framework_type
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

    def iter_list_assessment_frameworks(
        self,
        framework_type: "capo_auditmanager.types.framework_type.FrameworkType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_assessment_frameworks_response.ListAssessmentFrameworksResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_frameworks(
                framework_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessment_framework_share_requests(
        self,
        request_type: "capo_auditmanager.types.share_request_type.ShareRequestType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_assessment_framework_share_requests_response.ListAssessmentFrameworkShareRequestsResponse":
        """<p> Returns a list of sent or received share requests for custom frameworks in Audit Manager. </p>

        Args:
            request_type: <p> Specifies whether the share request is a sent request or a received request.</p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_assessment_framework_share_requests_request.ListAssessmentFrameworkShareRequestsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_assessment_framework_share_requests_response.ListAssessmentFrameworkShareRequestsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_framework_share_requests

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_framework_share_requests.list_assessment_framework_share_requests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_assessment_framework_share_requests_request.ListAssessmentFrameworkShareRequestsRequest = {
            "request_type": request_type
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

    def iter_list_assessment_framework_share_requests(
        self,
        request_type: "capo_auditmanager.types.share_request_type.ShareRequestType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_assessment_framework_share_requests_response.ListAssessmentFrameworkShareRequestsResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_framework_share_requests(
                request_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessment_reports(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_assessment_reports_response.ListAssessmentReportsResponse":
        """<p> Returns a list of assessment reports created in Audit Manager. </p>

        Args:
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_assessment_reports_request.ListAssessmentReportsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_assessment_reports_response.ListAssessmentReportsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_reports

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessment_reports.list_assessment_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_assessment_reports_request.ListAssessmentReportsRequest = {}
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

    def iter_list_assessment_reports(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_assessment_reports_response.ListAssessmentReportsResponse]":
        _token = next_token
        while True:
            _response = self.list_assessment_reports(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assessments(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        status: Optional[
            "capo_auditmanager.types.assessment_status.AssessmentStatus"
        ] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_assessments_response.ListAssessmentsResponse":
        """<p> Returns a list of current and past assessments from Audit Manager. </p>

        Args:
            status: <p> The current status of the assessment.</p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_assessments_request.ListAssessmentsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_assessments_response.ListAssessmentsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessments

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_assessments.list_assessments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_assessments_request.ListAssessmentsRequest = {}
        if status is not None:
            input_["status"] = status
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

    def iter_list_assessments(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        status: Optional[
            "capo_auditmanager.types.assessment_status.AssessmentStatus"
        ] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_assessments_response.ListAssessmentsResponse]":
        _token = next_token
        while True:
            _response = self.list_assessments(
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_control_domain_insights(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_control_domain_insights_response.ListControlDomainInsightsResponse":
        """<p>Lists the latest analytics data for control domains across all of your active assessments. </p> <p>Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p> <note> <p>A control domain is listed only if at least one of the controls within that domain collected evidence on the <code>lastUpdated</code> date of <code>controlDomainInsights</code>. If this condition isn’t met, no data is listed for that control domain.</p> </note>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results. </p>
            max_results: <p>Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_control_domain_insights_request.ListControlDomainInsightsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_control_domain_insights_response.ListControlDomainInsightsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_control_domain_insights

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_control_domain_insights.list_control_domain_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_control_domain_insights_request.ListControlDomainInsightsRequest = {}
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

    def iter_list_control_domain_insights(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_control_domain_insights_response.ListControlDomainInsightsResponse]":
        _token = next_token
        while True:
            _response = self.list_control_domain_insights(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_control_domain_insights_by_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_control_domain_insights_by_assessment_response.ListControlDomainInsightsByAssessmentResponse":
        """<p>Lists analytics data for control domains within a specified active assessment.</p> <p>Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p> <note> <p>A control domain is listed only if at least one of the controls within that domain collected evidence on the <code>lastUpdated</code> date of <code>controlDomainInsights</code>. If this condition isn’t met, no data is listed for that domain.</p> </note>

        Args:
            assessment_id: <p>The unique identifier for the active assessment. </p>
            next_token: <p>The pagination token that's used to fetch the next set of results. </p>
            max_results: <p>Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_control_domain_insights_by_assessment_request.ListControlDomainInsightsByAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_control_domain_insights_by_assessment_response.ListControlDomainInsightsByAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_control_domain_insights_by_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_control_domain_insights_by_assessment.list_control_domain_insights_by_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_control_domain_insights_by_assessment_request.ListControlDomainInsightsByAssessmentRequest = {
            "assessment_id": assessment_id
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

    def iter_list_control_domain_insights_by_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_control_domain_insights_by_assessment_response.ListControlDomainInsightsByAssessmentResponse]":
        _token = next_token
        while True:
            _response = self.list_control_domain_insights_by_assessment(
                assessment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_control_insights_by_control_domain(
        self,
        control_domain_id: "capo_auditmanager.types.control_domain_id.ControlDomainId",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_control_insights_by_control_domain_response.ListControlInsightsByControlDomainResponse":
        """<p>Lists the latest analytics data for controls within a specific control domain across all active assessments.</p> <note> <p>Control insights are listed only if the control belongs to the control domain that was specified and the control collected evidence on the <code>lastUpdated</code> date of <code>controlInsightsMetadata</code>. If neither of these conditions are met, no data is listed for that control. </p> </note>

        Args:
            control_domain_id: <p>The unique identifier for the control domain. </p> <p>Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a> in the Amazon Web Services Control Catalog API Reference.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results. </p>
            max_results: <p>Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_control_insights_by_control_domain_request.ListControlInsightsByControlDomainRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_control_insights_by_control_domain_response.ListControlInsightsByControlDomainResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_control_insights_by_control_domain

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_control_insights_by_control_domain.list_control_insights_by_control_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_control_insights_by_control_domain_request.ListControlInsightsByControlDomainRequest = {
            "control_domain_id": control_domain_id
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

    def iter_list_control_insights_by_control_domain(
        self,
        control_domain_id: "capo_auditmanager.types.control_domain_id.ControlDomainId",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_control_insights_by_control_domain_response.ListControlInsightsByControlDomainResponse]":
        _token = next_token
        while True:
            _response = self.list_control_insights_by_control_domain(
                control_domain_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_controls(
        self,
        control_type: "capo_auditmanager.types.control_type.ControlType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
        control_catalog_id: Optional[
            "capo_auditmanager.types.control_catalog_id.ControlCatalogId"
        ] = None,
    ) -> "capo_auditmanager.types.list_controls_response.ListControlsResponse":
        """<p> Returns a list of controls from Audit Manager. </p>

        Args:
            control_type: <p>A filter that narrows the list of controls to a specific type. </p>
            next_token: <p>The pagination token that's used to fetch the next set of results. </p>
            max_results: <p>The maximum number of results on a page or for an API request call. </p>
            control_catalog_id: <p>A filter that narrows the list of controls to a specific resource from the Amazon Web Services Control Catalog. </p> <p>To use this parameter, specify the ARN of the Control Catalog resource. You can specify either a control domain, a control objective, or a common control. For information about how to find the ARNs for these resources, see <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html"> <code>ListDomains</code> </a>, <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListObjectives.html"> <code>ListObjectives</code> </a>, and <a href="https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html"> <code>ListCommonControls</code> </a>.</p> <note> <p>You can only filter by one Control Catalog resource at a time. Specifying multiple resource ARNs isn’t currently supported. If you want to filter by more than one ARN, we recommend that you run the <code>ListControls</code> operation separately for each ARN. </p> </note> <p>Alternatively, specify <code>UNCATEGORIZED</code> to list controls that aren't mapped to a Control Catalog resource. For example, this operation might return a list of custom controls that don't belong to any control domain or control objective.</p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_controls_request.ListControlsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_controls_response.ListControlsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_controls

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_controls.list_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_controls_request.ListControlsRequest = {
            "control_type": control_type
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if control_catalog_id is not None:
            input_["control_catalog_id"] = control_catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_controls(
        self,
        control_type: "capo_auditmanager.types.control_type.ControlType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
        control_catalog_id: Optional[
            "capo_auditmanager.types.control_catalog_id.ControlCatalogId"
        ] = None,
    ) -> (
        "Iterator[capo_auditmanager.types.list_controls_response.ListControlsResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_controls(
                control_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                control_catalog_id=control_catalog_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_keywords_for_data_source(
        self,
        source: "capo_auditmanager.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "capo_auditmanager.types.list_keywords_for_data_source_response.ListKeywordsForDataSourceResponse":
        """<p>Returns a list of keywords that are pre-mapped to the specified control data source.</p>

        Args:
            source: <p>The control mapping data source that the keywords apply to. </p>
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_keywords_for_data_source_request.ListKeywordsForDataSourceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_keywords_for_data_source_response.ListKeywordsForDataSourceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_keywords_for_data_source

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_keywords_for_data_source.list_keywords_for_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_keywords_for_data_source_request.ListKeywordsForDataSourceRequest = {
            "source": source
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

    def iter_list_keywords_for_data_source(
        self,
        source: "capo_auditmanager.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_keywords_for_data_source_response.ListKeywordsForDataSourceResponse]":
        _token = next_token
        while True:
            _response = self.list_keywords_for_data_source(
                source,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_notifications(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_auditmanager.types.list_notifications_response.ListNotificationsResponse"
    ):
        """<p> Returns a list of all Audit Manager notifications. </p>

        Args:
            next_token: <p> The pagination token that's used to fetch the next set of results. </p>
            max_results: <p> Represents the maximum number of results on a page or for an API request call. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_notifications_request.ListNotificationsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_notifications_response.ListNotificationsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_notifications

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_notifications.list_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_notifications_request.ListNotificationsRequest = {}
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

    def iter_list_notifications(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        next_token: Optional["capo_auditmanager.types.token.Token"] = None,
        max_results: Optional["capo_auditmanager.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_auditmanager.types.list_notifications_response.ListNotificationsResponse]":
        _token = next_token
        while True:
            _response = self.list_notifications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_auditmanager.types.audit_manager_arn.AuditManagerArn",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Returns a list of tags for the specified resource in Audit Manager. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>

        Raises:
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_tags_for_resource

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_account(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        kms_key: Optional["capo_auditmanager.types.kms_key.KmsKey"] = None,
        delegated_admin_account: Optional[
            "capo_auditmanager.types.account_id.AccountId"
        ] = None,
    ) -> "capo_auditmanager.types.register_account_response.RegisterAccountResponse":
        """<p> Enables Audit Manager for the specified Amazon Web Services account. </p>

        Args:
            kms_key: <p> The KMS key details. </p>
            delegated_admin_account: <p> The delegated administrator account for Audit Manager. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.register_account_request.RegisterAccountRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.register_account_response.RegisterAccountResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.register_account

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.register_account.register_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.register_account_request.RegisterAccountRequest = {}
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if delegated_admin_account is not None:
            input_["delegated_admin_account"] = delegated_admin_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_organization_admin_account(
        self,
        admin_account_id: "capo_auditmanager.types.account_id.AccountId",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.register_organization_admin_account_response.RegisterOrganizationAdminAccountResponse":
        """<p> Enables an Amazon Web Services account within the organization as the delegated administrator for Audit Manager. </p>

        Args:
            admin_account_id: <p> The identifier for the delegated administrator account. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.register_organization_admin_account_request.RegisterOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.register_organization_admin_account_response.RegisterOrganizationAdminAccountResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.register_organization_admin_account

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.register_organization_admin_account.register_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.register_organization_admin_account_request.RegisterOrganizationAdminAccountRequest = {
            "admin_account_id": admin_account_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_assessment_framework_share(
        self,
        framework_id: "capo_auditmanager.types.uuid.UUID",
        destination_account: "capo_auditmanager.types.account_id.AccountId",
        destination_region: "capo_auditmanager.types.region.Region",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        comment: Optional[
            "capo_auditmanager.types.share_request_comment.ShareRequestComment"
        ] = None,
    ) -> "capo_auditmanager.types.start_assessment_framework_share_response.StartAssessmentFrameworkShareResponse":
        """<p> Creates a share request for a custom framework in Audit Manager. </p> <p>The share request specifies a recipient and notifies them that a custom framework is available. Recipients have 120 days to accept or decline the request. If no action is taken, the share request expires.</p> <p>When you create a share request, Audit Manager stores a snapshot of your custom framework in the US East (N. Virginia) Amazon Web Services Region. Audit Manager also stores a backup of the same snapshot in the US West (Oregon) Amazon Web Services Region.</p> <p>Audit Manager deletes the snapshot and the backup snapshot when one of the following events occurs:</p> <ul> <li> <p>The sender revokes the share request.</p> </li> <li> <p>The recipient declines the share request.</p> </li> <li> <p>The recipient encounters an error and doesn't successfully accept the share request.</p> </li> <li> <p>The share request expires before the recipient responds to the request.</p> </li> </ul> <p>When a sender <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/framework-sharing.html#framework-sharing-resend">resends a share request</a>, the snapshot is replaced with an updated version that corresponds with the latest version of the custom framework. </p> <p>When a recipient accepts a share request, the snapshot is replicated into their Amazon Web Services account under the Amazon Web Services Region that was specified in the share request. </p> <important> <p>When you invoke the <code>StartAssessmentFrameworkShare</code> API, you are about to share a custom framework with another Amazon Web Services account. You may not share a custom framework that is derived from a standard framework if the standard framework is designated as not eligible for sharing by Amazon Web Services, unless you have obtained permission to do so from the owner of the standard framework. To learn more about which standard frameworks are eligible for sharing, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/share-custom-framework-concepts-and-terminology.html#eligibility">Framework sharing eligibility</a> in the <i>Audit Manager User Guide</i>.</p> </important>

        Args:
            framework_id: <p> The unique identifier for the custom framework to be shared. </p>
            destination_account: <p> The Amazon Web Services account of the recipient. </p>
            destination_region: <p> The Amazon Web Services Region of the recipient. </p>
            comment: <p> An optional comment from the sender about the share request. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.start_assessment_framework_share_request.StartAssessmentFrameworkShareRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.start_assessment_framework_share_response.StartAssessmentFrameworkShareResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.start_assessment_framework_share

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.start_assessment_framework_share.start_assessment_framework_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.start_assessment_framework_share_request.StartAssessmentFrameworkShareRequest = {
            "framework_id": framework_id,
            "destination_account": destination_account,
            "destination_region": destination_region,
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

    def tag_resource(
        self,
        resource_arn: "capo_auditmanager.types.audit_manager_arn.AuditManagerArn",
        tags: "capo_auditmanager.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.tag_resource_response.TagResourceResponse":
        """<p> Tags the specified resource in Audit Manager. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource. </p>
            tags: <p> The tags that are associated with the resource. </p>

        Raises:
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.tag_resource

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_auditmanager.types.audit_manager_arn.AuditManagerArn",
        tag_keys: "capo_auditmanager.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes a tag from a resource in Audit Manager. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the specified resource. </p>
            tag_keys: <p> The name or key of the tag. </p>

        Raises:
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.untag_resource

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.untag_resource_request.UntagResourceRequest = {
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

    def update_assessment(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        scope: "capo_auditmanager.types.scope.Scope",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        assessment_name: Optional[
            "capo_auditmanager.types.assessment_name.AssessmentName"
        ] = None,
        assessment_description: Optional[
            "capo_auditmanager.types.assessment_description.AssessmentDescription"
        ] = None,
        assessment_reports_destination: Optional[
            "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
        ] = None,
        roles: Optional["capo_auditmanager.types.roles.Roles"] = None,
    ) -> "capo_auditmanager.types.update_assessment_response.UpdateAssessmentResponse":
        """<p> Edits an Audit Manager assessment. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            assessment_name: <p> The name of the assessment to be updated. </p>
            assessment_description: <p> The description of the assessment. </p>
            scope: <p> The scope of the assessment. </p>
            assessment_reports_destination: <p> The assessment report storage destination for the assessment that's being updated. </p>
            roles: <p> The list of roles for the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_assessment_request.UpdateAssessmentRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_assessment_response.UpdateAssessmentResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment.update_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_assessment_request.UpdateAssessmentRequest = {
            "assessment_id": assessment_id,
            "scope": scope,
        }
        if assessment_name is not None:
            input_["assessment_name"] = assessment_name
        if assessment_description is not None:
            input_["assessment_description"] = assessment_description
        if assessment_reports_destination is not None:
            input_["assessment_reports_destination"] = assessment_reports_destination
        if roles is not None:
            input_["roles"] = roles

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_assessment_control(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.control_set_id.ControlSetId",
        control_id: "capo_auditmanager.types.uuid.UUID",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        control_status: Optional[
            "capo_auditmanager.types.control_status.ControlStatus"
        ] = None,
        comment_body: Optional[
            "capo_auditmanager.types.control_comment_body.ControlCommentBody"
        ] = None,
    ) -> "capo_auditmanager.types.update_assessment_control_response.UpdateAssessmentControlResponse":
        """<p> Updates a control within an assessment in Audit Manager. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            control_set_id: <p> The unique identifier for the control set. </p>
            control_id: <p> The unique identifier for the control. </p>
            control_status: <p> The status of the control. </p>
            comment_body: <p> The comment body text for the control. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_assessment_control_request.UpdateAssessmentControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_assessment_control_response.UpdateAssessmentControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_control.update_assessment_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_assessment_control_request.UpdateAssessmentControlRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "control_id": control_id,
        }
        if control_status is not None:
            input_["control_status"] = control_status
        if comment_body is not None:
            input_["comment_body"] = comment_body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_assessment_control_set_status(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        control_set_id: "capo_auditmanager.types.string.String",
        status: "capo_auditmanager.types.control_set_status.ControlSetStatus",
        comment: "capo_auditmanager.types.delegation_comment.DelegationComment",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.update_assessment_control_set_status_response.UpdateAssessmentControlSetStatusResponse":
        """<p> Updates the status of a control set in an Audit Manager assessment. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            control_set_id: <p> The unique identifier for the control set. </p>
            status: <p> The status of the control set that's being updated. </p>
            comment: <p> The comment that's related to the status update. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_assessment_control_set_status_request.UpdateAssessmentControlSetStatusRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_assessment_control_set_status_response.UpdateAssessmentControlSetStatusResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_control_set_status

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_control_set_status.update_assessment_control_set_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_assessment_control_set_status_request.UpdateAssessmentControlSetStatusRequest = {
            "assessment_id": assessment_id,
            "control_set_id": control_set_id,
            "status": status,
            "comment": comment,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_assessment_framework(
        self,
        framework_id: "capo_auditmanager.types.uuid.UUID",
        name: "capo_auditmanager.types.framework_name.FrameworkName",
        control_sets: "capo_auditmanager.types.update_assessment_framework_control_sets.UpdateAssessmentFrameworkControlSets",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        description: Optional[
            "capo_auditmanager.types.framework_description.FrameworkDescription"
        ] = None,
        compliance_type: Optional[
            "capo_auditmanager.types.compliance_type.ComplianceType"
        ] = None,
    ) -> "capo_auditmanager.types.update_assessment_framework_response.UpdateAssessmentFrameworkResponse":
        """<p> Updates a custom framework in Audit Manager. </p>

        Args:
            framework_id: <p> The unique identifier for the framework. </p>
            name: <p> The name of the framework to be updated. </p>
            description: <p> The description of the updated framework. </p>
            compliance_type: <p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>
            control_sets: <p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_assessment_framework_request.UpdateAssessmentFrameworkRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_assessment_framework_response.UpdateAssessmentFrameworkResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_framework

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_framework.update_assessment_framework(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_assessment_framework_request.UpdateAssessmentFrameworkRequest = {
            "framework_id": framework_id,
            "name": name,
            "control_sets": control_sets,
        }
        if description is not None:
            input_["description"] = description
        if compliance_type is not None:
            input_["compliance_type"] = compliance_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_assessment_framework_share(
        self,
        request_id: "capo_auditmanager.types.uuid.UUID",
        request_type: "capo_auditmanager.types.share_request_type.ShareRequestType",
        action: "capo_auditmanager.types.share_request_action.ShareRequestAction",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.update_assessment_framework_share_response.UpdateAssessmentFrameworkShareResponse":
        """<p> Updates a share request for a custom framework in Audit Manager. </p>

        Args:
            request_id: <p> The unique identifier for the share request. </p>
            request_type: <p>Specifies whether the share request is a sent request or a received request.</p>
            action: <p>Specifies the update action for the share request.</p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_assessment_framework_share_request.UpdateAssessmentFrameworkShareRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_assessment_framework_share_response.UpdateAssessmentFrameworkShareResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_framework_share

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_framework_share.update_assessment_framework_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_assessment_framework_share_request.UpdateAssessmentFrameworkShareRequest = {
            "request_id": request_id,
            "request_type": request_type,
            "action": action,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_assessment_status(
        self,
        assessment_id: "capo_auditmanager.types.uuid.UUID",
        status: "capo_auditmanager.types.assessment_status.AssessmentStatus",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.update_assessment_status_response.UpdateAssessmentStatusResponse":
        """<p> Updates the status of an assessment in Audit Manager. </p>

        Args:
            assessment_id: <p> The unique identifier for the assessment. </p>
            status: <p> The current status of the assessment. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've reached your account quota for this resource type. To perform the requested action, delete some existing resources or <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">request a quota increase</a> from the Service Quotas console. For a list of Audit Manager service quotas, see <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html">Quotas and restrictions for Audit Manager</a>.</p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_assessment_status_request.UpdateAssessmentStatusRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_assessment_status_response.UpdateAssessmentStatusResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_status

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_assessment_status.update_assessment_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_assessment_status_request.UpdateAssessmentStatusRequest = {
            "assessment_id": assessment_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_control(
        self,
        control_id: "capo_auditmanager.types.uuid.UUID",
        name: "capo_auditmanager.types.control_name.ControlName",
        control_mapping_sources: "capo_auditmanager.types.control_mapping_sources.ControlMappingSources",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        description: Optional[
            "capo_auditmanager.types.control_description.ControlDescription"
        ] = None,
        testing_information: Optional[
            "capo_auditmanager.types.testing_information.TestingInformation"
        ] = None,
        action_plan_title: Optional[
            "capo_auditmanager.types.action_plan_title.ActionPlanTitle"
        ] = None,
        action_plan_instructions: Optional[
            "capo_auditmanager.types.action_plan_instructions.ActionPlanInstructions"
        ] = None,
    ) -> "capo_auditmanager.types.update_control_response.UpdateControlResponse":
        """<p> Updates a custom control in Audit Manager. </p>

        Args:
            control_id: <p> The identifier for the control. </p>
            name: <p> The name of the updated control. </p>
            description: <p> The optional description of the control. </p>
            testing_information: <p> The steps that you should follow to determine if the control is met. </p>
            action_plan_title: <p> The title of the action plan for remediating the control. </p>
            action_plan_instructions: <p> The recommended actions to carry out if the control isn't fulfilled. </p>
            control_mapping_sources: <p> The data mapping sources for the control. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_control_request.UpdateControlRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_control_response.UpdateControlResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_control

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_control.update_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_control_request.UpdateControlRequest = {
            "control_id": control_id,
            "name": name,
            "control_mapping_sources": control_mapping_sources,
        }
        if description is not None:
            input_["description"] = description
        if testing_information is not None:
            input_["testing_information"] = testing_information
        if action_plan_title is not None:
            input_["action_plan_title"] = action_plan_title
        if action_plan_instructions is not None:
            input_["action_plan_instructions"] = action_plan_instructions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_settings(
        self,
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
        sns_topic: Optional["capo_auditmanager.types.sns_arn.SnsArn"] = None,
        default_assessment_reports_destination: Optional[
            "capo_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
        ] = None,
        default_process_owners: Optional["capo_auditmanager.types.roles.Roles"] = None,
        kms_key: Optional["capo_auditmanager.types.kms_key.KmsKey"] = None,
        evidence_finder_enabled: Optional[
            "capo_auditmanager.types.boolean.Boolean"
        ] = None,
        deregistration_policy: Optional[
            "capo_auditmanager.types.deregistration_policy.DeregistrationPolicy"
        ] = None,
        default_export_destination: Optional[
            "capo_auditmanager.types.default_export_destination.DefaultExportDestination"
        ] = None,
    ) -> "capo_auditmanager.types.update_settings_response.UpdateSettingsResponse":
        """<p> Updates Audit Manager settings for the current account. </p>

        Args:
            sns_topic: <p> The Amazon Simple Notification Service (Amazon SNS) topic that Audit Manager sends notifications to. </p>
            default_assessment_reports_destination: <p> The default S3 destination bucket for storing assessment reports. </p>
            default_process_owners: <p> A list of the default audit owners. </p>
            kms_key: <p> The KMS key details. </p>
            evidence_finder_enabled: <p>Specifies whether the evidence finder feature is enabled. Change this attribute to enable or disable evidence finder.</p> <important> <p>When you use this attribute to disable evidence finder, Audit Manager deletes the event data store that’s used to query your evidence data. As a result, you can’t re-enable evidence finder and use the feature again. Your only alternative is to <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html">deregister</a> and then <a href="https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html">re-register</a> Audit Manager. </p> </important>
            deregistration_policy: <p>The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.</p>
            default_export_destination: <p> The default S3 destination bucket for storing evidence finder exports. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.update_settings_request.UpdateSettingsRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.update_settings_response.UpdateSettingsResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_settings

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.update_settings.update_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.update_settings_request.UpdateSettingsRequest = {}
        if sns_topic is not None:
            input_["sns_topic"] = sns_topic
        if default_assessment_reports_destination is not None:
            input_["default_assessment_reports_destination"] = (
                default_assessment_reports_destination
            )
        if default_process_owners is not None:
            input_["default_process_owners"] = default_process_owners
        if kms_key is not None:
            input_["kms_key"] = kms_key
        if evidence_finder_enabled is not None:
            input_["evidence_finder_enabled"] = evidence_finder_enabled
        if deregistration_policy is not None:
            input_["deregistration_policy"] = deregistration_policy
        if default_export_destination is not None:
            input_["default_export_destination"] = default_export_destination

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_assessment_report_integrity(
        self,
        s3_relative_path: "capo_auditmanager.types.s3_url.S3Url",
        *,
        config_overrides: Optional[AuditManagerClientConfig] = None,
    ) -> "capo_auditmanager.types.validate_assessment_report_integrity_response.ValidateAssessmentReportIntegrityResponse":
        """<p> Validates the integrity of an assessment report in Audit Manager. </p>

        Args:
            s3_relative_path: <p> The relative path of the Amazon S3 bucket that the assessment report is stored in. </p>

        Raises:
            capo_auditmanager.errors.access_denied_exception.AccessDeniedException: <p> Your account isn't registered with Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again. </p>
            capo_auditmanager.errors.internal_server_exception.InternalServerException: <p> An internal service error occurred during the processing of your request. Try again later. </p>
            capo_auditmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p> The resource that's specified in the request can't be found. </p>
            capo_auditmanager.errors.validation_exception.ValidationException: <p> The request has invalid or missing parameters. </p>
            capo_auditmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_auditmanager.types.validate_assessment_report_integrity_request.ValidateAssessmentReportIntegrityRequest]",
        ) -> OperationResponse[
            "capo_auditmanager.types.validate_assessment_report_integrity_response.ValidateAssessmentReportIntegrityResponse"
        ]:
            import capo_auditmanager._operations.bedrock_assessment_manager_lambda.validate_assessment_report_integrity

            output, http_response = (
                capo_auditmanager._operations.bedrock_assessment_manager_lambda.validate_assessment_report_integrity.validate_assessment_report_integrity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_auditmanager.types.validate_assessment_report_integrity_request.ValidateAssessmentReportIntegrityRequest = {
            "s3_relative_path": s3_relative_path
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
