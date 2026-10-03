from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_interconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_interconnect.types.attach_point
    import capo_interconnect.types.connection_bandwidth
    import capo_interconnect.types.connection_description
    import capo_interconnect.types.connection_id
    import capo_interconnect.types.connection_state
    import capo_interconnect.types.connection_summary
    import capo_interconnect.types.create_connection_request
    import capo_interconnect.types.create_connection_response
    import capo_interconnect.types.delete_connection_request
    import capo_interconnect.types.delete_connection_response
    import capo_interconnect.types.environment_id
    import capo_interconnect.types.get_connection_request
    import capo_interconnect.types.get_connection_response
    import capo_interconnect.types.list_connections_request
    import capo_interconnect.types.list_connections_response
    import capo_interconnect.types.max_results
    import capo_interconnect.types.next_token
    import capo_interconnect.types.provider
    import capo_interconnect.types.remote_account_identifier
    import capo_interconnect.types.tag_map
    import capo_interconnect.types.update_connection_request
    import capo_interconnect.types.update_connection_response
    from capo_interconnect._services.async_interconnect import (
        AsyncInterconnectClient,
        AsyncInterconnectClientConfig,
    )
    from capo_interconnect._services.interconnect import (
        InterconnectClient,
        InterconnectClientConfig,
    )


