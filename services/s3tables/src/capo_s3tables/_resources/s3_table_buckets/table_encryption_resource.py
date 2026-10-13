from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_s3tables._auth._signers
import capo_s3tables._auth._sigv4
from capo_s3tables._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_s3tables.types.get_table_encryption_request
    import capo_s3tables.types.get_table_encryption_response
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class TableEncryptionResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def get_table_encryption(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse":
        """<p>Gets the encryption configuration for a table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket containing the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_encryption

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_encryption.get_table_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableEncryption")
        )
        input_: capo_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTableEncryptionResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def get_table_encryption(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse":
        """<p>Gets the encryption configuration for a table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket containing the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_encryption

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_encryption.async_get_table_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableEncryption")
        )
        input_: capo_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
