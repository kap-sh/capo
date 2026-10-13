from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

from capo_partnercentral_account._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_account.types.alliance_lead_contact
    import capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request
    import capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response
    import capo_partnercentral_account.types.cancel_profile_update_task_request
    import capo_partnercentral_account.types.cancel_profile_update_task_response
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.create_partner_request
    import capo_partnercentral_account.types.create_partner_response
    import capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request
    import capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response
    import capo_partnercentral_account.types.domain_name
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.email_verification_code
    import capo_partnercentral_account.types.get_alliance_lead_contact_request
    import capo_partnercentral_account.types.get_alliance_lead_contact_response
    import capo_partnercentral_account.types.get_partner_request
    import capo_partnercentral_account.types.get_partner_response
    import capo_partnercentral_account.types.get_profile_update_task_request
    import capo_partnercentral_account.types.get_profile_update_task_response
    import capo_partnercentral_account.types.get_profile_visibility_request
    import capo_partnercentral_account.types.get_profile_visibility_response
    import capo_partnercentral_account.types.get_qualifications_association_details_request
    import capo_partnercentral_account.types.get_qualifications_association_details_response
    import capo_partnercentral_account.types.get_qualifications_association_task_request
    import capo_partnercentral_account.types.get_qualifications_association_task_response
    import capo_partnercentral_account.types.get_qualifications_disassociation_task_request
    import capo_partnercentral_account.types.get_qualifications_disassociation_task_response
    import capo_partnercentral_account.types.list_partners_request
    import capo_partnercentral_account.types.list_partners_response
    import capo_partnercentral_account.types.next_token
    import capo_partnercentral_account.types.partner_identifier
    import capo_partnercentral_account.types.partner_summary
    import capo_partnercentral_account.types.primary_solution_type
    import capo_partnercentral_account.types.profile_task_id
    import capo_partnercentral_account.types.profile_visibility
    import capo_partnercentral_account.types.put_alliance_lead_contact_request
    import capo_partnercentral_account.types.put_alliance_lead_contact_response
    import capo_partnercentral_account.types.put_profile_visibility_request
    import capo_partnercentral_account.types.put_profile_visibility_response
    import capo_partnercentral_account.types.qualifications_association_partner
    import capo_partnercentral_account.types.sensitive_unicode_string
    import capo_partnercentral_account.types.start_profile_update_task_request
    import capo_partnercentral_account.types.start_profile_update_task_response
    import capo_partnercentral_account.types.start_qualifications_association_task_request
    import capo_partnercentral_account.types.start_qualifications_association_task_response
    import capo_partnercentral_account.types.start_qualifications_disassociation_task_request
    import capo_partnercentral_account.types.start_qualifications_disassociation_task_response
    import capo_partnercentral_account.types.tag_list
    import capo_partnercentral_account.types.task_details
    from capo_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from capo_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class Partner:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        legal_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        primary_solution_type: "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
        alliance_lead_contact: "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_account.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse":
        """<p>Creates a new partner account in the AWS Partner Network with the specified details and configuration.</p>

        Args:
            catalog: <p>The catalog identifier where the partner account will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            legal_name: <p>The legal name of the organization becoming a partner.</p>
            primary_solution_type: <p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>
            alliance_lead_contact: <p>The primary contact person for alliance and partnership matters.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>
            tags: <p>A list of tags to associate with the partner account for organization and billing purposes.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.create_partner

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.create_partner.create_partner(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_partner_request

            return capo_partnercentral_account.types.create_partner_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_partner_response

            return capo_partnercentral_account.types.create_partner_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePartner",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest = {
            "catalog": catalog,
            "legal_name": legal_name,
            "primary_solution_type": primary_solution_type,
            "alliance_lead_contact": alliance_lead_contact,
            "email_verification_code": email_verification_code,
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

    def read(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse":
        """<p>Retrieves detailed information about a specific partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_partner_request.GetPartnerRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_partner

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_partner.get_partner(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.get_partner_response

            return (
                capo_partnercentral_account.types.get_partner_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPartner", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.get_partner_request.GetPartnerRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse"
    ):
        """<p>Lists partner accounts in the catalog, providing a summary view of all partners.</p>

        Args:
            catalog: <p>The catalog identifier to list partners from.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.list_partners_request.ListPartnersRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_partners

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.list_partners.list_partners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.list_partners_response

            return capo_partnercentral_account.types.list_partners_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPartners", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.list_partners_request.ListPartnersRequest = {
            "catalog": catalog
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

    def associate_aws_training_certification_email_domain(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        email: "capo_partnercentral_account.types.email.Email",
        email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Associates an email domain with AWS training and certification for the partner account, enabling automatic verification of employee certifications.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            email: <p>The email address used to verify domain ownership for AWS training and certification association.</p>
            email_verification_code: <p>The verification code sent to the email address to confirm domain ownership.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain.associate_aws_training_certification_email_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request

            return capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AssociateAwsTrainingCertificationEmailDomain",
                redact_input=_redact_input,
            ),
        )
        input_: capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "email": email,
            "email_verification_code": email_verification_code,
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

    def cancel_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_id: "capo_partnercentral_account.types.profile_task_id.ProfileTaskId",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse":
        """<p>Cancels an in-progress profile update task, stopping any pending changes to the partner profile.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_id: <p>The unique identifier of the profile update task to cancel.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_profile_update_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.cancel_profile_update_task.cancel_profile_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelProfileUpdateTask")
        )
        input_: capo_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "task_id": task_id,
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

    def disassociate_aws_training_certification_email_domain(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        domain_name: "capo_partnercentral_account.types.domain_name.DomainName",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Removes the association between an email domain and AWS training and certification for the partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            domain_name: <p>The domain name to disassociate from AWS training and certification.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain.disassociate_aws_training_certification_email_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisassociateAwsTrainingCertificationEmailDomain"),
        )
        input_: capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "domain_name": domain_name,
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

    def get_alliance_lead_contact(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse":
        """<p>Retrieves the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact.get_alliance_lead_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.get_alliance_lead_contact_response

            return capo_partnercentral_account.types.get_alliance_lead_contact_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAllianceLeadContact", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse":
        """<p>Retrieves information about a specific profile update task.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_profile_update_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_profile_update_task.get_profile_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetProfileUpdateTask")
        )
        input_: capo_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_profile_visibility(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse":
        """<p>Retrieves the visibility settings for a partner profile, determining who can see the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_profile_visibility

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_profile_visibility.get_profile_visibility(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetProfileVisibility")
        )
        input_: capo_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_qualifications_association_details(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_association_details_response.GetQualificationsAssociationDetailsResponse":
        """<p>Returns your current qualifications association status, the primary partner, and the full list of partners associated under the primary partner.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_qualifications_association_details_request.GetQualificationsAssociationDetailsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_qualifications_association_details_response.GetQualificationsAssociationDetailsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_details

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_details.get_qualifications_association_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQualificationsAssociationDetails")
        )
        input_: capo_partnercentral_account.types.get_qualifications_association_details_request.GetQualificationsAssociationDetailsRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_qualifications_association_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_association_task_response.GetQualificationsAssociationTaskResponse":
        """<p>Retrieves the status and details of the most recent qualifications association task for your partner account. Use this operation to poll the progress of an association task initiated by <code>StartQualificationsAssociationTask</code>.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications association task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_qualifications_association_task_request.GetQualificationsAssociationTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_qualifications_association_task_response.GetQualificationsAssociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_task.get_qualifications_association_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQualificationsAssociationTask")
        )
        input_: capo_partnercentral_account.types.get_qualifications_association_task_request.GetQualificationsAssociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_qualifications_disassociation_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_disassociation_task_response.GetQualificationsDisassociationTaskResponse":
        """<p>Retrieves the status and details of the most recent qualifications disassociation task for your partner account. Use this operation to poll the progress of a disassociation task initiated by <code>StartQualificationsDisassociationTask</code>.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications disassociation task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_qualifications_disassociation_task_request.GetQualificationsDisassociationTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_qualifications_disassociation_task_response.GetQualificationsDisassociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_disassociation_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_qualifications_disassociation_task.get_qualifications_disassociation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQualificationsDisassociationTask")
        )
        input_: capo_partnercentral_account.types.get_qualifications_disassociation_task_request.GetQualificationsDisassociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_alliance_lead_contact(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        alliance_lead_contact: "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        email_verification_code: Optional[
            "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode"
        ] = None,
    ) -> "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse":
        """<p>Creates or updates the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            alliance_lead_contact: <p>The alliance lead contact information to set for the partner account.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm the update.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact.put_alliance_lead_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.put_alliance_lead_contact_request

            return capo_partnercentral_account.types.put_alliance_lead_contact_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.put_alliance_lead_contact_response

            return capo_partnercentral_account.types.put_alliance_lead_contact_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "PutAllianceLeadContact",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "alliance_lead_contact": alliance_lead_contact,
        }
        if email_verification_code is not None:
            input_["email_verification_code"] = email_verification_code

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_profile_visibility(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        visibility: "capo_partnercentral_account.types.profile_visibility.ProfileVisibility",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse":
        """<p>Sets the visibility level for a partner profile, controlling who can view the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            visibility: <p>The visibility setting to apply to the partner profile.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.put_profile_visibility

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.put_profile_visibility.put_profile_visibility(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutProfileVisibility")
        )
        input_: capo_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "visibility": visibility,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_details: "capo_partnercentral_account.types.task_details.TaskDetails",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse":
        """<p>Initiates a profile update task to modify partner profile information asynchronously.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_details: <p>The details of the profile updates to be performed.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_profile_update_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.start_profile_update_task.start_profile_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartProfileUpdateTask")
        )
        input_: capo_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "task_details": task_details,
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

    def start_qualifications_association_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        primary_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_qualifications_association_task_response.StartQualificationsAssociationTaskResponse":
        """<p>Initiates an asynchronous task to associate your partner qualifications with a primary account. You must be a subsidiary of the primary account with an active subsidiary connection. Use <code>GetQualificationsAssociationTask</code> to monitor task progress.</p>

        Args:
            catalog: <p>The catalog in which to perform the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            primary_partner: <p>The primary (acquiring) partner's profile and account identifier to associate qualifications with. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. You cannot specify yourself as the primary partner.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.start_qualifications_association_task_request.StartQualificationsAssociationTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.start_qualifications_association_task_response.StartQualificationsAssociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_qualifications_association_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.start_qualifications_association_task.start_qualifications_association_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartQualificationsAssociationTask")
        )
        input_: capo_partnercentral_account.types.start_qualifications_association_task_request.StartQualificationsAssociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "primary_partner": primary_partner,
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

    def start_qualifications_disassociation_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        associated_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_qualifications_disassociation_task_response.StartQualificationsDisassociationTaskResponse":
        """<p>Initiates an asynchronous task to disassociate your partner qualifications from a primary account. You must currently be associated and cannot disassociate if you are the primary partner. Use <code>GetQualificationsDisassociationTask</code> to monitor task progress.</p>

        Args:
            catalog: <p>The catalog in which to perform the qualifications disassociation. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            associated_partner: <p>The primary partner's profile and account identifier that you are currently associated with and will disassociate from. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. The specified partner must match your current primary association.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.start_qualifications_disassociation_task_request.StartQualificationsDisassociationTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.start_qualifications_disassociation_task_response.StartQualificationsDisassociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_qualifications_disassociation_task

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.start_qualifications_disassociation_task.start_qualifications_disassociation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartQualificationsDisassociationTask")
        )
        input_: capo_partnercentral_account.types.start_qualifications_disassociation_task_request.StartQualificationsDisassociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "associated_partner": associated_partner,
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


class AsyncPartner:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        legal_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        primary_solution_type: "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType",
        alliance_lead_contact: "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_account.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse":
        """<p>Creates a new partner account in the AWS Partner Network with the specified details and configuration.</p>

        Args:
            catalog: <p>The catalog identifier where the partner account will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            legal_name: <p>The legal name of the organization becoming a partner.</p>
            primary_solution_type: <p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>
            alliance_lead_contact: <p>The primary contact person for alliance and partnership matters.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>
            tags: <p>A list of tags to associate with the partner account for organization and billing purposes.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.create_partner

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.create_partner.async_create_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_partner_request

            return capo_partnercentral_account.types.create_partner_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_partnercentral_account.types.create_partner_response.CreatePartnerResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_partner_response

            return capo_partnercentral_account.types.create_partner_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePartner",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_partnercentral_account.types.create_partner_request.CreatePartnerRequest = {
            "catalog": catalog,
            "legal_name": legal_name,
            "primary_solution_type": primary_solution_type,
            "alliance_lead_contact": alliance_lead_contact,
            "email_verification_code": email_verification_code,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse":
        """<p>Retrieves detailed information about a specific partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_partner_request.GetPartnerRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_partner

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_partner.async_get_partner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.get_partner_response.GetPartnerResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.get_partner_response

            return (
                capo_partnercentral_account.types.get_partner_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPartner", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.get_partner_request.GetPartnerRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        next_token: Optional[
            "capo_partnercentral_account.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse"
    ):
        """<p>Lists partner accounts in the catalog, providing a summary view of all partners.</p>

        Args:
            catalog: <p>The catalog identifier to list partners from.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.list_partners_request.ListPartnersRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_partners

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.list_partners.async_list_partners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.list_partners_response.ListPartnersResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.list_partners_response

            return capo_partnercentral_account.types.list_partners_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPartners", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.list_partners_request.ListPartnersRequest = {
            "catalog": catalog
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_aws_training_certification_email_domain(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        email: "capo_partnercentral_account.types.email.Email",
        email_verification_code: "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Associates an email domain with AWS training and certification for the partner account, enabling automatic verification of employee certifications.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            email: <p>The email address used to verify domain ownership for AWS training and certification association.</p>
            email_verification_code: <p>The verification code sent to the email address to confirm domain ownership.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_response.AssociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.associate_aws_training_certification_email_domain.async_associate_aws_training_certification_email_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request

            return capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AssociateAwsTrainingCertificationEmailDomain",
                redact_input=_redact_input,
            ),
        )
        input_: capo_partnercentral_account.types.associate_aws_training_certification_email_domain_request.AssociateAwsTrainingCertificationEmailDomainRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "email": email,
            "email_verification_code": email_verification_code,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_id: "capo_partnercentral_account.types.profile_task_id.ProfileTaskId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse":
        """<p>Cancels an in-progress profile update task, stopping any pending changes to the partner profile.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_id: <p>The unique identifier of the profile update task to cancel.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.cancel_profile_update_task_response.CancelProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_profile_update_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.cancel_profile_update_task.async_cancel_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelProfileUpdateTask")
        )
        input_: capo_partnercentral_account.types.cancel_profile_update_task_request.CancelProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "task_id": task_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_aws_training_certification_email_domain(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        domain_name: "capo_partnercentral_account.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse":
        """<p>Removes the association between an email domain and AWS training and certification for the partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            domain_name: <p>The domain name to disassociate from AWS training and certification.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_response.DisassociateAwsTrainingCertificationEmailDomainResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.disassociate_aws_training_certification_email_domain.async_disassociate_aws_training_certification_email_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisassociateAwsTrainingCertificationEmailDomain"),
        )
        input_: capo_partnercentral_account.types.disassociate_aws_training_certification_email_domain_request.DisassociateAwsTrainingCertificationEmailDomainRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "domain_name": domain_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_alliance_lead_contact(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse":
        """<p>Retrieves the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_alliance_lead_contact.async_get_alliance_lead_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.get_alliance_lead_contact_response.GetAllianceLeadContactResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.get_alliance_lead_contact_response

            return capo_partnercentral_account.types.get_alliance_lead_contact_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAllianceLeadContact", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.get_alliance_lead_contact_request.GetAllianceLeadContactRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse":
        """<p>Retrieves information about a specific profile update task.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_profile_update_task_response.GetProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_profile_update_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_profile_update_task.async_get_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetProfileUpdateTask")
        )
        input_: capo_partnercentral_account.types.get_profile_update_task_request.GetProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile_visibility(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse":
        """<p>Retrieves the visibility settings for a partner profile, determining who can see the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_profile_visibility_response.GetProfileVisibilityResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_profile_visibility

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_profile_visibility.async_get_profile_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetProfileVisibility")
        )
        input_: capo_partnercentral_account.types.get_profile_visibility_request.GetProfileVisibilityRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_qualifications_association_details(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_association_details_response.GetQualificationsAssociationDetailsResponse":
        """<p>Returns your current qualifications association status, the primary partner, and the full list of partners associated under the primary partner.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_qualifications_association_details_request.GetQualificationsAssociationDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_qualifications_association_details_response.GetQualificationsAssociationDetailsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_details

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_details.async_get_qualifications_association_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQualificationsAssociationDetails")
        )
        input_: capo_partnercentral_account.types.get_qualifications_association_details_request.GetQualificationsAssociationDetailsRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_qualifications_association_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_association_task_response.GetQualificationsAssociationTaskResponse":
        """<p>Retrieves the status and details of the most recent qualifications association task for your partner account. Use this operation to poll the progress of an association task initiated by <code>StartQualificationsAssociationTask</code>.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications association task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_qualifications_association_task_request.GetQualificationsAssociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_qualifications_association_task_response.GetQualificationsAssociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_qualifications_association_task.async_get_qualifications_association_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQualificationsAssociationTask")
        )
        input_: capo_partnercentral_account.types.get_qualifications_association_task_request.GetQualificationsAssociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_qualifications_disassociation_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_qualifications_disassociation_task_response.GetQualificationsDisassociationTaskResponse":
        """<p>Retrieves the status and details of the most recent qualifications disassociation task for your partner account. Use this operation to poll the progress of a disassociation task initiated by <code>StartQualificationsDisassociationTask</code>.</p>

        Args:
            catalog: <p>The catalog in which to look up the qualifications disassociation task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_qualifications_disassociation_task_request.GetQualificationsDisassociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_qualifications_disassociation_task_response.GetQualificationsDisassociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_qualifications_disassociation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_qualifications_disassociation_task.async_get_qualifications_disassociation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQualificationsDisassociationTask")
        )
        input_: capo_partnercentral_account.types.get_qualifications_disassociation_task_request.GetQualificationsDisassociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_alliance_lead_contact(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        alliance_lead_contact: "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        email_verification_code: Optional[
            "capo_partnercentral_account.types.email_verification_code.EmailVerificationCode"
        ] = None,
    ) -> "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse":
        """<p>Creates or updates the alliance lead contact information for a partner account.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            alliance_lead_contact: <p>The alliance lead contact information to set for the partner account.</p>
            email_verification_code: <p>The verification code sent to the alliance lead contact's email to confirm the update.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.put_alliance_lead_contact.async_put_alliance_lead_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.put_alliance_lead_contact_request

            return capo_partnercentral_account.types.put_alliance_lead_contact_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_partnercentral_account.types.put_alliance_lead_contact_response.PutAllianceLeadContactResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.put_alliance_lead_contact_response

            return capo_partnercentral_account.types.put_alliance_lead_contact_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "PutAllianceLeadContact",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_partnercentral_account.types.put_alliance_lead_contact_request.PutAllianceLeadContactRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "alliance_lead_contact": alliance_lead_contact,
        }
        if email_verification_code is not None:
            input_["email_verification_code"] = email_verification_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_profile_visibility(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        visibility: "capo_partnercentral_account.types.profile_visibility.ProfileVisibility",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse":
        """<p>Sets the visibility level for a partner profile, controlling who can view the profile information.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            visibility: <p>The visibility setting to apply to the partner profile.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.put_profile_visibility_response.PutProfileVisibilityResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.put_profile_visibility

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.put_profile_visibility.async_put_profile_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutProfileVisibility")
        )
        input_: capo_partnercentral_account.types.put_profile_visibility_request.PutProfileVisibilityRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "visibility": visibility,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_profile_update_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        task_details: "capo_partnercentral_account.types.task_details.TaskDetails",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse":
        """<p>Initiates a profile update task to modify partner profile information asynchronously.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            identifier: <p>The unique identifier of the partner account.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            task_details: <p>The details of the profile updates to be performed.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_profile_update_task_response.StartProfileUpdateTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_profile_update_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_profile_update_task.async_start_profile_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartProfileUpdateTask")
        )
        input_: capo_partnercentral_account.types.start_profile_update_task_request.StartProfileUpdateTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "task_details": task_details,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_qualifications_association_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        primary_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_qualifications_association_task_response.StartQualificationsAssociationTaskResponse":
        """<p>Initiates an asynchronous task to associate your partner qualifications with a primary account. You must be a subsidiary of the primary account with an active subsidiary connection. Use <code>GetQualificationsAssociationTask</code> to monitor task progress.</p>

        Args:
            catalog: <p>The catalog in which to perform the qualifications association. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            primary_partner: <p>The primary (acquiring) partner's profile and account identifier to associate qualifications with. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. You cannot specify yourself as the primary partner.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_qualifications_association_task_request.StartQualificationsAssociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_qualifications_association_task_response.StartQualificationsAssociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_qualifications_association_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_qualifications_association_task.async_start_qualifications_association_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartQualificationsAssociationTask")
        )
        input_: capo_partnercentral_account.types.start_qualifications_association_task_request.StartQualificationsAssociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "primary_partner": primary_partner,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_qualifications_disassociation_task(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier",
        associated_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_qualifications_disassociation_task_response.StartQualificationsDisassociationTaskResponse":
        """<p>Initiates an asynchronous task to disassociate your partner qualifications from a primary account. You must currently be associated and cannot disassociate if you are the primary partner. Use <code>GetQualificationsDisassociationTask</code> to monitor task progress.</p>

        Args:
            catalog: <p>The catalog in which to perform the qualifications disassociation. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>
            identifier: <p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            associated_partner: <p>The primary partner's profile and account identifier that you are currently associated with and will disassociate from. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. The specified partner must match your current primary association.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.start_qualifications_disassociation_task_request.StartQualificationsDisassociationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.start_qualifications_disassociation_task_response.StartQualificationsDisassociationTaskResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_qualifications_disassociation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.start_qualifications_disassociation_task.async_start_qualifications_disassociation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartQualificationsDisassociationTask")
        )
        input_: capo_partnercentral_account.types.start_qualifications_disassociation_task_request.StartQualificationsDisassociationTaskRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "associated_partner": associated_partner,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
