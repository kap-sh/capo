from __future__ import annotations

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
    import capo_partnercentral_account.types.accept_connection_invitation_request
    import capo_partnercentral_account.types.accept_connection_invitation_response
    import capo_partnercentral_account.types.cancel_connection_invitation_request
    import capo_partnercentral_account.types.cancel_connection_invitation_response
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.connection_invitation_id
    import capo_partnercentral_account.types.connection_invitation_summary
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.create_connection_invitation_request
    import capo_partnercentral_account.types.create_connection_invitation_response
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.get_connection_invitation_request
    import capo_partnercentral_account.types.get_connection_invitation_response
    import capo_partnercentral_account.types.invitation_status
    import capo_partnercentral_account.types.list_connection_invitations_request
    import capo_partnercentral_account.types.list_connection_invitations_response
    import capo_partnercentral_account.types.max_results
    import capo_partnercentral_account.types.next_token
    import capo_partnercentral_account.types.participant_identifier
    import capo_partnercentral_account.types.participant_identifier_list
    import capo_partnercentral_account.types.participant_type
    import capo_partnercentral_account.types.reject_connection_invitation_request
    import capo_partnercentral_account.types.reject_connection_invitation_response
    import capo_partnercentral_account.types.sensitive_unicode_string
    import capo_partnercentral_account.types.unicode_string_including_new_line
    from capo_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from capo_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class ConnectionInvitation:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType",
        email: "capo_partnercentral_account.types.email.Email",
        message: "capo_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine",
        name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        receiver_identifier: "capo_partnercentral_account.types.participant_identifier.ParticipantIdentifier",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse":
        """<p>Creates a new connection invitation to establish a partnership with another organization.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            connection_type: <p>The type of connection being requested (e.g., reseller, distributor, technology partner).</p>
            email: <p>The email address of the person to send the connection invitation to.</p>
            message: <p>A custom message to include with the connection invitation.</p>
            name: <p>The name of the person sending the connection invitation.</p>
            receiver_identifier: <p>The identifier of the organization or partner to invite for connection.</p>

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
            req: "OperationRequest[capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.create_connection_invitation

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.create_connection_invitation.create_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_connection_invitation_request

            return capo_partnercentral_account.types.create_connection_invitation_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_connection_invitation_response

            return capo_partnercentral_account.types.create_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateConnectionInvitation",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "connection_type": connection_type,
            "email": email,
            "message": message,
            "name": name,
            "receiver_identifier": receiver_identifier,
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
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse":
        """<p>Retrieves detailed information about a specific connection invitation.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection_invitation

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_connection_invitation.get_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.get_connection_invitation_response

            return capo_partnercentral_account.types.get_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetConnectionInvitation", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest = {
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
        connection_type: Optional[
            "capo_partnercentral_account.types.connection_type.ConnectionType"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
        participant_type: Optional[
            "capo_partnercentral_account.types.participant_type.ParticipantType"
        ] = None,
        status: Optional[
            "capo_partnercentral_account.types.invitation_status.InvitationStatus"
        ] = None,
    ) -> "capo_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse":
        """<p>Lists connection invitations for the partner account, with optional filtering by status, type, and other criteria.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connection invitations to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
            participant_type: <p>Filter results by participant type (inviter or invitee).</p>
            status: <p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_connection_invitations

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.list_connection_invitations.list_connection_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConnectionInvitations")
        )
        input_: capo_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest = {
            "catalog": catalog
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if max_results is not None:
            input_["max_results"] = max_results
        if other_participant_identifiers is not None:
            input_["other_participant_identifiers"] = other_participant_identifiers
        if participant_type is not None:
            input_["participant_type"] = participant_type
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def accept_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse":
        """<p>Accepts a connection invitation from another partner, establishing a formal partnership connection between the two parties.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to accept.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

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
            req: "OperationRequest[capo_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.accept_connection_invitation

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.accept_connection_invitation.accept_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.accept_connection_invitation_response

            return capo_partnercentral_account.types.accept_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AcceptConnectionInvitation", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse":
        """<p>Cancels a pending connection invitation before it has been accepted or rejected.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to cancel.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

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
            req: "OperationRequest[capo_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_connection_invitation

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.cancel_connection_invitation.cancel_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.cancel_connection_invitation_response

            return capo_partnercentral_account.types.cancel_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CancelConnectionInvitation", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        reason: Optional[str] = None,
    ) -> "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse":
        """<p>Rejects a connection invitation from another partner, declining the partnership request.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to reject.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            reason: <p>The reason for rejecting the connection invitation.</p>

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
            req: "OperationRequest[capo_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.reject_connection_invitation

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.reject_connection_invitation.reject_connection_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.reject_connection_invitation_response

            return capo_partnercentral_account.types.reject_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "RejectConnectionInvitation", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConnectionInvitation:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType",
        email: "capo_partnercentral_account.types.email.Email",
        message: "capo_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine",
        name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString",
        receiver_identifier: "capo_partnercentral_account.types.participant_identifier.ParticipantIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse":
        """<p>Creates a new connection invitation to establish a partnership with another organization.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation will be created.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            connection_type: <p>The type of connection being requested (e.g., reseller, distributor, technology partner).</p>
            email: <p>The email address of the person to send the connection invitation to.</p>
            message: <p>A custom message to include with the connection invitation.</p>
            name: <p>The name of the person sending the connection invitation.</p>
            receiver_identifier: <p>The identifier of the organization or partner to invite for connection.</p>

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
            req: "AsyncOperationRequest[capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.create_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.create_connection_invitation.async_create_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_connection_invitation_request

            return capo_partnercentral_account.types.create_connection_invitation_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_partnercentral_account.types.create_connection_invitation_response.CreateConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.create_connection_invitation_response

            return capo_partnercentral_account.types.create_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateConnectionInvitation",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_partnercentral_account.types.create_connection_invitation_request.CreateConnectionInvitationRequest = {
            "catalog": catalog,
            "client_token": client_token,
            "connection_type": connection_type,
            "email": email,
            "message": message,
            "name": name,
            "receiver_identifier": receiver_identifier,
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
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse":
        """<p>Retrieves detailed information about a specific connection invitation.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to retrieve.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_connection_invitation.async_get_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.get_connection_invitation_response.GetConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.get_connection_invitation_response

            return capo_partnercentral_account.types.get_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetConnectionInvitation", redact_output=_redact_output),
        )
        input_: capo_partnercentral_account.types.get_connection_invitation_request.GetConnectionInvitationRequest = {
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
        connection_type: Optional[
            "capo_partnercentral_account.types.connection_type.ConnectionType"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_account.types.max_results.MaxResults"
        ] = None,
        other_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
        participant_type: Optional[
            "capo_partnercentral_account.types.participant_type.ParticipantType"
        ] = None,
        status: Optional[
            "capo_partnercentral_account.types.invitation_status.InvitationStatus"
        ] = None,
    ) -> "capo_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse":
        """<p>Lists connection invitations for the partner account, with optional filtering by status, type, and other criteria.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            next_token: <p>The token for retrieving the next page of results in paginated responses.</p>
            connection_type: <p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>
            max_results: <p>The maximum number of connection invitations to return in a single response.</p>
            other_participant_identifiers: <p>Filter results by specific participant identifiers.</p>
            participant_type: <p>Filter results by participant type (inviter or invitee).</p>
            status: <p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.list_connection_invitations_response.ListConnectionInvitationsResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_connection_invitations

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.list_connection_invitations.async_list_connection_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConnectionInvitations")
        )
        input_: capo_partnercentral_account.types.list_connection_invitations_request.ListConnectionInvitationsRequest = {
            "catalog": catalog
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if max_results is not None:
            input_["max_results"] = max_results
        if other_participant_identifiers is not None:
            input_["other_participant_identifiers"] = other_participant_identifiers
        if participant_type is not None:
            input_["participant_type"] = participant_type
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse":
        """<p>Accepts a connection invitation from another partner, establishing a formal partnership connection between the two parties.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to accept.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

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
            req: "AsyncOperationRequest[capo_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.accept_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.accept_connection_invitation.async_accept_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.accept_connection_invitation_response.AcceptConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.accept_connection_invitation_response

            return capo_partnercentral_account.types.accept_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AcceptConnectionInvitation", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_account.types.accept_connection_invitation_request.AcceptConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse":
        """<p>Cancels a pending connection invitation before it has been accepted or rejected.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to cancel.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

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
            req: "AsyncOperationRequest[capo_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.cancel_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.cancel_connection_invitation.async_cancel_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.cancel_connection_invitation_response.CancelConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.cancel_connection_invitation_response

            return capo_partnercentral_account.types.cancel_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CancelConnectionInvitation", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_account.types.cancel_connection_invitation_request.CancelConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_connection_invitation(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        identifier: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId",
        client_token: "capo_partnercentral_account.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        reason: Optional[str] = None,
    ) -> "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse":
        """<p>Rejects a connection invitation from another partner, declining the partnership request.</p>

        Args:
            catalog: <p>The catalog identifier where the connection invitation exists.</p>
            identifier: <p>The unique identifier of the connection invitation to reject.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            reason: <p>The reason for rejecting the connection invitation.</p>

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
            req: "AsyncOperationRequest[capo_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.reject_connection_invitation

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.reject_connection_invitation.async_reject_connection_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_account.types.reject_connection_invitation_response.RejectConnectionInvitationResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_account.types.reject_connection_invitation_response

            return capo_partnercentral_account.types.reject_connection_invitation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "RejectConnectionInvitation", redact_output=_redact_output
            ),
        )
        input_: capo_partnercentral_account.types.reject_connection_invitation_request.RejectConnectionInvitationRequest = {
            "catalog": catalog,
            "identifier": identifier,
            "client_token": client_token,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
