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
    import capo_vpc_lattice.types.create_service_network_service_association_request
    import capo_vpc_lattice.types.create_service_network_service_association_response
    import capo_vpc_lattice.types.delete_service_network_service_association_request
    import capo_vpc_lattice.types.delete_service_network_service_association_response
    import capo_vpc_lattice.types.get_service_network_service_association_request
    import capo_vpc_lattice.types.get_service_network_service_association_response
    import capo_vpc_lattice.types.list_service_network_service_associations_request
    import capo_vpc_lattice.types.list_service_network_service_associations_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.service_network_identifier
    import capo_vpc_lattice.types.service_network_service_association_identifier
    import capo_vpc_lattice.types.service_network_service_association_summary
    import capo_vpc_lattice.types.tag_map
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ServiceNetworkServiceAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse":
        """<p>Associates the specified service with the specified service network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations">Manage service associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.</p> <p>You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.</p> <p>As a result of this operation, the association is created in the service network account and the association owner account.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            tags: <p>The tags for the association.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association.create_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest = {
            "service_identifier": service_identifier,
            "service_network_identifier": service_network_identifier,
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
        service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a service.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association.get_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest = {
            "service_network_service_association_identifier": service_network_service_association_identifier
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
        service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse":
        """<p>Deletes the association between a service and a service network. This operation fails if an association is still in progress.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

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
            req: "OperationRequest[capo_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association.delete_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest = {
            "service_network_service_association_identifier": service_network_service_association_identifier
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
        service_identifier: Optional[
            "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse":
        """<p>Lists the associations between a service network and a service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.</p> <p>Every association in Amazon VPC Lattice has a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource is shared with another account, the association includes the local account ID as the prefix in the ARN.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
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
            req: "OperationRequest[capo_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations.list_service_network_service_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if service_identifier is not None:
            input_["service_identifier"] = service_identifier
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


class AsyncServiceNetworkServiceAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        service_network_identifier: "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse":
        """<p>Associates the specified service with the specified service network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations">Manage service associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.</p> <p>You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.</p> <p>As a result of this operation, the association is created in the service network account and the association owner account.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            tags: <p>The tags for the association.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association.async_create_service_network_service_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest = {
            "service_identifier": service_identifier,
            "service_network_identifier": service_network_identifier,
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
        service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a service.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association.async_get_service_network_service_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest = {
            "service_network_service_association_identifier": service_network_service_association_identifier
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
        service_network_service_association_identifier: "capo_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse":
        """<p>Deletes the association between a service and a service network. This operation fails if an association is still in progress.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association.async_delete_service_network_service_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest = {
            "service_network_service_association_identifier": service_network_service_association_identifier
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
        service_identifier: Optional[
            "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse":
        """<p>Lists the associations between a service network and a service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.</p> <p>Every association in Amazon VPC Lattice has a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource is shared with another account, the association includes the local account ID as the prefix in the ARN.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
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
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations.async_list_service_network_service_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest = {}
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if service_identifier is not None:
            input_["service_identifier"] = service_identifier
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
