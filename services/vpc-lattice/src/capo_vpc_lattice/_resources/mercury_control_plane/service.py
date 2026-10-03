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
    import capo_vpc_lattice.types.auth_type
    import capo_vpc_lattice.types.certificate_arn
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_service_request
    import capo_vpc_lattice.types.create_service_response
    import capo_vpc_lattice.types.delete_service_request
    import capo_vpc_lattice.types.delete_service_response
    import capo_vpc_lattice.types.get_service_request
    import capo_vpc_lattice.types.get_service_response
    import capo_vpc_lattice.types.idle_timeout_seconds
    import capo_vpc_lattice.types.list_services_request
    import capo_vpc_lattice.types.list_services_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.service_custom_domain_name
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.service_name
    import capo_vpc_lattice.types.service_summary
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.update_service_request
    import capo_vpc_lattice.types.update_service_response
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class Service:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_vpc_lattice.types.service_name.ServiceName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
        custom_domain_name: Optional[
            "capo_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
        ] = None,
        certificate_arn: Optional[
            "capo_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        idle_timeout_seconds: Optional[
            "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
        ] = None,
    ) -> "capo_vpc_lattice.types.create_service_response.CreateServiceResponse":
        """<p>Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html">Services</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            tags: <p>The tags for the service.</p>
            custom_domain_name: <p>The custom domain name of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            idle_timeout_seconds: <p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_request.CreateServiceRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if idle_timeout_seconds is not None:
            input_["idle_timeout_seconds"] = idle_timeout_seconds

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
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_response.GetServiceResponse":
        """<p>Retrieves information about the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_response.GetServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_request.GetServiceRequest = {
            "service_identifier": service_identifier
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
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        certificate_arn: Optional[
            "capo_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        idle_timeout_seconds: Optional[
            "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_service_response.UpdateServiceResponse":
        """<p>Updates the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            idle_timeout_seconds: <p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_service_request.UpdateServiceRequest = {
            "service_identifier": service_identifier
        }
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if idle_timeout_seconds is not None:
            input_["idle_timeout_seconds"] = idle_timeout_seconds

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
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a service. A service can't be deleted if it's associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service">Delete a service</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_request.DeleteServiceRequest = {
            "service_identifier": service_identifier
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
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_services_response.ListServicesResponse":
        """<p>Lists the services owned by the caller account or shared with the caller account.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_services_response.ListServicesResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_services

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_services_request.ListServicesRequest = {}
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


class AsyncService:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_vpc_lattice.types.service_name.ServiceName",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
        custom_domain_name: Optional[
            "capo_vpc_lattice.types.service_custom_domain_name.ServiceCustomDomainName"
        ] = None,
        certificate_arn: Optional[
            "capo_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        idle_timeout_seconds: Optional[
            "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
        ] = None,
    ) -> "capo_vpc_lattice.types.create_service_response.CreateServiceResponse":
        """<p>Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html">Services</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            tags: <p>The tags for the service.</p>
            custom_domain_name: <p>The custom domain name of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            idle_timeout_seconds: <p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_service_request.CreateServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_service.async_create_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_request.CreateServiceRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if idle_timeout_seconds is not None:
            input_["idle_timeout_seconds"] = idle_timeout_seconds

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
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_response.GetServiceResponse":
        """<p>Retrieves information about the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_service_request.GetServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_service_response.GetServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_request.GetServiceRequest = {
            "service_identifier": service_identifier
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
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        certificate_arn: Optional[
            "capo_vpc_lattice.types.certificate_arn.CertificateArn"
        ] = None,
        auth_type: Optional["capo_vpc_lattice.types.auth_type.AuthType"] = None,
        idle_timeout_seconds: Optional[
            "capo_vpc_lattice.types.idle_timeout_seconds.IdleTimeoutSeconds"
        ] = None,
    ) -> "capo_vpc_lattice.types.update_service_response.UpdateServiceResponse":
        """<p>Updates the specified service.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>
            auth_type: <p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>
            idle_timeout_seconds: <p>The amount of time, in seconds, that a connection can remain idle (no data sent) before VPC Lattice closes it. The valid range is 60 to 600 seconds. If you don't specify a value, the default is 60 seconds. This setting does not change the maximum connection duration of 10 minutes; connections are still closed when they reach that limit.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.update_service_request.UpdateServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_service

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.update_service.async_update_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_service_request.UpdateServiceRequest = {
            "service_identifier": service_identifier
        }
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if idle_timeout_seconds is not None:
            input_["idle_timeout_seconds"] = idle_timeout_seconds

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
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a service. A service can't be deleted if it's associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service">Delete a service</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_service_request.DeleteServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_service.async_delete_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_request.DeleteServiceRequest = {
            "service_identifier": service_identifier
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
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_services_response.ListServicesResponse":
        """<p>Lists the services owned by the caller account or shared with the caller account.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_services_request.ListServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_services_response.ListServicesResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_services

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_services_request.ListServicesRequest = {}
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
