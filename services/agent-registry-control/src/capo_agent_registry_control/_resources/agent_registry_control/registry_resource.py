from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_agent_registry_control._auth._signers
import capo_agent_registry_control._auth._sigv4
from capo_agent_registry_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_agent_registry_control.types.approval_configuration
    import capo_agent_registry_control.types.auto_detection_configuration
    import capo_agent_registry_control.types.client_token
    import capo_agent_registry_control.types.create_registry_request
    import capo_agent_registry_control.types.create_registry_response
    import capo_agent_registry_control.types.delete_registry_request
    import capo_agent_registry_control.types.delete_registry_response
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.discovery_configuration
    import capo_agent_registry_control.types.encryption_configuration
    import capo_agent_registry_control.types.get_registry_request
    import capo_agent_registry_control.types.get_registry_response
    import capo_agent_registry_control.types.list_registries_request
    import capo_agent_registry_control.types.list_registries_response
    import capo_agent_registry_control.types.max_results
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.registry_filter_list
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_name
    import capo_agent_registry_control.types.registry_summary
    import capo_agent_registry_control.types.tags_map
    import capo_agent_registry_control.types.update_registry_request
    import capo_agent_registry_control.types.update_registry_response
    import capo_agent_registry_control.types.updated_approval_configuration
    import capo_agent_registry_control.types.updated_auto_detection_configuration
    import capo_agent_registry_control.types.updated_description
    import capo_agent_registry_control.types.updated_discovery_configuration
    from capo_agent_registry_control._services.agent_registry_control import (
        AgentRegistryControlClient,
        AgentRegistryControlClientConfig,
    )
    from capo_agent_registry_control._services.async_agent_registry_control import (
        AsyncAgentRegistryControlClient,
        AsyncAgentRegistryControlClientConfig,
    )


