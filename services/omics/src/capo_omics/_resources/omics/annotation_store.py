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
    import capo_omics.types.annotation_store_item
    import capo_omics.types.create_annotation_store_request
    import capo_omics.types.create_annotation_store_response
    import capo_omics.types.delete_annotation_store_request
    import capo_omics.types.delete_annotation_store_response
    import capo_omics.types.description
    import capo_omics.types.get_annotation_store_request
    import capo_omics.types.get_annotation_store_response
    import capo_omics.types.id_list
    import capo_omics.types.list_annotation_stores_filter
    import capo_omics.types.list_annotation_stores_request
    import capo_omics.types.list_annotation_stores_response
    import capo_omics.types.reference_item
    import capo_omics.types.sse_config
    import capo_omics.types.store_format
    import capo_omics.types.store_name
    import capo_omics.types.store_options
    import capo_omics.types.tag_map
    import capo_omics.types.update_annotation_store_request
    import capo_omics.types.update_annotation_store_response
    import capo_omics.types.version_name
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class AnnotationStore:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        store_format: "capo_omics.types.store_format.StoreFormat",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        reference: Optional["capo_omics.types.reference_item.ReferenceItem"] = None,
        name: Optional["capo_omics.types.store_name.StoreName"] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        version_name: Optional["capo_omics.types.version_name.VersionName"] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        store_options: Optional["capo_omics.types.store_options.StoreOptions"] = None,
    ) -> "capo_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates an annotation store.</p>

        Args:
            reference: <p>The genome reference for the store's annotations.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            store_format: <p>The annotation file format of the store.</p>
            store_options: <p>File parsing options for the annotation store.</p>

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
            req: "OperationRequest[capo_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.create_annotation_store

            output, http_response = (
                capo_omics._operations.omics.create_annotation_store.create_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest = {
            "store_format": store_format
        }
        if reference is not None:
            input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if version_name is not None:
            input_["version_name"] = version_name
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if store_options is not None:
            input_["store_options"] = store_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self, name: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "capo_omics.types.get_annotation_store_response.GetAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about an annotation store.</p>

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
            req: "OperationRequest[capo_omics.types.get_annotation_store_request.GetAnnotationStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_annotation_store_response.GetAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_store

            output, http_response = (
                capo_omics._operations.omics.get_annotation_store.get_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_annotation_store_request.GetAnnotationStoreRequest = {
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
    ) -> "capo_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates an annotation store.</p>

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
            req: "OperationRequest[capo_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.update_annotation_store

            output, http_response = (
                capo_omics._operations.omics.update_annotation_store.update_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest = {
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
    ) -> "capo_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes an annotation store.</p>

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
            req: "OperationRequest[capo_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_annotation_store

            output, http_response = (
                capo_omics._operations.omics.delete_annotation_store.delete_annotation_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest = {
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
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
        ] = None,
    ) -> (
        "capo_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
    ):
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of annotation stores.</p>

        Args:
            ids: <p>IDs of stores to list.</p>
            max_results: <p>The maximum number of stores to return in one page of results.</p>
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
            req: "OperationRequest[capo_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_stores

            output, http_response = (
                capo_omics._operations.omics.list_annotation_stores.list_annotation_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest = {}
        if ids is not None:
            input_["ids"] = ids
        if max_results is not None:
            input_["max_results"] = max_results
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


class AsyncAnnotationStore:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        store_format: "capo_omics.types.store_format.StoreFormat",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        reference: Optional["capo_omics.types.reference_item.ReferenceItem"] = None,
        name: Optional["capo_omics.types.store_name.StoreName"] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        version_name: Optional["capo_omics.types.version_name.VersionName"] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        store_options: Optional["capo_omics.types.store_options.StoreOptions"] = None,
    ) -> "capo_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Creates an annotation store.</p>

        Args:
            reference: <p>The genome reference for the store's annotations.</p>
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            tags: <p>Tags for the store.</p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            store_format: <p>The annotation file format of the store.</p>
            store_options: <p>File parsing options for the annotation store.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_annotation_store_response.CreateAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.create_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_annotation_store.async_create_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_annotation_store_request.CreateAnnotationStoreRequest = {
            "store_format": store_format
        }
        if reference is not None:
            input_["reference"] = reference
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if version_name is not None:
            input_["version_name"] = version_name
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if store_options is not None:
            input_["store_options"] = store_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self, name: str, *, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> "capo_omics.types.get_annotation_store_response.GetAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Gets information about an annotation store.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.get_annotation_store_request.GetAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_annotation_store_response.GetAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_annotation_store.async_get_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_annotation_store_request.GetAnnotationStoreRequest = {
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
    ) -> "capo_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Updates an annotation store.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_annotation_store_response.UpdateAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.update_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_annotation_store.async_update_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_annotation_store_request.UpdateAnnotationStoreRequest = {
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
    ) -> "capo_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse":
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Deletes an annotation store.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_annotation_store_response.DeleteAnnotationStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_annotation_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_annotation_store.async_delete_annotation_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_annotation_store_request.DeleteAnnotationStoreRequest = {
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
        ids: Optional["capo_omics.types.id_list.IdList"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
        ] = None,
    ) -> (
        "capo_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
    ):
        """<important> <p>Amazon Web Services HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html"> Amazon Web Services HealthOmics variant store and annotation store availability change</a>.</p> </important> <p>Retrieves a list of annotation stores.</p>

        Args:
            ids: <p>IDs of stores to list.</p>
            max_results: <p>The maximum number of stores to return in one page of results.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_annotation_stores_response.ListAnnotationStoresResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_annotation_stores.async_list_annotation_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_annotation_stores_request.ListAnnotationStoresRequest = {}
        if ids is not None:
            input_["ids"] = ids
        if max_results is not None:
            input_["max_results"] = max_results
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
