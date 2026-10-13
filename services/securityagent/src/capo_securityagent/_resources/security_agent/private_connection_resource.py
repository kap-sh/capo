from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_securityagent._auth._signers
import capo_securityagent._auth._sigv4
from capo_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_securityagent.types.certificate_chain
    import capo_securityagent.types.create_private_connection_input
    import capo_securityagent.types.create_private_connection_output
    import capo_securityagent.types.delete_private_connection_input
    import capo_securityagent.types.delete_private_connection_output
    import capo_securityagent.types.describe_private_connection_input
    import capo_securityagent.types.describe_private_connection_output
    import capo_securityagent.types.list_private_connections_input
    import capo_securityagent.types.list_private_connections_output
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.private_connection_mode
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.private_connection_summary
    import capo_securityagent.types.tag_map
    import capo_securityagent.types.update_private_connection_certificate_input
    import capo_securityagent.types.update_private_connection_certificate_output
    from capo_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from capo_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class PrivateConnectionResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def read(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves the details of a private connection.</p>

        Args:
            private_connection_name: <p>The name of the private connection to describe.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.describe_private_connection

            output, http_response = (
                capo_securityagent._operations.security_agent.describe_private_connection.describe_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribePrivateConnection")
        )
        input_: capo_securityagent.types.describe_private_connection_input.DescribePrivateConnectionInput = {
            "private_connection_name": private_connection_name
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
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a private connection.</p>

        Args:
            private_connection_name: <p>The name of the private connection to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_private_connection

            output, http_response = (
                capo_securityagent._operations.security_agent.delete_private_connection.delete_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePrivateConnection")
        )
        input_: capo_securityagent.types.delete_private_connection_input.DeletePrivateConnectionInput = {
            "private_connection_name": private_connection_name
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
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists the private connections in your account.</p>

        Args:
            max_results: <p>The maximum number of private connections to return in a single response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_private_connections

            output, http_response = (
                capo_securityagent._operations.security_agent.list_private_connections.list_private_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPrivateConnections")
        )
        input_: capo_securityagent.types.list_private_connections_input.ListPrivateConnectionsInput = {}
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

    def create_private_connection(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        mode: "capo_securityagent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a private connection for reaching a self-hosted provider instance over private networking using Amazon VPC Lattice.</p>

        Args:
            private_connection_name: <p>A unique name for the private connection within your account.</p>
            mode: <p>The configuration for the private connection. Specify either a service-managed or a self-managed mode.</p>
            tags: <p>The tags to attach to the private connection.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_private_connection

            output, http_response = (
                capo_securityagent._operations.security_agent.create_private_connection.create_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput",
        ) -> dict[str, Any]:
            import capo_securityagent.types.create_private_connection_input

            return capo_securityagent.types.create_private_connection_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePrivateConnection", redact_input=_redact_input),
        )
        input_: capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput = {
            "private_connection_name": private_connection_name,
            "mode": mode,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_private_connection_certificate(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        certificate: "capo_securityagent.types.certificate_chain.CertificateChain",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a private connection. Certificates can be added or replaced but not removed.</p>

        Args:
            private_connection_name: <p>The name of the private connection to update.</p>
            certificate: <p>The PEM-encoded certificate chain for the private connection.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_private_connection_certificate

            output, http_response = (
                capo_securityagent._operations.security_agent.update_private_connection_certificate.update_private_connection_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput",
        ) -> dict[str, Any]:
            import capo_securityagent.types.update_private_connection_certificate_input

            return capo_securityagent.types.update_private_connection_certificate_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePrivateConnectionCertificate", redact_input=_redact_input
            ),
        )
        input_: capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {
            "private_connection_name": private_connection_name,
            "certificate": certificate,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPrivateConnectionResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def read(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves the details of a private connection.</p>

        Args:
            private_connection_name: <p>The name of the private connection to describe.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.describe_private_connection

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.describe_private_connection.async_describe_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribePrivateConnection")
        )
        input_: capo_securityagent.types.describe_private_connection_input.DescribePrivateConnectionInput = {
            "private_connection_name": private_connection_name
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
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a private connection.</p>

        Args:
            private_connection_name: <p>The name of the private connection to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_private_connection

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_private_connection.async_delete_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePrivateConnection")
        )
        input_: capo_securityagent.types.delete_private_connection_input.DeletePrivateConnectionInput = {
            "private_connection_name": private_connection_name
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
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
    ) -> "capo_securityagent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists the private connections in your account.</p>

        Args:
            max_results: <p>The maximum number of private connections to return in a single response.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_private_connections

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_private_connections.async_list_private_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPrivateConnections")
        )
        input_: capo_securityagent.types.list_private_connections_input.ListPrivateConnectionsInput = {}
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

    async def create_private_connection(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        mode: "capo_securityagent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> "capo_securityagent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a private connection for reaching a self-hosted provider instance over private networking using Amazon VPC Lattice.</p>

        Args:
            private_connection_name: <p>A unique name for the private connection within your account.</p>
            mode: <p>The configuration for the private connection. Specify either a service-managed or a self-managed mode.</p>
            tags: <p>The tags to attach to the private connection.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_private_connection

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_private_connection.async_create_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput",
        ) -> dict[str, Any]:
            import capo_securityagent.types.create_private_connection_input

            return capo_securityagent.types.create_private_connection_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePrivateConnection", redact_input=_redact_input),
        )
        input_: capo_securityagent.types.create_private_connection_input.CreatePrivateConnectionInput = {
            "private_connection_name": private_connection_name,
            "mode": mode,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_private_connection_certificate(
        self,
        private_connection_name: "capo_securityagent.types.private_connection_name.PrivateConnectionName",
        certificate: "capo_securityagent.types.certificate_chain.CertificateChain",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a private connection. Certificates can be added or replaced but not removed.</p>

        Args:
            private_connection_name: <p>The name of the private connection to update.</p>
            certificate: <p>The PEM-encoded certificate chain for the private connection.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_private_connection_certificate

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_private_connection_certificate.async_update_private_connection_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput",
        ) -> dict[str, Any]:
            import capo_securityagent.types.update_private_connection_certificate_input

            return capo_securityagent.types.update_private_connection_certificate_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePrivateConnectionCertificate", redact_input=_redact_input
            ),
        )
        input_: capo_securityagent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {
            "private_connection_name": private_connection_name,
            "certificate": certificate,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
