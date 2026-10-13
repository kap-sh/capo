from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

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
    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.bucket
    import capo_timestream_influxdb.types.cluster_deployment_type
    import capo_timestream_influxdb.types.create_db_cluster_input
    import capo_timestream_influxdb.types.create_db_cluster_output
    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_cluster_name
    import capo_timestream_influxdb.types.db_cluster_summary
    import capo_timestream_influxdb.types.db_instance_for_cluster_summary
    import capo_timestream_influxdb.types.db_instance_id_list
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.delete_db_cluster_input
    import capo_timestream_influxdb.types.delete_db_cluster_output
    import capo_timestream_influxdb.types.failover_mode
    import capo_timestream_influxdb.types.get_db_cluster_input
    import capo_timestream_influxdb.types.get_db_cluster_output
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.list_db_clusters_input
    import capo_timestream_influxdb.types.list_db_clusters_output
    import capo_timestream_influxdb.types.list_db_instances_for_cluster_input
    import capo_timestream_influxdb.types.list_db_instances_for_cluster_output
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.next_token
    import capo_timestream_influxdb.types.organization
    import capo_timestream_influxdb.types.password
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.reboot_db_cluster_input
    import capo_timestream_influxdb.types.reboot_db_cluster_output
    import capo_timestream_influxdb.types.request_tag_map
    import capo_timestream_influxdb.types.update_db_cluster_input
    import capo_timestream_influxdb.types.update_db_cluster_output
    import capo_timestream_influxdb.types.username
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


