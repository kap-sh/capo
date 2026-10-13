from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_odb.types.create_odb_peering_connection_input
    import capo_odb.types.create_odb_peering_connection_output
    import capo_odb.types.delete_odb_peering_connection_input
    import capo_odb.types.delete_odb_peering_connection_output
    import capo_odb.types.general_input_string
    import capo_odb.types.get_odb_peering_connection_input
    import capo_odb.types.get_odb_peering_connection_output
    import capo_odb.types.list_odb_peering_connections_input
    import capo_odb.types.list_odb_peering_connections_output
    import capo_odb.types.odb_peering_connection_summary
    import capo_odb.types.peer_network_route_table_id_list
    import capo_odb.types.peered_cidr_list
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.update_odb_peering_connection_input
    import capo_odb.types.update_odb_peering_connection_output
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class OdbPeeringConnectionResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        peer_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peer_network_cidrs_to_be_added: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
        peer_network_route_table_ids: Optional[
            "capo_odb.types.peer_network_route_table_id_list.PeerNetworkRouteTableIdList"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_odb_peering_connection_output.CreateOdbPeeringConnectionOutput":
        """<p>Creates a peering connection between an ODB network and a VPC.</p> <p>A peering connection enables private connectivity between the networks for application-tier communication.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network that initiates the peering connection.</p>
            peer_network_id: <p>The unique identifier of the peer network. This can be either a VPC ID or another ODB network ID.</p>
            display_name: <p>The display name for the ODB peering connection.</p>
            peer_network_cidrs_to_be_added: <p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>
            peer_network_route_table_ids: <p>The unique identifier of the VPC route table for which a route to the ODB network is automatically created during peering connection establishment.</p>
            client_token: <p>The client token for the ODB peering connection request.</p> <p>Constraints:</p> <ul> <li> <p>Must be unique for each request.</p> </li> </ul>
            tags: <p>The tags to assign to the ODB peering connection.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.create_odb_peering_connection_input.CreateOdbPeeringConnectionInput]",
        ) -> OperationResponse[
            "capo_odb.types.create_odb_peering_connection_output.CreateOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.create_odb_peering_connection

            output, http_response = (
                capo_odb._operations.odb.create_odb_peering_connection.create_odb_peering_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateOdbPeeringConnection")
        )
        input_: capo_odb.types.create_odb_peering_connection_input.CreateOdbPeeringConnectionInput = {
            "odb_network_id": odb_network_id,
            "peer_network_id": peer_network_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peer_network_cidrs_to_be_added is not None:
            input_["peer_network_cidrs_to_be_added"] = peer_network_cidrs_to_be_added
        if peer_network_route_table_ids is not None:
            input_["peer_network_route_table_ids"] = peer_network_route_table_ids
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
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> (
        "capo_odb.types.get_odb_peering_connection_output.GetOdbPeeringConnectionOutput"
    ):
        """<p>Retrieves information about an ODB peering connection.</p>

        Args:
            odb_peering_connection_id: <p>The unique identifier of the ODB peering connection to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_odb_peering_connection_input.GetOdbPeeringConnectionInput]",
        ) -> OperationResponse[
            "capo_odb.types.get_odb_peering_connection_output.GetOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.get_odb_peering_connection

            output, http_response = (
                capo_odb._operations.odb.get_odb_peering_connection.get_odb_peering_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetOdbPeeringConnection")
        )
        input_: capo_odb.types.get_odb_peering_connection_input.GetOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
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
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peer_network_cidrs_to_be_added: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
        peer_network_cidrs_to_be_removed: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
    ) -> "capo_odb.types.update_odb_peering_connection_output.UpdateOdbPeeringConnectionOutput":
        """<p>Modifies the settings of an Oracle Database@Amazon Web Services peering connection. You can update the display name and add or remove CIDR blocks from the peering connection.</p>

        Args:
            odb_peering_connection_id: <p>The identifier of the Oracle Database@Amazon Web Services peering connection to update.</p>
            display_name: <p>A new display name for the peering connection.</p>
            peer_network_cidrs_to_be_added: <p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection. The CIDR blocks must not overlap with existing CIDR blocks in the Oracle Database@Amazon Web Services network.</p>
            peer_network_cidrs_to_be_removed: <p>A list of CIDR blocks to remove from the peering connection. The CIDR blocks must currently exist in the peering connection.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.update_odb_peering_connection_input.UpdateOdbPeeringConnectionInput]",
        ) -> OperationResponse[
            "capo_odb.types.update_odb_peering_connection_output.UpdateOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.update_odb_peering_connection

            output, http_response = (
                capo_odb._operations.odb.update_odb_peering_connection.update_odb_peering_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateOdbPeeringConnection")
        )
        input_: capo_odb.types.update_odb_peering_connection_input.UpdateOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peer_network_cidrs_to_be_added is not None:
            input_["peer_network_cidrs_to_be_added"] = peer_network_cidrs_to_be_added
        if peer_network_cidrs_to_be_removed is not None:
            input_["peer_network_cidrs_to_be_removed"] = (
                peer_network_cidrs_to_be_removed
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "capo_odb.types.delete_odb_peering_connection_output.DeleteOdbPeeringConnectionOutput":
        """<p>Deletes an ODB peering connection.</p> <p>When you delete an ODB peering connection, the underlying VPC peering connection is also deleted.</p>

        Args:
            odb_peering_connection_id: <p>The unique identifier of the ODB peering connection to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.delete_odb_peering_connection_input.DeleteOdbPeeringConnectionInput]",
        ) -> OperationResponse[
            "capo_odb.types.delete_odb_peering_connection_output.DeleteOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.delete_odb_peering_connection

            output, http_response = (
                capo_odb._operations.odb.delete_odb_peering_connection.delete_odb_peering_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteOdbPeeringConnection")
        )
        input_: capo_odb.types.delete_odb_peering_connection_input.DeleteOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
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
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_odb_peering_connections_output.ListOdbPeeringConnectionsOutput":
        """<p>Lists all ODB peering connections or those associated with a specific ODB network.</p>

        Args:
            max_results: <p>The maximum number of ODB peering connections to return in the response.</p> <p>Default: <code>20</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be between 1 and 100.</p> </li> </ul>
            next_token: <p>The pagination token for the next page of ODB peering connections.</p>
            odb_network_id: <p>The identifier of the ODB network to list peering connections for.</p> <p>If not specified, lists all ODB peering connections in the account.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_odb_peering_connections_input.ListOdbPeeringConnectionsInput]",
        ) -> OperationResponse[
            "capo_odb.types.list_odb_peering_connections_output.ListOdbPeeringConnectionsOutput"
        ]:
            import capo_odb._operations.odb.list_odb_peering_connections

            output, http_response = (
                capo_odb._operations.odb.list_odb_peering_connections.list_odb_peering_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOdbPeeringConnections")
        )
        input_: capo_odb.types.list_odb_peering_connections_input.ListOdbPeeringConnectionsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if odb_network_id is not None:
            input_["odb_network_id"] = odb_network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncOdbPeeringConnectionResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        peer_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peer_network_cidrs_to_be_added: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
        peer_network_route_table_ids: Optional[
            "capo_odb.types.peer_network_route_table_id_list.PeerNetworkRouteTableIdList"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_odb_peering_connection_output.CreateOdbPeeringConnectionOutput":
        """<p>Creates a peering connection between an ODB network and a VPC.</p> <p>A peering connection enables private connectivity between the networks for application-tier communication.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network that initiates the peering connection.</p>
            peer_network_id: <p>The unique identifier of the peer network. This can be either a VPC ID or another ODB network ID.</p>
            display_name: <p>The display name for the ODB peering connection.</p>
            peer_network_cidrs_to_be_added: <p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>
            peer_network_route_table_ids: <p>The unique identifier of the VPC route table for which a route to the ODB network is automatically created during peering connection establishment.</p>
            client_token: <p>The client token for the ODB peering connection request.</p> <p>Constraints:</p> <ul> <li> <p>Must be unique for each request.</p> </li> </ul>
            tags: <p>The tags to assign to the ODB peering connection.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_odb_peering_connection_input.CreateOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_odb_peering_connection_output.CreateOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.create_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_odb_peering_connection.async_create_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateOdbPeeringConnection")
        )
        input_: capo_odb.types.create_odb_peering_connection_input.CreateOdbPeeringConnectionInput = {
            "odb_network_id": odb_network_id,
            "peer_network_id": peer_network_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peer_network_cidrs_to_be_added is not None:
            input_["peer_network_cidrs_to_be_added"] = peer_network_cidrs_to_be_added
        if peer_network_route_table_ids is not None:
            input_["peer_network_route_table_ids"] = peer_network_route_table_ids
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
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> (
        "capo_odb.types.get_odb_peering_connection_output.GetOdbPeeringConnectionOutput"
    ):
        """<p>Retrieves information about an ODB peering connection.</p>

        Args:
            odb_peering_connection_id: <p>The unique identifier of the ODB peering connection to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_odb_peering_connection_input.GetOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_odb_peering_connection_output.GetOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.get_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_odb_peering_connection.async_get_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetOdbPeeringConnection")
        )
        input_: capo_odb.types.get_odb_peering_connection_input.GetOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
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
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peer_network_cidrs_to_be_added: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
        peer_network_cidrs_to_be_removed: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
    ) -> "capo_odb.types.update_odb_peering_connection_output.UpdateOdbPeeringConnectionOutput":
        """<p>Modifies the settings of an Oracle Database@Amazon Web Services peering connection. You can update the display name and add or remove CIDR blocks from the peering connection.</p>

        Args:
            odb_peering_connection_id: <p>The identifier of the Oracle Database@Amazon Web Services peering connection to update.</p>
            display_name: <p>A new display name for the peering connection.</p>
            peer_network_cidrs_to_be_added: <p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection. The CIDR blocks must not overlap with existing CIDR blocks in the Oracle Database@Amazon Web Services network.</p>
            peer_network_cidrs_to_be_removed: <p>A list of CIDR blocks to remove from the peering connection. The CIDR blocks must currently exist in the peering connection.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_odb_peering_connection_input.UpdateOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_odb_peering_connection_output.UpdateOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.update_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_odb_peering_connection.async_update_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateOdbPeeringConnection")
        )
        input_: capo_odb.types.update_odb_peering_connection_input.UpdateOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peer_network_cidrs_to_be_added is not None:
            input_["peer_network_cidrs_to_be_added"] = peer_network_cidrs_to_be_added
        if peer_network_cidrs_to_be_removed is not None:
            input_["peer_network_cidrs_to_be_removed"] = (
                peer_network_cidrs_to_be_removed
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_odb_peering_connection_output.DeleteOdbPeeringConnectionOutput":
        """<p>Deletes an ODB peering connection.</p> <p>When you delete an ODB peering connection, the underlying VPC peering connection is also deleted.</p>

        Args:
            odb_peering_connection_id: <p>The unique identifier of the ODB peering connection to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_odb_peering_connection_input.DeleteOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_odb_peering_connection_output.DeleteOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.delete_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_odb_peering_connection.async_delete_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteOdbPeeringConnection")
        )
        input_: capo_odb.types.delete_odb_peering_connection_input.DeleteOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
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
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_odb_peering_connections_output.ListOdbPeeringConnectionsOutput":
        """<p>Lists all ODB peering connections or those associated with a specific ODB network.</p>

        Args:
            max_results: <p>The maximum number of ODB peering connections to return in the response.</p> <p>Default: <code>20</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be between 1 and 100.</p> </li> </ul>
            next_token: <p>The pagination token for the next page of ODB peering connections.</p>
            odb_network_id: <p>The identifier of the ODB network to list peering connections for.</p> <p>If not specified, lists all ODB peering connections in the account.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_odb_peering_connections_input.ListOdbPeeringConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_odb_peering_connections_output.ListOdbPeeringConnectionsOutput"
        ]:
            import capo_odb._operations.odb.list_odb_peering_connections

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_odb_peering_connections.async_list_odb_peering_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOdbPeeringConnections")
        )
        input_: capo_odb.types.list_odb_peering_connections_input.ListOdbPeeringConnectionsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if odb_network_id is not None:
            input_["odb_network_id"] = odb_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
