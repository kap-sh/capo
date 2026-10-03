"""Generated from Smithy shape ``com.amazonaws.mq#UpdateBrokerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__boolean
    import capo_mq.types.__integer
    import capo_mq.types.__list_of__string
    import capo_mq.types.__string
    import capo_mq.types.authentication_strategy
    import capo_mq.types.configuration_id
    import capo_mq.types.data_replication_metadata_output
    import capo_mq.types.data_replication_mode
    import capo_mq.types.ldap_server_metadata_output
    import capo_mq.types.logs
    import capo_mq.types.weekly_start_time


class UpdateBrokerResponse(TypedDict, closed=True):
    authentication_strategy: NotRequired[
        "capo_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.</p>"""
    broker_id: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the broker.</p>"""
    configuration: NotRequired["capo_mq.types.configuration_id.ConfigurationId"]
    """<p>The ID of the updated configuration.</p>"""
    engine_version: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker engine version to upgrade to. For more information, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    host_instance_type: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's host instance type to upgrade to. For a list of supported instance types, see <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types">Broker instance types</a>.</p>"""
    ldap_server_metadata: NotRequired[
        "capo_mq.types.ldap_server_metadata_output.LdapServerMetadataOutput"
    ]
    """<p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p>"""
    logs: NotRequired["capo_mq.types.logs.Logs"]
    """<p>The list of information about logs to be enabled for the specified broker.</p>"""
    maintenance_window_start_time: NotRequired[
        "capo_mq.types.weekly_start_time.WeeklyStartTime"
    ]
    """<p>The parameters that determine the WeeklyStartTime.</p>"""
    resource_share_arns: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The pending broker's target list of resource shares</p>"""
    security_groups: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers.</p>"""
    data_replication_metadata: NotRequired[
        "capo_mq.types.data_replication_metadata_output.DataReplicationMetadataOutput"
    ]
    """<p>The replication details of the data replication-enabled broker. Only returned if dataReplicationMode is set to CRDR.</p>"""
    data_replication_mode: NotRequired[
        "capo_mq.types.data_replication_mode.DataReplicationMode"
    ]
    """<p>Describes whether this broker is a part of a data replication pair.</p>"""
    pending_data_replication_metadata: NotRequired[
        "capo_mq.types.data_replication_metadata_output.DataReplicationMetadataOutput"
    ]
    """<p>The pending replication details of the data replication-enabled broker. Only returned if pendingDataReplicationMode is set to CRDR.</p>"""
    pending_data_replication_mode: NotRequired[
        "capo_mq.types.data_replication_mode.DataReplicationMode"
    ]
    """<p>Describes whether this broker will be a part of a data replication pair after reboot.</p>"""
    storage_size: NotRequired["capo_mq.types.__integer.__integer"]
    """<p>The broker's storage size in GB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrokerResponse) -> dict:
    out: dict = {}
    if "authentication_strategy" in value:
        import capo_mq.types.authentication_strategy

        out["authenticationStrategy"] = (
            capo_mq.types.authentication_strategy.serialize_json(
                value["authentication_strategy"]
            )
        )
    if "auto_minor_version_upgrade" in value:
        out["autoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "configuration" in value:
        import capo_mq.types.configuration_id

        out["configuration"] = capo_mq.types.configuration_id.serialize_json(
            value["configuration"]
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "host_instance_type" in value:
        out["hostInstanceType"] = value["host_instance_type"]
    if "ldap_server_metadata" in value:
        import capo_mq.types.ldap_server_metadata_output

        out["ldapServerMetadata"] = (
            capo_mq.types.ldap_server_metadata_output.serialize_json(
                value["ldap_server_metadata"]
            )
        )
    if "logs" in value:
        import capo_mq.types.logs

        out["logs"] = capo_mq.types.logs.serialize_json(value["logs"])
    if "maintenance_window_start_time" in value:
        import capo_mq.types.weekly_start_time

        out["maintenanceWindowStartTime"] = (
            capo_mq.types.weekly_start_time.serialize_json(
                value["maintenance_window_start_time"]
            )
        )
    if "resource_share_arns" in value:
        import capo_mq.types.__list_of__string

        out["resourceShareArns"] = capo_mq.types.__list_of__string.serialize_json(
            value["resource_share_arns"]
        )
    if "security_groups" in value:
        import capo_mq.types.__list_of__string

        out["securityGroups"] = capo_mq.types.__list_of__string.serialize_json(
            value["security_groups"]
        )
    if "data_replication_metadata" in value:
        import capo_mq.types.data_replication_metadata_output

        out["dataReplicationMetadata"] = (
            capo_mq.types.data_replication_metadata_output.serialize_json(
                value["data_replication_metadata"]
            )
        )
    if "data_replication_mode" in value:
        import capo_mq.types.data_replication_mode

        out["dataReplicationMode"] = capo_mq.types.data_replication_mode.serialize_json(
            value["data_replication_mode"]
        )
    if "pending_data_replication_metadata" in value:
        import capo_mq.types.data_replication_metadata_output

        out["pendingDataReplicationMetadata"] = (
            capo_mq.types.data_replication_metadata_output.serialize_json(
                value["pending_data_replication_metadata"]
            )
        )
    if "pending_data_replication_mode" in value:
        import capo_mq.types.data_replication_mode

        out["pendingDataReplicationMode"] = (
            capo_mq.types.data_replication_mode.serialize_json(
                value["pending_data_replication_mode"]
            )
        )
    if "storage_size" in value:
        out["storageSize"] = value["storage_size"]
    return out


def deserialize_json(data: dict) -> UpdateBrokerResponse:
    out: UpdateBrokerResponse = {}  # type: ignore[typeddict-item]
    if data.get("authenticationStrategy") is not None:
        import capo_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            capo_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if data.get("autoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["autoMinorVersionUpgrade"]
    if data.get("brokerId") is not None:
        out["broker_id"] = data["brokerId"]
    if data.get("configuration") is not None:
        import capo_mq.types.configuration_id

        out["configuration"] = capo_mq.types.configuration_id.deserialize_json(
            data["configuration"]
        )
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("hostInstanceType") is not None:
        out["host_instance_type"] = data["hostInstanceType"]
    if data.get("ldapServerMetadata") is not None:
        import capo_mq.types.ldap_server_metadata_output

        out["ldap_server_metadata"] = (
            capo_mq.types.ldap_server_metadata_output.deserialize_json(
                data["ldapServerMetadata"]
            )
        )
    if data.get("logs") is not None:
        import capo_mq.types.logs

        out["logs"] = capo_mq.types.logs.deserialize_json(data["logs"])
    if data.get("maintenanceWindowStartTime") is not None:
        import capo_mq.types.weekly_start_time

        out["maintenance_window_start_time"] = (
            capo_mq.types.weekly_start_time.deserialize_json(
                data["maintenanceWindowStartTime"]
            )
        )
    if data.get("resourceShareArns") is not None:
        import capo_mq.types.__list_of__string

        out["resource_share_arns"] = capo_mq.types.__list_of__string.deserialize_json(
            data["resourceShareArns"]
        )
    if data.get("securityGroups") is not None:
        import capo_mq.types.__list_of__string

        out["security_groups"] = capo_mq.types.__list_of__string.deserialize_json(
            data["securityGroups"]
        )
    if data.get("dataReplicationMetadata") is not None:
        import capo_mq.types.data_replication_metadata_output

        out["data_replication_metadata"] = (
            capo_mq.types.data_replication_metadata_output.deserialize_json(
                data["dataReplicationMetadata"]
            )
        )
    if data.get("dataReplicationMode") is not None:
        import capo_mq.types.data_replication_mode

        out["data_replication_mode"] = (
            capo_mq.types.data_replication_mode.deserialize_json(
                data["dataReplicationMode"]
            )
        )
    if data.get("pendingDataReplicationMetadata") is not None:
        import capo_mq.types.data_replication_metadata_output

        out["pending_data_replication_metadata"] = (
            capo_mq.types.data_replication_metadata_output.deserialize_json(
                data["pendingDataReplicationMetadata"]
            )
        )
    if data.get("pendingDataReplicationMode") is not None:
        import capo_mq.types.data_replication_mode

        out["pending_data_replication_mode"] = (
            capo_mq.types.data_replication_mode.deserialize_json(
                data["pendingDataReplicationMode"]
            )
        )
    if data.get("storageSize") is not None:
        out["storage_size"] = data["storageSize"]
    return out