class ConnectionResource:
    def __init__(self, service: InterconnectClient) -> None:
        self._service = service

    def create(
        self,
        bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth",
        attach_point: "capo_interconnect.types.attach_point.AttachPoint",
        environment_id: "capo_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        remote_account: Optional[
            "capo_interconnect.types.remote_account_identifier.RemoteAccountIdentifier"
        ] = None,
        tags: Optional["capo_interconnect.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.create_connection_response.CreateConnectionResponse":
        """<p>Initiates the process to create a Connection across the specified Environment. </p> <p>The Environment dictates the specified partner and location to which the other end of the connection should attach. You can see a list of the available Environments by calling <a>ListEnvironments</a> </p> <p>The Attach Point specifies where within the AWS Network your connection will logically connect.</p> <p>After a successful call to this method, the resulting <a>Connection</a> will return an Activation Key which will need to be brought to the specific partner's portal to confirm the <a>Connection</a> on both sides. (See <a>Environment$activationPageUrl</a> for a direct link to the partner portal). </p>

        Args:
            description: <p>A description to distinguish this <a>Connection</a>.</p>
            bandwidth: <p>The desired bandwidth of the requested <a>Connection</a> </p>
            attach_point: <p>The Attach Point to which the connection should be associated."</p>
            environment_id: <p>The identifier of the <a>Environment</a> across which this <a>Connection</a> should be created.</p> <p>The available <a>Environment</a> objects can be determined using <a>ListEnvironments</a>.</p>
            remote_account: <p>Account and/or principal identifying information that can be verified by the partner of this specific Environment.</p>
            tags: <p>The tag to associate with the resulting <a>Connection</a>.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Connection on specific environment

            >>> client.create(bandwidth='1Gbps', environment_id='mce-aws-acme-1', remote_account={'identifier': 'PartnerAccountDetails'}, attach_point={'directConnectGateway': '90392BE3-219C-47FD-BBA5-03DF76D2542A'})
        """

        def _handler(
            req: "OperationRequest[capo_interconnect.types.create_connection_request.CreateConnectionRequest]",
        ) -> OperationResponse[
            "capo_interconnect.types.create_connection_response.CreateConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.create_connection

            output, http_response = (
                capo_interconnect._operations.interconnect.create_connection.create_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.create_connection_request.CreateConnectionRequest = {
            "bandwidth": bandwidth,
            "attach_point": attach_point,
            "environment_id": environment_id,
        }
        if description is not None:
            input_["description"] = description
        if remote_account is not None:
            input_["remote_account"] = remote_account
        if tags is not None:
            input_["tags"] = tags
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

    def read(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.get_connection_response.GetConnectionResponse":
        """<p>Describes the current state of a Connection resource as specified by the identifier. </p>

        Args:
            identifier: <p>The identifier of the requested <a>Connection</a> </p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get connection

            >>> client.read(identifier='mcc-abc12345')
        """

        def _handler(
            req: "OperationRequest[capo_interconnect.types.get_connection_request.GetConnectionRequest]",
        ) -> OperationResponse[
            "capo_interconnect.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.get_connection

            output, http_response = (
                capo_interconnect._operations.interconnect.get_connection.get_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.get_connection_request.GetConnectionRequest = {
            "identifier": identifier
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
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        bandwidth: Optional[
            "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.update_connection_response.UpdateConnectionResponse":
        """<p>Modifies an existing connection. Currently we support modifications to the connection's description and/or bandwidth.</p>

        Args:
            identifier: <p>The identifier of the <a>Connection</a> that should be updated.</p>
            description: <p>An updated description to apply to the <a>Connection</a> </p>
            bandwidth: <p>Request a new bandwidth size on the given <a>Connection</a>.</p> <p>Note that changes to the size may be subject to additional policy, and does require the remote partner provider to acknowledge and permit this new bandwidth size.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Connection Description

            >>> client.update(identifier='mcc-abc12345', description='Changed Description')
            Update Connection Bandwidth

            >>> client.update(identifier='mcc-abc12345', bandwidth='2Gbps')
        """

        def _handler(
            req: "OperationRequest[capo_interconnect.types.update_connection_request.UpdateConnectionRequest]",
        ) -> OperationResponse[
            "capo_interconnect.types.update_connection_response.UpdateConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.update_connection

            output, http_response = (
                capo_interconnect._operations.interconnect.update_connection.update_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.update_connection_request.UpdateConnectionRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if bandwidth is not None:
            input_["bandwidth"] = bandwidth
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

    def delete(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Deletes an existing Connection with the supplied identifier.</p> <p>This operation will also inform the remote partner of your intention to delete your connection. Note, the partner may still require you to delete to fully clean up resources, but the network connectivity provided by the <a>Connection</a> will cease to exist.</p>

        Args:
            identifier: <p>The identifier of the <a>Connection</a> to be deleted. </p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Connection

            >>> client.delete(identifier='mcc-abc12345')
        """

        def _handler(
            req: "OperationRequest[capo_interconnect.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> OperationResponse[
            "capo_interconnect.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.delete_connection

            output, http_response = (
                capo_interconnect._operations.interconnect.delete_connection.delete_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.delete_connection_request.DeleteConnectionRequest = {
            "identifier": identifier
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

    def list(
        self,
        *,
        config_overrides: Optional[InterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_interconnect.types.connection_state.ConnectionState"
        ] = None,
        environment_id: Optional[
            "capo_interconnect.types.environment_id.EnvironmentId"
        ] = None,
        provider: Optional["capo_interconnect.types.provider.Provider"] = None,
        attach_point: Optional[
            "capo_interconnect.types.attach_point.AttachPoint"
        ] = None,
    ) -> "capo_interconnect.types.list_connections_response.ListConnectionsResponse":
        """<p>Lists all connection objects to which the caller has access.</p> <p>Allows for optional filtering by the following properties:</p> <ul> <li> <p> <code>state</code> </p> </li> <li> <p> <code>environmentId</code> </p> </li> <li> <p> <code>provider</code> </p> </li> <li> <p> <code>attach point</code> </p> </li> </ul> <p>Only <a>Connection</a> objects matching all filters will be returned.</p>

        Args:
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>
            state: <p>Filter the results to only include <a>Connection</a> objects in the given <a>Connection$state</a>.</p>
            environment_id: <p>Filter the results to only include <a>Connection</a> objects on the given <a>Environment</a>.</p>
            provider: <p>Filter the results to only include <a>Connection</a> objects to the given <a>Provider</a>.</p>
            attach_point: <p>Filter results to only include <a>Connection</a> objects attached to the given <a>AttachPoint</a>.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List All Connections

            >>> client.list()
            List Connections in available state

            >>> client.list(state='available')
            List Connections on specific Environment

            >>> client.list(environment_id='mce-aws-acme-1')
        """

        def _handler(
            req: "OperationRequest[capo_interconnect.types.list_connections_request.ListConnectionsRequest]",
        ) -> OperationResponse[
            "capo_interconnect.types.list_connections_response.ListConnectionsResponse"
        ]:
            import capo_interconnect._operations.interconnect.list_connections

            output, http_response = (
                capo_interconnect._operations.interconnect.list_connections.list_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.list_connections_request.ListConnectionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if provider is not None:
            input_["provider"] = provider
        if attach_point is not None:
            input_["attach_point"] = attach_point

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConnectionResource:
    def __init__(self, service: AsyncInterconnectClient) -> None:
        self._service = service

    async def create(
        self,
        bandwidth: "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth",
        attach_point: "capo_interconnect.types.attach_point.AttachPoint",
        environment_id: "capo_interconnect.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        remote_account: Optional[
            "capo_interconnect.types.remote_account_identifier.RemoteAccountIdentifier"
        ] = None,
        tags: Optional["capo_interconnect.types.tag_map.TagMap"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.create_connection_response.CreateConnectionResponse":
        """<p>Initiates the process to create a Connection across the specified Environment. </p> <p>The Environment dictates the specified partner and location to which the other end of the connection should attach. You can see a list of the available Environments by calling <a>ListEnvironments</a> </p> <p>The Attach Point specifies where within the AWS Network your connection will logically connect.</p> <p>After a successful call to this method, the resulting <a>Connection</a> will return an Activation Key which will need to be brought to the specific partner's portal to confirm the <a>Connection</a> on both sides. (See <a>Environment$activationPageUrl</a> for a direct link to the partner portal). </p>

        Args:
            description: <p>A description to distinguish this <a>Connection</a>.</p>
            bandwidth: <p>The desired bandwidth of the requested <a>Connection</a> </p>
            attach_point: <p>The Attach Point to which the connection should be associated."</p>
            environment_id: <p>The identifier of the <a>Environment</a> across which this <a>Connection</a> should be created.</p> <p>The available <a>Environment</a> objects can be determined using <a>ListEnvironments</a>.</p>
            remote_account: <p>Account and/or principal identifying information that can be verified by the partner of this specific Environment.</p>
            tags: <p>The tag to associate with the resulting <a>Connection</a>.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Connection on specific environment

            >>> await client.create(bandwidth='1Gbps', environment_id='mce-aws-acme-1', remote_account={'identifier': 'PartnerAccountDetails'}, attach_point={'directConnectGateway': '90392BE3-219C-47FD-BBA5-03DF76D2542A'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.create_connection_request.CreateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.create_connection_response.CreateConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.create_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.create_connection_request.CreateConnectionRequest = {
            "bandwidth": bandwidth,
            "attach_point": attach_point,
            "environment_id": environment_id,
        }
        if description is not None:
            input_["description"] = description
        if remote_account is not None:
            input_["remote_account"] = remote_account
        if tags is not None:
            input_["tags"] = tags
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

    async def read(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
    ) -> "capo_interconnect.types.get_connection_response.GetConnectionResponse":
        """<p>Describes the current state of a Connection resource as specified by the identifier. </p>

        Args:
            identifier: <p>The identifier of the requested <a>Connection</a> </p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get connection

            >>> await client.read(identifier='mcc-abc12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.get_connection_request.GetConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.get_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.get_connection_request.GetConnectionRequest = {
            "identifier": identifier
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
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        description: Optional[
            "capo_interconnect.types.connection_description.ConnectionDescription"
        ] = None,
        bandwidth: Optional[
            "capo_interconnect.types.connection_bandwidth.ConnectionBandwidth"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.update_connection_response.UpdateConnectionResponse":
        """<p>Modifies an existing connection. Currently we support modifications to the connection's description and/or bandwidth.</p>

        Args:
            identifier: <p>The identifier of the <a>Connection</a> that should be updated.</p>
            description: <p>An updated description to apply to the <a>Connection</a> </p>
            bandwidth: <p>Request a new bandwidth size on the given <a>Connection</a>.</p> <p>Note that changes to the size may be subject to additional policy, and does require the remote partner provider to acknowledge and permit this new bandwidth size.</p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Connection Description

            >>> await client.update(identifier='mcc-abc12345', description='Changed Description')
            Update Connection Bandwidth

            >>> await client.update(identifier='mcc-abc12345', bandwidth='2Gbps')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.update_connection_request.UpdateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.update_connection_response.UpdateConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.update_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.update_connection_request.UpdateConnectionRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if bandwidth is not None:
            input_["bandwidth"] = bandwidth
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

    async def delete(
        self,
        identifier: "capo_interconnect.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_interconnect.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Deletes an existing Connection with the supplied identifier.</p> <p>This operation will also inform the remote partner of your intention to delete your connection. Note, the partner may still require you to delete to fully clean up resources, but the network connectivity provided by the <a>Connection</a> will cease to exist.</p>

        Args:
            identifier: <p>The identifier of the <a>Connection</a> to be deleted. </p>
            client_token: <p>Idempotency token used for the request.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Connection

            >>> await client.delete(identifier='mcc-abc12345')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import capo_interconnect._operations.interconnect.delete_connection

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.delete_connection_request.DeleteConnectionRequest = {
            "identifier": identifier
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

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncInterconnectClientConfig] = None,
        max_results: Optional["capo_interconnect.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_interconnect.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_interconnect.types.connection_state.ConnectionState"
        ] = None,
        environment_id: Optional[
            "capo_interconnect.types.environment_id.EnvironmentId"
        ] = None,
        provider: Optional["capo_interconnect.types.provider.Provider"] = None,
        attach_point: Optional[
            "capo_interconnect.types.attach_point.AttachPoint"
        ] = None,
    ) -> "capo_interconnect.types.list_connections_response.ListConnectionsResponse":
        """<p>Lists all connection objects to which the caller has access.</p> <p>Allows for optional filtering by the following properties:</p> <ul> <li> <p> <code>state</code> </p> </li> <li> <p> <code>environmentId</code> </p> </li> <li> <p> <code>provider</code> </p> </li> <li> <p> <code>attach point</code> </p> </li> </ul> <p>Only <a>Connection</a> objects matching all filters will be returned.</p>

        Args:
            max_results: <p>The max number of list results in a single paginated response.</p>
            next_token: <p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>
            state: <p>Filter the results to only include <a>Connection</a> objects in the given <a>Connection$state</a>.</p>
            environment_id: <p>Filter the results to only include <a>Connection</a> objects on the given <a>Environment</a>.</p>
            provider: <p>Filter the results to only include <a>Connection</a> objects to the given <a>Provider</a>.</p>
            attach_point: <p>Filter results to only include <a>Connection</a> objects attached to the given <a>AttachPoint</a>.</p>

        Raises:
            capo_interconnect.errors.access_denied_exception.AccessDeniedException: <p>The calling principal is not allowed to access the specified resource, or the resource does not exist.</p>
            capo_interconnect.errors.interconnect_client_exception.InterconnectClientException: <p>The request was denied due to incorrect client supplied parameters.</p>
            capo_interconnect.errors.interconnect_server_exception.InterconnectServerException: <p>The request resulted in an exception internal to the service.</p>
            capo_interconnect.errors.interconnect_validation_exception.InterconnectValidationException: <p>The input fails to satisfy the constraints specified.</p>
            capo_interconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that does not exist on the server.</p>
            capo_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation would result in the calling principal exceeding their allotted quota.</p>
            capo_interconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_interconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List All Connections

            >>> await client.list()
            List Connections in available state

            >>> await client.list(state='available')
            List Connections on specific Environment

            >>> await client.list(environment_id='mce-aws-acme-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_interconnect.types.list_connections_request.ListConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_interconnect.types.list_connections_response.ListConnectionsResponse"
        ]:
            import capo_interconnect._operations.interconnect.list_connections

            (
                output,
                http_response,
            ) = await capo_interconnect._operations.interconnect.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_interconnect.types.list_connections_request.ListConnectionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if provider is not None:
            input_["provider"] = provider
        if attach_point is not None:
            input_["attach_point"] = attach_point

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
