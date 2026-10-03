"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.kerberos_authentication_settings
    import capo_database_migration_service.types.replication_instance_class
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.tag_list
    import capo_database_migration_service.types.vpc_security_group_id_list


class CreateReplicationInstanceMessage(TypedDict, closed=True):
    replication_instance_identifier: (
        "capo_database_migration_service.types.string.String"
    )
    """<p>The replication instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>myrepinstance</code> </p>"""
    allocated_storage: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of storage (in gigabytes) to be initially allocated for the replication instance.</p>"""
    replication_instance_class: "capo_database_migration_service.types.replication_instance_class.ReplicationInstanceClass"
    """<p>The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to <code>"dms.c4.large"</code>.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html "> Choosing the right DMS replication instance</a>; and, <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html">Selecting the best size for a replication instance</a>. </p>"""
    vpc_security_group_ids: NotRequired[
        "capo_database_migration_service.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p> Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance. </p>"""
    availability_zone: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Availability Zone where the replication instance will be created. The default value is a random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region, for example: <code>us-east-1d</code>.</p>"""
    replication_subnet_group_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A subnet group to associate with the replication instance.</p>"""
    preferred_maintenance_window: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>Default: A 30-minute window selected at random from an 8-hour block of time per Amazon Web Services Region, occurring on a random day of the week.</p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>"""
    multi_az: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p> Specifies whether the replication instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the Multi-AZ parameter is set to <code>true</code>. </p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The engine version number of the replication instance.</p> <p>If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to <code>true</code>.</p> <p>Default: <code>true</code> </p>"""
    tags: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the replication instance.</p>"""
    kms_key_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An KMS key identifier that is used to encrypt the data on the replication instance.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    publicly_accessible: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p> Specifies the accessibility options for the replication instance. A value of <code>true</code> represents an instance with a public IP address. A value of <code>false</code> represents an instance with a private IP address. The default value is <code>true</code>. </p>"""
    dns_name_servers: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A list of custom DNS name servers supported for the replication instance to access your on-premise source or target database. This list overrides the default name servers supported by the replication instance. You can specify a comma-separated list of internet addresses for up to four on-premise DNS name servers. For example: <code>"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"</code> </p>"""
    resource_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A friendly name for the resource identifier at the end of the <code>EndpointArn</code> response parameter that is returned in the created <code>Endpoint</code> object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as <code>Example-App-ARN1</code>. For example, this value might result in the <code>EndpointArn</code> value <code>arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1</code>. If you don't specify a <code>ResourceIdentifier</code> value, DMS generates a default identifier value for the end of <code>EndpointArn</code>.</p>"""
    network_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>"""
    kerberos_authentication_settings: NotRequired[
        "capo_database_migration_service.types.kerberos_authentication_settings.KerberosAuthenticationSettings"
    ]
    """<p>Specifies the settings required for kerberos authentication when creating the replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationInstanceMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceIdentifier"] = value["replication_instance_identifier"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    out["ReplicationInstanceClass"] = value["replication_instance_class"]
    if "vpc_security_group_ids" in value:
        import capo_database_migration_service.types.vpc_security_group_id_list

        out["VpcSecurityGroupIds"] = (
            capo_database_migration_service.types.vpc_security_group_id_list.serialize_aws_json_1_1(
                value["vpc_security_group_ids"]
            )
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "replication_subnet_group_identifier" in value:
        out["ReplicationSubnetGroupIdentifier"] = value[
            "replication_subnet_group_identifier"
        ]
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "multi_az" in value:
        out["MultiAZ"] = value["multi_az"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "tags" in value:
        import capo_database_migration_service.types.tag_list

        out["Tags"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "dns_name_servers" in value:
        out["DnsNameServers"] = value["dns_name_servers"]
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "network_type" in value:
        out["NetworkType"] = value["network_type"]
    if "kerberos_authentication_settings" in value:
        import capo_database_migration_service.types.kerberos_authentication_settings

        out["KerberosAuthenticationSettings"] = (
            capo_database_migration_service.types.kerberos_authentication_settings.serialize_aws_json_1_1(
                value["kerberos_authentication_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationInstanceMessage:
    out: CreateReplicationInstanceMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceIdentifier") is not None:
        out["replication_instance_identifier"] = data["ReplicationInstanceIdentifier"]
    else:
        raise DeserializationError(
            "CreateReplicationInstanceMessage.replication_instance_identifier required"
        )
    if data.get("AllocatedStorage") is not None:
        out["allocated_storage"] = data["AllocatedStorage"]
    if data.get("ReplicationInstanceClass") is not None:
        out["replication_instance_class"] = data["ReplicationInstanceClass"]
    else:
        raise DeserializationError(
            "CreateReplicationInstanceMessage.replication_instance_class required"
        )
    if data.get("VpcSecurityGroupIds") is not None:
        import capo_database_migration_service.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_database_migration_service.types.vpc_security_group_id_list.deserialize_aws_json_1_1(
                data["VpcSecurityGroupIds"]
            )
        )
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("ReplicationSubnetGroupIdentifier") is not None:
        out["replication_subnet_group_identifier"] = data[
            "ReplicationSubnetGroupIdentifier"
        ]
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("MultiAZ") is not None:
        out["multi_az"] = data["MultiAZ"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("AutoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("PubliclyAccessible") is not None:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if data.get("DnsNameServers") is not None:
        out["dns_name_servers"] = data["DnsNameServers"]
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("NetworkType") is not None:
        out["network_type"] = data["NetworkType"]
    if data.get("KerberosAuthenticationSettings") is not None:
        import capo_database_migration_service.types.kerberos_authentication_settings

        out["kerberos_authentication_settings"] = (
            capo_database_migration_service.types.kerberos_authentication_settings.deserialize_aws_json_1_1(
                data["KerberosAuthenticationSettings"]
            )
        )
    return out
