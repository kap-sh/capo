from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_s3tables._auth._signers
import capo_s3tables._auth._sigv4
from capo_s3tables._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_s3tables.types.create_table_bucket_request
    import capo_s3tables.types.create_table_bucket_response
    import capo_s3tables.types.delete_table_bucket_metrics_configuration_request
    import capo_s3tables.types.delete_table_bucket_request
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.get_table_bucket_maintenance_configuration_request
    import capo_s3tables.types.get_table_bucket_maintenance_configuration_response
    import capo_s3tables.types.get_table_bucket_metrics_configuration_request
    import capo_s3tables.types.get_table_bucket_metrics_configuration_response
    import capo_s3tables.types.get_table_bucket_request
    import capo_s3tables.types.get_table_bucket_response
    import capo_s3tables.types.get_table_bucket_storage_class_request
    import capo_s3tables.types.get_table_bucket_storage_class_response
    import capo_s3tables.types.list_table_buckets_limit
    import capo_s3tables.types.list_table_buckets_request
    import capo_s3tables.types.list_table_buckets_response
    import capo_s3tables.types.next_token
    import capo_s3tables.types.put_table_bucket_maintenance_configuration_request
    import capo_s3tables.types.put_table_bucket_metrics_configuration_request
    import capo_s3tables.types.put_table_bucket_storage_class_request
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_maintenance_configuration_value
    import capo_s3tables.types.table_bucket_maintenance_type
    import capo_s3tables.types.table_bucket_name
    import capo_s3tables.types.table_bucket_summary
    import capo_s3tables.types.table_bucket_type
    import capo_s3tables.types.tags
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class TableBucketResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def create_table_bucket(
        self,
        name: "capo_s3tables.types.table_bucket_name.TableBucketName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        encryption_configuration: Optional[
            "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["capo_s3tables.types.tags.Tags"] = None,
    ) -> "capo_s3tables.types.create_table_bucket_response.CreateTableBucketResponse":
        """<p>Creates a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html">Creating a table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTableBucket</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> parameter you must have the <code>s3tables:PutTableBucketEncryption</code> permission.</p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableBucketStorageClass</code> permission.</p> </li> <li> <p>To create a table bucket with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permission.</p> </li> </ul> </dd> </dl>

        Args:
            name: <p>The name for the table bucket.</p>
            encryption_configuration: <p>The encryption configuration to use for the table bucket. This configuration specifies the default encryption settings that will be applied to all tables created in this bucket unless overridden at the table level. The configuration includes the encryption algorithm and, if using SSE-KMS, the KMS key to use.</p>
            storage_class_configuration: <p>The default storage class configuration for the table bucket. This configuration will be applied to all new tables created in this bucket unless overridden at the table level. If not specified, the service default storage class will be used.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permisson to create a table bucket with tags.</p> </note>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.create_table_bucket_request.CreateTableBucketRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.create_table_bucket_response.CreateTableBucketResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_table_bucket

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.create_table_bucket.create_table_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.create_table_bucket_request.CreateTableBucketRequest = {
            "name": name
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if storage_class_configuration is not None:
            input_["storage_class_configuration"] = storage_class_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_bucket(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html">Deleting a table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucket</code> permission to use this operation. </p> </dd> </dl>

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
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_request.DeleteTableBucketRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket.delete_table_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_request.DeleteTableBucketRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

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
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_table_bucket_metrics_configuration_request.DeleteTableBucketMetricsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket_metrics_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_bucket_metrics_configuration.delete_table_bucket_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_metrics_configuration_request.DeleteTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_response.GetTableBucketResponse":
        """<p>Gets details on a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-details.html">Viewing details about an Amazon S3 table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucket</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_request.GetTableBucketRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_response.GetTableBucketResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket.get_table_bucket(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_request.GetTableBucketRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_maintenance_configuration_response.GetTableBucketMaintenanceConfigurationResponse":
        """<p>Gets details about a maintenance configuration for a given table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html">Amazon S3 table bucket maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_maintenance_configuration_request.GetTableBucketMaintenanceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_maintenance_configuration_response.GetTableBucketMaintenanceConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_maintenance_configuration.get_table_bucket_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_maintenance_configuration_request.GetTableBucketMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_metrics_configuration_response.GetTableBucketMetricsConfigurationResponse":
        """<p>Gets the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

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
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_metrics_configuration_request.GetTableBucketMetricsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_metrics_configuration_response.GetTableBucketMetricsConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_metrics_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_metrics_configuration.get_table_bucket_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_metrics_configuration_request.GetTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_bucket_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_storage_class_response.GetTableBucketStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_bucket_storage_class_request.GetTableBucketStorageClassRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_bucket_storage_class_response.GetTableBucketStorageClassResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_storage_class

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_bucket_storage_class.get_table_bucket_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_storage_class_request.GetTableBucketStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_table_buckets(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_buckets: Optional[
            "capo_s3tables.types.list_table_buckets_limit.ListTableBucketsLimit"
        ] = None,
        type: Optional["capo_s3tables.types.table_bucket_type.TableBucketType"] = None,
    ) -> "capo_s3tables.types.list_table_buckets_response.ListTableBucketsResponse":
        """<p>Lists table buckets for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html">S3 Table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTableBuckets</code> permission to use this operation. </p> </dd> </dl>

        Args:
            prefix: <p>The prefix of the table buckets.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_buckets: <p>The maximum number of table buckets to return in the list.</p>
            type: <p>The type of table buckets to filter by in the list.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.list_table_buckets_request.ListTableBucketsRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_table_buckets_response.ListTableBucketsResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_table_buckets

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_table_buckets.list_table_buckets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.list_table_buckets_request.ListTableBucketsRequest = {}
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_buckets is not None:
            input_["max_buckets"] = max_buckets
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        type: "capo_s3tables.types.table_bucket_maintenance_type.TableBucketMaintenanceType",
        value: "capo_s3tables.types.table_bucket_maintenance_configuration_value.TableBucketMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html">Amazon S3 table bucket maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_maintenance_configuration_request.PutTableBucketMaintenanceConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_maintenance_configuration.put_table_bucket_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_maintenance_configuration_request.PutTableBucketMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "type": type,
            "value": value,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

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
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_metrics_configuration_request.PutTableBucketMetricsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_metrics_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_metrics_configuration.put_table_bucket_metrics_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_metrics_configuration_request.PutTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_bucket_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        storage_class_configuration: "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets or updates the storage class configuration for a table bucket. This configuration serves as the default storage class for all new tables created in the bucket, allowing you to optimize storage costs at the bucket level.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            storage_class_configuration: <p>The storage class configuration to apply to the table bucket. This configuration will serve as the default for new tables created in this bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_bucket_storage_class_request.PutTableBucketStorageClassRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_storage_class

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_bucket_storage_class.put_table_bucket_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_storage_class_request.PutTableBucketStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn,
            "storage_class_configuration": storage_class_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTableBucketResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def create_table_bucket(
        self,
        name: "capo_s3tables.types.table_bucket_name.TableBucketName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        encryption_configuration: Optional[
            "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["capo_s3tables.types.tags.Tags"] = None,
    ) -> "capo_s3tables.types.create_table_bucket_response.CreateTableBucketResponse":
        """<p>Creates a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html">Creating a table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTableBucket</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> parameter you must have the <code>s3tables:PutTableBucketEncryption</code> permission.</p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableBucketStorageClass</code> permission.</p> </li> <li> <p>To create a table bucket with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permission.</p> </li> </ul> </dd> </dl>

        Args:
            name: <p>The name for the table bucket.</p>
            encryption_configuration: <p>The encryption configuration to use for the table bucket. This configuration specifies the default encryption settings that will be applied to all tables created in this bucket unless overridden at the table level. The configuration includes the encryption algorithm and, if using SSE-KMS, the KMS key to use.</p>
            storage_class_configuration: <p>The default storage class configuration for the table bucket. This configuration will be applied to all new tables created in this bucket unless overridden at the table level. If not specified, the service default storage class will be used.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table bucket that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTableBucket</code> permisson to create a table bucket with tags.</p> </note>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.create_table_bucket_request.CreateTableBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.create_table_bucket_response.CreateTableBucketResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_table_bucket

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.create_table_bucket.async_create_table_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.create_table_bucket_request.CreateTableBucketRequest = {
            "name": name
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if storage_class_configuration is not None:
            input_["storage_class_configuration"] = storage_class_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_table_bucket(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-delete.html">Deleting a table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucket</code> permission to use this operation. </p> </dd> </dl>

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
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.delete_table_bucket_request.DeleteTableBucketRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.delete_table_bucket.async_delete_table_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_request.DeleteTableBucketRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

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
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.delete_table_bucket_metrics_configuration_request.DeleteTableBucketMetricsConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_bucket_metrics_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.delete_table_bucket_metrics_configuration.async_delete_table_bucket_metrics_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_bucket_metrics_configuration_request.DeleteTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_bucket(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_response.GetTableBucketResponse":
        """<p>Gets details on a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-details.html">Viewing details about an Amazon S3 table bucket</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucket</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_bucket_request.GetTableBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_bucket_response.GetTableBucketResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_bucket.async_get_table_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_request.GetTableBucketRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_bucket_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_maintenance_configuration_response.GetTableBucketMaintenanceConfigurationResponse":
        """<p>Gets details about a maintenance configuration for a given table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html">Amazon S3 table bucket maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_bucket_maintenance_configuration_request.GetTableBucketMaintenanceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_bucket_maintenance_configuration_response.GetTableBucketMaintenanceConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_maintenance_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_bucket_maintenance_configuration.async_get_table_bucket_maintenance_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_maintenance_configuration_request.GetTableBucketMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_metrics_configuration_response.GetTableBucketMetricsConfigurationResponse":
        """<p>Gets the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

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
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_bucket_metrics_configuration_request.GetTableBucketMetricsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_bucket_metrics_configuration_response.GetTableBucketMetricsConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_metrics_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_bucket_metrics_configuration.async_get_table_bucket_metrics_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_metrics_configuration_request.GetTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_bucket_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_bucket_storage_class_response.GetTableBucketStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_bucket_storage_class_request.GetTableBucketStorageClassRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_bucket_storage_class_response.GetTableBucketStorageClassResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_bucket_storage_class

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_bucket_storage_class.async_get_table_bucket_storage_class(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_bucket_storage_class_request.GetTableBucketStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_table_buckets(
        self,
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_buckets: Optional[
            "capo_s3tables.types.list_table_buckets_limit.ListTableBucketsLimit"
        ] = None,
        type: Optional["capo_s3tables.types.table_bucket_type.TableBucketType"] = None,
    ) -> "capo_s3tables.types.list_table_buckets_response.ListTableBucketsResponse":
        """<p>Lists table buckets for your account. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html">S3 Table buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTableBuckets</code> permission to use this operation. </p> </dd> </dl>

        Args:
            prefix: <p>The prefix of the table buckets.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_buckets: <p>The maximum number of table buckets to return in the list.</p>
            type: <p>The type of table buckets to filter by in the list.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.list_table_buckets_request.ListTableBucketsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.list_table_buckets_response.ListTableBucketsResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_table_buckets

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.list_table_buckets.async_list_table_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.list_table_buckets_request.ListTableBucketsRequest = {}
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_buckets is not None:
            input_["max_buckets"] = max_buckets
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_table_bucket_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        type: "capo_s3tables.types.table_bucket_maintenance_type.TableBucketMaintenanceType",
        value: "capo_s3tables.types.table_bucket_maintenance_configuration_value.TableBucketMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html">Amazon S3 table bucket maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the maintenance configuration.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_bucket_maintenance_configuration_request.PutTableBucketMaintenanceConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_maintenance_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_bucket_maintenance_configuration.async_put_table_bucket_maintenance_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_maintenance_configuration_request.PutTableBucketMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "type": type,
            "value": value,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_table_bucket_metrics_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets the metrics configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketMetricsConfiguration</code> permission to use this operation.</p> </dd> </dl>

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
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_bucket_metrics_configuration_request.PutTableBucketMetricsConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_metrics_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_bucket_metrics_configuration.async_put_table_bucket_metrics_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_metrics_configuration_request.PutTableBucketMetricsConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_table_bucket_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        storage_class_configuration: "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets or updates the storage class configuration for a table bucket. This configuration serves as the default storage class for all new tables created in the bucket, allowing you to optimize storage costs at the bucket level.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            storage_class_configuration: <p>The storage class configuration to apply to the table bucket. This configuration will serve as the default for new tables created in this bucket.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_bucket_storage_class_request.PutTableBucketStorageClassRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_bucket_storage_class

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_bucket_storage_class.async_put_table_bucket_storage_class(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_bucket_storage_class_request.PutTableBucketStorageClassRequest = {
            "table_bucket_arn": table_bucket_arn,
            "storage_class_configuration": storage_class_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
