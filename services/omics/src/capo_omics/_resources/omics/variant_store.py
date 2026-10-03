from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.create_variant_store_request
    import capo_omics.types.create_variant_store_response
    import capo_omics.types.delete_variant_store_request
    import capo_omics.types.delete_variant_store_response
    import capo_omics.types.description
    import capo_omics.types.get_variant_store_request
    import capo_omics.types.get_variant_store_response
    import capo_omics.types.id_list
    import capo_omics.types.list_variant_stores_filter
    import capo_omics.types.list_variant_stores_request
    import capo_omics.types.list_variant_stores_response
    import capo_omics.types.reference_item
    import capo_omics.types.sse_config
    import capo_omics.types.store_name
    import capo_omics.types.tag_map
    import capo_omics.types.update_variant_store_request
    import capo_omics.types.update_variant_store_response
    import capo_omics.types.variant_store_item
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class VariantStore:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        reference: "capo_omics.types.reference_item.ReferenceItem",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.store_name.StoreName"] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
    ) -> "capo_omics.types.create_variant_store_response.CreateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates a variant store.</p>

        Args:
            reference: <p>The genome reference for the store's variants.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_variant_store_request.CreateVariantStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_variant_store_response.CreateVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.create_variant_store

            output, http_response = (
                capo_omics._operations.omics.create_variant_store.create_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_variant_store_request.CreateVariantStoreRequest = {
            "reference": reference
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if sse_config is not None:
            input_["sse_config"] = sse_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self, name: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "capo_omics.types.get_variant_store_response.GetVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about a variant store.</p>

        Args:
            name: <p>The store's name.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_variant_store_request.GetVariantStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_variant_store_response.GetVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.get_variant_store

            output, http_response = (
                capo_omics._operations.omics.get_variant_store.get_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_variant_store_request.GetVariantStoreRequest = {
            "name": name
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
        name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_variant_store_response.UpdateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates a variant store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.update_variant_store_request.UpdateVariantStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.update_variant_store_response.UpdateVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.update_variant_store

            output, http_response = (
                capo_omics._operations.omics.update_variant_store.update_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_variant_store_request.UpdateVariantStoreRequest = {
            "name": name
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

    def delete(
        self,
        name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_variant_store_response.DeleteVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes a variant store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_variant_store_request.DeleteVariantStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.delete_variant_store_response.DeleteVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_variant_store

            output, http_response = (
                capo_omics._operations.omics.delete_variant_store.delete_variant_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_variant_store_request.DeleteVariantStoreRequest = {
            "name": name
        }
        if force is not None:
            input_["force"] = force

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
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
        ] = None,
    ) -> "capo_omics.types.list_variant_stores_response.ListVariantStoresResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of variant stores.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            ids: <p>A list of store IDs.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_variant_stores_request.ListVariantStoresRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_variant_stores_response.ListVariantStoresResponse"
        ]:
            import capo_omics._operations.omics.list_variant_stores

            output, http_response = (
                capo_omics._operations.omics.list_variant_stores.list_variant_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_variant_stores_request.ListVariantStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncVariantStore:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        reference: "capo_omics.types.reference_item.ReferenceItem",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.store_name.StoreName"] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
    ) -> "capo_omics.types.create_variant_store_response.CreateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates a variant store.</p>

        Args:
            reference: <p>The genome reference for the store's variants.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_variant_store_request.CreateVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_variant_store_response.CreateVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.create_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_variant_store.async_create_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_variant_store_request.CreateVariantStoreRequest = {
            "reference": reference
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if sse_config is not None:
            input_["sse_config"] = sse_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self, name: str, *, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> "capo_omics.types.get_variant_store_response.GetVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about a variant store.</p>

        Args:
            name: <p>The store's name.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_variant_store_request.GetVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_variant_store_response.GetVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.get_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_variant_store.async_get_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_variant_store_request.GetVariantStoreRequest = {
            "name": name
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
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_variant_store_response.UpdateVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates a variant store.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_variant_store_request.UpdateVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_variant_store_response.UpdateVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.update_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_variant_store.async_update_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_variant_store_request.UpdateVariantStoreRequest = {
            "name": name
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

    async def delete(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_variant_store_response.DeleteVariantStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes a variant store.</p>

        Args:
            name: <p>The store's name.</p>
            force: <p>Whether to force deletion.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_variant_store_request.DeleteVariantStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_variant_store_response.DeleteVariantStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_variant_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_variant_store.async_delete_variant_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_variant_store_request.DeleteVariantStoreRequest = {
            "name": name
        }
        if force is not None:
            input_["force"] = force

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
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_variant_stores_filter.ListVariantStoresFilter"
        ] = None,
    ) -> "capo_omics.types.list_variant_stores_response.ListVariantStoresResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of variant stores.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            ids: <p>A list of store IDs.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_variant_stores_request.ListVariantStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_variant_stores_response.ListVariantStoresResponse"
        ]:
            import capo_omics._operations.omics.list_variant_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_variant_stores.async_list_variant_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_variant_stores_request.ListVariantStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if ids is not None:
            input_["ids"] = ids
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
