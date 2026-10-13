from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_ssm_guiconnect._auth._signers
import capo_ssm_guiconnect._auth._sigv4
from capo_ssm_guiconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.client_token
    import capo_ssm_guiconnect.types.delete_connection_recording_preferences_request
    import capo_ssm_guiconnect.types.delete_connection_recording_preferences_response
    import capo_ssm_guiconnect.types.get_connection_recording_preferences_response
    from capo_ssm_guiconnect._services.async_ssm_gui_connect import (
        AsyncSSMGuiConnectClient,
        AsyncSSMGuiConnectClientConfig,
    )
    from capo_ssm_guiconnect._services.ssm_gui_connect import (
        SSMGuiConnectClient,
        SSMGuiConnectClientConfig,
    )


class ModifyRecordingPreferences:
    def __init__(self, service: SSMGuiConnectClient) -> None:
        self._service = service

    def read(
        self, *, config_overrides: Optional[SSMGuiConnectClientConfig] = None
    ) -> "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse":
        """<p>Returns the preferences specified for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieves the connection recording preferences for the account

            >>> client.read()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences

            output, http_response = (
                capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences.get_connection_recording_preferences(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConnectionRecordingPreferences")
        )

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        *,
        config_overrides: Optional[SSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "capo_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse":
        """<p>Deletes the preferences for recording RDP connections.</p>

        Args:
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete the connection recording preferences for the account

            >>> client.delete()
        """

        def _handler(
            req: "OperationRequest[capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest]",
        ) -> OperationResponse[
            "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences

            output, http_response = (
                capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences.delete_connection_recording_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConnectionRecordingPreferences")
        )
        input_: capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest = {}
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


class AsyncModifyRecordingPreferences:
    def __init__(self, service: AsyncSSMGuiConnectClient) -> None:
        self._service = service

    async def read(
        self, *, config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None
    ) -> "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse":
        """<p>Returns the preferences specified for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieves the connection recording preferences for the account

            >>> await client.read()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences

            (
                output,
                http_response,
            ) = await capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences.async_get_connection_recording_preferences(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConnectionRecordingPreferences")
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        *,
        config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "capo_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse":
        """<p>Deletes the preferences for recording RDP connections.</p>

        Args:
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete the connection recording preferences for the account

            >>> await client.delete()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences

            (
                output,
                http_response,
            ) = await capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences.async_delete_connection_recording_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConnectionRecordingPreferences")
        )
        input_: capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest = {}
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
