"""Generated from Smithy shape ``com.amazonaws.mq#DescribeBrokerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__boolean
    import capo_mq.types.__integer
    import capo_mq.types.__list_of__string
    import capo_mq.types.__list_of_action_required
    import capo_mq.types.__list_of_broker_instance
    import capo_mq.types.__list_of_user_summary
    import capo_mq.types.__map_of__string
    import capo_mq.types.__string
    import capo_mq.types.__timestamp_iso8601
    import capo_mq.types.authentication_strategy
    import capo_mq.types.broker_state
    import capo_mq.types.broker_storage_type
    import capo_mq.types.configurations
    import capo_mq.types.data_replication_metadata_output
    import capo_mq.types.data_replication_mode
    import capo_mq.types.deployment_mode
    import capo_mq.types.encryption_options
    import capo_mq.types.engine_type
    import capo_mq.types.ldap_server_metadata_output
    import capo_mq.types.logs_summary
    import capo_mq.types.weekly_start_time


class DescribeBrokerResponse(TypedDict, closed=True):
    actions_required: NotRequired[
        "capo_mq.types.__list_of_action_required.__listOfActionRequired"
    ]
    """<p>Actions required for a broker.</p>"""
    authentication_strategy: NotRequired[
        "capo_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.</p>"""
    broker_arn: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's Amazon Resource Name (ARN).</p>"""
    broker_id: NotRequired["capo_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    broker_instances: NotRequired[
        "capo_mq.types.__list_of_broker_instance.__listOfBrokerInstance"
    ]
    """<p>A list of information about allocated brokers.</p>"""
    broker_name: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's name. This value must be unique in your Amazon Web Services account account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.</p>"""
    broker_state: NotRequired["capo_mq.types.broker_state.BrokerState"]
    """<p>The broker's status.</p>"""
    configurations: NotRequired["capo_mq.types.configurations.Configurations"]
    """<p>The list of all revisions for the specified configuration.</p>"""
    created: NotRequired["capo_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time when the broker was created.</p>"""
    deployment_mode: NotRequired["capo_mq.types.deployment_mode.DeploymentMode"]
    """<p>The broker's deployment mode.</p>"""
    encryption_options: NotRequired[
        "capo_mq.types.encryption_options.EncryptionOptions"
    ]
    """<p>Encryption options for the broker.</p>"""
    engine_type: NotRequired["capo_mq.types.engine_type.EngineType"]
    """<p>The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>"""
    engine_version: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker engine version. For more information, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    host_instance_type: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's instance type.</p>"""
    ldap_server_metadata: NotRequired[
        "capo_mq.types.ldap_server_metadata_output.LdapServerMetadataOutput"
    ]
    """<p>The metadata of the LDAP server used to authenticate and authorize connections to the broker.</p>"""
    logs: NotRequired["capo_mq.types.logs_summary.LogsSummary"]
    """<p>The list of information about logs currently enabled and pending to be deployed for the specified broker.</p>"""
    maintenance_window_start_time: NotRequired[
        "capo_mq.types.weekly_start_time.WeeklyStartTime"
    ]
    """<p>The parameters that determine the WeeklyStartTime.</p>"""
    pending_authentication_strategy: NotRequired[
        "capo_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>The authentication strategy that will be applied when the broker is rebooted. The default is SIMPLE.</p>"""
    pending_engine_version: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker engine version to upgrade to. For more information, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    pending_host_instance_type: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker's host instance type to upgrade to. For a list of supported instance types, see <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/broker.html#broker-instance-types">Broker instance types</a>.</p>"""
    pending_ldap_server_metadata: NotRequired[
        "capo_mq.types.ldap_server_metadata_output.LdapServerMetadataOutput"
    ]
    """<p>The metadata of the LDAP server that will be used to authenticate and authorize connections to the broker after it is rebooted.</p>"""
    pending_security_groups: NotRequired[
        "capo_mq.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of pending security groups to authorize connections to brokers.</p>"""
    pending_storage_size: NotRequired["capo_mq.types.__integer.__integer"]
    """<p>The pending storage size in GB, to be applied on the next broker restart.</p>"""
    publicly_accessible: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables connections from applications outside of the VPC that hosts the broker's subnets.</p>"""
    security_groups: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.</p>"""
    storage_size: NotRequired["capo_mq.types.__integer.__integer"]
    """<p>The broker's storage size in GB.</p>"""
    storage_type: NotRequired["capo_mq.types.broker_storage_type.BrokerStorageType"]
    """<p>The broker's storage type.</p>"""
    subnet_ids: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones.</p>"""
    tags: NotRequired["capo_mq.types.__map_of__string.__mapOf__string"]
    """<p>The list of all tags associated with this broker.</p>"""
    users: NotRequired["capo_mq.types.__list_of_user_summary.__listOfUserSummary"]
    """<p>The list of all broker usernames for the specified broker.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBrokerResponse) -> dict:
    out: dict = {}
    if "actions_required" in value:
        import capo_mq.types.__list_of_action_required

        out["actionsRequired"] = capo_mq.types.__list_of_action_required.serialize_json(
            value["actions_required"]
        )
    if "authentication_strategy" in value:
        import capo_mq.types.authentication_strategy

        out["authenticationStrategy"] = (
            capo_mq.types.authentication_strategy.serialize_json(
                value["authentication_strategy"]
            )
        )
    if "auto_minor_version_upgrade" in value:
        out["autoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "broker_arn" in value:
        out["brokerArn"] = value["broker_arn"]
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "broker_instances" in value:
        import capo_mq.types.__list_of_broker_instance

        out["brokerInstances"] = capo_mq.types.__list_of_broker_instance.serialize_json(
            value["broker_instances"]
        )
    if "broker_name" in value:
        out["brokerName"] = value["broker_name"]
    if "broker_state" in value:
        import capo_mq.types.broker_state

        out["brokerState"] = capo_mq.types.broker_state.serialize_json(
            value["broker_state"]
        )
    if "configurations" in value:
        import capo_mq.types.configurations

        out["configurations"] = capo_mq.types.configurations.serialize_json(
            value["configurations"]
        )
    if "created" in value:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "deployment_mode" in value:
        import capo_mq.types.deployment_mode

        out["deploymentMode"] = capo_mq.types.deployment_mode.serialize_json(
            value["deployment_mode"]
        )
    if "encryption_options" in value:
        import capo_mq.types.encryption_options

        out["encryptionOptions"] = capo_mq.types.encryption_options.serialize_json(
            value["encryption_options"]
        )
    if "engine_type" in value:
        import capo_mq.types.engine_type

        out["engineType"] = capo_mq.types.engine_type.serialize_json(
            value["engine_type"]
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
        import capo_mq.types.logs_summary

        out["logs"] = capo_mq.types.logs_summary.serialize_json(value["logs"])
    if "maintenance_window_start_time" in value:
        import capo_mq.types.weekly_start_time

        out["maintenanceWindowStartTime"] = (
            capo_mq.types.weekly_start_time.serialize_json(
                value["maintenance_window_start_time"]
            )
        )
    if "pending_authentication_strategy" in value:
        import capo_mq.types.authentication_strategy

        out["pendingAuthenticationStrategy"] = (
            capo_mq.types.authentication_strategy.serialize_json(
                value["pending_authentication_strategy"]
            )
        )
    if "pending_engine_version" in value:
        out["pendingEngineVersion"] = value["pending_engine_version"]
    if "pending_host_instance_type" in value:
        out["pendingHostInstanceType"] = value["pending_host_instance_type"]
    if "pending_ldap_server_metadata" in value:
        import capo_mq.types.ldap_server_metadata_output

        out["pendingLdapServerMetadata"] = (
            capo_mq.types.ldap_server_metadata_output.serialize_json(
                value["pending_ldap_server_metadata"]
            )
        )
    if "pending_security_groups" in value:
        import capo_mq.types.__list_of__string

        out["pendingSecurityGroups"] = capo_mq.types.__list_of__string.serialize_json(
            value["pending_security_groups"]
        )
    if "pending_storage_size" in value:
        out["pendingStorageSize"] = value["pending_storage_size"]
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "security_groups" in value:
        import capo_mq.types.__list_of__string

        out["securityGroups"] = capo_mq.types.__list_of__string.serialize_json(
            value["security_groups"]
        )
    if "storage_size" in value:
        out["storageSize"] = value["storage_size"]
    if "storage_type" in value:
        import capo_mq.types.broker_storage_type

        out["storageType"] = capo_mq.types.broker_storage_type.serialize_json(
            value["storage_type"]
        )
    if "subnet_ids" in value:
        import capo_mq.types.__list_of__string

        out["subnetIds"] = capo_mq.types.__list_of__string.serialize_json(
            value["subnet_ids"]
        )
    if "tags" in value:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.serialize_json(value["tags"])
    if "users" in value:
        import capo_mq.types.__list_of_user_summary

        out["users"] = capo_mq.types.__list_of_user_summary.serialize_json(
            value["users"]
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
    return out


def deserialize_json(data: dict) -> DescribeBrokerResponse:
    out: DescribeBrokerResponse = {}  # type: ignore[typeddict-item]
    if data.get("actionsRequired") is not None:
        import capo_mq.types.__list_of_action_required

        out["actions_required"] = (
            capo_mq.types.__list_of_action_required.deserialize_json(
                data["actionsRequired"]
            )
        )
    if data.get("authenticationStrategy") is not None:
        import capo_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            capo_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if data.get("autoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["autoMinorVersionUpgrade"]
    if data.get("brokerArn") is not None:
        out["broker_arn"] = data["brokerArn"]
    if data.get("brokerId") is not None:
        out["broker_id"] = data["brokerId"]
    if data.get("brokerInstances") is not None:
        import capo_mq.types.__list_of_broker_instance

        out["broker_instances"] = (
            capo_mq.types.__list_of_broker_instance.deserialize_json(
                data["brokerInstances"]
            )
        )
    if data.get("brokerName") is not None:
        out["broker_name"] = data["brokerName"]
    if data.get("brokerState") is not None:
        import capo_mq.types.broker_state

        out["broker_state"] = capo_mq.types.broker_state.deserialize_json(
            data["brokerState"]
        )
    if data.get("configurations") is not None:
        import capo_mq.types.configurations

        out["configurations"] = capo_mq.types.configurations.deserialize_json(
            data["configurations"]
        )
    if data.get("created") is not None:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if data.get("deploymentMode") is not None:
        import capo_mq.types.deployment_mode

        out["deployment_mode"] = capo_mq.types.deployment_mode.deserialize_json(
            data["deploymentMode"]
        )
    if data.get("encryptionOptions") is not None:
        import capo_mq.types.encryption_options

        out["encryption_options"] = capo_mq.types.encryption_options.deserialize_json(
            data["encryptionOptions"]
        )
    if data.get("engineType") is not None:
        import capo_mq.types.engine_type

        out["engine_type"] = capo_mq.types.engine_type.deserialize_json(
            data["engineType"]
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
        import capo_mq.types.logs_summary

        out["logs"] = capo_mq.types.logs_summary.deserialize_json(data["logs"])
    if data.get("maintenanceWindowStartTime") is not None:
        import capo_mq.types.weekly_start_time

        out["maintenance_window_start_time"] = (
            capo_mq.types.weekly_start_time.deserialize_json(
                data["maintenanceWindowStartTime"]
            )
        )
    if data.get("pendingAuthenticationStrategy") is not None:
        import capo_mq.types.authentication_strategy

        out["pending_authentication_strategy"] = (
            capo_mq.types.authentication_strategy.deserialize_json(
                data["pendingAuthenticationStrategy"]
            )
        )
    if data.get("pendingEngineVersion") is not None:
        out["pending_engine_version"] = data["pendingEngineVersion"]
    if data.get("pendingHostInstanceType") is not None:
        out["pending_host_instance_type"] = data["pendingHostInstanceType"]
    if data.get("pendingLdapServerMetadata") is not None:
        import capo_mq.types.ldap_server_metadata_output

        out["pending_ldap_server_metadata"] = (
            capo_mq.types.ldap_server_metadata_output.deserialize_json(
                data["pendingLdapServerMetadata"]
            )
        )
    if data.get("pendingSecurityGroups") is not None:
        import capo_mq.types.__list_of__string

        out["pending_security_groups"] = (
            capo_mq.types.__list_of__string.deserialize_json(
                data["pendingSecurityGroups"]
            )
        )
    if data.get("pendingStorageSize") is not None:
        out["pending_storage_size"] = data["pendingStorageSize"]
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("securityGroups") is not None:
        import capo_mq.types.__list_of__string

        out["security_groups"] = capo_mq.types.__list_of__string.deserialize_json(
            data["securityGroups"]
        )
    if data.get("storageSize") is not None:
        out["storage_size"] = data["storageSize"]
    if data.get("storageType") is not None:
        import capo_mq.types.broker_storage_type

        out["storage_type"] = capo_mq.types.broker_storage_type.deserialize_json(
            data["storageType"]
        )
    if data.get("subnetIds") is not None:
        import capo_mq.types.__list_of__string

        out["subnet_ids"] = capo_mq.types.__list_of__string.deserialize_json(
            data["subnetIds"]
        )
    if data.get("tags") is not None:
        import capo_mq.types.__map_of__string

        out["tags"] = capo_mq.types.__map_of__string.deserialize_json(data["tags"])
    if data.get("users") is not None:
        import capo_mq.types.__list_of_user_summary

        out["users"] = capo_mq.types.__list_of_user_summary.deserialize_json(
            data["users"]
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
    return out
