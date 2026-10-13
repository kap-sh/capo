from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.cloud_connector_description
    import capo_iot_managed_integrations.types.cloud_connector_id
    import capo_iot_managed_integrations.types.cloud_connector_type
    import capo_iot_managed_integrations.types.connector_item
    import capo_iot_managed_integrations.types.create_cloud_connector_request
    import capo_iot_managed_integrations.types.create_cloud_connector_response
    import capo_iot_managed_integrations.types.delete_cloud_connector_request
    import capo_iot_managed_integrations.types.display_name
    import capo_iot_managed_integrations.types.endpoint_config
    import capo_iot_managed_integrations.types.endpoint_type
    import capo_iot_managed_integrations.types.get_cloud_connector_request
    import capo_iot_managed_integrations.types.get_cloud_connector_response
    import capo_iot_managed_integrations.types.lambda_arn
    import capo_iot_managed_integrations.types.list_cloud_connectors_request
    import capo_iot_managed_integrations.types.list_cloud_connectors_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.update_cloud_connector_request
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class CloudConnectorResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_iot_managed_integrations.types.display_name.DisplayName",
        endpoint_config: "capo_iot_managed_integrations.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
        endpoint_type: Optional[
            "capo_iot_managed_integrations.types.endpoint_type.EndpointType"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_cloud_connector_response.CreateCloudConnectorResponse":
        """<p>Creates a C2C (cloud-to-cloud) connector.</p>

        Args:
            name: <p>The display name of the C2C connector.</p>
            endpoint_config: <p>The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.</p>
            description: <p>A description of the C2C connector.</p>
            endpoint_type: <p>The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCloudConnector happy path for TP Link

            >>> client.create(name='Connector for TP Link Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion'}}, client_token='1234567890')
            CreateCloudConnector happy path for Ring

            >>> client.create(name='Connector for Ring Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion'}}, client_token='12312321')
            CreateCloudConnector error path for Ring connector which already exists

            >>> client.create(name='Connector for Ring Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion2'}}, client_token='1213123123')
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_cloud_connector_request.CreateCloudConnectorRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_cloud_connector_response.CreateCloudConnectorResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_cloud_connector

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_cloud_connector.create_cloud_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.create_cloud_connector_request.CreateCloudConnectorRequest = {
            "name": name,
            "endpoint_config": endpoint_config,
        }
        if description is not None:
            input_["description"] = description
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
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
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_cloud_connector_response.GetCloudConnectorResponse":
        """<p>Get configuration details for a cloud connector.</p>

        Args:
            identifier: <p>The identifier of the C2C connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetCloudConnector happy path for TP Link to get connector resource

            >>> client.read(identifier='123456789012')
            GetCloudConnector happy path for Ring to pending status

            >>> client.read(identifier='123456789012')
            GetCloudConnector error Id for Ring connector which does not exist

            >>> client.read(identifier='123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_cloud_connector_request.GetCloudConnectorRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_cloud_connector_response.GetCloudConnectorResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_cloud_connector

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_cloud_connector.get_cloud_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.get_cloud_connector_request.GetCloudConnectorRequest = {
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
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
    ) -> None:
        """<p>Update an existing cloud connector.</p>

        Args:
            identifier: <p>The unique identifier of the cloud connector to update.</p>
            name: <p>The new display name to assign to the cloud connector.</p>
            description: <p>The new description to assign to the cloud connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateCloudConnector happy path for TP Link to update display name

            >>> client.update(identifier='123456789012', name='Connector for TP Link Cloud V2')
            UpdateCloudConnector error Id for Ring connector which does not exist

            >>> client.update(identifier='123456789012', name='Connector for Ring Cloud')
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_cloud_connector

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.update_cloud_connector.update_cloud_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a cloud connector.</p>

        Args:
            identifier: <p>The identifier of the cloud connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_cloud_connector_request.DeleteCloudConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_cloud_connector

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_cloud_connector.delete_cloud_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.delete_cloud_connector_request.DeleteCloudConnectorRequest = {
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
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        type: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
        ] = None,
        lambda_arn: Optional[
            "capo_iot_managed_integrations.types.lambda_arn.LambdaArn"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_cloud_connectors_response.ListCloudConnectorsResponse":
        """<p>Returns a list of connectors filtered by its Lambda Amazon Resource Name (ARN) and <code>type</code>.</p>

        Args:
            type: <p>The type of cloud connectors to filter by when listing available connectors.</p>
            lambda_arn: <p>The Amazon Resource Name (ARN) of the Lambda function to filter cloud connectors by.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListCloudConnectors happy path to get a list of connector resources

            >>> client.list(max_results=5)
            ListCloudConnectors error path for unauthorized user

            >>> client.list(max_results=5)
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_cloud_connectors_request.ListCloudConnectorsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_cloud_connectors_response.ListCloudConnectorsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_cloud_connectors

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_cloud_connectors.list_cloud_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCloudConnectors")
        )
        input_: capo_iot_managed_integrations.types.list_cloud_connectors_request.ListCloudConnectorsRequest = {}
        if type is not None:
            input_["type"] = type
        if lambda_arn is not None:
            input_["lambda_arn"] = lambda_arn
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


class AsyncCloudConnectorResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_iot_managed_integrations.types.display_name.DisplayName",
        endpoint_config: "capo_iot_managed_integrations.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
        endpoint_type: Optional[
            "capo_iot_managed_integrations.types.endpoint_type.EndpointType"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_cloud_connector_response.CreateCloudConnectorResponse":
        """<p>Creates a C2C (cloud-to-cloud) connector.</p>

        Args:
            name: <p>The display name of the C2C connector.</p>
            endpoint_config: <p>The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.</p>
            description: <p>A description of the C2C connector.</p>
            endpoint_type: <p>The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCloudConnector happy path for TP Link

            >>> await client.create(name='Connector for TP Link Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion'}}, client_token='1234567890')
            CreateCloudConnector happy path for Ring

            >>> await client.create(name='Connector for Ring Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion'}}, client_token='12312321')
            CreateCloudConnector error path for Ring connector which already exists

            >>> await client.create(name='Connector for Ring Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion2'}}, client_token='1213123123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_cloud_connector_request.CreateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_cloud_connector_response.CreateCloudConnectorResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_cloud_connector.async_create_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.create_cloud_connector_request.CreateCloudConnectorRequest = {
            "name": name,
            "endpoint_config": endpoint_config,
        }
        if description is not None:
            input_["description"] = description
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
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
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_cloud_connector_response.GetCloudConnectorResponse":
        """<p>Get configuration details for a cloud connector.</p>

        Args:
            identifier: <p>The identifier of the C2C connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetCloudConnector happy path for TP Link to get connector resource

            >>> await client.read(identifier='123456789012')
            GetCloudConnector happy path for Ring to pending status

            >>> await client.read(identifier='123456789012')
            GetCloudConnector error Id for Ring connector which does not exist

            >>> await client.read(identifier='123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_cloud_connector_request.GetCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_cloud_connector_response.GetCloudConnectorResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_cloud_connector.async_get_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.get_cloud_connector_request.GetCloudConnectorRequest = {
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
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
    ) -> None:
        """<p>Update an existing cloud connector.</p>

        Args:
            identifier: <p>The unique identifier of the cloud connector to update.</p>
            name: <p>The new display name to assign to the cloud connector.</p>
            description: <p>The new description to assign to the cloud connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateCloudConnector happy path for TP Link to update display name

            >>> await client.update(identifier='123456789012', name='Connector for TP Link Cloud V2')
            UpdateCloudConnector error Id for Ring connector which does not exist

            >>> await client.update(identifier='123456789012', name='Connector for Ring Cloud')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_cloud_connector.async_update_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a cloud connector.</p>

        Args:
            identifier: <p>The identifier of the cloud connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_cloud_connector_request.DeleteCloudConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_cloud_connector.async_delete_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCloudConnector")
        )
        input_: capo_iot_managed_integrations.types.delete_cloud_connector_request.DeleteCloudConnectorRequest = {
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
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        type: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
        ] = None,
        lambda_arn: Optional[
            "capo_iot_managed_integrations.types.lambda_arn.LambdaArn"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_cloud_connectors_response.ListCloudConnectorsResponse":
        """<p>Returns a list of connectors filtered by its Lambda Amazon Resource Name (ARN) and <code>type</code>.</p>

        Args:
            type: <p>The type of cloud connectors to filter by when listing available connectors.</p>
            lambda_arn: <p>The Amazon Resource Name (ARN) of the Lambda function to filter cloud connectors by.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListCloudConnectors happy path to get a list of connector resources

            >>> await client.list(max_results=5)
            ListCloudConnectors error path for unauthorized user

            >>> await client.list(max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_cloud_connectors_request.ListCloudConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_cloud_connectors_response.ListCloudConnectorsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_cloud_connectors

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_cloud_connectors.async_list_cloud_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCloudConnectors")
        )
        input_: capo_iot_managed_integrations.types.list_cloud_connectors_request.ListCloudConnectorsRequest = {}
        if type is not None:
            input_["type"] = type
        if lambda_arn is not None:
            input_["lambda_arn"] = lambda_arn
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
