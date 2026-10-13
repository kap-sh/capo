from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.create_credential_locker_request
    import capo_iot_managed_integrations.types.create_credential_locker_response
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.credential_locker_name
    import capo_iot_managed_integrations.types.credential_locker_summary
    import capo_iot_managed_integrations.types.delete_credential_locker_request
    import capo_iot_managed_integrations.types.get_credential_locker_request
    import capo_iot_managed_integrations.types.get_credential_locker_response
    import capo_iot_managed_integrations.types.list_credential_lockers_request
    import capo_iot_managed_integrations.types.list_credential_lockers_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.tags_map
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class CredentialLockerResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse":
        """<p>Create a credential locker.</p> <note> <p>This operation will not trigger the creation of all the manufacturing resources.</p> </note>

        Args:
            name: <p>The name of the credential locker.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker.create_credential_locker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_credential_locker_request

            return capo_iot_managed_integrations.types.create_credential_locker_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCredentialLocker", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest = {}
        if name is not None:
            input_["name"] = name
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
        identifier: "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse":
        """<p>Get information on an existing credential locker</p>

        Args:
            identifier: <p>The identifier of the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker.get_credential_locker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_credential_locker_response

            return capo_iot_managed_integrations.types.get_credential_locker_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCredentialLocker", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a credential locker. </p> <note> <p>This operation can't be undone and any existing device won't be able to use IoT managed integrations.</p> </note>

        Args:
            identifier: <p>The identifier of the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker.delete_credential_locker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCredentialLocker")
        )
        input_: capo_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest = {
            "identifier": identifier
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
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse":
        """<p>List information on an existing credential locker.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers.list_credential_lockers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.list_credential_lockers_response

            return capo_iot_managed_integrations.types.list_credential_lockers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCredentialLockers", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest = {}
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


class AsyncCredentialLockerResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse":
        """<p>Create a credential locker.</p> <note> <p>This operation will not trigger the creation of all the manufacturing resources.</p> </note>

        Args:
            name: <p>The name of the credential locker.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker.async_create_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_credential_locker_request

            return capo_iot_managed_integrations.types.create_credential_locker_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCredentialLocker", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest = {}
        if name is not None:
            input_["name"] = name
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
        identifier: "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse":
        """<p>Get information on an existing credential locker</p>

        Args:
            identifier: <p>The identifier of the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker.async_get_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_credential_locker_response

            return capo_iot_managed_integrations.types.get_credential_locker_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCredentialLocker", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a credential locker. </p> <note> <p>This operation can't be undone and any existing device won't be able to use IoT managed integrations.</p> </note>

        Args:
            identifier: <p>The identifier of the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker.async_delete_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCredentialLocker")
        )
        input_: capo_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest = {
            "identifier": identifier
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
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse":
        """<p>List information on an existing credential locker.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers.async_list_credential_lockers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.list_credential_lockers_response

            return capo_iot_managed_integrations.types.list_credential_lockers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListCredentialLockers", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
