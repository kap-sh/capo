from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_medical_imaging._auth._signers
import capo_medical_imaging._auth._sigv4
from capo_medical_imaging._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_medical_imaging.types.client_token
    import capo_medical_imaging.types.create_datastore_request
    import capo_medical_imaging.types.create_datastore_response
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.datastore_name
    import capo_medical_imaging.types.datastore_status
    import capo_medical_imaging.types.datastore_summary
    import capo_medical_imaging.types.delete_datastore_request
    import capo_medical_imaging.types.delete_datastore_response
    import capo_medical_imaging.types.get_datastore_request
    import capo_medical_imaging.types.get_datastore_response
    import capo_medical_imaging.types.kms_key_arn
    import capo_medical_imaging.types.lambda_arn
    import capo_medical_imaging.types.list_datastores_request
    import capo_medical_imaging.types.list_datastores_response
    import capo_medical_imaging.types.lossless_storage_format
    import capo_medical_imaging.types.next_token
    import capo_medical_imaging.types.tag_map
    from capo_medical_imaging._services.async_medical_imaging import (
        AsyncMedicalImagingClient,
        AsyncMedicalImagingClientConfig,
    )
    from capo_medical_imaging._services.medical_imaging import (
        MedicalImagingClient,
        MedicalImagingClientConfig,
    )