class RegistryResource:
    def __init__(self, service: AgentRegistryControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_agent_registry_control.types.registry_name.RegistryName",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        description: Optional[
            "capo_agent_registry_control.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_agent_registry_control.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        discovery_configuration: Optional[
            "capo_agent_registry_control.types.discovery_configuration.DiscoveryConfiguration"
        ] = None,
        client_token: Optional[
            "capo_agent_registry_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_agent_registry_control.types.tags_map.TagsMap"] = None,
        approval_configuration: Optional[
            "capo_agent_registry_control.types.approval_configuration.ApprovalConfiguration"
        ] = None,
        auto_detection_configuration: Optional[
            "capo_agent_registry_control.types.auto_detection_configuration.AutoDetectionConfiguration"
        ] = None,
    ) -> "capo_agent_registry_control.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.</p>

        Args:
            name: <p>The name of the registry</p>
            description: <p>The description of the registry</p>
            encryption_configuration: <p>The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed Amazon Web Services KMS key encrypts the registry's content. Omit this field to use an Amazon Web Services-owned encryption key. You cannot change the encryption configuration after registry creation.</p>
            discovery_configuration: <p>Discovery configuration for the registry</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>Tags to associate with the registry</p>
            approval_configuration: <p>Approval configuration for registry records</p>
            auto_detection_configuration: <p>The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.create_registry_request.CreateRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.create_registry_response.CreateRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.create_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.create_registry.create_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.create_registry_request.CreateRegistryRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if discovery_configuration is not None:
            input_["discovery_configuration"] = discovery_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration
        if auto_detection_configuration is not None:
            input_["auto_detection_configuration"] = auto_detection_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.get_registry_response.GetRegistryResponse":
        """<p>Gets a registry by identifier (ARN or ID)</p>

        Args:
            registry_id: <p>The identifier of the registry to retrieve (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.get_registry_request.GetRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.get_registry_response.GetRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.get_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.get_registry.get_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.get_registry_request.GetRegistryRequest = {
            "registry_id": registry_id
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        name: Optional[
            "capo_agent_registry_control.types.registry_name.RegistryName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.updated_description.UpdatedDescription"
        ] = None,
        discovery_configuration: Optional[
            "capo_agent_registry_control.types.updated_discovery_configuration.UpdatedDiscoveryConfiguration"
        ] = None,
        approval_configuration: Optional[
            "capo_agent_registry_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"
        ] = None,
        auto_detection_configuration: Optional[
            "capo_agent_registry_control.types.updated_auto_detection_configuration.UpdatedAutoDetectionConfiguration"
        ] = None,
    ) -> "capo_agent_registry_control.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry. This operation uses PATCH semantics: specify only the fields you want to change, and omit the rest to leave them unchanged. Updates are applied asynchronously and the registry transitions to the UPDATING status while they are processed.</p>

        Args:
            registry_id: <p>The identifier of the registry to update (ARN or ID)</p>
            name: <p>The updated name of the registry</p>
            description: <p>The updated description of the registry</p>
            discovery_configuration: <p>The updated discovery configuration. Changing the discovery authorization can break existing consumers that rely on the previous authorization type.</p>
            approval_configuration: <p>The updated approval configuration. The change applies only to records that move to PENDING_APPROVAL after the update; records already in PENDING_APPROVAL are unaffected.</p>
            auto_detection_configuration: <p>The updated auto-detection configuration for the registry, with PATCH semantics. Omit this field to leave the current configuration unchanged. Supply an empty wrapper to unset it. Supply <code>optionalValue</code> to replace it.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.update_registry_request.UpdateRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.update_registry.update_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_request.UpdateRegistryRequest = {
            "registry_id": registry_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if discovery_configuration is not None:
            input_["discovery_configuration"] = discovery_configuration
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration
        if auto_detection_configuration is not None:
            input_["auto_detection_configuration"] = auto_detection_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Deletes a registry. Deletion is asynchronous: the registry transitions to the DELETING status and is removed along with its registry records.</p>

        Args:
            registry_id: <p>The identifier of the registry to delete (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.delete_registry_request.DeleteRegistryRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.delete_registry_response.DeleteRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.delete_registry

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.delete_registry.delete_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.delete_registry_request.DeleteRegistryRequest = {
            "registry_id": registry_id
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
        config_overrides: Optional[AgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_filter_list.RegistryFilterList"
        ] = None,
    ) -> "capo_agent_registry_control.types.list_registries_response.ListRegistriesResponse":
        """<p>Lists the registries in the caller's account and Region, with optional filtering by status and discovery authorizer type</p>

        Args:
            max_results: <p>Maximum number of results to return</p>
            next_token: <p>Token for pagination</p>
            filters: <p>Filters to apply to the registry list</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_agent_registry_control.types.list_registries_request.ListRegistriesRequest]",
        ) -> OperationResponse[
            "capo_agent_registry_control.types.list_registries_response.ListRegistriesResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_registries

            output, http_response = (
                capo_agent_registry_control._operations.agent_registry_control.list_registries.list_registries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_registries_request.ListRegistriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRegistryResource:
    def __init__(self, service: AsyncAgentRegistryControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_agent_registry_control.types.registry_name.RegistryName",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
        description: Optional[
            "capo_agent_registry_control.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_agent_registry_control.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        discovery_configuration: Optional[
            "capo_agent_registry_control.types.discovery_configuration.DiscoveryConfiguration"
        ] = None,
        client_token: Optional[
            "capo_agent_registry_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_agent_registry_control.types.tags_map.TagsMap"] = None,
        approval_configuration: Optional[
            "capo_agent_registry_control.types.approval_configuration.ApprovalConfiguration"
        ] = None,
        auto_detection_configuration: Optional[
            "capo_agent_registry_control.types.auto_detection_configuration.AutoDetectionConfiguration"
        ] = None,
    ) -> "capo_agent_registry_control.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.</p>

        Args:
            name: <p>The name of the registry</p>
            description: <p>The description of the registry</p>
            encryption_configuration: <p>The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed Amazon Web Services KMS key encrypts the registry's content. Omit this field to use an Amazon Web Services-owned encryption key. You cannot change the encryption configuration after registry creation.</p>
            discovery_configuration: <p>Discovery configuration for the registry</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>Tags to associate with the registry</p>
            approval_configuration: <p>Approval configuration for registry records</p>
            auto_detection_configuration: <p>The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.create_registry_request.CreateRegistryRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.create_registry_response.CreateRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.create_registry

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.create_registry.async_create_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.create_registry_request.CreateRegistryRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if discovery_configuration is not None:
            input_["discovery_configuration"] = discovery_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration
        if auto_detection_configuration is not None:
            input_["auto_detection_configuration"] = auto_detection_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.get_registry_response.GetRegistryResponse":
        """<p>Gets a registry by identifier (ARN or ID)</p>

        Args:
            registry_id: <p>The identifier of the registry to retrieve (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.get_registry_request.GetRegistryRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.get_registry_response.GetRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.get_registry

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.get_registry.async_get_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.get_registry_request.GetRegistryRequest = {
            "registry_id": registry_id
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
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
        name: Optional[
            "capo_agent_registry_control.types.registry_name.RegistryName"
        ] = None,
        description: Optional[
            "capo_agent_registry_control.types.updated_description.UpdatedDescription"
        ] = None,
        discovery_configuration: Optional[
            "capo_agent_registry_control.types.updated_discovery_configuration.UpdatedDiscoveryConfiguration"
        ] = None,
        approval_configuration: Optional[
            "capo_agent_registry_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"
        ] = None,
        auto_detection_configuration: Optional[
            "capo_agent_registry_control.types.updated_auto_detection_configuration.UpdatedAutoDetectionConfiguration"
        ] = None,
    ) -> "capo_agent_registry_control.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry. This operation uses PATCH semantics: specify only the fields you want to change, and omit the rest to leave them unchanged. Updates are applied asynchronously and the registry transitions to the UPDATING status while they are processed.</p>

        Args:
            registry_id: <p>The identifier of the registry to update (ARN or ID)</p>
            name: <p>The updated name of the registry</p>
            description: <p>The updated description of the registry</p>
            discovery_configuration: <p>The updated discovery configuration. Changing the discovery authorization can break existing consumers that rely on the previous authorization type.</p>
            approval_configuration: <p>The updated approval configuration. The change applies only to records that move to PENDING_APPROVAL after the update; records already in PENDING_APPROVAL are unaffected.</p>
            auto_detection_configuration: <p>The updated auto-detection configuration for the registry, with PATCH semantics. Omit this field to leave the current configuration unchanged. Supply an empty wrapper to unset it. Supply <code>optionalValue</code> to replace it.</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.update_registry_request.UpdateRegistryRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.update_registry

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.update_registry.async_update_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.update_registry_request.UpdateRegistryRequest = {
            "registry_id": registry_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if discovery_configuration is not None:
            input_["discovery_configuration"] = discovery_configuration
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration
        if auto_detection_configuration is not None:
            input_["auto_detection_configuration"] = auto_detection_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        registry_id: "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
    ) -> "capo_agent_registry_control.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Deletes a registry. Deletion is asynchronous: the registry transitions to the DELETING status and is removed along with its registry records.</p>

        Args:
            registry_id: <p>The identifier of the registry to delete (ARN or ID)</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.delete_registry_request.DeleteRegistryRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.delete_registry_response.DeleteRegistryResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.delete_registry

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.delete_registry.async_delete_registry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.delete_registry_request.DeleteRegistryRequest = {
            "registry_id": registry_id
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
        config_overrides: Optional[AsyncAgentRegistryControlClientConfig] = None,
        max_results: Optional[
            "capo_agent_registry_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_agent_registry_control.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "capo_agent_registry_control.types.registry_filter_list.RegistryFilterList"
        ] = None,
    ) -> "capo_agent_registry_control.types.list_registries_response.ListRegistriesResponse":
        """<p>Lists the registries in the caller's account and Region, with optional filtering by status and discovery authorizer type</p>

        Args:
            max_results: <p>Maximum number of results to return</p>
            next_token: <p>Token for pagination</p>
            filters: <p>Filters to apply to the registry list</p>

        Raises:
            capo_agent_registry_control.errors.access_denied_exception.AccessDeniedException: <p>The caller is not authorized to perform the requested action.</p>
            capo_agent_registry_control.errors.internal_server_exception.InternalServerException: <p>The request failed due to an unexpected internal error; the caller may retry.</p>
            capo_agent_registry_control.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling; the caller may retry after a delay.</p>
            capo_agent_registry_control.errors.validation_exception.ValidationException: <p>The request failed validation of one or more input fields.</p>
            capo_agent_registry_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_agent_registry_control.types.list_registries_request.ListRegistriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_agent_registry_control.types.list_registries_response.ListRegistriesResponse"
        ]:
            import capo_agent_registry_control._operations.agent_registry_control.list_registries

            (
                output,
                http_response,
            ) = await capo_agent_registry_control._operations.agent_registry_control.list_registries.async_list_registries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_agent_registry_control.types.list_registries_request.ListRegistriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
