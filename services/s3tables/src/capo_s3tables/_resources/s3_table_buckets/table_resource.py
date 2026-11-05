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
    import capo_s3tables.types.complete_table_migration_request
    import capo_s3tables.types.create_table_request
    import capo_s3tables.types.create_table_response
    import capo_s3tables.types.data_migration_settings
    import capo_s3tables.types.delete_table_request
    import capo_s3tables.types.destination_table
    import capo_s3tables.types.encryption_configuration
    import capo_s3tables.types.get_table_maintenance_configuration_request
    import capo_s3tables.types.get_table_maintenance_configuration_response
    import capo_s3tables.types.get_table_maintenance_job_status_request
    import capo_s3tables.types.get_table_maintenance_job_status_response
    import capo_s3tables.types.get_table_metadata_location_request
    import capo_s3tables.types.get_table_metadata_location_response
    import capo_s3tables.types.get_table_migration_request
    import capo_s3tables.types.get_table_migration_response
    import capo_s3tables.types.get_table_record_expiration_configuration_request
    import capo_s3tables.types.get_table_record_expiration_configuration_response
    import capo_s3tables.types.get_table_record_expiration_job_status_request
    import capo_s3tables.types.get_table_record_expiration_job_status_response
    import capo_s3tables.types.get_table_request
    import capo_s3tables.types.get_table_response
    import capo_s3tables.types.get_table_storage_class_request
    import capo_s3tables.types.get_table_storage_class_response
    import capo_s3tables.types.list_table_migrations_limit
    import capo_s3tables.types.list_table_migrations_request
    import capo_s3tables.types.list_table_migrations_response
    import capo_s3tables.types.list_tables_limit
    import capo_s3tables.types.list_tables_request
    import capo_s3tables.types.list_tables_response
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.migration_id
    import capo_s3tables.types.migration_output_configuration
    import capo_s3tables.types.migration_requested_state
    import capo_s3tables.types.migration_source_type
    import capo_s3tables.types.migration_state
    import capo_s3tables.types.migration_summary
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.next_token
    import capo_s3tables.types.open_table_format
    import capo_s3tables.types.put_table_maintenance_configuration_request
    import capo_s3tables.types.put_table_record_expiration_configuration_request
    import capo_s3tables.types.rename_table_request
    import capo_s3tables.types.role_arn
    import capo_s3tables.types.source_configuration
    import capo_s3tables.types.start_table_migration_request
    import capo_s3tables.types.start_table_migration_response
    import capo_s3tables.types.storage_class_configuration
    import capo_s3tables.types.sync_table_migration_request
    import capo_s3tables.types.sync_table_migration_response
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
    import capo_s3tables.types.update_table_migration_request
    import capo_s3tables.types.update_table_migration_response
    import capo_s3tables.types.version_token
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class TableResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def complete_table_migration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Completes the migration of a table. The table's most recent migration must be in the <code>succeeded</code>, <code>failed</code> or <code>cancelled</code> state. After you complete the migration, you can't sync the table again, and you can write to and maintain the table as you do any other table: compaction starts, and unreferenced file removal follows the table bucket's configuration. You can't undo this operation. Calling it again for the same table returns a <code>ConflictException</code>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CompleteTableMigration</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the migrated table to complete the migration of.</p>

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
            req: "OperationRequest[capo_s3tables.types.complete_table_migration_request.CompleteTableMigrationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.complete_table_migration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.complete_table_migration.complete_table_migration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CompleteTableMigration")
        )
        input_: capo_s3tables.types.complete_table_migration_request.CompleteTableMigrationRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateTable")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteTable")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTable")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMaintenanceConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMaintenanceJobStatus")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMetadataLocation")
        )
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

    def get_table_migration(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        migration_id: Optional["capo_s3tables.types.migration_id.MigrationId"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
    ) -> "capo_s3tables.types.get_table_migration_response.GetTableMigrationResponse":
        """<p>Gets the details of a migration, including its state, the reason it failed, its statistics and the location of its reports. Identify the migration by its <code>migrationId</code>, or specify the <code>tableARN</code> of a destination table to get that table's most recent migration.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMigration</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            migration_id: <p>The ID of the migration to get. Specify either <code>migrationId</code> or <code>tableARN</code>, not both.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the destination table. Gets the table's most recent migration. Specify either <code>tableARN</code> or <code>migrationId</code>, not both.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_migration_request.GetTableMigrationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_migration_response.GetTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_migration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_migration.get_table_migration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMigration")
        )
        input_: capo_s3tables.types.get_table_migration_request.GetTableMigrationRequest = {}
        if migration_id is not None:
            input_["migration_id"] = migration_id
        if table_arn is not None:
            input_["table_arn"] = table_arn

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableRecordExpirationConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableRecordExpirationJobStatus")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableStorageClass")
        )
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

    def list_table_migrations(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "capo_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
        state: Optional["capo_s3tables.types.migration_state.MigrationState"] = None,
        has_valid_plan: Optional[bool] = None,
        max_results: Optional[
            "capo_s3tables.types.list_table_migrations_limit.ListTableMigrationsLimit"
        ] = None,
        next_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
    ) -> (
        "capo_s3tables.types.list_table_migrations_response.ListTableMigrationsResponse"
    ):
        """<p>Lists the migrations whose destination is in a table bucket, a namespace or a table. Specify a <code>tableBucketARN</code> to list the migrations into a table bucket, and add a <code>namespace</code>, or a <code>namespace</code> and a <code>name</code>, to narrow the list. Or specify a <code>tableARN</code> to list the migrations into a table.</p> <p>Migrations are listed newest first. Results are paginated: use <code>maxResults</code> to set the page size, and pass the <code>nextToken</code> from a response to retrieve the next page of results. A page can contain fewer migrations than <code>maxResults</code>, or none, and still return a <code>nextToken</code>. Continue until a response has no <code>nextToken</code>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:ListTableMigrations</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to list migrations for.</p>
            namespace: <p>The namespace to list migrations for. Requires <code>tableBucketARN</code>.</p>
            name: <p>The name of the table to list migrations for. Requires <code>tableBucketARN</code> and <code>namespace</code>.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table to list migrations for. The list includes the migrations into this table. To also list migrations into an earlier table of the same name, specify <code>tableBucketARN</code>, <code>namespace</code> and <code>name</code> instead. Specify either <code>tableARN</code> or <code>tableBucketARN</code>, not both.</p>
            state: <p>The state to filter the list by. For the valid values, see the <code>state</code> member of <code>GetTableMigration</code>.</p>
            has_valid_plan: <p>The <code>hasValidPlan</code> value to filter the list by. Migrations that are still planning aren't listed, whichever value you specify.</p>
            max_results: <p>The maximum number of migrations to return, from 1 to 1,000. If you don't specify a value, the default is 100.</p>
            next_token: <p>The <code>nextToken</code> from a previous response, to get the next page of results.</p>

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
            req: "OperationRequest[capo_s3tables.types.list_table_migrations_request.ListTableMigrationsRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_table_migrations_response.ListTableMigrationsResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_table_migrations

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_table_migrations.list_table_migrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTableMigrations")
        )
        input_: capo_s3tables.types.list_table_migrations_request.ListTableMigrationsRequest = {}
        if table_bucket_arn is not None:
            input_["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input_["namespace"] = namespace
        if name is not None:
            input_["name"] = name
        if table_arn is not None:
            input_["table_arn"] = table_arn
        if state is not None:
            input_["state"] = state
        if has_valid_plan is not None:
            input_["has_valid_plan"] = has_valid_plan
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTables")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableMaintenanceConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableRecordExpirationConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RenameTable")
        )
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

    def start_table_migration(
        self,
        role_arn: "capo_s3tables.types.role_arn.RoleArn",
        destination_table: "capo_s3tables.types.destination_table.DestinationTable",
        source_type: "capo_s3tables.types.migration_source_type.MigrationSourceType",
        source: "capo_s3tables.types.source_configuration.SourceConfiguration",
        migration_output: "capo_s3tables.types.migration_output_configuration.MigrationOutputConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        data_migration: Optional[
            "capo_s3tables.types.data_migration_settings.DataMigrationSettings"
        ] = None,
        review_migration_plan: Optional[bool] = None,
    ) -> (
        "capo_s3tables.types.start_table_migration_response.StartTableMigrationResponse"
    ):
        """<p>Starts migrating an Amazon Web Services Glue Data Catalog table into a new table in a table bucket. The migration runs asynchronously: this operation returns the migration ID and its initial state, and you track progress with <code>GetTableMigration</code>.</p> <p>The namespace must already exist, and a table with the specified name must not. The migration creates the table during planning and commits data to it as it runs. Until you call <code>CompleteTableMigration</code>, you can read the table but you can't write to it. If the migration fails or is cancelled, the table and the data already committed to it remain.</p> <p>The migration first checks the source and the destination, and writes the table compatibility and object compatibility reports to the bucket that you specify in <code>migrationOutput</code>. If you set <code>reviewMigrationPlan</code> to <code>true</code>, the migration waits in the <code>pendingReview</code> state so that you can review the reports, and continues only when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. Otherwise it continues to migrate the data, and writes the object migration report when the migration ends. If planning fails, the migration writes no object migration report.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:StartTableMigration</code> permission to use this operation.</p> </li> <li> <p>You must have the <code>iam:PassRole</code> permission on the role that you specify in <code>roleARN</code>, with a condition that allows passing it to <code>migration.s3tables.amazonaws.com</code>. The associated resource is the table bucket.</p> </li> <li> <p>If <code>destinationTable</code> specifies SSE-KMS encryption, you must have the <code>kms:DescribeKey</code> and <code>kms:GenerateDataKey</code> permissions on the KMS key. You must also grant the S3 Tables maintenance principal access to the key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </li> </ul> </dd> </dl>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the migration uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow <code>migration.s3tables.amazonaws.com</code> to assume it. You can limit the trust policy to the destination table bucket with the <code>aws:SourceArn</code> and <code>aws:SourceAccount</code> condition keys.</p>
            destination_table: <p>The table to create and migrate the source into.</p>
            source_type: <p>The type of the source. It must match the member that you set in <code>source</code>.</p>
            source: <p>The source table to migrate.</p>
            data_migration: <p>The maintenance settings and migration policies for the destination table.</p>
            review_migration_plan: <p>Specifies whether the migration waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data. If <code>true</code>, the migration continues when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. The default is <code>false</code>.</p>
            migration_output: <p>The bucket and prefixes that the migration writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.</p>

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
            req: "OperationRequest[capo_s3tables.types.start_table_migration_request.StartTableMigrationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.start_table_migration_response.StartTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.start_table_migration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.start_table_migration.start_table_migration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartTableMigration")
        )
        input_: capo_s3tables.types.start_table_migration_request.StartTableMigrationRequest = {
            "role_arn": role_arn,
            "destination_table": destination_table,
            "source_type": source_type,
            "source": source,
            "migration_output": migration_output,
        }
        if data_migration is not None:
            input_["data_migration"] = data_migration
        if review_migration_plan is not None:
            input_["review_migration_plan"] = review_migration_plan

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def sync_table_migration(
        self,
        role_arn: "capo_s3tables.types.role_arn.RoleArn",
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        migration_output: "capo_s3tables.types.migration_output_configuration.MigrationOutputConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        review_migration_plan: Optional[bool] = None,
    ) -> "capo_s3tables.types.sync_table_migration_response.SyncTableMigrationResponse":
        """<p>Migrates the changes in the source table since the previous start or sync, such as added and deleted source objects, into the destination table. The sync runs asynchronously: this operation returns the migration ID of the sync and its initial state, and you track progress with <code>GetTableMigration</code>.</p> <p>A sync uses the source, destination and data migration settings of the table's migration, and plans the work and writes its reports in the same way as <code>StartTableMigration</code>. You can sync after a start or sync that succeeded, failed or was cancelled, if an earlier start or sync of the table has a valid plan (<code>hasValidPlan</code>). You can't sync a table while a start or sync is in progress for it, and you can sync a table until you call <code>CompleteTableMigration</code> for it. If a source object that an earlier migration migrated has since been overwritten, the sync fails.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:SyncTableMigration</code> permission to use this operation.</p> </li> <li> <p>You must have the <code>iam:PassRole</code> permission on the role that you specify in <code>roleARN</code>, with a condition that allows passing it to <code>migration.s3tables.amazonaws.com</code>. The associated resource is the table.</p> </li> </ul> </dd> </dl>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the sync uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow <code>migration.s3tables.amazonaws.com</code> to assume it. You can limit the trust policy to the destination table bucket with the <code>aws:SourceArn</code> and <code>aws:SourceAccount</code> condition keys.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the destination table to sync. The table must have a migration, and you must not have called <code>CompleteTableMigration</code> for it.</p>
            review_migration_plan: <p>Specifies whether the sync waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data. If <code>true</code>, the migration continues when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. The default is <code>false</code>.</p>
            migration_output: <p>The bucket and prefixes that the sync writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.</p>

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
            req: "OperationRequest[capo_s3tables.types.sync_table_migration_request.SyncTableMigrationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.sync_table_migration_response.SyncTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.sync_table_migration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.sync_table_migration.sync_table_migration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SyncTableMigration")
        )
        input_: capo_s3tables.types.sync_table_migration_request.SyncTableMigrationRequest = {
            "role_arn": role_arn,
            "table_arn": table_arn,
            "migration_output": migration_output,
        }
        if review_migration_plan is not None:
            input_["review_migration_plan"] = review_migration_plan

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateTableMetadataLocation")
        )
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

    def update_table_migration(
        self,
        requested_state: "capo_s3tables.types.migration_requested_state.MigrationRequestedState",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
        migration_id: Optional["capo_s3tables.types.migration_id.MigrationId"] = None,
        update_description: Optional[str] = None,
    ) -> "capo_s3tables.types.update_table_migration_response.UpdateTableMigrationResponse":
        """<p>Requests a state change for a migration. Identify the migration by its <code>migrationId</code> or by the <code>tableARN</code> of its destination table.</p> <p>Set <code>requestedState</code> to <code>queued</code> to continue a migration in the <code>pendingReview</code> state; the migration moves to <code>queued</code> or <code>migrating</code>. Set it to <code>cancelled</code> to cancel a migration in the <code>new</code>, <code>planning</code>, <code>pendingReview</code>, <code>queued</code> or <code>migrating</code> state; the migration moves to <code>cancelling</code>, finishes the work in progress, and then ends in the <code>cancelled</code> state, or in the <code>failed</code> state if any objects failed to migrate. Data that the migration already committed stays in the destination table.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:UpdateTableMigration</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the destination table. Updates the table's most recent migration. Until the migration creates the destination table, specify <code>migrationId</code>. Specify either <code>tableARN</code> or <code>migrationId</code>, not both.</p>
            migration_id: <p>The ID of the migration to update. Specify either <code>migrationId</code> or <code>tableARN</code>, not both.</p>
            requested_state: <p>The state to move the migration to: <code>queued</code> to continue a migration in the <code>pendingReview</code> state, or <code>cancelled</code> to cancel a migration in the <code>new</code>, <code>planning</code>, <code>pendingReview</code>, <code>queued</code> or <code>migrating</code> state.</p>
            update_description: <p>A description of the update, up to 1,024 characters, with no control characters. <code>GetTableMigration</code> doesn't return it.</p>

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
            req: "OperationRequest[capo_s3tables.types.update_table_migration_request.UpdateTableMigrationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.update_table_migration_response.UpdateTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.update_table_migration

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.update_table_migration.update_table_migration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateTableMigration")
        )
        input_: capo_s3tables.types.update_table_migration_request.UpdateTableMigrationRequest = {
            "requested_state": requested_state
        }
        if table_arn is not None:
            input_["table_arn"] = table_arn
        if migration_id is not None:
            input_["migration_id"] = migration_id
        if update_description is not None:
            input_["update_description"] = update_description

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

    async def complete_table_migration(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Completes the migration of a table. The table's most recent migration must be in the <code>succeeded</code>, <code>failed</code> or <code>cancelled</code> state. After you complete the migration, you can't sync the table again, and you can write to and maintain the table as you do any other table: compaction starts, and unreferenced file removal follows the table bucket's configuration. You can't undo this operation. Calling it again for the same table returns a <code>ConflictException</code>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CompleteTableMigration</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the migrated table to complete the migration of.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.complete_table_migration_request.CompleteTableMigrationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.complete_table_migration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.complete_table_migration.async_complete_table_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CompleteTableMigration")
        )
        input_: capo_s3tables.types.complete_table_migration_request.CompleteTableMigrationRequest = {
            "table_arn": table_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateTable")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteTable")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTable")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMaintenanceConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMaintenanceJobStatus")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMetadataLocation")
        )
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

    async def get_table_migration(
        self,
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        migration_id: Optional["capo_s3tables.types.migration_id.MigrationId"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
    ) -> "capo_s3tables.types.get_table_migration_response.GetTableMigrationResponse":
        """<p>Gets the details of a migration, including its state, the reason it failed, its statistics and the location of its reports. Identify the migration by its <code>migrationId</code>, or specify the <code>tableARN</code> of a destination table to get that table's most recent migration.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMigration</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            migration_id: <p>The ID of the migration to get. Specify either <code>migrationId</code> or <code>tableARN</code>, not both.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the destination table. Gets the table's most recent migration. Specify either <code>tableARN</code> or <code>migrationId</code>, not both.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_migration_request.GetTableMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_migration_response.GetTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_migration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_migration.async_get_table_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableMigration")
        )
        input_: capo_s3tables.types.get_table_migration_request.GetTableMigrationRequest = {}
        if migration_id is not None:
            input_["migration_id"] = migration_id
        if table_arn is not None:
            input_["table_arn"] = table_arn

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableRecordExpirationConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableRecordExpirationJobStatus")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableStorageClass")
        )
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

    async def list_table_migrations(
        self,
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "capo_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional["capo_s3tables.types.namespace_name.NamespaceName"] = None,
        name: Optional["capo_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
        state: Optional["capo_s3tables.types.migration_state.MigrationState"] = None,
        has_valid_plan: Optional[bool] = None,
        max_results: Optional[
            "capo_s3tables.types.list_table_migrations_limit.ListTableMigrationsLimit"
        ] = None,
        next_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
    ) -> (
        "capo_s3tables.types.list_table_migrations_response.ListTableMigrationsResponse"
    ):
        """<p>Lists the migrations whose destination is in a table bucket, a namespace or a table. Specify a <code>tableBucketARN</code> to list the migrations into a table bucket, and add a <code>namespace</code>, or a <code>namespace</code> and a <code>name</code>, to narrow the list. Or specify a <code>tableARN</code> to list the migrations into a table.</p> <p>Migrations are listed newest first. Results are paginated: use <code>maxResults</code> to set the page size, and pass the <code>nextToken</code> from a response to retrieve the next page of results. A page can contain fewer migrations than <code>maxResults</code>, or none, and still return a <code>nextToken</code>. Continue until a response has no <code>nextToken</code>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:ListTableMigrations</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to list migrations for.</p>
            namespace: <p>The namespace to list migrations for. Requires <code>tableBucketARN</code>.</p>
            name: <p>The name of the table to list migrations for. Requires <code>tableBucketARN</code> and <code>namespace</code>.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table to list migrations for. The list includes the migrations into this table. To also list migrations into an earlier table of the same name, specify <code>tableBucketARN</code>, <code>namespace</code> and <code>name</code> instead. Specify either <code>tableARN</code> or <code>tableBucketARN</code>, not both.</p>
            state: <p>The state to filter the list by. For the valid values, see the <code>state</code> member of <code>GetTableMigration</code>.</p>
            has_valid_plan: <p>The <code>hasValidPlan</code> value to filter the list by. Migrations that are still planning aren't listed, whichever value you specify.</p>
            max_results: <p>The maximum number of migrations to return, from 1 to 1,000. If you don't specify a value, the default is 100.</p>
            next_token: <p>The <code>nextToken</code> from a previous response, to get the next page of results.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.list_table_migrations_request.ListTableMigrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.list_table_migrations_response.ListTableMigrationsResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_table_migrations

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.list_table_migrations.async_list_table_migrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTableMigrations")
        )
        input_: capo_s3tables.types.list_table_migrations_request.ListTableMigrationsRequest = {}
        if table_bucket_arn is not None:
            input_["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input_["namespace"] = namespace
        if name is not None:
            input_["name"] = name
        if table_arn is not None:
            input_["table_arn"] = table_arn
        if state is not None:
            input_["state"] = state
        if has_valid_plan is not None:
            input_["has_valid_plan"] = has_valid_plan
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTables")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableMaintenanceConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableRecordExpirationConfiguration")
        )
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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RenameTable")
        )
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

    async def start_table_migration(
        self,
        role_arn: "capo_s3tables.types.role_arn.RoleArn",
        destination_table: "capo_s3tables.types.destination_table.DestinationTable",
        source_type: "capo_s3tables.types.migration_source_type.MigrationSourceType",
        source: "capo_s3tables.types.source_configuration.SourceConfiguration",
        migration_output: "capo_s3tables.types.migration_output_configuration.MigrationOutputConfiguration",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        data_migration: Optional[
            "capo_s3tables.types.data_migration_settings.DataMigrationSettings"
        ] = None,
        review_migration_plan: Optional[bool] = None,
    ) -> (
        "capo_s3tables.types.start_table_migration_response.StartTableMigrationResponse"
    ):
        """<p>Starts migrating an Amazon Web Services Glue Data Catalog table into a new table in a table bucket. The migration runs asynchronously: this operation returns the migration ID and its initial state, and you track progress with <code>GetTableMigration</code>.</p> <p>The namespace must already exist, and a table with the specified name must not. The migration creates the table during planning and commits data to it as it runs. Until you call <code>CompleteTableMigration</code>, you can read the table but you can't write to it. If the migration fails or is cancelled, the table and the data already committed to it remain.</p> <p>The migration first checks the source and the destination, and writes the table compatibility and object compatibility reports to the bucket that you specify in <code>migrationOutput</code>. If you set <code>reviewMigrationPlan</code> to <code>true</code>, the migration waits in the <code>pendingReview</code> state so that you can review the reports, and continues only when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. Otherwise it continues to migrate the data, and writes the object migration report when the migration ends. If planning fails, the migration writes no object migration report.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:StartTableMigration</code> permission to use this operation.</p> </li> <li> <p>You must have the <code>iam:PassRole</code> permission on the role that you specify in <code>roleARN</code>, with a condition that allows passing it to <code>migration.s3tables.amazonaws.com</code>. The associated resource is the table bucket.</p> </li> <li> <p>If <code>destinationTable</code> specifies SSE-KMS encryption, you must have the <code>kms:DescribeKey</code> and <code>kms:GenerateDataKey</code> permissions on the KMS key. You must also grant the S3 Tables maintenance principal access to the key. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </li> </ul> </dd> </dl>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the migration uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow <code>migration.s3tables.amazonaws.com</code> to assume it. You can limit the trust policy to the destination table bucket with the <code>aws:SourceArn</code> and <code>aws:SourceAccount</code> condition keys.</p>
            destination_table: <p>The table to create and migrate the source into.</p>
            source_type: <p>The type of the source. It must match the member that you set in <code>source</code>.</p>
            source: <p>The source table to migrate.</p>
            data_migration: <p>The maintenance settings and migration policies for the destination table.</p>
            review_migration_plan: <p>Specifies whether the migration waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data. If <code>true</code>, the migration continues when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. The default is <code>false</code>.</p>
            migration_output: <p>The bucket and prefixes that the migration writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.start_table_migration_request.StartTableMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.start_table_migration_response.StartTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.start_table_migration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.start_table_migration.async_start_table_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartTableMigration")
        )
        input_: capo_s3tables.types.start_table_migration_request.StartTableMigrationRequest = {
            "role_arn": role_arn,
            "destination_table": destination_table,
            "source_type": source_type,
            "source": source,
            "migration_output": migration_output,
        }
        if data_migration is not None:
            input_["data_migration"] = data_migration
        if review_migration_plan is not None:
            input_["review_migration_plan"] = review_migration_plan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def sync_table_migration(
        self,
        role_arn: "capo_s3tables.types.role_arn.RoleArn",
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        migration_output: "capo_s3tables.types.migration_output_configuration.MigrationOutputConfiguration",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        review_migration_plan: Optional[bool] = None,
    ) -> "capo_s3tables.types.sync_table_migration_response.SyncTableMigrationResponse":
        """<p>Migrates the changes in the source table since the previous start or sync, such as added and deleted source objects, into the destination table. The sync runs asynchronously: this operation returns the migration ID of the sync and its initial state, and you track progress with <code>GetTableMigration</code>.</p> <p>A sync uses the source, destination and data migration settings of the table's migration, and plans the work and writes its reports in the same way as <code>StartTableMigration</code>. You can sync after a start or sync that succeeded, failed or was cancelled, if an earlier start or sync of the table has a valid plan (<code>hasValidPlan</code>). You can't sync a table while a start or sync is in progress for it, and you can sync a table until you call <code>CompleteTableMigration</code> for it. If a source object that an earlier migration migrated has since been overwritten, the sync fails.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:SyncTableMigration</code> permission to use this operation.</p> </li> <li> <p>You must have the <code>iam:PassRole</code> permission on the role that you specify in <code>roleARN</code>, with a condition that allows passing it to <code>migration.s3tables.amazonaws.com</code>. The associated resource is the table.</p> </li> </ul> </dd> </dl>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the sync uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow <code>migration.s3tables.amazonaws.com</code> to assume it. You can limit the trust policy to the destination table bucket with the <code>aws:SourceArn</code> and <code>aws:SourceAccount</code> condition keys.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the destination table to sync. The table must have a migration, and you must not have called <code>CompleteTableMigration</code> for it.</p>
            review_migration_plan: <p>Specifies whether the sync waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data. If <code>true</code>, the migration continues when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. The default is <code>false</code>.</p>
            migration_output: <p>The bucket and prefixes that the sync writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.sync_table_migration_request.SyncTableMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.sync_table_migration_response.SyncTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.sync_table_migration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.sync_table_migration.async_sync_table_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SyncTableMigration")
        )
        input_: capo_s3tables.types.sync_table_migration_request.SyncTableMigrationRequest = {
            "role_arn": role_arn,
            "table_arn": table_arn,
            "migration_output": migration_output,
        }
        if review_migration_plan is not None:
            input_["review_migration_plan"] = review_migration_plan

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

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateTableMetadataLocation")
        )
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

    async def update_table_migration(
        self,
        requested_state: "capo_s3tables.types.migration_requested_state.MigrationRequestedState",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        table_arn: Optional["capo_s3tables.types.table_arn.TableARN"] = None,
        migration_id: Optional["capo_s3tables.types.migration_id.MigrationId"] = None,
        update_description: Optional[str] = None,
    ) -> "capo_s3tables.types.update_table_migration_response.UpdateTableMigrationResponse":
        """<p>Requests a state change for a migration. Identify the migration by its <code>migrationId</code> or by the <code>tableARN</code> of its destination table.</p> <p>Set <code>requestedState</code> to <code>queued</code> to continue a migration in the <code>pendingReview</code> state; the migration moves to <code>queued</code> or <code>migrating</code>. Set it to <code>cancelled</code> to cancel a migration in the <code>new</code>, <code>planning</code>, <code>pendingReview</code>, <code>queued</code> or <code>migrating</code> state; the migration moves to <code>cancelling</code>, finishes the work in progress, and then ends in the <code>cancelled</code> state, or in the <code>failed</code> state if any objects failed to migrate. Data that the migration already committed stays in the destination table.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:UpdateTableMigration</code> permission to use this operation.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the destination table. Updates the table's most recent migration. Until the migration creates the destination table, specify <code>migrationId</code>. Specify either <code>tableARN</code> or <code>migrationId</code>, not both.</p>
            migration_id: <p>The ID of the migration to update. Specify either <code>migrationId</code> or <code>tableARN</code>, not both.</p>
            requested_state: <p>The state to move the migration to: <code>queued</code> to continue a migration in the <code>pendingReview</code> state, or <code>cancelled</code> to cancel a migration in the <code>new</code>, <code>planning</code>, <code>pendingReview</code>, <code>queued</code> or <code>migrating</code> state.</p>
            update_description: <p>A description of the update, up to 1,024 characters, with no control characters. <code>GetTableMigration</code> doesn't return it.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.update_table_migration_request.UpdateTableMigrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.update_table_migration_response.UpdateTableMigrationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.update_table_migration

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.update_table_migration.async_update_table_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateTableMigration")
        )
        input_: capo_s3tables.types.update_table_migration_request.UpdateTableMigrationRequest = {
            "requested_state": requested_state
        }
        if table_arn is not None:
            input_["table_arn"] = table_arn
        if migration_id is not None:
            input_["migration_id"] = migration_id
        if update_description is not None:
            input_["update_description"] = update_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
