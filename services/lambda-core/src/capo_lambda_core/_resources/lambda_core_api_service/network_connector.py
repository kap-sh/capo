from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_lambda_core._auth._signers
import capo_lambda_core._auth._sigv4
from capo_lambda_core._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda_core.types.client_token_string
    import capo_lambda_core.types.create_network_connector_request
    import capo_lambda_core.types.create_network_connector_response
    import capo_lambda_core.types.delete_network_connector_request
    import capo_lambda_core.types.delete_network_connector_response
    import capo_lambda_core.types.get_network_connector_request
    import capo_lambda_core.types.get_network_connector_response
    import capo_lambda_core.types.list_network_connectors_request
    import capo_lambda_core.types.list_network_connectors_response
    import capo_lambda_core.types.max_hundred_list_items
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_identifier
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_role_arn
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.network_connector_summary
    import capo_lambda_core.types.network_connector_tags
    import capo_lambda_core.types.string
    import capo_lambda_core.types.update_network_connector_request
    import capo_lambda_core.types.update_network_connector_response
    from capo_lambda_core._services.async_lambda_core import (
        AsyncLambdaCoreClient,
        AsyncLambdaCoreClientConfig,
    )
    from capo_lambda_core._services.lambda_core import (
        LambdaCoreClient,
        LambdaCoreClientConfig,
    )


