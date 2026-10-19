"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#UpdateDbInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_instance_identifier
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.deployment_type
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.port


class UpdateDbInstanceInput(TypedDict, closed=True):
    identifier: (
        "capo_timestream_influxdb.types.db_instance_identifier.DbInstanceIdentifier"
    )
    """<p>The id of the DB instance.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to send to specified S3 bucket.</p>"""
    db_parameter_group_identifier: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p> <p>If you change the Port value, your database restarts immediately.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.deployment_type.DeploymentType"
    ]
    """<p>Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>"""
    allocated_storage: NotRequired[
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage to allocate for your DB storage type (in gibibytes).</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>Specifies the maintenance schedule for the DB instance, including the preferred maintenance window and timezone.</p>"""
    db_backup_configurations: NotRequired[
        "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
    ]
    """<p>A list of backup configurations to update for the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDbInstanceInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "log_delivery_configuration" in value:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "port" in value:
        out["port"] = value["port"]
    if "db_instance_type" in value:
        import capo_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
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
    if "maintenance_schedule" in value:
        import capo_timestream_influxdb.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            capo_timestream_influxdb.types.maintenance_schedule.serialize_aws_json_1_0(
                value["maintenance_schedule"]
            )
        )
    if "db_backup_configurations" in value:
        import capo_timestream_influxdb.types.db_backup_configuration_input_list

        out["dbBackupConfigurations"] = (
            capo_timestream_influxdb.types.db_backup_configuration_input_list.serialize_aws_json_1_0(
                value["db_backup_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDbInstanceInput:
    out: UpdateDbInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("logDeliveryConfiguration") is not None:
        import capo_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            capo_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if data.get("dbParameterGroupIdentifier") is not None:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
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
    if data.get("maintenanceSchedule") is not None:
        import capo_timestream_influxdb.types.maintenance_schedule

        out["maintenance_schedule"] = (
            capo_timestream_influxdb.types.maintenance_schedule.deserialize_aws_json_1_0(
                data["maintenanceSchedule"]
            )
        )
    if data.get("dbBackupConfigurations") is not None:
        import capo_timestream_influxdb.types.db_backup_configuration_input_list

        out["db_backup_configurations"] = (
            capo_timestream_influxdb.types.db_backup_configuration_input_list.deserialize_aws_json_1_0(
                data["dbBackupConfigurations"]
            )
        )
    return out
