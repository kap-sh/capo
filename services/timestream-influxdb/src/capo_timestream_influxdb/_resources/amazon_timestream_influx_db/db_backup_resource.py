from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

from capo_timestream_influxdb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.create_db_backup_input
    import capo_timestream_influxdb.types.create_db_backup_output
    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_backup_id
    import capo_timestream_influxdb.types.db_backup_name
    import capo_timestream_influxdb.types.db_backup_summary
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.db_resource_name
    import capo_timestream_influxdb.types.delete_db_backup_input
    import capo_timestream_influxdb.types.delete_db_backup_output
    import capo_timestream_influxdb.types.get_db_backup_input
    import capo_timestream_influxdb.types.get_db_backup_output
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.list_db_backups_input
    import capo_timestream_influxdb.types.list_db_backups_output
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.next_token
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.request_tag_map
    import capo_timestream_influxdb.types.resource_deployment_type
    import capo_timestream_influxdb.types.restore_from_db_backup_input
    import capo_timestream_influxdb.types.restore_from_db_backup_output
    import capo_timestream_influxdb.types.restore_mode
    import capo_timestream_influxdb.types.retention_days
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list
    from capo_timestream_influxdb._services.async_timestream_influx_db import (
        AsyncTimestreamInfluxDBClient,
        AsyncTimestreamInfluxDBClientConfig,
    )
    from capo_timestream_influxdb._services.timestream_influx_db import (
        TimestreamInfluxDBClient,
        TimestreamInfluxDBClientConfig,
    )


