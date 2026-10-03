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
    import capo_s3tables.types.create_table_request
    import capo_s3tables.types.create_table_response
    import capo_s3tables.types.delete_table_request
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.get_table_maintenance_configuration_request
    import capo_s3tables.types.get_table_maintenance_configuration_response
    import capo_s3tables.types.get_table_maintenance_job_status_request
    import capo_s3tables.types.get_table_maintenance_job_status_response
    import capo_s3tables.types.get_table_metadata_location_request
    import capo_s3tables.types.get_table_metadata_location_response
    import capo_s3tables.types.get_table_record_expiration_configuration_request
    import capo_s3tables.types.get_table_record_expiration_configuration_response
    import capo_s3tables.types.get_table_record_expiration_job_status_request
    import capo_s3tables.types.get_table_record_expiration_job_status_response
    import capo_s3tables.types.get_table_request
    import capo_s3tables.types.get_table_response
    import capo_s3tables.types.get_table_storage_class_request
    import capo_s3tables.types.get_table_storage_class_response
    import capo_s3tables.types.list_tables_limit
    import capo_s3tables.types.list_tables_request
    import capo_s3tables.types.list_tables_response
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.next_token
    import capo_s3tables.types.open_table_format
    import capo_s3tables.types.put_table_maintenance_configuration_request
    import capo_s3tables.types.put_table_record_expiration_configuration_request
    import capo_s3tables.types.rename_table_request
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_maintenance_configuration_value
    import capo_s3tables.types.table_maintenance_type
    import capo_s3tables.types.table_metadata
    import capo_s3tables.types.table_name
    import capo_s3tables.types.table_record_expiration_configuration_value
    import capo_s3tables.types.table_summary
    import capo_s3tables.types.tags
    import capo_s3tables.types.update_table_metadata_location_request
    import capo_s3tables.types.update_table_metadata_location_response
    import capo_s3tables.types.version_token
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class TableResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def create_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        format: "capo_s3tables.types.open_table_format.OpenTableFormat",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        metadata: Optional["capo_s3tables.types.table_metadata.TableMetadata"] = None,
        encryption_configuration: Optional[
            "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["capo_s3tables.types.tags.Tags"] = None,
    ) -> "capo_s3tables.types.create_table_response.CreateTableResponse":
        """<p>Creates a new table associated with the given namespace in a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html">Creating an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTable</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>metadata</code> request parameter you must have the <code>s3tables:PutTableData</code> permission. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> request parameter you must have the <code>s3tables:PutTableEncryption</code> permission. </p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableStorageClass</code> permission.</p> </li> <li> <p>To create a table with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission.</p> </li> </ul> <note> <p>Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>. </p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>
            namespace: <p>The namespace to associated with the table.</p>
            name: <p>The name for the table.</p>
            format: <p>The format for the table.</p>
            metadata: <p>The metadata for the table.</p>
            encryption_configuration: <p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>
            storage_class_configuration: <p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>

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
            req: "OperationRequest[capo_s3tables.types.create_table_request.CreateTableRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.create_table_response.CreateTableResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.create_table.create_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.create_table_request.CreateTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "format": format,
        }
        if metadata is not None:
            input_["metadata"] = metadata
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

    def delete_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html">Deleting an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.delete_table_request.DeleteTableRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table.delete_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_request.DeleteTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "capo_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
    ) -> "capo_s3tables.types.get_table_response.GetTableResponse":
        """<p>Gets details about a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the table.</p>
            namespace: <p>The name of the namespace the table is associated with.</p>
            name: <p>The name of the table.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_request.GetTableRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_response.GetTableResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table.get_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_request.GetTableRequest = {}
        if table_bucket_arn is not None:
            input_["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input_["namespace"] = namespace
        if name is not None:
            input_["name"] = name
        if table_arn is not None:
            input_["table_arn"] = table_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse":
        """<p>Gets details about the maintenance configuration of a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMaintenanceConfiguration</code> permission to use this operation. </p> </li> <li> <p>You must have the <code>s3tables:GetTableData</code> permission to use set the compaction strategy to <code>sort</code> or <code>zorder</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration.get_table_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest = {
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

    def get_table_maintenance_job_status(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse":
        """<p>Gets the status of a maintenance job for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMaintenanceJobStatus</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace the table is associated with. </p>
            name: <p>The name of the table containing the maintenance job status you want to check.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status.get_table_maintenance_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest = {
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

    def get_table_metadata_location(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse":
        """<p>Gets the location of the table metadata.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_metadata_location

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_metadata_location.get_table_metadata_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest = {
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

    def get_table_record_expiration_configuration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse":
        """<p>Retrieves the expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is <code>enabled</code>, records expire and are automatically removed from the table after the specified number of days.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration.get_table_record_expiration_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_record_expiration_job_status(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse":
        """<p>Retrieves the status, metrics, and details of the latest record expiration job for a table. This includes when the job ran, and whether it succeeded or failed. If the job ran successfully, this also includes statistics about the records that were removed.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationJobStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status.get_table_record_expiration_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
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
            req: "OperationRequest[capo_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_storage_class

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_storage_class.get_table_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest = {
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

    def list_tables(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_tables: Optional[
            "capo_s3tables.types.list_tables_limit.ListTablesLimit"
        ] = None,
    ) -> "capo_s3tables.types.list_tables_response.ListTablesResponse":
        """<p>List tables in the given table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTables</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the tables.</p>
            prefix: <p>The prefix of the tables.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_tables: <p>The maximum number of tables to return.</p>

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
            req: "OperationRequest[capo_s3tables.types.list_tables_request.ListTablesRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_tables_response.ListTablesResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_tables

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_tables.list_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.list_tables_request.ListTablesRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_tables is not None:
            input_["max_tables"] = max_tables

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        type: "capo_s3tables.types.table_maintenance_type.TableMaintenanceType",
        value: "capo_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table associated with the maintenance configuration.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration.put_table_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
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

    def put_table_record_expiration_configuration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        value: "capo_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates or updates the expiration configuration settings for records in a table, including the status of the configuration. If you enable record expiration for a table, records expire and are automatically removed from the table after the number of days that you specify.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            value: <p>The record expiration configuration to apply to the table, including the status (<code>enabled</code> or <code>disabled</code>) and retention period in days.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration.put_table_record_expiration_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest = {
            "table_arn": table_arn,
            "value": value,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rename_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        new_namespace_name: Optional[
            "capo_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        new_name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Renames a table or a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:RenameTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace associated with the table. </p>
            name: <p>The current name of the table.</p>
            new_namespace_name: <p>The new name for the namespace.</p>
            new_name: <p>The new name for the table.</p>
            version_token: <p>The version token of the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.rename_table_request.RenameTableRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.rename_table

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.rename_table.rename_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.rename_table_request.RenameTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }
        if new_namespace_name is not None:
            input_["new_namespace_name"] = new_namespace_name
        if new_name is not None:
            input_["new_name"] = new_name
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_table_metadata_location(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        version_token: "capo_s3tables.types.version_token.VersionToken",
        metadata_location: "capo_s3tables.types.metadata_location.MetadataLocation",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse":
        """<p>Updates the metadata location for a table. The metadata location of a table must be an S3 URI that begins with the table's warehouse location. The metadata location for an Apache Iceberg table must end with <code>.metadata.json</code>, or if the metadata file is Gzip-compressed, <code>.metadata.json.gz</code>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:UpdateTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table. </p>
            metadata_location: <p>The new metadata location for the table. </p>

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
            req: "OperationRequest[capo_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.update_table_metadata_location

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.update_table_metadata_location.update_table_metadata_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "version_token": version_token,
            "metadata_location": metadata_location,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTableResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def create_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        format: "capo_s3tables.types.open_table_format.OpenTableFormat",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        metadata: Optional["capo_s3tables.types.table_metadata.TableMetadata"] = None,
        encryption_configuration: Optional[
            "capo_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "capo_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["capo_s3tables.types.tags.Tags"] = None,
    ) -> "capo_s3tables.types.create_table_response.CreateTableResponse":
        """<p>Creates a new table associated with the given namespace in a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html">Creating an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTable</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>metadata</code> request parameter you must have the <code>s3tables:PutTableData</code> permission. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> request parameter you must have the <code>s3tables:PutTableEncryption</code> permission. </p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableStorageClass</code> permission.</p> </li> <li> <p>To create a table with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission.</p> </li> </ul> <note> <p>Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>. </p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>
            namespace: <p>The namespace to associated with the table.</p>
            name: <p>The name for the table.</p>
            format: <p>The format for the table.</p>
            metadata: <p>The metadata for the table.</p>
            encryption_configuration: <p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>
            storage_class_configuration: <p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>

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
            req: "AsyncOperationRequest[capo_s3tables.types.create_table_request.CreateTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.create_table_response.CreateTableResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_table

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.create_table.async_create_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.create_table_request.CreateTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "format": format,
        }
        if metadata is not None:
            input_["metadata"] = metadata
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

    async def delete_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html">Deleting an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.delete_table_request.DeleteTableRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.delete_table.async_delete_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_table_request.DeleteTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }
        if version_token is not None:
            input_["version_token"] = version_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table(
        self,
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "capo_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
    ) -> "capo_s3tables.types.get_table_response.GetTableResponse":
        """<p>Gets details about a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the table.</p>
            namespace: <p>The name of the namespace the table is associated with.</p>
            name: <p>The name of the table.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_request.GetTableRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_response.GetTableResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table.async_get_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_request.GetTableRequest = {}
        if table_bucket_arn is not None:
            input_["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input_["namespace"] = namespace
        if name is not None:
            input_["name"] = name
        if table_arn is not None:
            input_["table_arn"] = table_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse":
        """<p>Gets details about the maintenance configuration of a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMaintenanceConfiguration</code> permission to use this operation. </p> </li> <li> <p>You must have the <code>s3tables:GetTableData</code> permission to use set the compaction strategy to <code>sort</code> or <code>zorder</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration.async_get_table_maintenance_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest = {
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

    async def get_table_maintenance_job_status(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse":
        """<p>Gets the status of a maintenance job for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMaintenanceJobStatus</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace the table is associated with. </p>
            name: <p>The name of the table containing the maintenance job status you want to check.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status.async_get_table_maintenance_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest = {
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

    async def get_table_metadata_location(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse":
        """<p>Gets the location of the table metadata.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_metadata_location

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_metadata_location.async_get_table_metadata_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest = {
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

    async def get_table_record_expiration_configuration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse":
        """<p>Retrieves the expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is <code>enabled</code>, records expire and are automatically removed from the table after the specified number of days.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration.async_get_table_record_expiration_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest = {
            "table_arn": table_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_record_expiration_job_status(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse":
        """<p>Retrieves the status, metrics, and details of the latest record expiration job for a table. This includes when the job ran, and whether it succeeded or failed. If the job ran successfully, this also includes statistics about the records that were removed.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationJobStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status.async_get_table_record_expiration_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest = {
            "table_arn": table_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_storage_class(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_storage_class

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_storage_class.async_get_table_storage_class(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest = {
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

    async def list_tables(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_tables: Optional[
            "capo_s3tables.types.list_tables_limit.ListTablesLimit"
        ] = None,
    ) -> "capo_s3tables.types.list_tables_response.ListTablesResponse":
        """<p>List tables in the given table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTables</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the tables.</p>
            prefix: <p>The prefix of the tables.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_tables: <p>The maximum number of tables to return.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.list_tables_request.ListTablesRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.list_tables_response.ListTablesResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_tables

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.list_tables.async_list_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.list_tables_request.ListTablesRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_tables is not None:
            input_["max_tables"] = max_tables

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_table_maintenance_configuration(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        type: "capo_s3tables.types.table_maintenance_type.TableMaintenanceType",
        value: "capo_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table associated with the maintenance configuration.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration.async_put_table_maintenance_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
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

    async def put_table_record_expiration_configuration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        value: "capo_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates or updates the expiration configuration settings for records in a table, including the status of the configuration. If you enable record expiration for a table, records expire and are automatically removed from the table after the number of days that you specify.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            value: <p>The record expiration configuration to apply to the table, including the status (<code>enabled</code> or <code>disabled</code>) and retention period in days.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The requested operation is not allowed on this resource. This may occur when attempting to modify a resource that is managed by a service or has restrictions that prevent the operation.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration.async_put_table_record_expiration_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest = {
            "table_arn": table_arn,
            "value": value,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rename_table(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        new_namespace_name: Optional[
            "capo_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        new_name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        version_token: Optional[
            "capo_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Renames a table or a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:RenameTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace associated with the table. </p>
            name: <p>The current name of the table.</p>
            new_namespace_name: <p>The new name for the namespace.</p>
            new_name: <p>The new name for the table.</p>
            version_token: <p>The version token of the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.rename_table_request.RenameTableRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.rename_table

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.rename_table.async_rename_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.rename_table_request.RenameTableRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
        }
        if new_namespace_name is not None:
            input_["new_namespace_name"] = new_namespace_name
        if new_name is not None:
            input_["new_name"] = new_name
        if version_token is not None:
            input_["version_token"] = version_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_table_metadata_location(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        name: "capo_s3tables.types.table_name.TableName",
        version_token: "capo_s3tables.types.version_token.VersionToken",
        metadata_location: "capo_s3tables.types.metadata_location.MetadataLocation",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse":
        """<p>Updates the metadata location for a table. The metadata location of a table must be an S3 URI that begins with the table's warehouse location. The metadata location for an Apache Iceberg table must end with <code>.metadata.json</code>, or if the metadata file is Gzip-compressed, <code>.metadata.json.gz</code>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:UpdateTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table. </p>
            metadata_location: <p>The new metadata location for the table. </p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.update_table_metadata_location

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.update_table_metadata_location.async_update_table_metadata_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
            "name": name,
            "version_token": version_token,
            "metadata_location": metadata_location,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
