"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#UpdateDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.failover_mode
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.port


class UpdateDbClusterInput(TypedDict, closed=True):
    db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to update.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>The log delivery configuration to apply to the DB cluster.</p>"""
    db_parameter_group_identifier: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>Update the DB cluster to use the specified DB parameter group.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>Update the DB cluster to use the specified port.</p>"""
    db_instance_type: NotRequired[
        "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>Update the DB cluster to use the specified DB instance Type.</p>"""
    failover_mode: NotRequired[
        "capo_timestream_influxdb.types.failover_mode.FailoverMode"
    ]
    """<p>Update the DB cluster's failover behavior.</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>"""
    db_backup_configurations: NotRequired[
        "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
    ]
    """<p>A list of backup configurations to update for the DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
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
    if "failover_mode" in value:
        import capo_timestream_influxdb.types.failover_mode

        out["failoverMode"] = (
            capo_timestream_influxdb.types.failover_mode.serialize_aws_json_1_0(
                value["failover_mode"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> UpdateDbClusterInput:
    out: UpdateDbClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("dbClusterId") is not None:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        out["db_cluster_id"] = ""
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
    if data.get("failoverMode") is not None:
        import capo_timestream_influxdb.types.failover_mode

        out["failover_mode"] = (
            capo_timestream_influxdb.types.failover_mode.deserialize_aws_json_1_0(
                data["failoverMode"]
            )
        )
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
