"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeleteDbBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.cluster_configuration
    import capo_timestream_influxdb.types.date
    import capo_timestream_influxdb.types.db_backup_id
    import capo_timestream_influxdb.types.db_backup_name
    import capo_timestream_influxdb.types.db_backup_status
    import capo_timestream_influxdb.types.db_backup_type
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_id
    import capo_timestream_influxdb.types.db_resource_id
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.engine_type
    import capo_timestream_influxdb.types.failover_mode
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.resource_deployment_type
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list


class DeleteDbBackupOutput(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_backup_id.DbBackupId"
    """<p>Service-generated unique identifier of the deleted backup.</p>"""
    name: NotRequired["capo_timestream_influxdb.types.db_backup_name.DbBackupName"]
    """<p>The customer-provided name of the deleted backup.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the deleted backup.</p>"""
    status: NotRequired[
        "capo_timestream_influxdb.types.db_backup_status.DbBackupStatus"
    ]
    """<p>The current status of the backup.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when the backup was created.</p>"""
    expires_after: NotRequired["capo_timestream_influxdb.types.date.Date"]
    """<p>The date after which the backup was set to be automatically deleted.</p>"""
    db_resource_id: NotRequired[
        "capo_timestream_influxdb.types.db_resource_id.DbResourceId"
    ]
    """<p>The identifier of the DB resource that the backup was created from.</p>"""
    type: NotRequired["capo_timestream_influxdb.types.db_backup_type.DbBackupType"]
    """<p>The type of backup.</p>"""
    engine_type: NotRequired["capo_timestream_influxdb.types.engine_type.EngineType"]
    """<p>The engine type of the resource that the backup was created from.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
    ]
    """<p>The deployment type of the resource that the backup was created from.</p>"""
    kms_key_id: NotRequired["capo_timestream_influxdb.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key ARN used for encryption of the resource at the time of backup.</p>"""
    cluster_configuration: NotRequired[
        "capo_timestream_influxdb.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>The cluster configuration of the resource at the time of backup.</p>"""
    db_parameter_group_id: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_id.DbParameterGroupId"
    ]
    """<p>The identifier of the DB parameter group associated with the backup.</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The DB instance type of the resource at the time of backup.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>The log delivery configuration of the resource at the time of backup.</p>"""
    failover_mode: NotRequired[
        "capo_timestream_influxdb.types.failover_mode.FailoverMode"
    ]
    """<p>The failover mode of the resource at the time of backup.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The storage type of the resource at the time of backup.</p>"""
    allocated_storage: NotRequired[
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The allocated storage of the resource at the time of backup, in GiB.</p>"""
    vpc_subnet_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    ]
    """<p>The VPC subnet IDs associated with the resource at the time of backup.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>The VPC security group IDs associated with the resource at the time of backup.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Indicates whether the resource was publicly accessible at the time of backup.</p>"""
    port: NotRequired["int"]
    """<p>The port number of the resource at the time of backup.</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>The network type of the resource at the time of backup.</p>"""
    influx_auth_parameters_secret_arn: NotRequired["str"]
    """<p>The ARN of the Secrets Manager secret containing the InfluxDB auth parameters.</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The maintenance schedule of the resource at the time of backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDbBackupOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_timestream_influxdb.types.db_backup_status

        out["status"] = (
            capo_timestream_influxdb.types.db_backup_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_at" in value:
        import capo_timestream_influxdb._protocol.serialize

        out["createdAt"] = capo_timestream_influxdb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "expires_after" in value:
        out["expiresAfter"] = value["expires_after"]
    if "db_resource_id" in value:
        out["dbResourceId"] = value["db_resource_id"]
    if "type" in value:
        import capo_timestream_influxdb.types.db_backup_type

        out["type"] = (
            capo_timestream_influxdb.types.db_backup_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "engine_type" in value:
        import capo_timestream_influxdb.types.engine_type

        out["engineType"] = (
            capo_timestream_influxdb.types.engine_type.serialize_aws_json_1_0(
                value["engine_type"]
            )
        )
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.resource_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "cluster_configuration" in value:
        import capo_timestream_influxdb.types.cluster_configuration

        out["clusterConfiguration"] = (
            capo_timestream_influxdb.types.cluster_configuration.serialize_aws_json_1_0(
                value["cluster_configuration"]
            )
        )
    if "db_parameter_group_id" in value:
        out["dbParameterGroupId"] = value["db_parameter_group_id"]
    if "db_instance_type" in value:
        import capo_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "log_delivery_configuration" in value:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "failover_mode" in value:
        import capo_timestream_influxdb.types.failover_mode

        out["failoverMode"] = (
            capo_timestream_influxdb.types.failover_mode.serialize_aws_json_1_0(
                value["failover_mode"]
            )
        )
    if "db_storage_type" in value:
        import capo_timestream_influxdb.types.db_storage_type

        out["dbStorageType"] = (
            capo_timestream_influxdb.types.db_storage_type.serialize_aws_json_1_0(
                value["db_storage_type"]
            )
        )
    if "allocated_storage" in value:
        out["allocatedStorage"] = value["allocated_storage"]
    if "vpc_subnet_ids" in value:
        import capo_timestream_influxdb.types.vpc_subnet_id_list

        out["vpcSubnetIds"] = (
            capo_timestream_influxdb.types.vpc_subnet_id_list.serialize_aws_json_1_0(
                value["vpc_subnet_ids"]
            )
        )
    if "vpc_security_group_ids" in value:
        import capo_timestream_influxdb.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            capo_timestream_influxdb.types.vpc_security_group_id_list.serialize_aws_json_1_0(
                value["vpc_security_group_ids"]
            )
        )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "port" in value:
        out["port"] = value["port"]
    if "network_type" in value:
        import capo_timestream_influxdb.types.network_type

        out["networkType"] = (
            capo_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "influx_auth_parameters_secret_arn" in value:
        out["influxAuthParametersSecretArn"] = value[
            "influx_auth_parameters_secret_arn"
        ]
    if "maintenance_schedule" in value:
        import capo_timestream_influxdb.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            capo_timestream_influxdb.types.maintenance_schedule.serialize_aws_json_1_0(
                value["maintenance_schedule"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDbBackupOutput:
    out: DeleteDbBackupOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_timestream_influxdb.types.db_backup_status

        out["status"] = (
            capo_timestream_influxdb.types.db_backup_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("expiresAfter") is not None:
        out["expires_after"] = data["expiresAfter"]
    if data.get("dbResourceId") is not None:
        out["db_resource_id"] = data["dbResourceId"]
    if data.get("type") is not None:
        import capo_timestream_influxdb.types.db_backup_type

        out["type"] = (
            capo_timestream_influxdb.types.db_backup_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if data.get("engineType") is not None:
        import capo_timestream_influxdb.types.engine_type

        out["engine_type"] = (
            capo_timestream_influxdb.types.engine_type.deserialize_aws_json_1_0(
                data["engineType"]
            )
        )
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.resource_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("clusterConfiguration") is not None:
        import capo_timestream_influxdb.types.cluster_configuration

        out["cluster_configuration"] = (
            capo_timestream_influxdb.types.cluster_configuration.deserialize_aws_json_1_0(
                data["clusterConfiguration"]
            )
        )
    if data.get("dbParameterGroupId") is not None:
        out["db_parameter_group_id"] = data["dbParameterGroupId"]
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if data.get("logDeliveryConfiguration") is not None:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if data.get("failoverMode") is not None:
        import capo_timestream_influxdb.types.failover_mode

        out["failover_mode"] = (
            capo_timestream_influxdb.types.failover_mode.deserialize_aws_json_1_0(
                data["failoverMode"]
            )
        )
    if data.get("dbStorageType") is not None:
        import capo_timestream_influxdb.types.db_storage_type

        out["db_storage_type"] = (
            capo_timestream_influxdb.types.db_storage_type.deserialize_aws_json_1_0(
                data["dbStorageType"]
            )
        )
    if data.get("allocatedStorage") is not None:
        out["allocated_storage"] = data["allocatedStorage"]
    if data.get("vpcSubnetIds") is not None:
        import capo_timestream_influxdb.types.vpc_subnet_id_list

        out["vpc_subnet_ids"] = (
            capo_timestream_influxdb.types.vpc_subnet_id_list.deserialize_aws_json_1_0(
                data["vpcSubnetIds"]
            )
        )
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_timestream_influxdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_timestream_influxdb.types.vpc_security_group_id_list.deserialize_aws_json_1_0(
                data["vpcSecurityGroupIds"]
            )
        )
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("networkType") is not None:
        import capo_timestream_influxdb.types.network_type

        out["network_type"] = (
            capo_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if data.get("influxAuthParametersSecretArn") is not None:
        out["influx_auth_parameters_secret_arn"] = data["influxAuthParametersSecretArn"]
    if data.get("maintenanceSchedule") is not None:
        import capo_timestream_influxdb.types.maintenance_schedule

        out["maintenance_schedule"] = (
            capo_timestream_influxdb.types.maintenance_schedule.deserialize_aws_json_1_0(
                data["maintenanceSchedule"]
            )
        )
    return out
