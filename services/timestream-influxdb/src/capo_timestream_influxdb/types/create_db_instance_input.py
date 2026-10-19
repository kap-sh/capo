"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbInstanceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.allocated_storage
    import capo_timestream_influxdb.types.bucket
    import capo_timestream_influxdb.types.db_backup_configuration_input_list
    import capo_timestream_influxdb.types.db_instance_name
    import capo_timestream_influxdb.types.db_instance_type
    import capo_timestream_influxdb.types.db_parameter_group_identifier
    import capo_timestream_influxdb.types.db_storage_type
    import capo_timestream_influxdb.types.deployment_type
    import capo_timestream_influxdb.types.kms_key_id
    import capo_timestream_influxdb.types.log_delivery_configuration
    import capo_timestream_influxdb.types.maintenance_schedule
    import capo_timestream_influxdb.types.network_type
    import capo_timestream_influxdb.types.organization
    import capo_timestream_influxdb.types.password
    import capo_timestream_influxdb.types.port
    import capo_timestream_influxdb.types.request_tag_map
    import capo_timestream_influxdb.types.username
    import capo_timestream_influxdb.types.vpc_security_group_id_list
    import capo_timestream_influxdb.types.vpc_subnet_id_list


class CreateDbInstanceInput(TypedDict, closed=True):
    name: "capo_timestream_influxdb.types.db_instance_name.DbInstanceName"
    """<p>The name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB instance names must be unique per customer and per region.</p>"""
    username: NotRequired["capo_timestream_influxdb.types.username.Username"]
    """<p>The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Amazon Secrets Manager in your account.</p>"""
    password: "capo_timestream_influxdb.types.password.Password"
    """<p>The password of the initial admin user created in InfluxDB v2. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a Secret created in Secrets Manager in your account.</p>"""
    organization: NotRequired[
        "capo_timestream_influxdb.types.organization.Organization"
    ]
    """<p>The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.</p>"""
    bucket: NotRequired["capo_timestream_influxdb.types.bucket.Bucket"]
    """<p>The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.</p>"""
    db_instance_type: "capo_timestream_influxdb.types.db_instance_type.DbInstanceType"
    """<p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>"""
    vpc_subnet_ids: "capo_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    """<p>A list of VPC subnet IDs to associate with the DB instance. Provide at least two VPC subnet IDs in different availability zones when deploying with a Multi-AZ standby.</p>"""
    vpc_security_group_ids: "capo_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    """<p>A list of VPC security group IDs to associate with the DB instance.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Configures the DB instance with a public IP to facilitate access.</p>"""
    db_storage_type: NotRequired[
        "capo_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type to read and write InfluxDB data.</p> <p>You can choose between 3 different types of provisioned Influx IOPS included storage according to your workloads requirements:</p> <ul> <li> <p>Influx IO Included 3000 IOPS</p> </li> <li> <p>Influx IO Included 12000 IOPS</p> </li> <li> <p>Influx IO Included 16000 IOPS</p> </li> </ul>"""
    allocated_storage: (
        "capo_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    )
    """<p>The amount of storage to allocate for your DB storage type in GiB (gibibytes).</p>"""
    db_parameter_group_identifier: NotRequired[
        "capo_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>"""
    deployment_type: NotRequired[
        "capo_timestream_influxdb.types.deployment_type.DeploymentType"
    ]
    """<p>Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.</p>"""
    log_delivery_configuration: NotRequired[
        "capo_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to a specified S3 bucket.</p>"""
    maintenance_schedule: NotRequired[
        "capo_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>Specifies the maintenance schedule for the DB instance, including the preferred maintenance window and timezone.</p>"""
    tags: NotRequired["capo_timestream_influxdb.types.request_tag_map.RequestTagMap"]
    """<p>A list of key-value pairs to associate with the DB instance.</p>"""
    port: NotRequired["capo_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>"""
    network_type: NotRequired["capo_timestream_influxdb.types.network_type.NetworkType"]
    """<p>Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_backup_configurations: NotRequired[
        "capo_timestream_influxdb.types.db_backup_configuration_input_list.DbBackupConfigurationInputList"
    ]
    """<p>A list of backup configurations to enable automated backups for the DB instance.</p>"""
    kms_key_id: NotRequired["capo_timestream_influxdb.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key identifier to use for encryption of the DB instance. Can be a key ID, key ARN, alias name, or alias ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbInstanceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "username" in value:
        out["username"] = value["username"]
    out["password"] = value["password"]
    if "organization" in value:
        out["organization"] = value["organization"]
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    import capo_timestream_influxdb.types.db_instance_type

    out["dbInstanceType"] = (
        capo_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
            value["db_instance_type"]
        )
    )
    import capo_timestream_influxdb.types.vpc_subnet_id_list

    out["vpcSubnetIds"] = (
        capo_timestream_influxdb.types.vpc_subnet_id_list.serialize_aws_json_1_0(
            value["vpc_subnet_ids"]
        )
    )
    import capo_timestream_influxdb.types.vpc_security_group_id_list

    out["vpcSecurityGroupIds"] = (
        capo_timestream_influxdb.types.vpc_security_group_id_list.serialize_aws_json_1_0(
            value["vpc_security_group_ids"]
        )
    )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "db_storage_type" in value:
        import capo_timestream_influxdb.types.db_storage_type

        out["dbStorageType"] = (
            capo_timestream_influxdb.types.db_storage_type.serialize_aws_json_1_0(
                value["db_storage_type"]
            )
        )
    out["allocatedStorage"] = value["allocated_storage"]
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "deployment_type" in value:
        import capo_timestream_influxdb.types.deployment_type

        out["deploymentType"] = (
            capo_timestream_influxdb.types.deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> CreateDbInstanceInput:
    out: CreateDbInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDbInstanceInput.name required")
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("password") is not None:
        out["password"] = data["password"]
    else:
        raise DeserializationError("CreateDbInstanceInput.password required")
    if data.get("organization") is not None:
        out["organization"] = data["organization"]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("dbInstanceType") is not None:
        import capo_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            capo_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    else:
        raise DeserializationError("CreateDbInstanceInput.db_instance_type required")
    if data.get("vpcSubnetIds") is not None:
        import capo_timestream_influxdb.types.vpc_subnet_id_list

        out["vpc_subnet_ids"] = (
            capo_timestream_influxdb.types.vpc_subnet_id_list.deserialize_aws_json_1_0(
                data["vpcSubnetIds"]
            )
        )
    else:
        raise DeserializationError("CreateDbInstanceInput.vpc_subnet_ids required")
    if data.get("vpcSecurityGroupIds") is not None:
        import capo_timestream_influxdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_timestream_influxdb.types.vpc_security_group_id_list.deserialize_aws_json_1_0(
                data["vpcSecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDbInstanceInput.vpc_security_group_ids required"
        )
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("dbStorageType") is not None:
        import capo_timestream_influxdb.types.db_storage_type

        out["db_storage_type"] = (
            capo_timestream_influxdb.types.db_storage_type.deserialize_aws_json_1_0(
                data["dbStorageType"]
            )
        )
    if data.get("allocatedStorage") is not None:
        out["allocated_storage"] = data["allocatedStorage"]
    else:
        raise DeserializationError("CreateDbInstanceInput.allocated_storage required")
    if data.get("dbParameterGroupIdentifier") is not None:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if data.get("deploymentType") is not None:
        import capo_timestream_influxdb.types.deployment_type

        out["deployment_type"] = (
            capo_timestream_influxdb.types.deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
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


def redact_sensitive(value: CreateDbInstanceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