class DbClusterResource:
    def __init__(self, service: TimestreamInfluxDBClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_timestream_influxdb.types.db_cluster_name.DbClusterName",
        db_instance_type: "capo_timestream_influxdb.types.db_instance_type.DbInstanceType",
        vpc_subnet_ids: "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList",
        vpc_security_group_ids: "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        username: Optional["capo_timestream_influxdb.types.username.Username"] = None,
        password: Optional["capo_timestream_influxdb.types.password.Password"] = None,
        organization: Optional[
            "capo_timestream_influxdb.types.organization.Organization"
        ] = None,
        bucket: Optional["capo_timestream_influxdb.types.bucket.Bucket"] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        db_storage_type: Optional[
            "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
        ] = None,
        allocated_storage: Optional[
            "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
        ] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
        ] = None,
        failover_mode: Optional[
            "capo_timestream_influxdb.types.failover_mode.FailoverMode"
        ] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.create_db_cluster_output.CreateDbClusterOutput"
    ):
        """<p>Creates a new Timestream for InfluxDB cluster.</p>

        Args:
            name: <p>The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB cluster names must be unique per customer and per region.</p>
            username: <p>The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>
            password: <p>The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>
            organization: <p>The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.</p>
            bucket: <p>The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.</p>
            port: <p>The port number on which InfluxDB accepts connections.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086 for InfluxDB v2, 8181 for InfluxDB v3</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>
            db_parameter_group_identifier: <p>The ID of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>
            db_instance_type: <p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>
            db_storage_type: <p>The Timestream for InfluxDB DB storage type to read and write InfluxDB data.</p> <p>You can choose between three different types of provisioned Influx IOPS Included storage according to your workload requirements:</p> <ul> <li> <p>Influx I/O Included 3000 IOPS</p> </li> <li> <p>Influx I/O Included 12000 IOPS</p> </li> <li> <p>Influx I/O Included 16000 IOPS</p> </li> </ul>
            allocated_storage: <p>The amount of storage to allocate for your DB storage type in GiB (gibibytes).</p>
            network_type: <p>Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>
            publicly_accessible: <p>Configures the Timestream for InfluxDB cluster with a public IP to facilitate access from outside the VPC.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs to associate with the DB cluster. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs to associate with the Timestream for InfluxDB cluster.</p>
            deployment_type: <p>Specifies the type of cluster to create.</p>
            failover_mode: <p>Specifies the behavior of failure recovery when the primary node of the cluster fails.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to a specified S3 bucket.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to enable automated backups for the DB cluster.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the DB cluster. Can be a key ID, key ARN, alias name, or alias ARN.</p>
            tags: <p>A list of key-value pairs to associate with the DB instance.</p>

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
            req: "OperationRequest[capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.create_db_cluster_output.CreateDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_cluster

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_cluster.create_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput",
        ) -> dict[str, Any]:
            import capo_timestream_influxdb.types.create_db_cluster_input

            return (
                capo_timestream_influxdb.types.create_db_cluster_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDbCluster", redact_input=_redact_input),
        )
        input_: capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput = {
            "name": name,
            "db_instance_type": db_instance_type,
            "vpc_subnet_ids": vpc_subnet_ids,
            "vpc_security_group_ids": vpc_security_group_ids,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if organization is not None:
            input_["organization"] = organization
        if bucket is not None:
            input_["bucket"] = bucket
        if port is not None:
            input_["port"] = port
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if db_storage_type is not None:
            input_["db_storage_type"] = db_storage_type
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if network_type is not None:
            input_["network_type"] = network_type
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if failover_mode is not None:
            input_["failover_mode"] = failover_mode
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_cluster_output.GetDbClusterOutput":
        """<p>Retrieves information about a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to retrieve.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_timestream_influxdb.types.get_db_cluster_input.GetDbClusterInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.get_db_cluster_output.GetDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_cluster

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_cluster.get_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbCluster")
        )
        input_: capo_timestream_influxdb.types.get_db_cluster_input.GetDbClusterInput = {
            "db_cluster_id": db_cluster_id
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
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_instance_type: Optional[
            "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
        ] = None,
        failover_mode: Optional[
            "capo_timestream_influxdb.types.failover_mode.FailoverMode"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.update_db_cluster_output.UpdateDbClusterOutput"
    ):
        """<p>Updates a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to update.</p>
            log_delivery_configuration: <p>The log delivery configuration to apply to the DB cluster.</p>
            db_parameter_group_identifier: <p>Update the DB cluster to use the specified DB parameter group.</p>
            port: <p>Update the DB cluster to use the specified port.</p>
            db_instance_type: <p>Update the DB cluster to use the specified DB instance Type.</p>
            failover_mode: <p>Update the DB cluster's failover behavior.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to update for the DB cluster.</p>

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
            req: "OperationRequest[capo_timestream_influxdb.types.update_db_cluster_input.UpdateDbClusterInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.update_db_cluster_output.UpdateDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_cluster

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_cluster.update_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDbCluster")
        )
        input_: capo_timestream_influxdb.types.update_db_cluster_input.UpdateDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if port is not None:
            input_["port"] = port
        if db_instance_type is not None:
            input_["db_instance_type"] = db_instance_type
        if failover_mode is not None:
            input_["failover_mode"] = failover_mode
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        retain_automated_backups: Optional[bool] = None,
    ) -> (
        "capo_timestream_influxdb.types.delete_db_cluster_output.DeleteDbClusterOutput"
    ):
        """<p>Deletes a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster.</p>
            retain_automated_backups: <p>Specifies whether to retain automated backups after the DB cluster is deleted. If set to true, automated backups are not deleted and can be restored later.</p>

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
            req: "OperationRequest[capo_timestream_influxdb.types.delete_db_cluster_input.DeleteDbClusterInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.delete_db_cluster_output.DeleteDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_cluster

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_cluster.delete_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDbCluster")
        )
        input_: capo_timestream_influxdb.types.delete_db_cluster_input.DeleteDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if retain_automated_backups is not None:
            input_["retain_automated_backups"] = retain_automated_backups

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
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_clusters_output.ListDbClustersOutput":
        """<p>Returns a list of Timestream for InfluxDB DB clusters.</p>

        Args:
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
            req: "OperationRequest[capo_timestream_influxdb.types.list_db_clusters_input.ListDbClustersInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.list_db_clusters_output.ListDbClustersOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_clusters

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_clusters.list_db_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbClusters")
        )
        input_: capo_timestream_influxdb.types.list_db_clusters_input.ListDbClustersInput = {}
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

    def list_db_instances_for_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_instances_for_cluster_output.ListDbInstancesForClusterOutput":
        """<p>Returns a list of Timestream for InfluxDB clusters.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster.</p>
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
            req: "OperationRequest[capo_timestream_influxdb.types.list_db_instances_for_cluster_input.ListDbInstancesForClusterInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.list_db_instances_for_cluster_output.ListDbInstancesForClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances_for_cluster

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances_for_cluster.list_db_instances_for_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbInstancesForCluster")
        )
        input_: capo_timestream_influxdb.types.list_db_instances_for_cluster_input.ListDbInstancesForClusterInput = {
            "db_cluster_id": db_cluster_id
        }
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

    def reboot_db_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[TimestreamInfluxDBClientConfig] = None,
        instance_ids: Optional[
            "capo_timestream_influxdb.types.db_instance_id_list.DbInstanceIdList"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.reboot_db_cluster_output.RebootDbClusterOutput"
    ):
        """<p>Reboots a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to reboot.</p>
            instance_ids: <p>A list of service-generated unique DB Instance Ids belonging to the DB Cluster to reboot.</p>

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
            req: "OperationRequest[capo_timestream_influxdb.types.reboot_db_cluster_input.RebootDbClusterInput]",
        ) -> OperationResponse[
            "capo_timestream_influxdb.types.reboot_db_cluster_output.RebootDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_cluster

            output, http_response = (
                capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_cluster.reboot_db_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RebootDbCluster")
        )
        input_: capo_timestream_influxdb.types.reboot_db_cluster_input.RebootDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDbClusterResource:
    def __init__(self, service: AsyncTimestreamInfluxDBClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_timestream_influxdb.types.db_cluster_name.DbClusterName",
        db_instance_type: "capo_timestream_influxdb.types.db_instance_type.DbInstanceType",
        vpc_subnet_ids: "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList",
        vpc_security_group_ids: "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        username: Optional["capo_timestream_influxdb.types.username.Username"] = None,
        password: Optional["capo_timestream_influxdb.types.password.Password"] = None,
        organization: Optional[
            "capo_timestream_influxdb.types.organization.Organization"
        ] = None,
        bucket: Optional["capo_timestream_influxdb.types.bucket.Bucket"] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        db_storage_type: Optional[
            "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
        ] = None,
        allocated_storage: Optional[
            "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
        ] = None,
        network_type: Optional[
            "capo_timestream_influxdb.types.network_type.NetworkType"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        deployment_type: Optional[
            "capo_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
        ] = None,
        failover_mode: Optional[
            "capo_timestream_influxdb.types.failover_mode.FailoverMode"
        ] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
        kms_key_id: Optional[
            "capo_timestream_influxdb.types.kms_key_id.KmsKeyId"
        ] = None,
        tags: Optional[
            "capo_timestream_influxdb.types.request_tag_map.RequestTagMap"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.create_db_cluster_output.CreateDbClusterOutput"
    ):
        """<p>Creates a new Timestream for InfluxDB cluster.</p>

        Args:
            name: <p>The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB cluster names must be unique per customer and per region.</p>
            username: <p>The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>
            password: <p>The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>
            organization: <p>The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.</p>
            bucket: <p>The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.</p>
            port: <p>The port number on which InfluxDB accepts connections.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086 for InfluxDB v2, 8181 for InfluxDB v3</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>
            db_parameter_group_identifier: <p>The ID of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>
            db_instance_type: <p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>
            db_storage_type: <p>The Timestream for InfluxDB DB storage type to read and write InfluxDB data.</p> <p>You can choose between three different types of provisioned Influx IOPS Included storage according to your workload requirements:</p> <ul> <li> <p>Influx I/O Included 3000 IOPS</p> </li> <li> <p>Influx I/O Included 12000 IOPS</p> </li> <li> <p>Influx I/O Included 16000 IOPS</p> </li> </ul>
            allocated_storage: <p>The amount of storage to allocate for your DB storage type in GiB (gibibytes).</p>
            network_type: <p>Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>
            publicly_accessible: <p>Configures the Timestream for InfluxDB cluster with a public IP to facilitate access from outside the VPC.</p>
            vpc_subnet_ids: <p>A list of VPC subnet IDs to associate with the DB cluster. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.</p>
            vpc_security_group_ids: <p>A list of VPC security group IDs to associate with the Timestream for InfluxDB cluster.</p>
            deployment_type: <p>Specifies the type of cluster to create.</p>
            failover_mode: <p>Specifies the behavior of failure recovery when the primary node of the cluster fails.</p>
            log_delivery_configuration: <p>Configuration for sending InfluxDB engine logs to a specified S3 bucket.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to enable automated backups for the DB cluster.</p>
            kms_key_id: <p>The Amazon Web Services KMS key identifier to use for encryption of the DB cluster. Can be a key ID, key ARN, alias name, or alias ARN.</p>
            tags: <p>A list of key-value pairs to associate with the DB instance.</p>

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
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.create_db_cluster_output.CreateDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_cluster.async_create_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput",
        ) -> dict[str, Any]:
            import capo_timestream_influxdb.types.create_db_cluster_input

            return (
                capo_timestream_influxdb.types.create_db_cluster_input.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDbCluster", redact_input=_redact_input),
        )
        input_: capo_timestream_influxdb.types.create_db_cluster_input.CreateDbClusterInput = {
            "name": name,
            "db_instance_type": db_instance_type,
            "vpc_subnet_ids": vpc_subnet_ids,
            "vpc_security_group_ids": vpc_security_group_ids,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if organization is not None:
            input_["organization"] = organization
        if bucket is not None:
            input_["bucket"] = bucket
        if port is not None:
            input_["port"] = port
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if db_storage_type is not None:
            input_["db_storage_type"] = db_storage_type
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if network_type is not None:
            input_["network_type"] = network_type
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if deployment_type is not None:
            input_["deployment_type"] = deployment_type
        if failover_mode is not None:
            input_["failover_mode"] = failover_mode
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
    ) -> "capo_timestream_influxdb.types.get_db_cluster_output.GetDbClusterOutput":
        """<p>Retrieves information about a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to retrieve.</p>

        Raises:
            capo_timestream_influxdb.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_timestream_influxdb.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_timestream_influxdb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found or does not exist.</p>
            capo_timestream_influxdb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_timestream_influxdb.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Timestream for InfluxDB.</p>
            capo_timestream_influxdb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.get_db_cluster_input.GetDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.get_db_cluster_output.GetDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_cluster.async_get_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbCluster")
        )
        input_: capo_timestream_influxdb.types.get_db_cluster_input.GetDbClusterInput = {
            "db_cluster_id": db_cluster_id
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
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        log_delivery_configuration: Optional[
            "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
        ] = None,
        db_parameter_group_identifier: Optional[
            "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
        ] = None,
        port: Optional["capo_timestream_influxdb.types.port.Port"] = None,
        db_instance_type: Optional[
            "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
        ] = None,
        failover_mode: Optional[
            "capo_timestream_influxdb.types.failover_mode.FailoverMode"
        ] = None,
        maintenance_schedule: Optional[
            "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
        ] = None,
        db_backup_configurations: Optional[
            "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.update_db_cluster_output.UpdateDbClusterOutput"
    ):
        """<p>Updates a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to update.</p>
            log_delivery_configuration: <p>The log delivery configuration to apply to the DB cluster.</p>
            db_parameter_group_identifier: <p>Update the DB cluster to use the specified DB parameter group.</p>
            port: <p>Update the DB cluster to use the specified port.</p>
            db_instance_type: <p>Update the DB cluster to use the specified DB instance Type.</p>
            failover_mode: <p>Update the DB cluster's failover behavior.</p>
            maintenance_schedule: <p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>
            db_backup_configurations: <p>A list of backup configurations to update for the DB cluster.</p>

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
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.update_db_cluster_input.UpdateDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.update_db_cluster_output.UpdateDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.update_db_cluster.async_update_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDbCluster")
        )
        input_: capo_timestream_influxdb.types.update_db_cluster_input.UpdateDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if log_delivery_configuration is not None:
            input_["log_delivery_configuration"] = log_delivery_configuration
        if db_parameter_group_identifier is not None:
            input_["db_parameter_group_identifier"] = db_parameter_group_identifier
        if port is not None:
            input_["port"] = port
        if db_instance_type is not None:
            input_["db_instance_type"] = db_instance_type
        if failover_mode is not None:
            input_["failover_mode"] = failover_mode
        if maintenance_schedule is not None:
            input_["maintenance_schedule"] = maintenance_schedule
        if db_backup_configurations is not None:
            input_["db_backup_configurations"] = db_backup_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        retain_automated_backups: Optional[bool] = None,
    ) -> (
        "capo_timestream_influxdb.types.delete_db_cluster_output.DeleteDbClusterOutput"
    ):
        """<p>Deletes a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster.</p>
            retain_automated_backups: <p>Specifies whether to retain automated backups after the DB cluster is deleted. If set to true, automated backups are not deleted and can be restored later.</p>

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
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.delete_db_cluster_input.DeleteDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.delete_db_cluster_output.DeleteDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.delete_db_cluster.async_delete_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDbCluster")
        )
        input_: capo_timestream_influxdb.types.delete_db_cluster_input.DeleteDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if retain_automated_backups is not None:
            input_["retain_automated_backups"] = retain_automated_backups

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
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_clusters_output.ListDbClustersOutput":
        """<p>Returns a list of Timestream for InfluxDB DB clusters.</p>

        Args:
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
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_clusters_input.ListDbClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_clusters_output.ListDbClustersOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_clusters

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_clusters.async_list_db_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbClusters")
        )
        input_: capo_timestream_influxdb.types.list_db_clusters_input.ListDbClustersInput = {}
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

    async def list_db_instances_for_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        next_token: Optional[
            "capo_timestream_influxdb.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_timestream_influxdb.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_timestream_influxdb.types.list_db_instances_for_cluster_output.ListDbInstancesForClusterOutput":
        """<p>Returns a list of Timestream for InfluxDB clusters.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster.</p>
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
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.list_db_instances_for_cluster_input.ListDbInstancesForClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.list_db_instances_for_cluster_output.ListDbInstancesForClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances_for_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_instances_for_cluster.async_list_db_instances_for_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbInstancesForCluster")
        )
        input_: capo_timestream_influxdb.types.list_db_instances_for_cluster_input.ListDbInstancesForClusterInput = {
            "db_cluster_id": db_cluster_id
        }
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

    async def reboot_db_cluster(
        self,
        db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId",
        *,
        config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None,
        instance_ids: Optional[
            "capo_timestream_influxdb.types.db_instance_id_list.DbInstanceIdList"
        ] = None,
    ) -> (
        "capo_timestream_influxdb.types.reboot_db_cluster_output.RebootDbClusterOutput"
    ):
        """<p>Reboots a Timestream for InfluxDB cluster.</p>

        Args:
            db_cluster_id: <p>Service-generated unique identifier of the DB cluster to reboot.</p>
            instance_ids: <p>A list of service-generated unique DB Instance Ids belonging to the DB Cluster to reboot.</p>

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
            req: "AsyncOperationRequest[capo_timestream_influxdb.types.reboot_db_cluster_input.RebootDbClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_timestream_influxdb.types.reboot_db_cluster_output.RebootDbClusterOutput"
        ]:
            import capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_cluster

            (
                output,
                http_response,
            ) = await capo_timestream_influxdb._operations.amazon_timestream_influx_db.reboot_db_cluster.async_reboot_db_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RebootDbCluster")
        )
        input_: capo_timestream_influxdb.types.reboot_db_cluster_input.RebootDbClusterInput = {
            "db_cluster_id": db_cluster_id
        }
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
