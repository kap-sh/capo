"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.arn
    import capo_timestream_influxdb.types.db_backup_configuration_output_list
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_instance_id
    import capo_timestream_influxdb.types.db_instance_name
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.deployment_type
    import capo_timestream_influxdb.types.instance_mode
    import capo_timestream_influxdb.types.instance_mode_list
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.status
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list


class GetDbInstanceOutput(TypedDict, closed=True):
    id: "capo_timestream_influxdb.types.db_instance_id.DbInstanceId"
    """<p>A service-generated unique identifier.</p>"""
    name: "capo_timestream_influxdb.types.db_instance_name.DbInstanceName"
    """<p>The customer-supplied name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands.</p>"""
    arn: "capo_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB instance.</p>"""
    status: NotRequired["capo_timestream_influxdb.types.status.Status"]
    """<p>The status of the DB instance.</p>"""
    endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB instance type that InfluxDB runs on.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>"""
    allocated_storage: NotRequired[
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage allocated for your DB storage type (in gibibytes).</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.deployment_type.DeploymentType"
    ]
    """<p>Specifies whether the Timestream for InfluxDB is deployed as Single-AZ or with a MultiAZ Standby for High availability.</p>"""
    vpc_subnet_ids: "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    """<p>A list of VPC subnet IDs associated with the DB instance.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Indicates if the DB instance has a public IP to facilitate access.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group IDs associated with the DB instance.</p>"""
    db_parameter_group_identifier: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The id of the DB parameter group assigned to your DB instance.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone in which the DB instance resides.</p>"""
    secondary_availability_zone: NotRequired["str"]
    """<p>The Availability Zone in which the standby instance is located when deploying with a MultiAZ standby instance.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to send to specified S3 bucket.</p>"""
    influx_auth_parameters_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.</p>"""
    db_cluster_id: NotRequired[
        "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    ]
    """<p>Specifies the DbCluster to which this DbInstance belongs to.</p>"""
    instance_mode: NotRequired[
        "capo_timestream_influxdb.types.instance_mode.InstanceMode"
    ]
    """<p>Specifies the DbInstance's role in the cluster.</p>"""
    instance_modes: NotRequired[
        "capo_timestream_influxdb.types.instance_mode_list.InstanceModeList"
    ]
    """<p>Specifies the DbInstance's roles in the cluster.</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The maintenance schedule for the DB instance.</p>"""
    last_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the last completed maintenance operation on the DB instance.</p>"""
    next_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the next scheduled maintenance operation on the DB instance.</p>"""
    db_backup_configurations: NotRequired[
        "capo_timestream_influxdb.types.db_backup_configuration_output_list.DbBackupConfigurationOutputList"
    ]
    """<p>The backup configurations for the DB instance.</p>"""
    kms_key_id: NotRequired["capo_timestream_influxdb.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key ARN used for encryption of the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import capo_timestream_influxdb.types.status

        out["status"] = capo_timestream_influxdb.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "port" in value:
        out["port"] = value["port"]
    if "network_type" in value:
        import capo_timestream_influxdb.types.network_type

        out["networkType"] = (
            capo_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "db_instance_type" in value:
        import capo_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
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
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    import capo_timestream_influxdb.types.vpc_subnet_id_list

    out["vpcSubnetIds"] = (
        capo_timestream_influxdb.types.vpc_subnet_id_list.serialize_aws_json_1_0(
            value["vpc_subnet_ids"]
        )
    )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "vpc_security_group_ids" in value:
        import capo_timestream_influxdb.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            capo_timestream_influxdb.types.vpc_security_group_id_list.serialize_aws_json_1_0(
                value["vpc_security_group_ids"]
            )
        )
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "secondary_availability_zone" in value:
        out["secondaryAvailabilityZone"] = value["secondary_availability_zone"]
    if "log_delivery_configuration" in value:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "influx_auth_parameters_secret_arn" in value:
        out["influxAuthParametersSecretArn"] = value[
            "influx_auth_parameters_secret_arn"
        ]
    if "db_cluster_id" in value:
        out["dbClusterId"] = value["db_cluster_id"]
    if "instance_mode" in value:
        import capo_timestream_influxdb.types.instance_mode

        out["instanceMode"] = (
            capo_timestream_influxdb.types.instance_mode.serialize_aws_json_1_0(
                value["instance_mode"]
            )
        )
    if "instance_modes" in value:
        import capo_timestream_influxdb.types.instance_mode_list

        out["instanceModes"] = (
            capo_timestream_influxdb.types.instance_mode_list.serialize_aws_json_1_0(
                value["instance_modes"]
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


def deserialize_aws_json_1_0(data: dict) -> GetDbInstanceOutput:
    out: GetDbInstanceOutput = {}  # type: ignore[typeddict-item]
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
        import capo_timestream_influxdb.types.status

        out["status"] = capo_timestream_influxdb.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("networkType") is not None:
        import capo_timestream_influxdb.types.network_type

        out["network_type"] = (
            capo_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
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
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if data.get("vpcSubnetIds") is not None:
        import capo_timestream_influxdb.types.vpc_subnet_id_list

        out["vpc_subnet_ids"] = (
            capo_timestream_influxdb.types.vpc_subnet_id_list.deserialize_aws_json_1_0(
                data["vpcSubnetIds"]
            )
        )
    else:
        out["vpc_subnet_ids"] = []
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_timestream_influxdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_timestream_influxdb.types.vpc_security_group_id_list.deserialize_aws_json_1_0(
                data["vpcSecurityGroupIds"]
            )
        )
    if data.get("dbParameterGroupIdentifier") is not None:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("secondaryAvailabilityZone") is not None:
        out["secondary_availability_zone"] = data["secondaryAvailabilityZone"]
    if data.get("logDeliveryConfiguration") is not None:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if data.get("influxAuthParametersSecretArn") is not None:
        out["influx_auth_parameters_secret_arn"] = data["influxAuthParametersSecretArn"]
    if data.get("dbClusterId") is not None:
        out["db_cluster_id"] = data["dbClusterId"]
    if data.get("instanceMode") is not None:
        import capo_timestream_influxdb.types.instance_mode

        out["instance_mode"] = (
            capo_timestream_influxdb.types.instance_mode.deserialize_aws_json_1_0(
                data["instanceMode"]
            )
        )
    if data.get("instanceModes") is not None:
        import capo_timestream_influxdb.types.instance_mode_list

        out["instance_modes"] = (
            capo_timestream_influxdb.types.instance_mode_list.deserialize_aws_json_1_0(
                data["instanceModes"]
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
