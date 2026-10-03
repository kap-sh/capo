from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_rtbfabric._auth._signers
import capo_rtbfabric._auth._sigv4
from capo_rtbfabric._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_rtbfabric.types.create_requester_gateway_request
    import capo_rtbfabric.types.create_requester_gateway_response
    import capo_rtbfabric.types.delete_requester_gateway_request
    import capo_rtbfabric.types.delete_requester_gateway_response
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.get_requester_gateway_request
    import capo_rtbfabric.types.get_requester_gateway_response
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.update_requester_gateway_request
    import capo_rtbfabric.types.update_requester_gateway_response
    import capo_rtbfabric.types.vpc_id
    from capo_rtbfabric._services.async_rtb_fabric import (
        AsyncRTBFabricClient,
        AsyncRTBFabricClientConfig,
    )
    from capo_rtbfabric._services.rtb_fabric import (
        RTBFabricClient,
        RTBFabricClientConfig,
    )


class RequesterGateway:
    def __init__(self, service: RTBFabricClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "capo_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        client_token: str,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "capo_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse":
        """<p>Creates a requester gateway.</p>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            description: <p>An optional description for the requester gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a requester gateway
            Create requester gateway

            >>> client.create(description='My requester gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_requester_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.create_requester_gateway.create_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
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
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse":
        """<p>Retrieves information about a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get requester gateway details
            Get requester gateway

            >>> client.read(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_requester_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.get_requester_gateway.get_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest = {
            "gateway_id": gateway_id
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
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse":
        """<p>Deletes a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a requester gateway
            Delete requester gateway

            >>> client.delete(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_requester_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.delete_requester_gateway.delete_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_requester_gateway(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        description: Optional[str] = None,
    ) -> "capo_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse":
        """<p>Updates a requester gateway.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the requester gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update requester gateway
            Update requester gateway

            >>> client.update_requester_gateway(gateway_id='rtb-gw-12345678', description='Updated requester gateway description', client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_requester_gateway

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.update_requester_gateway.update_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRequesterGateway:
    def __init__(self, service: AsyncRTBFabricClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "capo_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "capo_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse":
        """<p>Creates a requester gateway.</p>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            description: <p>An optional description for the requester gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a requester gateway
            Create requester gateway

            >>> await client.create(description='My requester gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_requester_gateway.async_create_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
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
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse":
        """<p>Retrieves information about a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get requester gateway details
            Get requester gateway

            >>> await client.read(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_requester_gateway.async_get_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest = {
            "gateway_id": gateway_id
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
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse":
        """<p>Deletes a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a requester gateway
            Delete requester gateway

            >>> await client.delete(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_requester_gateway.async_delete_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_requester_gateway(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        description: Optional[str] = None,
    ) -> "capo_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse":
        """<p>Updates a requester gateway.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the requester gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update requester gateway
            Update requester gateway

            >>> await client.update_requester_gateway(gateway_id='rtb-gw-12345678', description='Updated requester gateway description', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_requester_gateway.async_update_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
