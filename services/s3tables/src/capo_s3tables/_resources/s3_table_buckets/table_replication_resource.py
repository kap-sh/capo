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
    import capo_s3tables.types.delete_table_replication_request
    import capo_s3tables.types.get_table_replication_request
    import capo_s3tables.types.get_table_replication_response
    import capo_s3tables.types.get_table_replication_status_request
    import capo_s3tables.types.get_table_replication_status_response
    import capo_s3tables.types.put_table_replication_request
    import capo_s3tables.types.put_table_replication_response
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_replication_configuration
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class TableReplicationResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def delete_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        version_token: str,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the replication configuration for a specific table. After deletion, new updates to this table will no longer be replicated to destination tables, though existing replicated copies will remain in destination buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            version_token: <p>A version token from a previous GetTableReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>

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
            req: "OperationRequest[capo_s3tables.types.delete_table_replication_request.DeleteTableReplicationRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_table_replication.delete_table_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteTableReplication")
        )
        input_: capo_s3tables.types.delete_table_replication_request.DeleteTableReplicationRequest = {
            "table_arn": table_arn,
            "version_token": version_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> (
        "capo_s3tables.types.get_table_replication_response.GetTableReplicationResponse"
    ):
        """<p>Retrieves the replication configuration for a specific table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
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
            req: "OperationRequest[capo_s3tables.types.get_table_replication_request.GetTableReplicationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_replication_response.GetTableReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_replication.get_table_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableReplication")
        )
        input_: capo_s3tables.types.get_table_replication_request.GetTableReplicationRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_replication_status(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_replication_status_response.GetTableReplicationStatusResponse":
        """<p>Retrieves the replication status for a table, including the status of replication to each destination. This operation provides visibility into replication health and progress.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableReplicationStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

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
            req: "OperationRequest[capo_s3tables.types.get_table_replication_status_request.GetTableReplicationStatusRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_table_replication_status_response.GetTableReplicationStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_replication_status

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_table_replication_status.get_table_replication_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableReplicationStatus")
        )
        input_: capo_s3tables.types.get_table_replication_status_request.GetTableReplicationStatusRequest = {
            "table_arn": table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        configuration: "capo_s3tables.types.table_replication_configuration.TableReplicationConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[str] = None,
    ) -> (
        "capo_s3tables.types.put_table_replication_response.PutTableReplicationResponse"
    ):
        """<p>Creates or updates the replication configuration for a specific table. This operation allows you to define table-level replication independently of bucket-level replication, providing granular control over which tables are replicated and where.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:PutTableReplication</code> permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source table and write to all destination tables.</p> </li> <li> <p>You must also have the following permissions:</p> <ul> <li> <p> <code>s3tables:GetTable</code> permission on the source table being replicated.</p> </li> <li> <p> <code>s3tables:CreateTable</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:CreateNamespace</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:GetTableMaintenanceConfig</code> permission for the source table.</p> </li> <li> <p> <code>s3tables:PutTableMaintenanceConfig</code> permission for the destination table.</p> </li> </ul> </li> <li> <p>You must have <code>iam:PassRole</code> permission with condition allowing roles to be passed to <code>replication.s3tables.amazonaws.com</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the source table.</p>
            version_token: <p>A version token from a previous GetTableReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>
            configuration: <p>The replication configuration to apply to the table, including the IAM role and replication rules.</p>

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
            req: "OperationRequest[capo_s3tables.types.put_table_replication_request.PutTableReplicationRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.put_table_replication_response.PutTableReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.put_table_replication

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.put_table_replication.put_table_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableReplication")
        )
        input_: capo_s3tables.types.put_table_replication_request.PutTableReplicationRequest = {
            "table_arn": table_arn,
            "configuration": configuration,
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


class AsyncTableReplicationResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def delete_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        version_token: str,
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the replication configuration for a specific table. After deletion, new updates to this table will no longer be replicated to destination tables, though existing replicated copies will remain in destination buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            version_token: <p>A version token from a previous GetTableReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.delete_table_replication_request.DeleteTableReplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_table_replication

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.delete_table_replication.async_delete_table_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteTableReplication")
        )
        input_: capo_s3tables.types.delete_table_replication_request.DeleteTableReplicationRequest = {
            "table_arn": table_arn,
            "version_token": version_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> (
        "capo_s3tables.types.get_table_replication_response.GetTableReplicationResponse"
    ):
        """<p>Retrieves the replication configuration for a specific table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_replication_request.GetTableReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_replication_response.GetTableReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_replication

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_replication.async_get_table_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableReplication")
        )
        input_: capo_s3tables.types.get_table_replication_request.GetTableReplicationRequest = {
            "table_arn": table_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_replication_status(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_table_replication_status_response.GetTableReplicationStatusResponse":
        """<p>Retrieves the replication status for a table, including the status of replication to each destination. This operation provides visibility into replication health and progress.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableReplicationStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.get_table_replication_status_request.GetTableReplicationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_table_replication_status_response.GetTableReplicationStatusResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_table_replication_status

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_table_replication_status.async_get_table_replication_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTableReplicationStatus")
        )
        input_: capo_s3tables.types.get_table_replication_status_request.GetTableReplicationStatusRequest = {
            "table_arn": table_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_table_replication(
        self,
        table_arn: "capo_s3tables.types.table_arn.TableARN",
        configuration: "capo_s3tables.types.table_replication_configuration.TableReplicationConfiguration",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        version_token: Optional[str] = None,
    ) -> (
        "capo_s3tables.types.put_table_replication_response.PutTableReplicationResponse"
    ):
        """<p>Creates or updates the replication configuration for a specific table. This operation allows you to define table-level replication independently of bucket-level replication, providing granular control over which tables are replicated and where.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:PutTableReplication</code> permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source table and write to all destination tables.</p> </li> <li> <p>You must also have the following permissions:</p> <ul> <li> <p> <code>s3tables:GetTable</code> permission on the source table being replicated.</p> </li> <li> <p> <code>s3tables:CreateTable</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:CreateNamespace</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:GetTableMaintenanceConfig</code> permission for the source table.</p> </li> <li> <p> <code>s3tables:PutTableMaintenanceConfig</code> permission for the destination table.</p> </li> </ul> </li> <li> <p>You must have <code>iam:PassRole</code> permission with condition allowing roles to be passed to <code>replication.s3tables.amazonaws.com</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the source table.</p>
            version_token: <p>A version token from a previous GetTableReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>
            configuration: <p>The replication configuration to apply to the table, including the IAM role and replication rules.</p>

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
            req: "AsyncOperationRequest[capo_s3tables.types.put_table_replication_request.PutTableReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.put_table_replication_response.PutTableReplicationResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.put_table_replication

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.put_table_replication.async_put_table_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutTableReplication")
        )
        input_: capo_s3tables.types.put_table_replication_request.PutTableReplicationRequest = {
            "table_arn": table_arn,
            "configuration": configuration,
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
