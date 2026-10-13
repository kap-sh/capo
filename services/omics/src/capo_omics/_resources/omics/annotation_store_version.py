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
    import capo_omics.types.annotation_store_version_item
    import capo_omics.types.create_annotation_store_version_request
    import capo_omics.types.create_annotation_store_version_response
    import capo_omics.types.delete_annotation_store_versions_request
    import capo_omics.types.delete_annotation_store_versions_response
    import capo_omics.types.description
    import capo_omics.types.get_annotation_store_version_request
    import capo_omics.types.get_annotation_store_version_response
    import capo_omics.types.list_annotation_store_versions_filter
    import capo_omics.types.list_annotation_store_versions_request
    import capo_omics.types.list_annotation_store_versions_response
    import capo_omics.types.store_name
    import capo_omics.types.tag_map
    import capo_omics.types.update_annotation_store_version_request
    import capo_omics.types.update_annotation_store_version_response
    import capo_omics.types.version_list
    import capo_omics.types.version_name
    import capo_omics.types.version_options
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class AnnotationStoreVersion:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_omics.types.store_name.StoreName",
        version_name: "capo_omics.types.version_name.VersionName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        version_options: Optional[
            "capo_omics.types.version_options.VersionOptions"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse":
        """<p> Creates a new version of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store version from which versions are being created. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            description: <p> The description of an annotation store version. </p>
            version_options: <p> The options for an annotation store version. </p>
            tags: <p> Any tags added to annotation store version. </p>

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
            req: "OperationRequest[capo_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.create_annotation_store_version

            output, http_response = (
                capo_omics._operations.omics.create_annotation_store_version.create_annotation_store_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAnnotationStoreVersion")
        )
        input_: capo_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
        }
        if description is not None:
            input_["description"] = description
        if version_options is not None:
            input_["version_options"] = version_options
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
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse":
        """<p> Retrieves the metadata for an annotation store version. </p>

        Args:
            name: <p> The name given to an annotation store version to distinguish it from others. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from others. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_store_version

            output, http_response = (
                capo_omics._operations.omics.get_annotation_store_version.get_annotation_store_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAnnotationStoreVersion")
        )
        input_: capo_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
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
        version_name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse":
        """<p> Updates the description of an annotation store version. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            version_name: <p> The name of an annotation store version. </p>
            description: <p> The description of an annotation store. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest]",
        ) -> OperationResponse[
            "capo_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.update_annotation_store_version

            output, http_response = (
                capo_omics._operations.omics.update_annotation_store_version.update_annotation_store_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAnnotationStoreVersion")
        )
        input_: capo_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
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

    def list(
        self,
        name: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
        ] = None,
    ) -> "capo_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse":
        """<p> Lists the versions of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            max_results: <p> The maximum number of annotation store versions to return in one page of results. </p>
            next_token: <p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>
            filter: <p> A filter to apply to the list of annotation store versions. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_store_versions

            output, http_response = (
                capo_omics._operations.omics.list_annotation_store_versions.list_annotation_store_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAnnotationStoreVersions")
        )
        input_: capo_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest = {
            "name": name
        }
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

    def delete_annotation_store_versions(
        self,
        name: str,
        versions: "capo_omics.types.version_list.VersionList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse":
        """<p> Deletes one or multiple versions of an annotation store. </p>

        Args:
            name: <p> The name of the annotation store from which versions are being deleted. </p>
            versions: <p> The versions of an annotation store to be deleted. </p>
            force: <p> Forces the deletion of an annotation store version when imports are in-progress.. </p>

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
            req: "OperationRequest[capo_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse"
        ]:
            import capo_omics._operations.omics.delete_annotation_store_versions

            output, http_response = (
                capo_omics._operations.omics.delete_annotation_store_versions.delete_annotation_store_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAnnotationStoreVersions")
        )
        input_: capo_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest = {
            "name": name,
            "versions": versions,
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


class AsyncAnnotationStoreVersion:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_omics.types.store_name.StoreName",
        version_name: "capo_omics.types.version_name.VersionName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
        version_options: Optional[
            "capo_omics.types.version_options.VersionOptions"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse":
        """<p> Creates a new version of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store version from which versions are being created. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from other versions. </p>
            description: <p> The description of an annotation store version. </p>
            version_options: <p> The options for an annotation store version. </p>
            tags: <p> Any tags added to annotation store version. </p>

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
            req: "AsyncOperationRequest[capo_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_annotation_store_version_response.CreateAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.create_annotation_store_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_annotation_store_version.async_create_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAnnotationStoreVersion")
        )
        input_: capo_omics.types.create_annotation_store_version_request.CreateAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
        }
        if description is not None:
            input_["description"] = description
        if version_options is not None:
            input_["version_options"] = version_options
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
        name: str,
        version_name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse":
        """<p> Retrieves the metadata for an annotation store version. </p>

        Args:
            name: <p> The name given to an annotation store version to distinguish it from others. </p>
            version_name: <p> The name given to an annotation store version to distinguish it from others. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_annotation_store_version_response.GetAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.get_annotation_store_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_annotation_store_version.async_get_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAnnotationStoreVersion")
        )
        input_: capo_omics.types.get_annotation_store_version_request.GetAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
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
        version_name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional["capo_omics.types.description.Description"] = None,
    ) -> "capo_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse":
        """<p> Updates the description of an annotation store version. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            version_name: <p> The name of an annotation store version. </p>
            description: <p> The description of an annotation store. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_annotation_store_version_response.UpdateAnnotationStoreVersionResponse"
        ]:
            import capo_omics._operations.omics.update_annotation_store_version

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_annotation_store_version.async_update_annotation_store_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAnnotationStoreVersion")
        )
        input_: capo_omics.types.update_annotation_store_version_request.UpdateAnnotationStoreVersionRequest = {
            "name": name,
            "version_name": version_name,
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

    async def list(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filter: Optional[
            "capo_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
        ] = None,
    ) -> "capo_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse":
        """<p> Lists the versions of an annotation store. </p>

        Args:
            name: <p> The name of an annotation store. </p>
            max_results: <p> The maximum number of annotation store versions to return in one page of results. </p>
            next_token: <p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>
            filter: <p> A filter to apply to the list of annotation store versions. </p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_annotation_store_versions_response.ListAnnotationStoreVersionsResponse"
        ]:
            import capo_omics._operations.omics.list_annotation_store_versions

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_annotation_store_versions.async_list_annotation_store_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAnnotationStoreVersions")
        )
        input_: capo_omics.types.list_annotation_store_versions_request.ListAnnotationStoreVersionsRequest = {
            "name": name
        }
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

    async def delete_annotation_store_versions(
        self,
        name: str,
        versions: "capo_omics.types.version_list.VersionList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse":
        """<p> Deletes one or multiple versions of an annotation store. </p>

        Args:
            name: <p> The name of the annotation store from which versions are being deleted. </p>
            versions: <p> The versions of an annotation store to be deleted. </p>
            force: <p> Forces the deletion of an annotation store version when imports are in-progress.. </p>

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
            req: "AsyncOperationRequest[capo_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_annotation_store_versions_response.DeleteAnnotationStoreVersionsResponse"
        ]:
            import capo_omics._operations.omics.delete_annotation_store_versions

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_annotation_store_versions.async_delete_annotation_store_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAnnotationStoreVersions")
        )
        input_: capo_omics.types.delete_annotation_store_versions_request.DeleteAnnotationStoreVersionsRequest = {
            "name": name,
            "versions": versions,
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
