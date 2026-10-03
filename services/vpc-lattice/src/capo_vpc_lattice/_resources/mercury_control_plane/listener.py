from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_listener_request
    import capo_vpc_lattice.types.create_listener_response
    import capo_vpc_lattice.types.delete_listener_request
    import capo_vpc_lattice.types.delete_listener_response
    import capo_vpc_lattice.types.get_listener_request
    import capo_vpc_lattice.types.get_listener_response
    import capo_vpc_lattice.types.list_listeners_request
    import capo_vpc_lattice.types.list_listeners_response
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.listener_name
    import capo_vpc_lattice.types.listener_protocol
    import capo_vpc_lattice.types.listener_summary
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.port
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.update_listener_request
    import capo_vpc_lattice.types.update_listener_response
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class Listener:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        name: "capo_vpc_lattice.types.listener_name.ListenerName",
        protocol: "capo_vpc_lattice.types.listener_protocol.ListenerProtocol",
        default_action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        port: Optional["capo_vpc_lattice.types.port.Port"] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_listener_response.CreateListenerResponse":
        """<p>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html">Listeners</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            name: <p>The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            protocol: <p>The listener protocol.</p>
            port: <p>The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.</p>
            default_action: <p>The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_listener_request.CreateListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_listener_response.CreateListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_listener.create_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_listener_request.CreateListenerRequest = {
            "service_identifier": service_identifier,
            "name": name,
            "protocol": protocol,
            "default_action": default_action,
        }
        if port is not None:
            input_["port"] = port
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_listener_response.GetListenerResponse":
        """<p>Retrieves information about the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_listener_request.GetListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_listener_response.GetListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_listener.get_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_listener_request.GetListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        default_action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_listener_response.UpdateListenerResponse":
        """<p>Updates the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            default_action: <p>The action for the default rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_listener_request.UpdateListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_listener_response.UpdateListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_listener.update_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_listener_request.UpdateListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "default_action": default_action,
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_listener_response.DeleteListenerResponse":
        """<p>Deletes the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_listener_request.DeleteListenerRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_listener_response.DeleteListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_listener

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_listener.delete_listener(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_listener_request.DeleteListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_listeners_response.ListListenersResponse":
        """<p>Lists the listeners for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_listeners_request.ListListenersRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_listeners_response.ListListenersResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_listeners

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_listeners.list_listeners(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_listeners_request.ListListenersRequest = {
            "service_identifier": service_identifier
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


class AsyncListener:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        name: "capo_vpc_lattice.types.listener_name.ListenerName",
        protocol: "capo_vpc_lattice.types.listener_protocol.ListenerProtocol",
        default_action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        port: Optional["capo_vpc_lattice.types.port.Port"] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_listener_response.CreateListenerResponse":
        """<p>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html">Listeners</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            name: <p>The name of the listener. A listener name must be unique within a service. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            protocol: <p>The listener protocol.</p>
            port: <p>The listener port. You can specify a value from 1 to 65535. For HTTP, the default is 80. For HTTPS, the default is 443.</p>
            default_action: <p>The action for the default rule. Each listener has a default rule. The default rule is used if no other rules match.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_listener_request.CreateListenerRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_listener_response.CreateListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_listener

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_listener.async_create_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_listener_request.CreateListenerRequest = {
            "service_identifier": service_identifier,
            "name": name,
            "protocol": protocol,
            "default_action": default_action,
        }
        if port is not None:
            input_["port"] = port
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_listener_response.GetListenerResponse":
        """<p>Retrieves information about the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_listener_request.GetListenerRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_listener_response.GetListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_listener

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_listener.async_get_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_listener_request.GetListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        default_action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_listener_response.UpdateListenerResponse":
        """<p>Updates the specified listener for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            default_action: <p>The action for the default rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.update_listener_request.UpdateListenerRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.update_listener_response.UpdateListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_listener

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.update_listener.async_update_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_listener_request.UpdateListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "default_action": default_action,
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_listener_response.DeleteListenerResponse":
        """<p>Deletes the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_listener_request.DeleteListenerRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_listener_response.DeleteListenerResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_listener

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_listener.async_delete_listener(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_listener_request.DeleteListenerRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_listeners_response.ListListenersResponse":
        """<p>Lists the listeners for the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_listeners_request.ListListenersRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_listeners_response.ListListenersResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_listeners

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_listeners.async_list_listeners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_listeners_request.ListListenersRequest = {
            "service_identifier": service_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
