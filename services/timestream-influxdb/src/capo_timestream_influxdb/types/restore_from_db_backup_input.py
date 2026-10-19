"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RestoreFromDbBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_backup_id
    import capo_timestream_influxdb.types.db_resource_name
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.request_tag_map
    import capo_timestream_influxdb.types.resource_deployment_type
    import capo_timestream_influxdb.types.restore_mode
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list


class RestoreFromDbBackupInput(TypedDict, closed=True):
    name: "capo_timestream_influxdb.types.db_resource_name.DbResourceName"
    """<p>The name of the new resource to create from the restore. If restoring to an existing resource, the name must match the existing resource name.</p>"""
    db_backup_id: "capo_timestream_influxdb.types.db_backup_id.DbBackupId"
    """<p>The identifier of the backup to restore from.</p>"""
    restore_to_time: NotRequired["datetime.datetime"]
    """<p>The point in time to restore to, for continuous backups. Must be within the backup's retention window.</p>"""
    restore_mode: NotRequired["capo_timestream_influxdb.types.restore_mode.RestoreMode"]
    """<p>Specifies whether to restore to a new resource or replace the existing resource. Valid values are NEW_RESOURCE (default) and REPLACE_EXISTING.</p>"""
    vpc_subnet_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    ]
    """<p>A list of VPC subnet IDs for the restored resource. If not specified, the restored resource uses the same subnets as the backup.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group IDs for the restored resource. If not specified, the restored resource uses the same security groups as the backup.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Specifies whether the restored resource is publicly accessible.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to the specified S3 bucket for the restored resource.</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The maintenance schedule for the restored resource.</p>"""
    tags: NotRequired["capo_timestream_influxdb.types.request_tag_map.RequestTagMap"]
    """<p>A list of key-value pairs to associate with the restored resource.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which the restored InfluxDB resource accepts connections.</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>Specifies the network type of the restored resource. Valid values are IPV4 and DUAL.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.resource_deployment_type.ResourceDeploymentType"
    ]
    """<p>Specifies the deployment type of the restored resource. Valid values are SINGLE_AZ, WITH_MULTIAZ_STANDBY, and MULTI_NODE_READ_REPLICAS.</p>"""
    db_backup_configurations: NotRequired[
        "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
    ]
    """<p>A list of backup configurations to apply to the restored resource.</p>"""
    kms_key_id: NotRequired["capo_timestream_influxdb.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key identifier to use for encryption of the restored resource. Can be a key ID, key ARN, alias name, or alias ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreFromDbBackupInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["dbBackupId"] = value["db_backup_id"]
    if "restore_to_time" in value:
        import capo_timestream_influxdb._protocol.serialize

        out["restoreToTime"] = (
            capo_timestream_influxdb._protocol.serialize.fmt_date_time(
                value["restore_to_time"]
            )
        )
    if "restore_mode" in value:
        import capo_timestream_influxdb.types.restore_mode

        out["restoreMode"] = (
            capo_timestream_influxdb.types.restore_mode.serialize_aws_json_1_0(
                value["restore_mode"]
            )
        )
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
    if "tags" in value:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    if "network_type" in value:
        import capo_timestream_influxdb.types.network_type

        out["networkType"] = (
            capo_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.resource_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "db_backup_configurations" in value:
        import capo_timestream_influxdb.types.db_backup_configuration_input_list

        out["dbBackupConfigurations"] = (
            capo_timestream_influxdb.types.db_backup_configuration_input_list.serialize_aws_json_1_0(
                value["db_backup_configurations"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreFromDbBackupInput:
    out: RestoreFromDbBackupInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dbBackupId") is not None:
        out["db_backup_id"] = data["dbBackupId"]
    else:
        out["db_backup_id"] = ""
    if data.get("restoreToTime") is not None:
        import datetime

        out["restore_to_time"] = datetime.datetime.fromisoformat(
            data["restoreToTime"].replace("Z", "+00:00")
        )
    if data.get("restoreMode") is not None:
        import capo_timestream_influxdb.types.restore_mode

        out["restore_mode"] = (
            capo_timestream_influxdb.types.restore_mode.deserialize_aws_json_1_0(
                data["restoreMode"]
            )
        )
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
    if data.get("tags") is not None:
        import capo_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            capo_timestream_influxdb.types.request_tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("networkType") is not None:
        import capo_timestream_influxdb.types.network_type

        out["network_type"] = (
            capo_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.resource_deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.resource_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if data.get("dbBackupConfigurations") is not None:
        import capo_timestream_influxdb.types.db_backup_configuration_input_list

        out["db_backup_configurations"] = (
            capo_timestream_influxdb.types.db_backup_configuration_input_list.deserialize_aws_json_1_0(
                data["dbBackupConfigurations"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
