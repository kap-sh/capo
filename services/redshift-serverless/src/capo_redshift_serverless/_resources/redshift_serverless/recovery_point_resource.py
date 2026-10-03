from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request
    import capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response
    import capo_redshift_serverless.types.get_recovery_point_request
    import capo_redshift_serverless.types.get_recovery_point_response
    import capo_redshift_serverless.types.list_recovery_points_request
    import capo_redshift_serverless.types.list_recovery_points_response
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.recovery_point
    import capo_redshift_serverless.types.restore_from_recovery_point_request
    import capo_redshift_serverless.types.restore_from_recovery_point_response
    import capo_redshift_serverless.types.restore_table_from_recovery_point_request
    import capo_redshift_serverless.types.restore_table_from_recovery_point_response
    import capo_redshift_serverless.types.tag_list
    import capo_redshift_serverless.types.workgroup_name
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class RecoveryPointResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def convert_recovery_point_to_snapshot(
        self,
        recovery_point_id: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
    ) -> "capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response.ConvertRecoveryPointToSnapshotResponse":
        """<p>Converts a recovery point to a snapshot. For more information about recovery points and snapshots, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html">Working with snapshots and recovery points</a>.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point.</p>
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>How long to retain the snapshot.</p>
            tags: <p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the created snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request.ConvertRecoveryPointToSnapshotRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response.ConvertRecoveryPointToSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.convert_recovery_point_to_snapshot

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.convert_recovery_point_to_snapshot.convert_recovery_point_to_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request.ConvertRecoveryPointToSnapshotRequest = {
            "recovery_point_id": recovery_point_id,
            "snapshot_name": snapshot_name,
        }
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recovery_point(
        self,
        recovery_point_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_recovery_point_response.GetRecoveryPointResponse":
        """<p>Returns information about a recovery point.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_recovery_point_request.GetRecoveryPointRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_recovery_point_response.GetRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_recovery_point

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_recovery_point.get_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_recovery_point_request.GetRecoveryPointRequest = {
            "recovery_point_id": recovery_point_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_recovery_points(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        namespace_arn: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.list_recovery_points_response.ListRecoveryPointsResponse":
        """<p>Returns an array of recovery points.</p>

        Args:
            next_token: <p>If your initial <code>ListRecoveryPoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListRecoveryPoints</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            start_time: <p>The time when the recovery point's creation was initiated.</p>
            end_time: <p>The time when creation of the recovery point finished.</p>
            namespace_name: <p>The name of the namespace to list recovery points for.</p>
            namespace_arn: <p>The Amazon Resource Name (ARN) of the namespace from which to list recovery points.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_recovery_points_request.ListRecoveryPointsRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_recovery_points_response.ListRecoveryPointsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_recovery_points

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_recovery_points.list_recovery_points(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_recovery_points_request.ListRecoveryPointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_from_recovery_point(
        self,
        recovery_point_id: str,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        maintain_integration: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_from_recovery_point_response.RestoreFromRecoveryPointResponse":
        """<p>Restore the data from a recovery point.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point to restore from.</p>
            namespace_name: <p>The name of the namespace to restore data into.</p>
            workgroup_name: <p>The name of the workgroup used to restore data.</p>
            maintain_integration: <p>If <code>true</code>, maintain existing data sharing, zero-ETL and S3 event integrations when restoring. Otherwise, integrations will not be maintained after the restore operation. Integrations are only maintained when restored to the same serverless namespace.</p> <p>Default: true</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.restore_from_recovery_point_request.RestoreFromRecoveryPointRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.restore_from_recovery_point_response.RestoreFromRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_from_recovery_point

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.restore_from_recovery_point.restore_from_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_from_recovery_point_request.RestoreFromRecoveryPointRequest = {
            "recovery_point_id": recovery_point_id,
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
        }
        if maintain_integration is not None:
            input_["maintain_integration"] = maintain_integration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_table_from_recovery_point(
        self,
        namespace_name: str,
        workgroup_name: str,
        recovery_point_id: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        source_schema_name: Optional[str] = None,
        target_database_name: Optional[str] = None,
        target_schema_name: Optional[str] = None,
        activate_case_sensitive_identifier: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_table_from_recovery_point_response.RestoreTableFromRecoveryPointResponse":
        """<p>Restores a table from a recovery point to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with interleaved sort keys.</p>

        Args:
            namespace_name: <p>Namespace of the recovery point to restore from.</p>
            workgroup_name: <p>The workgroup to restore the table to.</p>
            recovery_point_id: <p>The ID of the recovery point to restore the table from.</p>
            source_database_name: <p>The name of the source database that contains the table being restored.</p>
            source_schema_name: <p>The name of the source schema that contains the table being restored.</p>
            source_table_name: <p>The name of the source table being restored.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create from the restore operation.</p>
            activate_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.restore_table_from_recovery_point_request.RestoreTableFromRecoveryPointRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.restore_table_from_recovery_point_response.RestoreTableFromRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_table_from_recovery_point

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.restore_table_from_recovery_point.restore_table_from_recovery_point(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_table_from_recovery_point_request.RestoreTableFromRecoveryPointRequest = {
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
            "recovery_point_id": recovery_point_id,
            "source_database_name": source_database_name,
            "source_table_name": source_table_name,
            "new_table_name": new_table_name,
        }
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        if activate_case_sensitive_identifier is not None:
            input_["activate_case_sensitive_identifier"] = (
                activate_case_sensitive_identifier
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRecoveryPointResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def convert_recovery_point_to_snapshot(
        self,
        recovery_point_id: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
    ) -> "capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response.ConvertRecoveryPointToSnapshotResponse":
        """<p>Converts a recovery point to a snapshot. For more information about recovery points and snapshots, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html">Working with snapshots and recovery points</a>.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point.</p>
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>How long to retain the snapshot.</p>
            tags: <p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the created snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request.ConvertRecoveryPointToSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response.ConvertRecoveryPointToSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.convert_recovery_point_to_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.convert_recovery_point_to_snapshot.async_convert_recovery_point_to_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request.ConvertRecoveryPointToSnapshotRequest = {
            "recovery_point_id": recovery_point_id,
            "snapshot_name": snapshot_name,
        }
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recovery_point(
        self,
        recovery_point_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_recovery_point_response.GetRecoveryPointResponse":
        """<p>Returns information about a recovery point.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_recovery_point_request.GetRecoveryPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_recovery_point_response.GetRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_recovery_point

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_recovery_point.async_get_recovery_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_recovery_point_request.GetRecoveryPointRequest = {
            "recovery_point_id": recovery_point_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_recovery_points(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        namespace_arn: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.list_recovery_points_response.ListRecoveryPointsResponse":
        """<p>Returns an array of recovery points.</p>

        Args:
            next_token: <p>If your initial <code>ListRecoveryPoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListRecoveryPoints</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            start_time: <p>The time when the recovery point's creation was initiated.</p>
            end_time: <p>The time when creation of the recovery point finished.</p>
            namespace_name: <p>The name of the namespace to list recovery points for.</p>
            namespace_arn: <p>The Amazon Resource Name (ARN) of the namespace from which to list recovery points.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_recovery_points_request.ListRecoveryPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_recovery_points_response.ListRecoveryPointsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_recovery_points

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_recovery_points.async_list_recovery_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_recovery_points_request.ListRecoveryPointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_from_recovery_point(
        self,
        recovery_point_id: str,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        maintain_integration: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_from_recovery_point_response.RestoreFromRecoveryPointResponse":
        """<p>Restore the data from a recovery point.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point to restore from.</p>
            namespace_name: <p>The name of the namespace to restore data into.</p>
            workgroup_name: <p>The name of the workgroup used to restore data.</p>
            maintain_integration: <p>If <code>true</code>, maintain existing data sharing, zero-ETL and S3 event integrations when restoring. Otherwise, integrations will not be maintained after the restore operation. Integrations are only maintained when restored to the same serverless namespace.</p> <p>Default: true</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.restore_from_recovery_point_request.RestoreFromRecoveryPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.restore_from_recovery_point_response.RestoreFromRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_from_recovery_point

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.restore_from_recovery_point.async_restore_from_recovery_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_from_recovery_point_request.RestoreFromRecoveryPointRequest = {
            "recovery_point_id": recovery_point_id,
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
        }
        if maintain_integration is not None:
            input_["maintain_integration"] = maintain_integration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_table_from_recovery_point(
        self,
        namespace_name: str,
        workgroup_name: str,
        recovery_point_id: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_schema_name: Optional[str] = None,
        target_database_name: Optional[str] = None,
        target_schema_name: Optional[str] = None,
        activate_case_sensitive_identifier: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_table_from_recovery_point_response.RestoreTableFromRecoveryPointResponse":
        """<p>Restores a table from a recovery point to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with interleaved sort keys.</p>

        Args:
            namespace_name: <p>Namespace of the recovery point to restore from.</p>
            workgroup_name: <p>The workgroup to restore the table to.</p>
            recovery_point_id: <p>The ID of the recovery point to restore the table from.</p>
            source_database_name: <p>The name of the source database that contains the table being restored.</p>
            source_schema_name: <p>The name of the source schema that contains the table being restored.</p>
            source_table_name: <p>The name of the source table being restored.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create from the restore operation.</p>
            activate_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.restore_table_from_recovery_point_request.RestoreTableFromRecoveryPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.restore_table_from_recovery_point_response.RestoreTableFromRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_table_from_recovery_point

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.restore_table_from_recovery_point.async_restore_table_from_recovery_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_table_from_recovery_point_request.RestoreTableFromRecoveryPointRequest = {
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
            "recovery_point_id": recovery_point_id,
            "source_database_name": source_database_name,
            "source_table_name": source_table_name,
            "new_table_name": new_table_name,
        }
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        if activate_case_sensitive_identifier is not None:
            input_["activate_case_sensitive_identifier"] = (
                activate_case_sensitive_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