class NetworkConnector:
    def __init__(self, service: LambdaCoreClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName",
        configuration: "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
        operator_role: Optional[
            "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
        ] = None,
        client_token: Optional[
            "capo_lambda_core.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional[
            "capo_lambda_core.types.network_connector_tags.NetworkConnectorTags"
        ] = None,
    ) -> "capo_lambda_core.types.create_network_connector_response.CreateNetworkConnectorResponse":
        """<p>Creates a network connector that enables Lambda compute resources to route outbound traffic through your Amazon VPC. The network connector provisions elastic network interfaces (ENIs) in the subnets you specify, providing a managed network path to private resources such as databases, caches, and internal APIs.</p> <p>This operation is asynchronous. The network connector starts in <code>PENDING</code> state while ENIs are provisioned in your VPC (provisioning typically takes up to 10 minutes). Use <code>GetNetworkConnector</code> to poll the connector state until it reaches <code>ACTIVE</code>. Once active, you can attach the connector to Lambda MicroVMs at run time using the <code>egressNetworkConnectors</code> parameter on <code>RunMicroVm</code>.</p> <p>This operation is idempotent when you provide a <code>ClientToken</code> — if you retry a request that completed successfully using the same client token, the operation returns the existing connector without creating a duplicate.</p>

        Args:
            name: <p>A unique name for the network connector within your account and Region. You can use the name to identify the connector in subsequent API calls.</p>
            configuration: <p>The network configuration for the connector. Specify a <code>VpcEgressConfiguration</code> to enable outbound traffic routing through your VPC.</p>
            operator_role: <p>The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This role must have permissions for <code>ec2:CreateNetworkInterface</code>, <code>ec2:DeleteNetworkInterface</code>, and related describe operations.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the API returns the existing connector without creating a duplicate.</p>
            tags: <p>A map of key-value pairs to associate with the network connector for organization, cost allocation, or access control.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.network_connector_limit_exceeded_exception.NetworkConnectorLimitExceededException: <p>The account has reached the maximum number of network connectors allowed. Delete unused connectors or request a limit increase through Service Quotas.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in <code>ACTIVE</code> state.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.create_network_connector_request.CreateNetworkConnectorRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.create_network_connector_response.CreateNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_network_connector

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.create_network_connector.create_network_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.create_network_connector_request.CreateNetworkConnectorRequest = {
            "name": name,
            "configuration": configuration,
        }
        if operator_role is not None:
            input_["operator_role"] = operator_role
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
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.get_network_connector_response.GetNetworkConnectorResponse":
        """<p>Retrieves the current configuration, state, and metadata of a network connector. The <code>Identifier</code> parameter accepts the connector ID, name, or full ARN. Use this operation to poll connector state after creation or update, or to inspect the current VPC configuration and any failure reasons.</p> <p>The response includes the full connector configuration, current state, and — if the connector has been updated — the <code>LastUpdateStatus</code> and <code>LastUpdateStatusReasonCode</code> fields that indicate whether the most recent update succeeded or failed.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.get_network_connector_request.GetNetworkConnectorRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.get_network_connector_response.GetNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_network_connector

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.get_network_connector.get_network_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.get_network_connector_request.GetNetworkConnectorRequest = {
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
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
        configuration: Optional[
            "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
        ] = None,
        operator_role: Optional[
            "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
        ] = None,
        client_token: Optional[
            "capo_lambda_core.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_lambda_core.types.update_network_connector_response.UpdateNetworkConnectorResponse":
        """<p>Updates the VPC configuration or operator role of an existing network connector. You can modify the subnet IDs, security group IDs, network protocol, or operator role. The connector must be in <code>ACTIVE</code> state to accept updates.</p> <p>This operation is asynchronous. The connector remains in <code>ACTIVE</code> state during the update — existing workloads that reference this connector are not disrupted. Use <code>GetNetworkConnector</code> to monitor the <code>LastUpdateStatus</code> field, which transitions through <code>InProgress</code> to <code>Successful</code> or <code>Failed</code>. If the update fails, the <code>LastUpdateStatusReasonCode</code> field provides a specific error code for troubleshooting. This operation is idempotent when you provide a <code>ClientToken</code>.</p>

        Args:
            configuration: <p>The updated network configuration for the connector. Provide the full <code>VpcEgressConfiguration</code> including all subnet IDs and security group IDs — this replaces the existing configuration.</p>
            operator_role: <p>The updated ARN of the IAM role that Lambda assumes to manage ENIs. Use this to change the operator role without recreating the connector.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the update request.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in <code>ACTIVE</code> state.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.update_network_connector_request.UpdateNetworkConnectorRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.update_network_connector_response.UpdateNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_network_connector

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.update_network_connector.update_network_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.update_network_connector_request.UpdateNetworkConnectorRequest = {
            "identifier": identifier
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if operator_role is not None:
            input_["operator_role"] = operator_role
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
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.delete_network_connector_response.DeleteNetworkConnectorResponse":
        """<p>Initiates deletion of a network connector. The connector transitions to <code>DELETING</code> state while elastic network interfaces are cleaned up asynchronously. After deletion completes, subsequent calls to <code>GetNetworkConnector</code> return <code>ResourceNotFoundException</code>.</p> <p>This operation is idempotent — calling delete on a connector that is already deleting or has been deleted succeeds without error. You can delete connectors in <code>ACTIVE</code> or <code>FAILED</code> states. Before deleting a connector, ensure that no Lambda MicroVMs are using it, as they will lose VPC egress connectivity immediately.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in <code>ACTIVE</code> state.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.delete_network_connector_request.DeleteNetworkConnectorRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.delete_network_connector_response.DeleteNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_network_connector

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.delete_network_connector.delete_network_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.delete_network_connector_request.DeleteNetworkConnectorRequest = {
            "identifier": identifier
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
        config_overrides: Optional[LambdaCoreClientConfig] = None,
        state: Optional[
            "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
        ] = None,
        marker: Optional["capo_lambda_core.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
        ] = None,
    ) -> "capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse":
        """<p>Returns a paginated list of network connectors in your account for the current Region. You can optionally filter results by connector state. Use the <code>Marker</code> parameter from a previous response to retrieve the next page of results.</p> <p>Each item in the response includes the connector ARN, name, ID, type, current state, and last modified timestamp. To retrieve full configuration details for a specific connector, use <code>GetNetworkConnector</code>.</p>

        Args:
            state: <p>Optional filter to return only connectors in the specified state (for example, <code>ACTIVE</code> or <code>FAILED</code>).</p>
            marker: <p>The pagination token from a previous <code>ListNetworkConnectors</code> response. Use this value to retrieve the next page of results.</p>
            max_items: <p>The maximum number of connectors to return per page. Valid range: 1 to 100.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_network_connectors

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.list_network_connectors.list_network_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest = {}
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncNetworkConnector:
    def __init__(self, service: AsyncLambdaCoreClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName",
        configuration: "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        operator_role: Optional[
            "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
        ] = None,
        client_token: Optional[
            "capo_lambda_core.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional[
            "capo_lambda_core.types.network_connector_tags.NetworkConnectorTags"
        ] = None,
    ) -> "capo_lambda_core.types.create_network_connector_response.CreateNetworkConnectorResponse":
        """<p>Creates a network connector that enables Lambda compute resources to route outbound traffic through your Amazon VPC. The network connector provisions elastic network interfaces (ENIs) in the subnets you specify, providing a managed network path to private resources such as databases, caches, and internal APIs.</p> <p>This operation is asynchronous. The network connector starts in <code>PENDING</code> state while ENIs are provisioned in your VPC (provisioning typically takes up to 10 minutes). Use <code>GetNetworkConnector</code> to poll the connector state until it reaches <code>ACTIVE</code>. Once active, you can attach the connector to Lambda MicroVMs at run time using the <code>egressNetworkConnectors</code> parameter on <code>RunMicroVm</code>.</p> <p>This operation is idempotent when you provide a <code>ClientToken</code> — if you retry a request that completed successfully using the same client token, the operation returns the existing connector without creating a duplicate.</p>

        Args:
            name: <p>A unique name for the network connector within your account and Region. You can use the name to identify the connector in subsequent API calls.</p>
            configuration: <p>The network configuration for the connector. Specify a <code>VpcEgressConfiguration</code> to enable outbound traffic routing through your VPC.</p>
            operator_role: <p>The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This role must have permissions for <code>ec2:CreateNetworkInterface</code>, <code>ec2:DeleteNetworkInterface</code>, and related describe operations.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the API returns the existing connector without creating a duplicate.</p>
            tags: <p>A map of key-value pairs to associate with the network connector for organization, cost allocation, or access control.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.network_connector_limit_exceeded_exception.NetworkConnectorLimitExceededException: <p>The account has reached the maximum number of network connectors allowed. Delete unused connectors or request a limit increase through Service Quotas.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in <code>ACTIVE</code> state.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.create_network_connector_request.CreateNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.create_network_connector_response.CreateNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.create_network_connector.async_create_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.create_network_connector_request.CreateNetworkConnectorRequest = {
            "name": name,
            "configuration": configuration,
        }
        if operator_role is not None:
            input_["operator_role"] = operator_role
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
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.get_network_connector_response.GetNetworkConnectorResponse":
        """<p>Retrieves the current configuration, state, and metadata of a network connector. The <code>Identifier</code> parameter accepts the connector ID, name, or full ARN. Use this operation to poll connector state after creation or update, or to inspect the current VPC configuration and any failure reasons.</p> <p>The response includes the full connector configuration, current state, and — if the connector has been updated — the <code>LastUpdateStatus</code> and <code>LastUpdateStatusReasonCode</code> fields that indicate whether the most recent update succeeded or failed.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.get_network_connector_request.GetNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.get_network_connector_response.GetNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.get_network_connector.async_get_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.get_network_connector_request.GetNetworkConnectorRequest = {
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
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        configuration: Optional[
            "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
        ] = None,
        operator_role: Optional[
            "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
        ] = None,
        client_token: Optional[
            "capo_lambda_core.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_lambda_core.types.update_network_connector_response.UpdateNetworkConnectorResponse":
        """<p>Updates the VPC configuration or operator role of an existing network connector. You can modify the subnet IDs, security group IDs, network protocol, or operator role. The connector must be in <code>ACTIVE</code> state to accept updates.</p> <p>This operation is asynchronous. The connector remains in <code>ACTIVE</code> state during the update — existing workloads that reference this connector are not disrupted. Use <code>GetNetworkConnector</code> to monitor the <code>LastUpdateStatus</code> field, which transitions through <code>InProgress</code> to <code>Successful</code> or <code>Failed</code>. If the update fails, the <code>LastUpdateStatusReasonCode</code> field provides a specific error code for troubleshooting. This operation is idempotent when you provide a <code>ClientToken</code>.</p>

        Args:
            configuration: <p>The updated network configuration for the connector. Provide the full <code>VpcEgressConfiguration</code> including all subnet IDs and security group IDs — this replaces the existing configuration.</p>
            operator_role: <p>The updated ARN of the IAM role that Lambda assumes to manage ENIs. Use this to change the operator role without recreating the connector.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the update request.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in <code>ACTIVE</code> state.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.update_network_connector_request.UpdateNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.update_network_connector_response.UpdateNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.update_network_connector.async_update_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.update_network_connector_request.UpdateNetworkConnectorRequest = {
            "identifier": identifier
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if operator_role is not None:
            input_["operator_role"] = operator_role
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
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.delete_network_connector_response.DeleteNetworkConnectorResponse":
        """<p>Initiates deletion of a network connector. The connector transitions to <code>DELETING</code> state while elastic network interfaces are cleaned up asynchronously. After deletion completes, subsequent calls to <code>GetNetworkConnector</code> return <code>ResourceNotFoundException</code>.</p> <p>This operation is idempotent — calling delete on a connector that is already deleting or has been deleted succeeds without error. You can delete connectors in <code>ACTIVE</code> or <code>FAILED</code> states. Before deleting a connector, ensure that no Lambda MicroVMs are using it, as they will lose VPC egress connectivity immediately.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to update a connector that is not in <code>ACTIVE</code> state.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified network connector does not exist. Verify the identifier (ID, name, or ARN) and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.delete_network_connector_request.DeleteNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.delete_network_connector_response.DeleteNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.delete_network_connector.async_delete_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.delete_network_connector_request.DeleteNetworkConnectorRequest = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        state: Optional[
            "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
        ] = None,
        marker: Optional["capo_lambda_core.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
        ] = None,
    ) -> "capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse":
        """<p>Returns a paginated list of network connectors in your account for the current Region. You can optionally filter results by connector state. Use the <code>Marker</code> parameter from a previous response to retrieve the next page of results.</p> <p>Each item in the response includes the connector ARN, name, ID, type, current state, and last modified timestamp. To retrieve full configuration details for a specific connector, use <code>GetNetworkConnector</code>.</p>

        Args:
            state: <p>Optional filter to return only connectors in the specified state (for example, <code>ACTIVE</code> or <code>FAILED</code>).</p>
            marker: <p>The pagination token from a previous <code>ListNetworkConnectors</code> response. Use this value to retrieve the next page of results.</p>
            max_items: <p>The maximum number of connectors to return per page. Valid range: 1 to 100.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_network_connectors

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.list_network_connectors.async_list_network_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest = {}
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
