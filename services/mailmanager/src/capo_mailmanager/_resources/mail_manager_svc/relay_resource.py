from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_mailmanager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mailmanager.types.create_relay_request
    import capo_mailmanager.types.create_relay_response
    import capo_mailmanager.types.delete_relay_request
    import capo_mailmanager.types.delete_relay_response
    import capo_mailmanager.types.get_relay_request
    import capo_mailmanager.types.get_relay_response
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.list_relays_request
    import capo_mailmanager.types.list_relays_response
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.relay
    import capo_mailmanager.types.relay_authentication
    import capo_mailmanager.types.relay_id
    import capo_mailmanager.types.relay_name
    import capo_mailmanager.types.relay_server_name
    import capo_mailmanager.types.relay_server_port
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.update_relay_request
    import capo_mailmanager.types.update_relay_response
    from capo_mailmanager._services.async_mail_manager import (
        AsyncMailManagerClient,
        AsyncMailManagerClientConfig,
    )
    from capo_mailmanager._services.mail_manager import (
        MailManagerClient,
        MailManagerClientConfig,
    )


class RelayResource:
    def __init__(self, service: MailManagerClient) -> None:
        self._service = service

    def create(
        self,
        relay_name: "capo_mailmanager.types.relay_name.RelayName",
        server_name: "capo_mailmanager.types.relay_server_name.RelayServerName",
        server_port: "capo_mailmanager.types.relay_server_port.RelayServerPort",
        authentication: "capo_mailmanager.types.relay_authentication.RelayAuthentication",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_relay_response.CreateRelayResponse":
        """<p>Creates a relay resource which can be used in rules to relay incoming emails to defined relay destinations. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            relay_name: <p>The unique name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.create_relay_request.CreateRelayRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.create_relay_response.CreateRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_relay

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.create_relay.create_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_relay_request.CreateRelayRequest = {
            "relay_name": relay_name,
            "server_name": server_name,
            "server_port": server_port,
            "authentication": authentication,
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
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_relay_response.GetRelayResponse":
        """<p>Fetch the relay resource and it's attributes.</p>

        Args:
            relay_id: <p>A unique relay identifier.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.get_relay_request.GetRelayRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.get_relay_response.GetRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_relay

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.get_relay.get_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_relay_request.GetRelayRequest = {
            "relay_id": relay_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        relay_name: Optional["capo_mailmanager.types.relay_name.RelayName"] = None,
        server_name: Optional[
            "capo_mailmanager.types.relay_server_name.RelayServerName"
        ] = None,
        server_port: Optional[
            "capo_mailmanager.types.relay_server_port.RelayServerPort"
        ] = None,
        authentication: Optional[
            "capo_mailmanager.types.relay_authentication.RelayAuthentication"
        ] = None,
    ) -> "capo_mailmanager.types.update_relay_response.UpdateRelayResponse":
        """<p>Updates the attributes of an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
            relay_name: <p>The name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.update_relay_request.UpdateRelayRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.update_relay_response.UpdateRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_relay

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.update_relay.update_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_relay_request.UpdateRelayRequest = {
            "relay_id": relay_id
        }
        if relay_name is not None:
            input_["relay_name"] = relay_name
        if server_name is not None:
            input_["server_name"] = server_name
        if server_port is not None:
            input_["server_port"] = server_port
        if authentication is not None:
            input_["authentication"] = authentication

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_relay_response.DeleteRelayResponse":
        """<p>Deletes an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.delete_relay_request.DeleteRelayRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.delete_relay_response.DeleteRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_relay

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.delete_relay.delete_relay(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_relay_request.DeleteRelayRequest = {
            "relay_id": relay_id
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
        config_overrides: Optional[MailManagerClientConfig] = None,
        page_size: Optional[int] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_mailmanager.types.list_relays_response.ListRelaysResponse":
        """<p>Lists all the existing relay resources.</p>

        Args:
            page_size: <p>The number of relays to be returned in one request.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mailmanager.types.list_relays_request.ListRelaysRequest]",
        ) -> OperationResponse[
            "capo_mailmanager.types.list_relays_response.ListRelaysResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_relays

            output, http_response = (
                capo_mailmanager._operations.mail_manager_svc.list_relays.list_relays(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_relays_request.ListRelaysRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRelayResource:
    def __init__(self, service: AsyncMailManagerClient) -> None:
        self._service = service

    async def create(
        self,
        relay_name: "capo_mailmanager.types.relay_name.RelayName",
        server_name: "capo_mailmanager.types.relay_server_name.RelayServerName",
        server_port: "capo_mailmanager.types.relay_server_port.RelayServerPort",
        authentication: "capo_mailmanager.types.relay_authentication.RelayAuthentication",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        client_token: Optional[
            "capo_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_mailmanager.types.tag_list.TagList"] = None,
    ) -> "capo_mailmanager.types.create_relay_response.CreateRelayResponse":
        """<p>Creates a relay resource which can be used in rules to relay incoming emails to defined relay destinations. </p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            relay_name: <p>The unique name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>
            tags: <p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when an operation exceeds a predefined service quota or limit.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.create_relay_request.CreateRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.create_relay_response.CreateRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.create_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.create_relay.async_create_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.create_relay_request.CreateRelayRequest = {
            "relay_name": relay_name,
            "server_name": server_name,
            "server_port": server_port,
            "authentication": authentication,
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
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.get_relay_response.GetRelayResponse":
        """<p>Fetch the relay resource and it's attributes.</p>

        Args:
            relay_id: <p>A unique relay identifier.</p>

        Raises:
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.get_relay_request.GetRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.get_relay_response.GetRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.get_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.get_relay.async_get_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.get_relay_request.GetRelayRequest = {
            "relay_id": relay_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        relay_name: Optional["capo_mailmanager.types.relay_name.RelayName"] = None,
        server_name: Optional[
            "capo_mailmanager.types.relay_server_name.RelayServerName"
        ] = None,
        server_port: Optional[
            "capo_mailmanager.types.relay_server_port.RelayServerPort"
        ] = None,
        authentication: Optional[
            "capo_mailmanager.types.relay_authentication.RelayAuthentication"
        ] = None,
    ) -> "capo_mailmanager.types.update_relay_response.UpdateRelayResponse":
        """<p>Updates the attributes of an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>
            relay_name: <p>The name of the relay resource.</p>
            server_name: <p>The destination relay server address.</p>
            server_port: <p>The destination relay server port.</p>
            authentication: <p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.update_relay_request.UpdateRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.update_relay_response.UpdateRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.update_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.update_relay.async_update_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.update_relay_request.UpdateRelayRequest = {
            "relay_id": relay_id
        }
        if relay_name is not None:
            input_["relay_name"] = relay_name
        if server_name is not None:
            input_["server_name"] = server_name
        if server_port is not None:
            input_["server_port"] = server_port
        if authentication is not None:
            input_["authentication"] = authentication

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        relay_id: "capo_mailmanager.types.relay_id.RelayId",
        *,
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
    ) -> "capo_mailmanager.types.delete_relay_response.DeleteRelayResponse":
        """<p>Deletes an existing relay resource.</p>

        Args:
            relay_id: <p>The unique relay identifier.</p>

        Raises:
            capo_mailmanager.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when a requested resource is not found.</p>
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.delete_relay_request.DeleteRelayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.delete_relay_response.DeleteRelayResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.delete_relay

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.delete_relay.async_delete_relay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.delete_relay_request.DeleteRelayRequest = {
            "relay_id": relay_id
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
        config_overrides: Optional[AsyncMailManagerClientConfig] = None,
        page_size: Optional[int] = None,
        next_token: Optional[
            "capo_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_mailmanager.types.list_relays_response.ListRelaysResponse":
        """<p>Lists all the existing relay resources.</p>

        Args:
            page_size: <p>The number of relays to be returned in one request.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>

        Raises:
            capo_mailmanager.errors.validation_exception.ValidationException: <p>The request validation has failed. For details, see the accompanying error message.</p>
            capo_mailmanager.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mailmanager.types.list_relays_request.ListRelaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_mailmanager.types.list_relays_response.ListRelaysResponse"
        ]:
            import capo_mailmanager._operations.mail_manager_svc.list_relays

            (
                output,
                http_response,
            ) = await capo_mailmanager._operations.mail_manager_svc.list_relays.async_list_relays(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mailmanager.types.list_relays_request.ListRelaysRequest = {}
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
