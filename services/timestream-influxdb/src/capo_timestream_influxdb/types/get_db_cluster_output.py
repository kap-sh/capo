"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.cluster_configuration
    import capo_timestream_influxdb.types.cluster_deployment_type
    import capo_timestream_influxdb.types.cluster_status
    import capo_timestream_influxdb.types.db_backup_configuration_output_list
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_cluster_name
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.engine_type
    import capo_timestream_influxdb.types.failover_mode
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list


class GetDbClusterOutput(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to retrieve.</p>"""
    name: "capo_timestream_influxdb.types.db_cluster_name.DbClusterName"
    """<p>Customer-supplied name of the Timestream for InfluxDB cluster.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB cluster.</p>"""
    status: NotRequired["capo_timestream_influxdb.types.cluster_status.ClusterStatus"]
    """<p>The status of the DB cluster.</p>"""
    endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to the Timestream for InfluxDB cluster for write and read operations.</p>"""
    reader_endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to the Timestream for InfluxDB cluster for read-only operations.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
    ]
    """<p>Deployment type of the DB cluster.</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB instance type that InfluxDB runs on.</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>"""
    allocated_storage: NotRequired[
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage allocated for your DB storage type (in gibibytes).</p>"""
    engine_type: NotRequired["capo_timestream_influxdb.types.engine_type.EngineType"]
    """<p>The engine type of your DB cluster.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Indicates if the DB cluster has a public IP to facilitate access from outside the VPC.</p>"""
    db_parameter_group_identifier: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The ID of the DB parameter group assigned to your DB cluster.</p>"""
    effective_db_parameter_group_identifier: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The ID of the DB parameter group actually applied to your DB cluster. When the service applies optimized defaults, it creates a service-managed DB parameter group and this field reflects that group, while dbParameterGroupIdentifier reflects the customer-provided DB parameter group. When no service-managed DB parameter group is applied, this value matches dbParameterGroupIdentifier.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to send to specified S3 bucket.</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The maintenance schedule for the DB cluster.</p>"""
    last_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the last completed maintenance operation on the DB cluster.</p>"""
    next_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the next scheduled maintenance operation on the DB cluster.</p>"""
    influx_auth_parameters_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.</p>"""
    vpc_subnet_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    ]
    """<p>A list of VPC subnet IDs associated with the DB cluster.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group IDs associated with the DB cluster.</p>"""
    failover_mode: NotRequired[
        "capo_timestream_influxdb.types.failover_mode.FailoverMode"
    ]
    """<p>The configured failover mode for the DB cluster.</p>"""
    cluster_configuration: NotRequired[
        "capo_timestream_influxdb.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>Configuration for node modes in the DbCluster.</p>"""
    db_backup_configurations: NotRequired[
        "capo_timestream_influxdb.types.db_backup_configuration_output_list.DbBackupConfigurationOutputList"
    ]
    """<p>The backup configurations for the DB cluster.</p>"""
    kms_key_id: NotRequired["capo_timestream_influxdb.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key ARN used for encryption of the DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbClusterOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_timestream_influxdb.types.cluster_status

        out["status"] = (
            capo_timestream_influxdb.types.cluster_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "reader_endpoint" in value:
        out["readerEndpoint"] = value["reader_endpoint"]
    if "port" in value:
        out["port"] = value["port"]
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.cluster_deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.cluster_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "db_instance_type" in value:
        import capo_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "network_type" in value:
        import capo_timestream_influxdb.types.network_type

        out["networkType"] = (
            capo_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
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
    if "engine_type" in value:
        import capo_timestream_influxdb.types.engine_type

        out["engineType"] = (
            capo_timestream_influxdb.types.engine_type.serialize_aws_json_1_0(
                value["engine_type"]
            )
        )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "effective_db_parameter_group_identifier" in value:
        out["effectiveDbParameterGroupIdentifier"] = value[
            "effective_db_parameter_group_identifier"
        ]
    if "log_delivery_configuration" in value:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "maintenance_schedule" in value:
        import capo_timestream_influxdb.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            capo_timestream_influxdb.types.maintenance_schedule.serialize_aws_json_1_0(
                value["maintenance_schedule"]
            )
        )
    if "last_maintenance_time" in value:
        import capo_timestream_influxdb._protocol.serialize

        out["lastMaintenanceTime"] = (
            capo_timestream_influxdb._protocol.serialize.fmt_date_time(
                value["last_maintenance_time"]
            )
        )
    if "next_maintenance_time" in value:
        import capo_timestream_influxdb._protocol.serialize

        out["nextMaintenanceTime"] = (
            capo_timestream_influxdb._protocol.serialize.fmt_date_time(
                value["next_maintenance_time"]
            )
        )
    if "influx_auth_parameters_secret_arn" in value:
        out["influxAuthParametersSecretArn"] = value[
            "influx_auth_parameters_secret_arn"
        ]
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
    if "failover_mode" in value:
        import capo_timestream_influxdb.types.failover_mode

        out["failoverMode"] = (
            capo_timestream_influxdb.types.failover_mode.serialize_aws_json_1_0(
                value["failover_mode"]
            )
        )
    if "cluster_configuration" in value:
        import capo_timestream_influxdb.types.cluster_configuration

        out["clusterConfiguration"] = (
            capo_timestream_influxdb.types.cluster_configuration.serialize_aws_json_1_0(
                value["cluster_configuration"]
            )
        )
    if "db_backup_configurations" in value:
        import capo_timestream_influxdb.types.db_backup_configuration_output_list

        out["dbBackupConfigurations"] = (
            capo_timestream_influxdb.types.db_backup_configuration_output_list.serialize_aws_json_1_0(
                value["db_backup_configurations"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbClusterOutput:
    out: GetDbClusterOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_timestream_influxdb.types.cluster_status

        out["status"] = (
            capo_timestream_influxdb.types.cluster_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("readerEndpoint") is not None:
        out["reader_endpoint"] = data["readerEndpoint"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.cluster_deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.cluster_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if data.get("networkType") is not None:
        import capo_timestream_influxdb.types.network_type

        out["network_type"] = (
            capo_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
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
    if data.get("engineType") is not None:
        import capo_timestream_influxdb.types.engine_type

        out["engine_type"] = (
            capo_timestream_influxdb.types.engine_type.deserialize_aws_json_1_0(
                data["engineType"]
            )
        )
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("dbParameterGroupIdentifier") is not None:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if data.get("effectiveDbParameterGroupIdentifier") is not None:
        out["effective_db_parameter_group_identifier"] = data[
            "effectiveDbParameterGroupIdentifier"
        ]
    if data.get("logDeliveryConfiguration") is not None:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if data.get("maintenanceSchedule") is not None:
        import capo_timestream_influxdb.types.maintenance_schedule

        out["maintenance_schedule"] = (
            capo_timestream_influxdb.types.maintenance_schedule.deserialize_aws_json_1_0(
                data["maintenanceSchedule"]
            )
        )
    if data.get("lastMaintenanceTime") is not None:
        import datetime

        out["last_maintenance_time"] = datetime.datetime.fromisoformat(
            data["lastMaintenanceTime"].replace("Z", "+00:00")
        )
    if data.get("nextMaintenanceTime") is not None:
        import datetime

        out["next_maintenance_time"] = datetime.datetime.fromisoformat(
            data["nextMaintenanceTime"].replace("Z", "+00:00")
        )
    if data.get("influxAuthParametersSecretArn") is not None:
        out["influx_auth_parameters_secret_arn"] = data["influxAuthParametersSecretArn"]
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
    if data.get("failoverMode") is not None:
        import capo_timestream_influxdb.types.failover_mode

        out["failover_mode"] = (
            capo_timestream_influxdb.types.failover_mode.deserialize_aws_json_1_0(
                data["failoverMode"]
            )
        )
    if data.get("clusterConfiguration") is not None:
        import capo_timestream_influxdb.types.cluster_configuration

        out["cluster_configuration"] = (
            capo_timestream_influxdb.types.cluster_configuration.deserialize_aws_json_1_0(
                data["clusterConfiguration"]
            )
        )
    if data.get("dbBackupConfigurations") is not None:
        import capo_timestream_influxdb.types.db_backup_configuration_output_list

        out["db_backup_configurations"] = (
            capo_timestream_influxdb.types.db_backup_configuration_output_list.deserialize_aws_json_1_0(
                data["dbBackupConfigurations"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
