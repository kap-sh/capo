from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_service_network_resource_association_request
    import capo_vpc_lattice.types.create_service_network_resource_association_response
    import capo_vpc_lattice.types.delete_service_network_resource_association_request
    import capo_vpc_lattice.types.delete_service_network_resource_association_response
    import capo_vpc_lattice.types.get_service_network_resource_association_request
    import capo_vpc_lattice.types.get_service_network_resource_association_response
    import capo_vpc_lattice.types.list_service_network_resource_associations_request
    import capo_vpc_lattice.types.list_service_network_resource_associations_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.resource_configuration_identifier
    import capo_vpc_lattice.types.service_network_identifier
    import capo_vpc_lattice.types.service_network_identifier_without_regex
    import capo_vpc_lattice.types.service_network_resource_association_identifier
    import capo_vpc_lattice.types.service_network_resource_association_summary
    import capo_vpc_lattice.types.tag_map
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ServiceNetworkResourceAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        private_dns_enabled: Optional["capo_vpc_lattice.types.boolean.Boolean"] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_resource_association_response.CreateServiceNetworkResourceAssociationResponse":
        """<p>Associates the specified service network with the specified resource configuration. This allows the resource configuration to receive connections through the service network, including through a service network VPC endpoint.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_configuration_identifier: <p>The ID of the resource configuration to associate with the service network.</p>
            service_network_identifier: <p>The ID of the service network to associate with the resource configuration.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the service network resource association. </p>
            tags: <p>A key-value pair to associate with a resource.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.create_service_network_resource_association_request.CreateServiceNetworkResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_network_resource_association_response.CreateServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_resource_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service_network_resource_association.create_service_network_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateServiceNetworkResourceAssociation"),
        )
        input_: capo_vpc_lattice.types.create_service_network_resource_association_request.CreateServiceNetworkResourceAssociationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier,
            "service_network_identifier": service_network_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
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
        service_network_resource_association_identifier: "capo_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_resource_association_response.GetServiceNetworkResourceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a resource configuration.</p>

        Args:
            service_network_resource_association_identifier: <p>The ID of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_network_resource_association_request.GetServiceNetworkResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_network_resource_association_response.GetServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_resource_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service_network_resource_association.get_service_network_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetServiceNetworkResourceAssociation")
        )
        input_: capo_vpc_lattice.types.get_service_network_resource_association_request.GetServiceNetworkResourceAssociationRequest = {
            "service_network_resource_association_identifier": service_network_resource_association_identifier
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
        service_network_resource_association_identifier: "capo_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_resource_association_response.DeleteServiceNetworkResourceAssociationResponse":
        """<p>Deletes the association between a service network and a resource configuration.</p>

        Args:
            service_network_resource_association_identifier: <p>The ID of the association.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_network_resource_association_request.DeleteServiceNetworkResourceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_network_resource_association_response.DeleteServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_resource_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_resource_association.delete_service_network_resource_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteServiceNetworkResourceAssociation"),
        )
        input_: capo_vpc_lattice.types.delete_service_network_resource_association_request.DeleteServiceNetworkResourceAssociationRequest = {
            "service_network_resource_association_identifier": service_network_resource_association_identifier
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
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        resource_configuration_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        include_children: Optional[bool] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_resource_associations_response.ListServiceNetworkResourceAssociationsResponse":
        """<p>Lists the associations between a service network and a resource configuration.</p>

        Args:
            service_network_identifier: <p>The ID of the service network.</p>
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>
            include_children: <p>Include service network resource associations of the child resource configuration with the grouped resource configuration.</p> <p>The type is boolean and the default value is false.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_service_network_resource_associations_request.ListServiceNetworkResourceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_network_resource_associations_response.ListServiceNetworkResourceAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_resource_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_network_resource_associations.list_service_network_resource_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListServiceNetworkResourceAssociations")
        )
        input_: capo_vpc_lattice.types.list_service_network_resource_associations_request.ListServiceNetworkResourceAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if resource_configuration_identifier is not None:
            input_["resource_configuration_identifier"] = (
                resource_configuration_identifier
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_children is not None:
            input_["include_children"] = include_children

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceNetworkResourceAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier_without_regex.ServiceNetworkIdentifierWithoutRegex",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        private_dns_enabled: Optional["capo_vpc_lattice.types.boolean.Boolean"] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_resource_association_response.CreateServiceNetworkResourceAssociationResponse":
        """<p>Associates the specified service network with the specified resource configuration. This allows the resource configuration to receive connections through the service network, including through a service network VPC endpoint.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_configuration_identifier: <p>The ID of the resource configuration to associate with the service network.</p>
            service_network_identifier: <p>The ID of the service network to associate with the resource configuration.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the service network resource association. </p>
            tags: <p>A key-value pair to associate with a resource.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_service_network_resource_association_request.CreateServiceNetworkResourceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_service_network_resource_association_response.CreateServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_resource_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_service_network_resource_association.async_create_service_network_resource_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateServiceNetworkResourceAssociation"),
        )
        input_: capo_vpc_lattice.types.create_service_network_resource_association_request.CreateServiceNetworkResourceAssociationRequest = {
            "resource_configuration_identifier": resource_configuration_identifier,
            "service_network_identifier": service_network_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
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
        service_network_resource_association_identifier: "capo_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_resource_association_response.GetServiceNetworkResourceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a resource configuration.</p>

        Args:
            service_network_resource_association_identifier: <p>The ID of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_service_network_resource_association_request.GetServiceNetworkResourceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_service_network_resource_association_response.GetServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_resource_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_service_network_resource_association.async_get_service_network_resource_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetServiceNetworkResourceAssociation")
        )
        input_: capo_vpc_lattice.types.get_service_network_resource_association_request.GetServiceNetworkResourceAssociationRequest = {
            "service_network_resource_association_identifier": service_network_resource_association_identifier
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
        service_network_resource_association_identifier: "capo_vpc_lattice.types.service_network_resource_association_identifier.ServiceNetworkResourceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_resource_association_response.DeleteServiceNetworkResourceAssociationResponse":
        """<p>Deletes the association between a service network and a resource configuration.</p>

        Args:
            service_network_resource_association_identifier: <p>The ID of the association.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_service_network_resource_association_request.DeleteServiceNetworkResourceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_service_network_resource_association_response.DeleteServiceNetworkResourceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_resource_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_resource_association.async_delete_service_network_resource_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteServiceNetworkResourceAssociation"),
        )
        input_: capo_vpc_lattice.types.delete_service_network_resource_association_request.DeleteServiceNetworkResourceAssociationRequest = {
            "service_network_resource_association_identifier": service_network_resource_association_identifier
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
        service_network_identifier: Optional[
            "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        resource_configuration_identifier: Optional[
            "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
        include_children: Optional[bool] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_resource_associations_response.ListServiceNetworkResourceAssociationsResponse":
        """<p>Lists the associations between a service network and a resource configuration.</p>

        Args:
            service_network_identifier: <p>The ID of the service network.</p>
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>
            include_children: <p>Include service network resource associations of the child resource configuration with the grouped resource configuration.</p> <p>The type is boolean and the default value is false.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_service_network_resource_associations_request.ListServiceNetworkResourceAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_service_network_resource_associations_response.ListServiceNetworkResourceAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_resource_associations

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_service_network_resource_associations.async_list_service_network_resource_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListServiceNetworkResourceAssociations")
        )
        input_: capo_vpc_lattice.types.list_service_network_resource_associations_request.ListServiceNetworkResourceAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if resource_configuration_identifier is not None:
            input_["resource_configuration_identifier"] = (
                resource_configuration_identifier
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_children is not None:
            input_["include_children"] = include_children

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
