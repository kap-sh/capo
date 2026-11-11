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
    import capo_s3tables.types.get_table_bucket_logging_request
    import capo_s3tables.types.get_table_bucket_logging_response
    import capo_s3tables.types.put_table_bucket_logging_request
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_logging_status
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class TableBucketLoggingResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def get_table_bucket_logging(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_logging_response.GetTableBucketLoggingResponse":
        """<p>Gets the server access logging configuration for a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-server-logs.html">Server access logging for table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketLogging</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the server access logging configuration of a table bucket
            The following example gets the server access logging configuration of a table bucket that has logging enabled.

            >>> client.get_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket')
            To get the server access logging configuration of a table bucket that has logging disabled
            The following example gets the server access logging configuration of a table bucket that has logging disabled. The response has an empty logging status.

            >>> client.get_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket')
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_logging_request.GetTableBucketLoggingRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_logging_response.GetTableBucketLoggingResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_logging

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_logging.get_table_bucket_logging(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableBucketLogging")
        )
        input_: capo_s3tables.types.get_table_bucket_logging_request.GetTableBucketLoggingRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_logging(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        table_bucket_logging_status: "capo_s3tables.types.table_bucket_logging_status.TableBucketLoggingStatus",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets, updates, or removes the server access logging configuration for a table bucket. When logging is enabled, Amazon S3 delivers a record of the requests made to the table bucket and its tables to the target general purpose bucket that you specify. To disable logging, call this operation with an empty <code>tableBucketLoggingStatus</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-server-logs.html">Server access logging for table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketLogging</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            table_bucket_logging_status: <p>The logging status to apply to the table bucket. To disable logging, specify an empty <code>tableBucketLoggingStatus</code>.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable server access logging for a table bucket
            The following example enables server access logging for a table bucket. Logs are delivered to the specified general purpose bucket, with object keys partitioned by the time of the logged events.

            >>> client.put_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket', table_bucket_logging_status={'loggingEnabled': {'targetBucket': 'amzn-s3-demo-destination-bucket', 'targetPrefix': 'logs/', 'targetObjectKeyFormat': {'partitionedPrefix': {'partitionDateSource': 'EventTime'}}}})
            To disable server access logging for a table bucket
            The following example disables server access logging for a table bucket by specifying an empty logging status.

            >>> client.put_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket', table_bucket_logging_status={})
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_logging_request.PutTableBucketLoggingRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_logging

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_logging.put_table_bucket_logging(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableBucketLogging")
        )
        input_: capo_s3tables.types.put_table_bucket_logging_request.PutTableBucketLoggingRequest = {
            "table_bucket_arn": table_bucket_arn,
            "table_bucket_logging_status": table_bucket_logging_status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTableBucketLoggingResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def get_table_bucket_logging(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_logging_response.GetTableBucketLoggingResponse":
        """<p>Gets the server access logging configuration for a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-server-logs.html">Server access logging for table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketLogging</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the server access logging configuration of a table bucket
            The following example gets the server access logging configuration of a table bucket that has logging enabled.

            >>> await client.get_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket')
            To get the server access logging configuration of a table bucket that has logging disabled
            The following example gets the server access logging configuration of a table bucket that has logging disabled. The response has an empty logging status.

            >>> await client.get_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_bucket_logging_request.GetTableBucketLoggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_bucket_logging_response.GetTableBucketLoggingResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_logging

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_bucket_logging.async_get_table_bucket_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableBucketLogging")
        )
        input_: capo_s3tables.types.get_table_bucket_logging_request.GetTableBucketLoggingRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_table_bucket_logging(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        table_bucket_logging_status: "capo_s3tables.types.table_bucket_logging_status.TableBucketLoggingStatus",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets, updates, or removes the server access logging configuration for a table bucket. When logging is enabled, Amazon S3 delivers a record of the requests made to the table bucket and its tables to the target general purpose bucket that you specify. To disable logging, call this operation with an empty <code>tableBucketLoggingStatus</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-server-logs.html">Server access logging for table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketLogging</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            table_bucket_logging_status: <p>The logging status to apply to the table bucket. To disable logging, specify an empty <code>tableBucketLoggingStatus</code>.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable server access logging for a table bucket
            The following example enables server access logging for a table bucket. Logs are delivered to the specified general purpose bucket, with object keys partitioned by the time of the logged events.

            >>> await client.put_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket', table_bucket_logging_status={'loggingEnabled': {'targetBucket': 'amzn-s3-demo-destination-bucket', 'targetPrefix': 'logs/', 'targetObjectKeyFormat': {'partitionedPrefix': {'partitionDateSource': 'EventTime'}}}})
            To disable server access logging for a table bucket
            The following example disables server access logging for a table bucket by specifying an empty logging status.

            >>> await client.put_table_bucket_logging(table_bucket_arn='arn:aws:s3tables:us-east-1:111122223333:bucket/amzn-s3-demo-table-bucket', table_bucket_logging_status={})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_bucket_logging_request.PutTableBucketLoggingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_logging

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_bucket_logging.async_put_table_bucket_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableBucketLogging")
        )
        input_: capo_s3tables.types.put_table_bucket_logging_request.PutTableBucketLoggingRequest = {
            "table_bucket_arn": table_bucket_arn,
            "table_bucket_logging_status": table_bucket_logging_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
