from __future__ import annotations

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
    import capo_iot_managed_integrations.types.get_schema_version_request
    import capo_iot_managed_integrations.types.get_schema_version_response
    import capo_iot_managed_integrations.types.list_schema_versions_request
    import capo_iot_managed_integrations.types.list_schema_versions_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.schema_id
    import capo_iot_managed_integrations.types.schema_version_format
    import capo_iot_managed_integrations.types.schema_version_list_item
    import capo_iot_managed_integrations.types.schema_version_namespace_name
    import capo_iot_managed_integrations.types.schema_version_type
    import capo_iot_managed_integrations.types.schema_version_version
    import capo_iot_managed_integrations.types.schema_version_visibility
    import capo_iot_managed_integrations.types.schema_versioned_id
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class SchemaVersionResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def read(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        schema_versioned_id: "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        format: Optional[
            "capo_iot_managed_integrations.types.schema_version_format.SchemaVersionFormat"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.get_schema_version_response.GetSchemaVersionResponse":
        """<p>Gets a schema version with the provided information.</p>

        Args:
            type: <p>The type of schema version.</p>
            schema_versioned_id: <p>Schema id with a version specified. If the version is missing, it defaults to latest version.</p>
            format: <p>The format of the schema version.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetSchemaVersion happy path for an example schema version.

            >>> client.read(schema_versioned_id='matter.ColorControl@1.4', type='capability')
            GetSchemaVersion happy path for an example schema version.

            >>> client.read(schema_versioned_id='matter.ColorControl@1.4', type='capability', format='ZCL')
            GetSchemaVersion error path for an example schema version that does not exist.

            >>> client.read(schema_versioned_id='matter.ColorControl@$latest', type='capability')
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_schema_version_request.GetSchemaVersionRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_schema_version_response.GetSchemaVersionResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_schema_version

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_schema_version.get_schema_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSchemaVersion")
        )
        input_: capo_iot_managed_integrations.types.get_schema_version_request.GetSchemaVersionRequest = {
            "type": type,
            "schema_versioned_id": schema_versioned_id,
        }
        if format is not None:
            input_["format"] = format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        schema_id: Optional[
            "capo_iot_managed_integrations.types.schema_id.SchemaId"
        ] = None,
        namespace: Optional[
            "capo_iot_managed_integrations.types.schema_version_namespace_name.SchemaVersionNamespaceName"
        ] = None,
        visibility: Optional[
            "capo_iot_managed_integrations.types.schema_version_visibility.SchemaVersionVisibility"
        ] = None,
        semantic_version: Optional[
            "capo_iot_managed_integrations.types.schema_version_version.SchemaVersionVersion"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_schema_versions_response.ListSchemaVersionsResponse":
        """<p>Lists schema versions with the provided information.</p>

        Args:
            type: <p>Filter on the type of schema version.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            schema_id: <p>Filter on the id of the schema version.</p>
            namespace: <p>Filter on the name of the schema version.</p>
            visibility: <p>The visibility of the schema version.</p>
            semantic_version: <p>The schema version. If this is left blank, it defaults to the latest version.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListSchemaVersions happy path for an example schema version.

            >>> client.list(schema_id='example.ColorControl', type='capability')
            ListSchemaVersions by version.

            >>> client.list(type='capability', semantic_version='34.56')
            ListSchemaVersions error  for invalid input.

            >>> client.list(schema_id='example.ColorControl', type='capability', namespace='matter')
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_schema_versions_request.ListSchemaVersionsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_schema_versions_response.ListSchemaVersionsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_schema_versions

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_schema_versions.list_schema_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSchemaVersions")
        )
        input_: capo_iot_managed_integrations.types.list_schema_versions_request.ListSchemaVersionsRequest = {
            "type": type
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if namespace is not None:
            input_["namespace"] = namespace
        if visibility is not None:
            input_["visibility"] = visibility
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSchemaVersionResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def read(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        schema_versioned_id: "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        format: Optional[
            "capo_iot_managed_integrations.types.schema_version_format.SchemaVersionFormat"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.get_schema_version_response.GetSchemaVersionResponse":
        """<p>Gets a schema version with the provided information.</p>

        Args:
            type: <p>The type of schema version.</p>
            schema_versioned_id: <p>Schema id with a version specified. If the version is missing, it defaults to latest version.</p>
            format: <p>The format of the schema version.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetSchemaVersion happy path for an example schema version.

            >>> await client.read(schema_versioned_id='matter.ColorControl@1.4', type='capability')
            GetSchemaVersion happy path for an example schema version.

            >>> await client.read(schema_versioned_id='matter.ColorControl@1.4', type='capability', format='ZCL')
            GetSchemaVersion error path for an example schema version that does not exist.

            >>> await client.read(schema_versioned_id='matter.ColorControl@$latest', type='capability')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_schema_version_request.GetSchemaVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_schema_version_response.GetSchemaVersionResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_schema_version

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_schema_version.async_get_schema_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSchemaVersion")
        )
        input_: capo_iot_managed_integrations.types.get_schema_version_request.GetSchemaVersionRequest = {
            "type": type,
            "schema_versioned_id": schema_versioned_id,
        }
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        schema_id: Optional[
            "capo_iot_managed_integrations.types.schema_id.SchemaId"
        ] = None,
        namespace: Optional[
            "capo_iot_managed_integrations.types.schema_version_namespace_name.SchemaVersionNamespaceName"
        ] = None,
        visibility: Optional[
            "capo_iot_managed_integrations.types.schema_version_visibility.SchemaVersionVisibility"
        ] = None,
        semantic_version: Optional[
            "capo_iot_managed_integrations.types.schema_version_version.SchemaVersionVersion"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_schema_versions_response.ListSchemaVersionsResponse":
        """<p>Lists schema versions with the provided information.</p>

        Args:
            type: <p>Filter on the type of schema version.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            schema_id: <p>Filter on the id of the schema version.</p>
            namespace: <p>Filter on the name of the schema version.</p>
            visibility: <p>The visibility of the schema version.</p>
            semantic_version: <p>The schema version. If this is left blank, it defaults to the latest version.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListSchemaVersions happy path for an example schema version.

            >>> await client.list(schema_id='example.ColorControl', type='capability')
            ListSchemaVersions by version.

            >>> await client.list(type='capability', semantic_version='34.56')
            ListSchemaVersions error  for invalid input.

            >>> await client.list(schema_id='example.ColorControl', type='capability', namespace='matter')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_schema_versions_request.ListSchemaVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_schema_versions_response.ListSchemaVersionsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_schema_versions

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_schema_versions.async_list_schema_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSchemaVersions")
        )
        input_: capo_iot_managed_integrations.types.list_schema_versions_request.ListSchemaVersionsRequest = {
            "type": type
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if namespace is not None:
            input_["namespace"] = namespace
        if visibility is not None:
            input_["visibility"] = visibility
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
