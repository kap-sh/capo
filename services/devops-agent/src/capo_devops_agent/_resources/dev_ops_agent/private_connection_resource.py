from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_devops_agent._auth._signers
import capo_devops_agent._auth._sigv4
from capo_devops_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_devops_agent.types.certificate_string
    import capo_devops_agent.types.create_private_connection_input
    import capo_devops_agent.types.create_private_connection_output
    import capo_devops_agent.types.delete_private_connection_input
    import capo_devops_agent.types.delete_private_connection_output
    import capo_devops_agent.types.describe_private_connection_input
    import capo_devops_agent.types.describe_private_connection_output
    import capo_devops_agent.types.list_private_connections_input
    import capo_devops_agent.types.list_private_connections_output
    import capo_devops_agent.types.private_connection_mode
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.tags
    import capo_devops_agent.types.update_private_connection_certificate_input
    import capo_devops_agent.types.update_private_connection_certificate_output
    from capo_devops_agent._services.async_dev_ops_agent import (
        AsyncDevOpsAgentClient,
        AsyncDevOpsAgentClientConfig,
    )
    from capo_devops_agent._services.dev_ops_agent import (
        DevOpsAgentClient,
        DevOpsAgentClientConfig,
    )


class PrivateConnectionResource:
    def __init__(self, service: DevOpsAgentClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        mode: "capo_devops_agent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a Private Connection to a target resource.</p>

        Args:
            name: <p>Unique name for this Private Connection within the account.</p>
            mode: <p>Private Connection mode configuration.</p>
            tags: <p>Tags to add to the Private Connection at creation time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_private_connection

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.create_private_connection.create_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePrivateConnection")
        )
        input_: capo_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput = {
            "name": name,
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

    def read(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves details of an existing Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.describe_private_connection

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.describe_private_connection.describe_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribePrivateConnection")
        )
        input_: capo_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput = {
            "name": name
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
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a Private Connection. The deletion is asynchronous and returns DELETE_IN_PROGRESS status.</p>

        Args:
            name: <p>The name of the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_private_connection

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.delete_private_connection.delete_private_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePrivateConnection")
        )
        input_: capo_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self, *, config_overrides: Optional[DevOpsAgentClientConfig] = None
    ) -> "capo_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists all Private Connections in the caller's account.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_private_connections

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.list_private_connections.list_private_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPrivateConnections")
        )
        input_: capo_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_private_connection_certificate(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        certificate: "capo_devops_agent.types.certificate_string.CertificateString",
        *,
        config_overrides: Optional[DevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
            certificate: <p>The new certificate for the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> OperationResponse[
            "capo_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_private_connection_certificate

            output, http_response = (
                capo_devops_agent._operations.dev_ops_agent.update_private_connection_certificate.update_private_connection_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePrivateConnectionCertificate")
        )
        input_: capo_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {
            "name": name,
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
    def __init__(self, service: AsyncDevOpsAgentClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        mode: "capo_devops_agent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a Private Connection to a target resource.</p>

        Args:
            name: <p>Unique name for this Private Connection within the account.</p>
            mode: <p>Private Connection mode configuration.</p>
            tags: <p>Tags to add to the Private Connection at creation time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_private_connection

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_private_connection.async_create_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePrivateConnection")
        )
        input_: capo_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput = {
            "name": name,
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

    async def read(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves details of an existing Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.describe_private_connection

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.describe_private_connection.async_describe_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribePrivateConnection")
        )
        input_: capo_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput = {
            "name": name
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
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a Private Connection. The deletion is asynchronous and returns DELETE_IN_PROGRESS status.</p>

        Args:
            name: <p>The name of the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_private_connection

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.delete_private_connection.async_delete_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePrivateConnection")
        )
        input_: capo_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self, *, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> "capo_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists all Private Connections in the caller's account.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_private_connections

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_private_connections.async_list_private_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPrivateConnections")
        )
        input_: capo_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_private_connection_certificate(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        certificate: "capo_devops_agent.types.certificate_string.CertificateString",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
            certificate: <p>The new certificate for the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_private_connection_certificate

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_private_connection_certificate.async_update_private_connection_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePrivateConnectionCertificate")
        )
        input_: capo_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {
            "name": name,
            "certificate": certificate,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
