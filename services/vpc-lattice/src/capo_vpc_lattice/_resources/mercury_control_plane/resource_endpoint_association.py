from __future__ import annotations

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
    import capo_vpc_lattice.types.delete_resource_endpoint_association_request
    import capo_vpc_lattice.types.delete_resource_endpoint_association_response
    import capo_vpc_lattice.types.list_resource_endpoint_associations_request
    import capo_vpc_lattice.types.list_resource_endpoint_associations_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.resource_configuration_identifier
    import capo_vpc_lattice.types.resource_endpoint_association_identifier
    import capo_vpc_lattice.types.resource_endpoint_association_summary
    import capo_vpc_lattice.types.vpc_endpoint_id
    import capo_vpc_lattice.types.vpc_endpoint_owner
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ResourceEndpointAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def delete(
        self,
        resource_endpoint_association_identifier: "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse":
        """<p>Disassociates the resource configuration from the resource VPC endpoint.</p>

        Args:
            resource_endpoint_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association.delete_resource_endpoint_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteResourceEndpointAssociation")
        )
        input_: capo_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest = {
            "resource_endpoint_association_identifier": resource_endpoint_association_identifier
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
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_endpoint_association_identifier: Optional[
            "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_owner: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse":
        """<p>Lists the associations for the specified VPC endpoint.</p>

        Args:
            resource_configuration_identifier: <p>The ID for the resource configuration associated with the VPC endpoint.</p>
            resource_endpoint_association_identifier: <p>The ID of the association.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint in the association.</p>
            vpc_endpoint_owner: <p>The owner of the VPC endpoint in the association.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations.list_resource_endpoint_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListResourceEndpointAssociations")
        )
        input_: capo_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }
        if resource_endpoint_association_identifier is not None:
            input_["resource_endpoint_association_identifier"] = (
                resource_endpoint_association_identifier
            )
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if vpc_endpoint_owner is not None:
            input_["vpc_endpoint_owner"] = vpc_endpoint_owner
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


class AsyncResourceEndpointAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def delete(
        self,
        resource_endpoint_association_identifier: "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse":
        """<p>Disassociates the resource configuration from the resource VPC endpoint.</p>

        Args:
            resource_endpoint_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_resource_endpoint_association_response.DeleteResourceEndpointAssociationResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_resource_endpoint_association.async_delete_resource_endpoint_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteResourceEndpointAssociation")
        )
        input_: capo_vpc_lattice.types.delete_resource_endpoint_association_request.DeleteResourceEndpointAssociationRequest = {
            "resource_endpoint_association_identifier": resource_endpoint_association_identifier
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
        resource_configuration_identifier: "capo_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        resource_endpoint_association_identifier: Optional[
            "capo_vpc_lattice.types.resource_endpoint_association_identifier.ResourceEndpointAssociationIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        vpc_endpoint_owner: Optional[
            "capo_vpc_lattice.types.vpc_endpoint_owner.VpcEndpointOwner"
        ] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse":
        """<p>Lists the associations for the specified VPC endpoint.</p>

        Args:
            resource_configuration_identifier: <p>The ID for the resource configuration associated with the VPC endpoint.</p>
            resource_endpoint_association_identifier: <p>The ID of the association.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint in the association.</p>
            vpc_endpoint_owner: <p>The owner of the VPC endpoint in the association.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_resource_endpoint_associations_response.ListResourceEndpointAssociationsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_resource_endpoint_associations.async_list_resource_endpoint_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListResourceEndpointAssociations")
        )
        input_: capo_vpc_lattice.types.list_resource_endpoint_associations_request.ListResourceEndpointAssociationsRequest = {
            "resource_configuration_identifier": resource_configuration_identifier
        }
        if resource_endpoint_association_identifier is not None:
            input_["resource_endpoint_association_identifier"] = (
                resource_endpoint_association_identifier
            )
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
        if vpc_endpoint_owner is not None:
            input_["vpc_endpoint_owner"] = vpc_endpoint_owner
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
