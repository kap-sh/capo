from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_partnercentral_selling._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.accept_engagement_invitation_request
    import capo_partnercentral_selling.types.aws_account_id_or_alias_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.create_engagement_invitation_request
    import capo_partnercentral_selling.types.create_engagement_invitation_response
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_invitation_summary
    import capo_partnercentral_selling.types.engagement_invitations_payload_type
    import capo_partnercentral_selling.types.get_engagement_invitation_request
    import capo_partnercentral_selling.types.get_engagement_invitation_response
    import capo_partnercentral_selling.types.invitation
    import capo_partnercentral_selling.types.invitation_status_list
    import capo_partnercentral_selling.types.list_engagement_invitations_request
    import capo_partnercentral_selling.types.list_engagement_invitations_response
    import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.participant_type
    import capo_partnercentral_selling.types.reject_engagement_invitation_request
    import capo_partnercentral_selling.types.rejection_reason_string
    from capo_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from capo_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class EngagementInvitation:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        invitation: "capo_partnercentral_selling.types.invitation.Invitation",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_invitation_response.CreateEngagementInvitationResponse":
        """<p> This action creates an invitation from a sender to a single receiver to join an engagement. </p>

        Args:
            catalog: <p> Specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed. </p>
            client_token: <p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate invitation creations. </p>
            engagement_identifier: <p> The unique identifier of the <code>Engagement</code> associated with the invitation. This parameter ensures the invitation is created within the correct <code>Engagement</code> context. </p>
            invitation: <p> The <code>Invitation</code> object all information necessary to initiate an engagement invitation to a partner. It contains a personalized message from the sender, the invitation's receiver, and a payload. The <code>Payload</code> can be the <code>OpportunityInvitation</code>, which includes detailed structures for sender contacts, partner responsibilities, customer information, and project details, or <code>LeadInvitation</code>, which includes structures for customer information and interaction details. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.create_engagement_invitation_request.CreateEngagementInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.create_engagement_invitation_response.CreateEngagementInvitationResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_invitation

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_invitation.create_engagement_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_invitation_request.CreateEngagementInvitationRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "engagement_identifier": engagement_identifier,
            "invitation": invitation,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_engagement_invitation_response.GetEngagementInvitationResponse":
        """<p>Retrieves the details of an engagement invitation shared by AWS with a partner. The information includes aspects such as customer, project details, and lifecycle information. To connect an engagement invitation with an opportunity, match the invitation’s <code>Payload.Project.Title</code> with opportunity <code>Project.Title</code>.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. The field accepts values from the predefined set: <code>AWS</code> for live operations or <code>Sandbox</code> for testing environments.</p>
            identifier: <p>Specifies the unique identifier for the retrieved engagement invitation.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_engagement_invitation_request.GetEngagementInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_engagement_invitation_response.GetEngagementInvitationResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement_invitation

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement_invitation.get_engagement_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_engagement_invitation_request.GetEngagementInvitationRequest = {
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        participant_type: "capo_partnercentral_selling.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.OpportunityEngagementInvitationSort"
        ] = None,
        payload_type: Optional[
            "capo_partnercentral_selling.types.engagement_invitations_payload_type.EngagementInvitationsPayloadType"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.invitation_status_list.InvitationStatusList"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        sender_aws_account_id: Optional[
            "capo_partnercentral_selling.types.aws_account_id_or_alias_list.AwsAccountIdOrAliasList"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_invitations_response.ListEngagementInvitationsResponse":
        """<p>Retrieves a list of engagement invitations sent to the partner. This allows partners to view all pending or past engagement invitations, helping them track opportunities shared by AWS.</p>

        Args:
            catalog: <p>Specifies the catalog from which to list the engagement invitations. Use <code>AWS</code> for production invitations or <code>Sandbox</code> for testing environments.</p>
            max_results: <p>Specifies the maximum number of engagement invitations to return in the response. If more results are available, a pagination token will be provided.</p>
            next_token: <p>A pagination token used to retrieve additional pages of results when the response to a previous request was truncated. Pass this token to continue listing invitations from where the previous call left off.</p>
            sort: <p>Specifies the sorting options for listing engagement invitations. Invitations can be sorted by fields such as <code>InvitationDate</code> or <code>Status</code> to help partners view results in their preferred order.</p>
            payload_type: <p>Defines the type of payload associated with the engagement invitations to be listed. The attributes in this payload help decide on acceptance or rejection of the invitation.</p>
            participant_type: <p>Specifies the type of participant for which to list engagement invitations. Identifies the role of the participant.</p>
            status: <p> Status values to filter the invitations. </p>
            engagement_identifier: <p> Retrieves a list of engagement invitation summaries based on specified filters. The ListEngagementInvitations operation allows you to view all invitations that you have sent or received. You must specify the ParticipantType to filter invitations where you are either the SENDER or the RECEIVER. Invitations will automatically expire if not accepted within 15 days. </p>
            sender_aws_account_id: <p> List of sender AWS account IDs to filter the invitations. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_engagement_invitations_request.ListEngagementInvitationsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_engagement_invitations_response.ListEngagementInvitationsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_invitations

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_invitations.list_engagement_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_invitations_request.ListEngagementInvitationsRequest = {
            "catalog": catalog,
            "participant_type": participant_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if payload_type is not None:
            input_["payload_type"] = payload_type
        if status is not None:
            input_["status"] = status
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if sender_aws_account_id is not None:
            input_["sender_aws_account_id"] = sender_aws_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def accept_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Use the <code>AcceptEngagementInvitation</code> action to accept an engagement invitation shared by AWS. Accepting the invitation indicates your willingness to participate in the engagement, granting you access to all engagement-related data.</p>

        Args:
            catalog: <p>The <code>CatalogType</code> parameter specifies the catalog associated with the engagement invitation. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement invitation is managed.</p>
            identifier: <p> The <code>Identifier</code> parameter in the <code>AcceptEngagementInvitationRequest</code> specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier ensures that the intended invitation is accepted. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.accept_engagement_invitation_request.AcceptEngagementInvitationRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.accept_engagement_invitation

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.accept_engagement_invitation.accept_engagement_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.accept_engagement_invitation_request.AcceptEngagementInvitationRequest = {
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

    def reject_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        rejection_reason: Optional[
            "capo_partnercentral_selling.types.rejection_reason_string.RejectionReasonString"
        ] = None,
    ) -> None:
        """<p>This action rejects an <code>EngagementInvitation</code> that AWS shared. Rejecting an invitation indicates that the partner doesn't want to pursue the opportunity, and all related data will become inaccessible thereafter.</p>

        Args:
            catalog: <p>This is the catalog that's associated with the engagement invitation. Acceptable values are <code>AWS</code> or <code>Sandbox</code>, and these values determine the environment in which the opportunity is managed.</p>
            identifier: <p>This is the unique identifier of the rejected <code>EngagementInvitation</code>. Providing the correct identifier helps to ensure that the intended invitation is rejected.</p>
            rejection_reason: <p>This describes the reason for rejecting the engagement invitation, which helps AWS track usage patterns. Acceptable values include the following:</p> <ul> <li> <p> <i>Customer problem unclear:</i> The customer's problem isn't understood.</p> </li> <li> <p> <i>Next steps unclear:</i> The next steps required to proceed aren't understood.</p> </li> <li> <p> <i>Unable to support:</i> The partner is unable to provide support due to resource or capability constraints.</p> </li> <li> <p> <i>Duplicate of partner referral:</i> The opportunity is a duplicate of an existing referral.</p> </li> <li> <p> <i>Other:</i> Any reason not covered by other values.</p> </li> </ul>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.reject_engagement_invitation_request.RejectEngagementInvitationRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.reject_engagement_invitation

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.reject_engagement_invitation.reject_engagement_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.reject_engagement_invitation_request.RejectEngagementInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if rejection_reason is not None:
            input_["rejection_reason"] = rejection_reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEngagementInvitation:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        invitation: "capo_partnercentral_selling.types.invitation.Invitation",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_invitation_response.CreateEngagementInvitationResponse":
        """<p> This action creates an invitation from a sender to a single receiver to join an engagement. </p>

        Args:
            catalog: <p> Specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed. </p>
            client_token: <p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate invitation creations. </p>
            engagement_identifier: <p> The unique identifier of the <code>Engagement</code> associated with the invitation. This parameter ensures the invitation is created within the correct <code>Engagement</code> context. </p>
            invitation: <p> The <code>Invitation</code> object all information necessary to initiate an engagement invitation to a partner. It contains a personalized message from the sender, the invitation's receiver, and a payload. The <code>Payload</code> can be the <code>OpportunityInvitation</code>, which includes detailed structures for sender contacts, partner responsibilities, customer information, and project details, or <code>LeadInvitation</code>, which includes structures for customer information and interaction details. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.create_engagement_invitation_request.CreateEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.create_engagement_invitation_response.CreateEngagementInvitationResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_invitation.async_create_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_invitation_request.CreateEngagementInvitationRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "engagement_identifier": engagement_identifier,
            "invitation": invitation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_engagement_invitation_response.GetEngagementInvitationResponse":
        """<p>Retrieves the details of an engagement invitation shared by AWS with a partner. The information includes aspects such as customer, project details, and lifecycle information. To connect an engagement invitation with an opportunity, match the invitation’s <code>Payload.Project.Title</code> with opportunity <code>Project.Title</code>.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the request. The field accepts values from the predefined set: <code>AWS</code> for live operations or <code>Sandbox</code> for testing environments.</p>
            identifier: <p>Specifies the unique identifier for the retrieved engagement invitation.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.get_engagement_invitation_request.GetEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.get_engagement_invitation_response.GetEngagementInvitationResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.get_engagement_invitation.async_get_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_engagement_invitation_request.GetEngagementInvitationRequest = {
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
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        participant_type: "capo_partnercentral_selling.types.participant_type.ParticipantType",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        sort: Optional[
            "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.OpportunityEngagementInvitationSort"
        ] = None,
        payload_type: Optional[
            "capo_partnercentral_selling.types.engagement_invitations_payload_type.EngagementInvitationsPayloadType"
        ] = None,
        status: Optional[
            "capo_partnercentral_selling.types.invitation_status_list.InvitationStatusList"
        ] = None,
        engagement_identifier: Optional[
            "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
        ] = None,
        sender_aws_account_id: Optional[
            "capo_partnercentral_selling.types.aws_account_id_or_alias_list.AwsAccountIdOrAliasList"
        ] = None,
    ) -> "capo_partnercentral_selling.types.list_engagement_invitations_response.ListEngagementInvitationsResponse":
        """<p>Retrieves a list of engagement invitations sent to the partner. This allows partners to view all pending or past engagement invitations, helping them track opportunities shared by AWS.</p>

        Args:
            catalog: <p>Specifies the catalog from which to list the engagement invitations. Use <code>AWS</code> for production invitations or <code>Sandbox</code> for testing environments.</p>
            max_results: <p>Specifies the maximum number of engagement invitations to return in the response. If more results are available, a pagination token will be provided.</p>
            next_token: <p>A pagination token used to retrieve additional pages of results when the response to a previous request was truncated. Pass this token to continue listing invitations from where the previous call left off.</p>
            sort: <p>Specifies the sorting options for listing engagement invitations. Invitations can be sorted by fields such as <code>InvitationDate</code> or <code>Status</code> to help partners view results in their preferred order.</p>
            payload_type: <p>Defines the type of payload associated with the engagement invitations to be listed. The attributes in this payload help decide on acceptance or rejection of the invitation.</p>
            participant_type: <p>Specifies the type of participant for which to list engagement invitations. Identifies the role of the participant.</p>
            status: <p> Status values to filter the invitations. </p>
            engagement_identifier: <p> Retrieves a list of engagement invitation summaries based on specified filters. The ListEngagementInvitations operation allows you to view all invitations that you have sent or received. You must specify the ParticipantType to filter invitations where you are either the SENDER or the RECEIVER. Invitations will automatically expire if not accepted within 15 days. </p>
            sender_aws_account_id: <p> List of sender AWS account IDs to filter the invitations. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.list_engagement_invitations_request.ListEngagementInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_selling.types.list_engagement_invitations_response.ListEngagementInvitationsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_invitations

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.list_engagement_invitations.async_list_engagement_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_engagement_invitations_request.ListEngagementInvitationsRequest = {
            "catalog": catalog,
            "participant_type": participant_type,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort is not None:
            input_["sort"] = sort
        if payload_type is not None:
            input_["payload_type"] = payload_type
        if status is not None:
            input_["status"] = status
        if engagement_identifier is not None:
            input_["engagement_identifier"] = engagement_identifier
        if sender_aws_account_id is not None:
            input_["sender_aws_account_id"] = sender_aws_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Use the <code>AcceptEngagementInvitation</code> action to accept an engagement invitation shared by AWS. Accepting the invitation indicates your willingness to participate in the engagement, granting you access to all engagement-related data.</p>

        Args:
            catalog: <p>The <code>CatalogType</code> parameter specifies the catalog associated with the engagement invitation. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement invitation is managed.</p>
            identifier: <p> The <code>Identifier</code> parameter in the <code>AcceptEngagementInvitationRequest</code> specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier ensures that the intended invitation is accepted. </p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.accept_engagement_invitation_request.AcceptEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.accept_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.accept_engagement_invitation.async_accept_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.accept_engagement_invitation_request.AcceptEngagementInvitationRequest = {
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

    async def reject_engagement_invitation(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        rejection_reason: Optional[
            "capo_partnercentral_selling.types.rejection_reason_string.RejectionReasonString"
        ] = None,
    ) -> None:
        """<p>This action rejects an <code>EngagementInvitation</code> that AWS shared. Rejecting an invitation indicates that the partner doesn't want to pursue the opportunity, and all related data will become inaccessible thereafter.</p>

        Args:
            catalog: <p>This is the catalog that's associated with the engagement invitation. Acceptable values are <code>AWS</code> or <code>Sandbox</code>, and these values determine the environment in which the opportunity is managed.</p>
            identifier: <p>This is the unique identifier of the rejected <code>EngagementInvitation</code>. Providing the correct identifier helps to ensure that the intended invitation is rejected.</p>
            rejection_reason: <p>This describes the reason for rejecting the engagement invitation, which helps AWS track usage patterns. Acceptable values include the following:</p> <ul> <li> <p> <i>Customer problem unclear:</i> The customer's problem isn't understood.</p> </li> <li> <p> <i>Next steps unclear:</i> The next steps required to proceed aren't understood.</p> </li> <li> <p> <i>Unable to support:</i> The partner is unable to provide support due to resource or capability constraints.</p> </li> <li> <p> <i>Duplicate of partner referral:</i> The opportunity is a duplicate of an existing referral.</p> </li> <li> <p> <i>Other:</i> Any reason not covered by other values.</p> </li> </ul>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href="https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_selling.types.reject_engagement_invitation_request.RejectEngagementInvitationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.reject_engagement_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_selling._operations.aws_partner_central_selling.reject_engagement_invitation.async_reject_engagement_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.reject_engagement_invitation_request.RejectEngagementInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
        }
        if rejection_reason is not None:
            input_["rejection_reason"] = rejection_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
