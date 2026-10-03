"""Generated from Smithy shape ``com.amazonaws.mq#CreateBrokerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__boolean
    import capo_mq.types.__integer
    import capo_mq.types.__list_of__string
    import capo_mq.types.__list_of_user
    import capo_mq.types.__map_of__string
    import capo_mq.types.__string
    import capo_mq.types.authentication_strategy
    import capo_mq.types.broker_storage_type
    import capo_mq.types.configuration_id
    import capo_mq.types.data_replication_mode
    import capo_mq.types.deployment_mode
    import capo_mq.types.encryption_options
    import capo_mq.types.engine_type
    import capo_mq.types.ldap_server_metadata_input
    import capo_mq.types.logs
    import capo_mq.types.weekly_start_time


class CreateBrokerRequest(TypedDict, closed=True):
    authentication_strategy: NotRequired[
        "capo_mq.types.authentication_strategy.AuthenticationStrategy"
    ]
    """<p>Optional. The authentication strategy used to secure the broker. The default is SIMPLE.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. Set to true by default, if no value is specified.</p> <note><p>Must be set to true for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.</p></note>"""
    broker_name: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The broker's name. This value must be unique in your Amazon Web Services account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.</p> <important><p>Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other Amazon Web Services services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.</p></important>"""
    configuration: NotRequired["capo_mq.types.configuration_id.ConfigurationId"]
    """<p>A list of information about the configuration.</p>"""
    creator_request_id: NotRequired["capo_mq.types.__string.__string"]
    """<p>The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action.</p> <note><p>We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the creatorRequestId if your application doesn't require idempotency.</p></note>"""
    deployment_mode: NotRequired["capo_mq.types.deployment_mode.DeploymentMode"]
    """<p>Required. The broker's deployment mode.</p>"""
    encryption_options: NotRequired[
        "capo_mq.types.encryption_options.EncryptionOptions"
    ]
    """<p>Encryption options for the broker.</p>"""
    engine_type: NotRequired["capo_mq.types.engine_type.EngineType"]
    """<p>Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.</p>"""
    engine_version: NotRequired["capo_mq.types.__string.__string"]
    """<p>The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html">ActiveMQ version management</a> and the <a href="https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html">RabbitMQ version management</a> sections in the Amazon MQ Developer Guide.</p>"""
    host_instance_type: NotRequired["capo_mq.types.__string.__string"]
    """<p>Required. The broker's instance type.</p>"""
    ldap_server_metadata: NotRequired[
        "capo_mq.types.ldap_server_metadata_input.LdapServerMetadataInput"
    ]
    """<p>Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.</p>"""
    logs: NotRequired["capo_mq.types.logs.Logs"]
    """<p>Enables Amazon CloudWatch logging for brokers.</p>"""
    maintenance_window_start_time: NotRequired[
        "capo_mq.types.weekly_start_time.WeeklyStartTime"
    ]
    """<p>The parameters that determine the WeeklyStartTime.</p>"""
    publicly_accessible: NotRequired["capo_mq.types.__boolean.__boolean"]
    """<p>Enables connections from applications outside of the VPC that hosts the broker's subnets. Set to false by default, if no value is provided.</p>"""
    security_groups: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.</p>"""
    storage_size: NotRequired["capo_mq.types.__integer.__integer"]
    """<p>The broker's storage size in GB.</p>"""
    storage_type: NotRequired["capo_mq.types.broker_storage_type.BrokerStorageType"]
    """<p>The broker's storage type.</p>"""
    subnet_ids: NotRequired["capo_mq.types.__list_of__string.__listOf__string"]
    """<p>The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE_STANDBY_MULTI_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER_MULTI_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.</p> <important><p>If you specify subnets in a <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html">shared VPC</a> for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your Amazon Web Services account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your Amazon Web Services account.</p></important>"""
    tags: NotRequired["capo_mq.types.__map_of__string.__mapOf__string"]
    """<p>Create tags when creating the broker.</p>"""
    users: NotRequired["capo_mq.types.__list_of_user.__listOfUser"]
    """<p>The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, an administrative user is required if using simple authentication and authorization. For brokers using OAuth2, this user is optional. When provided, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.</p>"""
    data_replication_mode: NotRequired[
        "capo_mq.types.data_replication_mode.DataReplicationMode"
    ]
    """<p>Defines whether this broker is a part of a data replication pair.</p>"""
    data_replication_primary_broker_arn: NotRequired["capo_mq.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrokerRequest) -> dict:
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
    if "broker_name" in value:
        out["brokerName"] = value["broker_name"]
    if "configuration" in value:
        import capo_mq.types.configuration_id

        out["configuration"] = capo_mq.types.configuration_id.serialize_json(
            value["configuration"]
        )
    if "creator_request_id" in value:
        out["creatorRequestId"] = value["creator_request_id"]
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
        import capo_mq.types.ldap_server_metadata_input

        out["ldapServerMetadata"] = (
            capo_mq.types.ldap_server_metadata_input.serialize_json(
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
        import capo_mq.types.__list_of_user

        out["users"] = capo_mq.types.__list_of_user.serialize_json(value["users"])
    if "data_replication_mode" in value:
        import capo_mq.types.data_replication_mode

        out["dataReplicationMode"] = capo_mq.types.data_replication_mode.serialize_json(
            value["data_replication_mode"]
        )
    if "data_replication_primary_broker_arn" in value:
        out["dataReplicationPrimaryBrokerArn"] = value[
            "data_replication_primary_broker_arn"
        ]
    return out


def deserialize_json(data: dict) -> CreateBrokerRequest:
    out: CreateBrokerRequest = {}  # type: ignore[typeddict-item]
    if data.get("authenticationStrategy") is not None:
        import capo_mq.types.authentication_strategy

        out["authentication_strategy"] = (
            capo_mq.types.authentication_strategy.deserialize_json(
                data["authenticationStrategy"]
            )
        )
    if data.get("autoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["autoMinorVersionUpgrade"]
    if data.get("brokerName") is not None:
        out["broker_name"] = data["brokerName"]
    if data.get("configuration") is not None:
        import capo_mq.types.configuration_id

        out["configuration"] = capo_mq.types.configuration_id.deserialize_json(
            data["configuration"]
        )
    if data.get("creatorRequestId") is not None:
        out["creator_request_id"] = data["creatorRequestId"]
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
        import capo_mq.types.ldap_server_metadata_input

        out["ldap_server_metadata"] = (
            capo_mq.types.ldap_server_metadata_input.deserialize_json(
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
        import capo_mq.types.__list_of_user

        out["users"] = capo_mq.types.__list_of_user.deserialize_json(data["users"])
    if data.get("dataReplicationMode") is not None:
        import capo_mq.types.data_replication_mode

        out["data_replication_mode"] = (
            capo_mq.types.data_replication_mode.deserialize_json(
                data["dataReplicationMode"]
            )
        )
    if data.get("dataReplicationPrimaryBrokerArn") is not None:
        out["data_replication_primary_broker_arn"] = data[
            "dataReplicationPrimaryBrokerArn"
        ]
    return out
