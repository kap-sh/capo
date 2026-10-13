from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.configuration_description
    import capo_omics.types.configuration_list_item
    import capo_omics.types.configuration_list_token
    import capo_omics.types.configuration_name
    import capo_omics.types.configuration_request_id
    import capo_omics.types.create_configuration_request
    import capo_omics.types.create_configuration_response
    import capo_omics.types.delete_configuration_request
    import capo_omics.types.get_configuration_request
    import capo_omics.types.get_configuration_response
    import capo_omics.types.list_configurations_request
    import capo_omics.types.list_configurations_response
    import capo_omics.types.run_configurations
    import capo_omics.types.tag_map
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class ConfigurationResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_omics.types.configuration_name.ConfigurationName",
        run_configurations: "capo_omics.types.run_configurations.RunConfigurations",
        request_id: "capo_omics.types.configuration_request_id.ConfigurationRequestId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.configuration_description.ConfigurationDescription"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_configuration_response.CreateConfigurationResponse":
        """<p>Create a new configuration.</p>

        Args:
            name: <p>User-friendly name for the configuration.</p>
            description: <p>Optional description for the configuration.</p>
            run_configurations: <p>Required run-specific configurations.</p>
            tags: <p>Optional tags for the configuration.</p>
            request_id: <p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import capo_omics._operations.omics.create_configuration

            output, http_response = (
                capo_omics._operations.omics.create_configuration.create_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguration")
        )
        input_: capo_omics.types.create_configuration_request.CreateConfigurationRequest = {
            "name": name,
            "run_configurations": run_configurations,
            "request_id": request_id,
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
        name: "capo_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_configuration_response.GetConfigurationResponse":
        """<p>Retrieve configuration details for specified name.</p>

        Args:
            name: <p>Configuration name to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_configuration_request.GetConfigurationRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import capo_omics._operations.omics.get_configuration

            output, http_response = (
                capo_omics._operations.omics.get_configuration.get_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguration")
        )
        input_: capo_omics.types.get_configuration_request.GetConfigurationRequest = {
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
        name: "capo_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Delete an existing configuration.</p>

        Args:
            name: <p>Configuration name to delete.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.delete_configuration

            output, http_response = (
                capo_omics._operations.omics.delete_configuration.delete_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguration")
        )
        input_: capo_omics.types.delete_configuration_request.DeleteConfigurationRequest = {
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
        self,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional[
            "capo_omics.types.configuration_list_token.ConfigurationListToken"
        ] = None,
    ) -> "capo_omics.types.list_configurations_response.ListConfigurationsResponse":
        """<p>List all configurations for the account.</p>

        Args:
            max_results: <p>Maximum number of results to return.</p>
            starting_token: <p>Pagination token for retrieving next page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import capo_omics._operations.omics.list_configurations

            output, http_response = (
                capo_omics._operations.omics.list_configurations.list_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfigurations")
        )
        input_: capo_omics.types.list_configurations_request.ListConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_token is not None:
            input_["starting_token"] = starting_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConfigurationResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_omics.types.configuration_name.ConfigurationName",
        run_configurations: "capo_omics.types.run_configurations.RunConfigurations",
        request_id: "capo_omics.types.configuration_request_id.ConfigurationRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.configuration_description.ConfigurationDescription"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_configuration_response.CreateConfigurationResponse":
        """<p>Create a new configuration.</p>

        Args:
            name: <p>User-friendly name for the configuration.</p>
            description: <p>Optional description for the configuration.</p>
            run_configurations: <p>Required run-specific configurations.</p>
            tags: <p>Optional tags for the configuration.</p>
            request_id: <p>Optional request idempotency token. If not specified, a universally unique identifier (UUID) will be automatically generated for the request.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_configuration_request.CreateConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_configuration_response.CreateConfigurationResponse"
        ]:
            import capo_omics._operations.omics.create_configuration

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_configuration.async_create_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguration")
        )
        input_: capo_omics.types.create_configuration_request.CreateConfigurationRequest = {
            "name": name,
            "run_configurations": run_configurations,
            "request_id": request_id,
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
        name: "capo_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_configuration_response.GetConfigurationResponse":
        """<p>Retrieve configuration details for specified name.</p>

        Args:
            name: <p>Configuration name to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_configuration_request.GetConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import capo_omics._operations.omics.get_configuration

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_configuration.async_get_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguration")
        )
        input_: capo_omics.types.get_configuration_request.GetConfigurationRequest = {
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
        name: "capo_omics.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Delete an existing configuration.</p>

        Args:
            name: <p>Configuration name to delete.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_configuration_request.DeleteConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_configuration

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_configuration.async_delete_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguration")
        )
        input_: capo_omics.types.delete_configuration_request.DeleteConfigurationRequest = {
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
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional[
            "capo_omics.types.configuration_list_token.ConfigurationListToken"
        ] = None,
    ) -> "capo_omics.types.list_configurations_response.ListConfigurationsResponse":
        """<p>List all configurations for the account.</p>

        Args:
            max_results: <p>Maximum number of results to return.</p>
            starting_token: <p>Pagination token for retrieving next page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_configurations_request.ListConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_configurations_response.ListConfigurationsResponse"
        ]:
            import capo_omics._operations.omics.list_configurations

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_configurations.async_list_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfigurations")
        )
        input_: capo_omics.types.list_configurations_request.ListConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_token is not None:
            input_["starting_token"] = starting_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