class DbBackupResource:
    def __init__(self, service: TimestreamInfluxDBClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_timestream_influxdb.types.db_backup_name.DbBackupName",
        db_resource_id: "capo_timestream_influxdb.types.db_resource_id.DbResourceId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        retention_days: Optional[
            "capo_timestream_influxdb.types.retention_days.RetentionDays"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_backup_output.CreateDbBackupOutput":
        """<p>Creates a new on-demand backup of a Timestream for InfluxDB resource.</p>

        Args:
            name: <p>The name of the backup. Must be unique within the account and region.</p>
            db_resource_id: <p>The id of the DB instance or DB cluster to back up.</p>
            retention_days: <p>The number of days to retain the backup. Valid values are 1 to 3650.</p>
            tags: <p>A list of key-value pairs to associate with the backup.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.create_db_backup_input.CreateDbBackupInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.create_db_backup_output.CreateDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_backup

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_backup.create_db_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDbBackup")
        )
        input_: capo_timestream_influxdb.types.create_db_backup_input.CreateDbBackupInput = {
            "name": name,
            "db_resource_id": db_resource_id,
        }
        if retention_days is not None:
            input_["retention_days"] = retention_days
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
        identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_backup_output.GetDbBackupOutput":
        """<p>Returns information about a specific Timestream for InfluxDB backup.</p>

        Args:
            identifier: <p>The identifier of the backup to retrieve information for.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.get_db_backup_input.GetDbBackupInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.get_db_backup_output.GetDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_backup

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_backup.get_db_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbBackup")
        )
        input_: capo_timestream_influxdb.types.get_db_backup_input.GetDbBackupInput = {
            "identifier": identifier
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
        identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.delete_db_backup_output.DeleteDbBackupOutput":
        """<p>Deletes a Timestream for InfluxDB backup.</p>

        Args:
            identifier: <p>The identifier of the backup to delete.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.delete_db_backup_input.DeleteDbBackupInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.delete_db_backup_output.DeleteDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_backup

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_backup.delete_db_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDbBackup")
        )
        input_: capo_timestream_influxdb.types.delete_db_backup_input.DeleteDbBackupInput = {
            "identifier": identifier
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
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        db_resource_id: Optional[
            "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
        ] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_backups_output.ListDbBackupsOutput":
        """<p>Returns a list of Timestream for InfluxDB backups.</p>

        Args:
            db_resource_id: <p>The identifier of the DB instance or DB cluster to list backups for. If not specified, returns all backups in the account and region.</p>
            next_token: <p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.list_db_backups_input.ListDbBackupsInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.list_db_backups_output.ListDbBackupsOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_backups

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_backups.list_db_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbBackups")
        )
        input_: capo_timestream_influxdb.types.list_db_backups_input.ListDbBackupsInput = {}
        if db_resource_id is not None:
            input_["db_resource_id"] = db_resource_id
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

    def restore_from_db_backup(
        self,
        name: "capo_timestream_influxdb.types.db_resource_name.DbResourceName",
        db_backup_id: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        restore_to_time: Optional[datetime.datetime] = None,
        restore_mode: Optional[
            "capo_timestream_influxdb.types.restore_mode.RestoreMode"
        ] = None,
        vpc_subnet_ids: Optional[
            "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_timestream_influxdb.types.restore_from_db_backup_output.RestoreFromDbBackupOutput":
        """<p>Restores a Timestream for InfluxDB resource from a backup. By default, a new resource is created. You can optionally restore to the same resource using the REPLACE_EXISTING restore mode.</p>

        Args:
            name: <p>The name of the new resource to create from the restore. If restoring to an existing resource, the name must match the existing resource name.</p>
            db_backup_id: <p>The identifier of the backup to restore from.</p>
            restore_to_time: <p>The point in time to restore to, for continuous backups. Must be within the backup's retention window.</p>
            restore_mode: <p>Specifies whether to restore to a new resource or replace the existing resource. Valid values are NEW_RESOURCE (default) and REPLACE_EXISTING.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs for the restored resource. If not specified, the restored resource uses the same subnets as the backup.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs for the restored resource. If not specified, the restored resource uses the same security groups as the backup.</p>
            publicly_accessible: <p>Specifies whether the restored resource is publicly accessible.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to the specified S3 bucket for the restored resource.</p>
            maintenance_schedule: <p>The maintenance schedule for the restored resource.</p>
            tags: <p>A list of key-value pairs to associate with the restored resource.</p>
            port: <p>The port number on which the restored InfluxDB resource accepts connections.</p>
            network_type: <p>Specifies the network type of the restored resource. Valid values are IPV4 and DUAL.</p>
            deployment_type: <p>Specifies the deployment type of the restored resource. Valid values are SINGLE_AZ, WITH_MULTIAZ_STANDBY, and MULTI_NODE_READ_REPLICAS.</p>
            db_backup_configurations: <p>A list of backup configurations to apply to the restored resource.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the restored resource. Can be a key ID, key ARN, alias name, or alias ARN.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.restore_from_db_backup_input.RestoreFromDbBackupInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.restore_from_db_backup_output.RestoreFromDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.restore_from_db_backup

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.restore_from_db_backup.restore_from_db_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreFromDbBackup")
        )
        input_: capo_timestream_influxdb.types.restore_from_db_backup_input.RestoreFromDbBackupInput = {
            "name": name,
            "db_backup_id": db_backup_id,
        }
        if restore_to_time is not None:
            input_["restore_to_time"] = restore_to_time
        if restore_mode is not None:
            input_["restore_mode"] = restore_mode
        if vpc_subnet_ids is not None:
            input_["vpc_subnet_ids"] = vpc_subnet_ids
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if network_type is not None:
            input_["network_type"] = network_type
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDbBackupResource:
    def __init__(self, service: AsyncTimestreamInfluxDBClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_timestream_influxdb.types.db_backup_name.DbBackupName",
        db_resource_id: "capo_timestream_influxdb.types.db_resource_id.DbResourceId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        retention_days: Optional[
            "capo_timestream_influxdb.types.retention_days.RetentionDays"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> "capo_timestream_influxdb.types.create_db_backup_output.CreateDbBackupOutput":
        """<p>Creates a new on-demand backup of a Timestream for InfluxDB resource.</p>

        Args:
            name: <p>The name of the backup. Must be unique within the account and region.</p>
            db_resource_id: <p>The id of the DB instance or DB cluster to back up.</p>
            retention_days: <p>The number of days to retain the backup. Valid values are 1 to 3650.</p>
            tags: <p>A list of key-value pairs to associate with the backup.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_backup_input.CreateDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_backup_output.CreateDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_backup.async_create_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateDbBackup")
        )
        input_: capo_timestream_influxdb.types.create_db_backup_input.CreateDbBackupInput = {
            "name": name,
            "db_resource_id": db_resource_id,
        }
        if retention_days is not None:
            input_["retention_days"] = retention_days
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
        identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_backup_output.GetDbBackupOutput":
        """<p>Returns information about a specific Timestream for InfluxDB backup.</p>

        Args:
            identifier: <p>The identifier of the backup to retrieve information for.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_backup_input.GetDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_backup_output.GetDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_backup.async_get_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbBackup")
        )
        input_: capo_timestream_influxdb.types.get_db_backup_input.GetDbBackupInput = {
            "identifier": identifier
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
        identifier: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.delete_db_backup_output.DeleteDbBackupOutput":
        """<p>Deletes a Timestream for InfluxDB backup.</p>

        Args:
            identifier: <p>The identifier of the backup to delete.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.delete_db_backup_input.DeleteDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.delete_db_backup_output.DeleteDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_backup.async_delete_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDbBackup")
        )
        input_: capo_timestream_influxdb.types.delete_db_backup_input.DeleteDbBackupInput = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        db_resource_id: Optional[
            "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
        ] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_backups_output.ListDbBackupsOutput":
        """<p>Returns a list of Timestream for InfluxDB backups.</p>

        Args:
            db_resource_id: <p>The identifier of the DB instance or DB cluster to list backups for. If not specified, returns all backups in the account and region.</p>
            next_token: <p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_backups_input.ListDbBackupsInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_backups_output.ListDbBackupsOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_backups

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_backups.async_list_db_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbBackups")
        )
        input_: capo_timestream_influxdb.types.list_db_backups_input.ListDbBackupsInput = {}
        if db_resource_id is not None:
            input_["db_resource_id"] = db_resource_id
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

    async def restore_from_db_backup(
        self,
        name: "capo_timestream_influxdb.types.db_resource_name.DbResourceName",
        db_backup_id: "capo_timestream_influxdb.types.db_backup_id.DbBackupId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        restore_to_time: Optional[datetime.datetime] = None,
        restore_mode: Optional[
            "capo_timestream_influxdb.types.restore_mode.RestoreMode"
        ] = None,
        vpc_subnet_ids: Optional[
            "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_timestream_influxdb.types.restore_from_db_backup_output.RestoreFromDbBackupOutput":
        """<p>Restores a Timestream for InfluxDB resource from a backup. By default, a new resource is created. You can optionally restore to the same resource using the REPLACE_EXISTING restore mode.</p>

        Args:
            name: <p>The name of the new resource to create from the restore. If restoring to an existing resource, the name must match the existing resource name.</p>
            db_backup_id: <p>The identifier of the backup to restore from.</p>
            restore_to_time: <p>The point in time to restore to, for continuous backups. Must be within the backup's retention window.</p>
            restore_mode: <p>Specifies whether to restore to a new resource or replace the existing resource. Valid values are NEW_RESOURCE (default) and REPLACE_EXISTING.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs for the restored resource. If not specified, the restored resource uses the same subnets as the backup.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs for the restored resource. If not specified, the restored resource uses the same security groups as the backup.</p>
            publicly_accessible: <p>Specifies whether the restored resource is publicly accessible.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to the specified S3 bucket for the restored resource.</p>
            maintenance_schedule: <p>The maintenance schedule for the restored resource.</p>
            tags: <p>A list of key-value pairs to associate with the restored resource.</p>
            port: <p>The port number on which the restored InfluxDB resource accepts connections.</p>
            network_type: <p>Specifies the network type of the restored resource. Valid values are IPV4 and DUAL.</p>
            deployment_type: <p>Specifies the deployment type of the restored resource. Valid values are SINGLE_AZ, WITH_MULTIAZ_STANDBY, and MULTI_NODE_READ_REPLICAS.</p>
            db_backup_configurations: <p>A list of backup configurations to apply to the restored resource.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the restored resource. Can be a key ID, key ARN, alias name, or alias ARN.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.conflict_exception.ConflictException: <p>The request conflicts with an existing resource in Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.restore_from_db_backup_input.RestoreFromDbBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.restore_from_db_backup_output.RestoreFromDbBackupOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.restore_from_db_backup

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.restore_from_db_backup.async_restore_from_db_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreFromDbBackup")
        )
        input_: capo_timestream_influxdb.types.restore_from_db_backup_input.RestoreFromDbBackupInput = {
            "name": name,
            "db_backup_id": db_backup_id,
        }
        if restore_to_time is not None:
            input_["restore_to_time"] = restore_to_time
        if restore_mode is not None:
            input_["restore_mode"] = restore_mode
        if vpc_subnet_ids is not None:
            input_["vpc_subnet_ids"] = vpc_subnet_ids
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if network_type is not None:
            input_["network_type"] = network_type
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
