from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    import capo_partnercentral_account.types.access_type
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.get_connection_preferences_request
    import capo_partnercentral_account.types.get_connection_preferences_response
    import capo_partnercentral_account.types.participant_identifier_list
    import capo_partnercentral_account.types.revision
    import capo_partnercentral_account.types.update_connection_preferences_request
    import capo_partnercentral_account.types.update_connection_preferences_response
    from capo_partnercentral_account._services.async_partner_central_account import (
        AsyncPartnerCentralAccountClient,
        AsyncPartnerCentralAccountClientConfig,
    )
    from capo_partnercentral_account._services.partner_central_account import (
        PartnerCentralAccountClient,
        PartnerCentralAccountClientConfig,
    )


class ConnectionPreferences:
    def __init__(self, service: PartnerCentralAccountClient) -> None:
        self._service = service

    def read(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse":
        """<p>Retrieves the connection preferences for a partner account, including access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection_preferences

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_connection_preferences.get_connection_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConnectionPreferences")
        )
        input_: capo_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest = {
            "catalog": catalog
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_connection_preferences(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        revision: "capo_partnercentral_account.types.revision.Revision",
        access_type: "capo_partnercentral_account.types.access_type.AccessType",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        excluded_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "capo_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse":
        """<p>Updates the connection preferences for a partner account, modifying access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            revision: <p>The revision number of the connection preferences for optimistic locking.</p>
            access_type: <p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>
            excluded_participant_identifiers: <p>The updated list of participant identifiers to exclude from connections.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.update_connection_preferences

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.update_connection_preferences.update_connection_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConnectionPreferences")
        )
        input_: capo_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest = {
            "catalog": catalog,
            "revision": revision,
            "access_type": access_type,
        }
        if excluded_participant_identifiers is not None:
            input_["excluded_participant_identifiers"] = (
                excluded_participant_identifiers
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConnectionPreferences:
    def __init__(self, service: AsyncPartnerCentralAccountClient) -> None:
        self._service = service

    async def read(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse":
        """<p>Retrieves the connection preferences for a partner account, including access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.get_connection_preferences_response.GetConnectionPreferencesResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_connection_preferences

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.get_connection_preferences.async_get_connection_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConnectionPreferences")
        )
        input_: capo_partnercentral_account.types.get_connection_preferences_request.GetConnectionPreferencesRequest = {
            "catalog": catalog
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connection_preferences(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        revision: "capo_partnercentral_account.types.revision.Revision",
        access_type: "capo_partnercentral_account.types.access_type.AccessType",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        excluded_participant_identifiers: Optional[
            "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
        ] = None,
    ) -> "capo_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse":
        """<p>Updates the connection preferences for a partner account, modifying access settings and exclusions.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            revision: <p>The revision number of the connection preferences for optimistic locking.</p>
            access_type: <p>The access type setting for connections (e.g., open, restricted, invitation-only).</p>
            excluded_participant_identifiers: <p>The updated list of participant identifiers to exclude from connections.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_account.types.update_connection_preferences_response.UpdateConnectionPreferencesResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.update_connection_preferences

            (
                output,
                http_response,
            ) = await capo_partnercentral_account._operations.partner_central_account.update_connection_preferences.async_update_connection_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConnectionPreferences")
        )
        input_: capo_partnercentral_account.types.update_connection_preferences_request.UpdateConnectionPreferencesRequest = {
            "catalog": catalog,
            "revision": revision,
            "access_type": access_type,
        }
        if excluded_participant_identifiers is not None:
            input_["excluded_participant_identifiers"] = (
                excluded_participant_identifiers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