class DatastoreResource:
    def __init__(self, service: MedicalImagingClient) -> None:
        self._service = service

    def create(
        self,
        client_token: "capo_medical_imaging.types.client_token.ClientToken",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_name: Optional[
            "capo_medical_imaging.types.datastore_name.DatastoreName"
        ] = None,
        tags: Optional["capo_medical_imaging.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional[
            "capo_medical_imaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
        lambda_authorizer_arn: Optional[
            "capo_medical_imaging.types.lambda_arn.LambdaArn"
        ] = None,
        lossless_storage_format: Optional[
            "capo_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
        ] = None,
    ) -> "capo_medical_imaging.types.create_datastore_response.CreateDatastoreResponse":
        """<p>Create a data store.</p>

        Args:
            datastore_name: <p>The data store name.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            tags: <p>The tags provided when creating a data store.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>
            lambda_authorizer_arn: <p>The ARN of the authorizer's Lambda function.</p>
            lossless_storage_format: <p>The lossless storage format for the datastore.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.create_datastore_request.CreateDatastoreRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.create_datastore_response.CreateDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.create_datastore

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.create_datastore.create_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDatastore")
        )
        input_: capo_medical_imaging.types.create_datastore_request.CreateDatastoreRequest = {
            "client_token": client_token
        }
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if lambda_authorizer_arn is not None:
            input_["lambda_authorizer_arn"] = lambda_authorizer_arn
        if lossless_storage_format is not None:
            input_["lossless_storage_format"] = lossless_storage_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.get_datastore_response.GetDatastoreResponse":
        """<p>Get data store properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.get_datastore_request.GetDatastoreRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.get_datastore_response.GetDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_datastore

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.get_datastore.get_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDatastore")
        )
        input_: capo_medical_imaging.types.get_datastore_request.GetDatastoreRequest = {
            "datastore_id": datastore_id
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
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse":
        """<p>Delete a data store.</p> <note> <p>Before a data store can be deleted, you must first delete all image sets within it.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.delete_datastore

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.delete_datastore.delete_datastore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDatastore")
        )
        input_: capo_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest = {
            "datastore_id": datastore_id
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
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        datastore_status: Optional[
            "capo_medical_imaging.types.datastore_status.DatastoreStatus"
        ] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_medical_imaging.types.list_datastores_response.ListDatastoresResponse":
        """<p>List data stores.</p>

        Args:
            datastore_status: <p>The data store status.</p>
            next_token: <p>The pagination token used to request the list of data stores on the next page.</p>
            max_results: <p>Valid Range: Minimum value of 1. Maximum value of 50.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medical_imaging.types.list_datastores_request.ListDatastoresRequest]",
        ) -> OperationResponse[
            "capo_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.list_datastores

            output, http_response = (
                capo_medical_imaging._operations.ahi_gateway_service.list_datastores.list_datastores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDatastores")
        )
        input_: capo_medical_imaging.types.list_datastores_request.ListDatastoresRequest = {}
        if datastore_status is not None:
            input_["datastore_status"] = datastore_status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDatastoreResource:
    def __init__(self, service: AsyncMedicalImagingClient) -> None:
        self._service = service

    async def create(
        self,
        client_token: "capo_medical_imaging.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        datastore_name: Optional[
            "capo_medical_imaging.types.datastore_name.DatastoreName"
        ] = None,
        tags: Optional["capo_medical_imaging.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional[
            "capo_medical_imaging.types.kms_key_arn.KmsKeyArn"
        ] = None,
        lambda_authorizer_arn: Optional[
            "capo_medical_imaging.types.lambda_arn.LambdaArn"
        ] = None,
        lossless_storage_format: Optional[
            "capo_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
        ] = None,
    ) -> "capo_medical_imaging.types.create_datastore_response.CreateDatastoreResponse":
        """<p>Create a data store.</p>

        Args:
            datastore_name: <p>The data store name.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            tags: <p>The tags provided when creating a data store.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>
            lambda_authorizer_arn: <p>The ARN of the authorizer's Lambda function.</p>
            lossless_storage_format: <p>The lossless storage format for the datastore.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_medical_imaging.types.create_datastore_request.CreateDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_medical_imaging.types.create_datastore_response.CreateDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.create_datastore

            (
                output,
                http_response,
            ) = await capo_medical_imaging._operations.ahi_gateway_service.create_datastore.async_create_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDatastore")
        )
        input_: capo_medical_imaging.types.create_datastore_request.CreateDatastoreRequest = {
            "client_token": client_token
        }
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if lambda_authorizer_arn is not None:
            input_["lambda_authorizer_arn"] = lambda_authorizer_arn
        if lossless_storage_format is not None:
            input_["lossless_storage_format"] = lossless_storage_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.get_datastore_response.GetDatastoreResponse":
        """<p>Get data store properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_medical_imaging.types.get_datastore_request.GetDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_medical_imaging.types.get_datastore_response.GetDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.get_datastore

            (
                output,
                http_response,
            ) = await capo_medical_imaging._operations.ahi_gateway_service.get_datastore.async_get_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDatastore")
        )
        input_: capo_medical_imaging.types.get_datastore_request.GetDatastoreRequest = {
            "datastore_id": datastore_id
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
        datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "capo_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse":
        """<p>Delete a data store.</p> <note> <p>Before a data store can be deleted, you must first delete all image sets within it.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_medical_imaging.types.delete_datastore_response.DeleteDatastoreResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.delete_datastore

            (
                output,
                http_response,
            ) = await capo_medical_imaging._operations.ahi_gateway_service.delete_datastore.async_delete_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDatastore")
        )
        input_: capo_medical_imaging.types.delete_datastore_request.DeleteDatastoreRequest = {
            "datastore_id": datastore_id
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
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        datastore_status: Optional[
            "capo_medical_imaging.types.datastore_status.DatastoreStatus"
        ] = None,
        next_token: Optional["capo_medical_imaging.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_medical_imaging.types.list_datastores_response.ListDatastoresResponse":
        """<p>List data stores.</p>

        Args:
            datastore_status: <p>The data store status.</p>
            next_token: <p>The pagination token used to request the list of data stores on the next page.</p>
            max_results: <p>Valid Range: Minimum value of 1. Maximum value of 50.</p>

        Raises:
            capo_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            capo_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            capo_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            capo_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_medical_imaging.types.list_datastores_request.ListDatastoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_medical_imaging.types.list_datastores_response.ListDatastoresResponse"
        ]:
            import capo_medical_imaging._operations.ahi_gateway_service.list_datastores

            (
                output,
                http_response,
            ) = await capo_medical_imaging._operations.ahi_gateway_service.list_datastores.async_list_datastores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDatastores")
        )
        input_: capo_medical_imaging.types.list_datastores_request.ListDatastoresRequest = {}
        if datastore_status is not None:
            input_["datastore_status"] = datastore_status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
