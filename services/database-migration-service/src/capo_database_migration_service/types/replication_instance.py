"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.integer
    import capo_database_migration_service.types.kerberos_authentication_settings
    import capo_database_migration_service.types.replication_instance_class
    import capo_database_migration_service.types.replication_instance_ipv6_address_list
    import capo_database_migration_service.types.replication_instance_private_ip_address_list
    import capo_database_migration_service.types.replication_instance_public_ip_address_list
    import capo_database_migration_service.types.replication_pending_modified_values
    import capo_database_migration_service.types.replication_subnet_group
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp
    import capo_database_migration_service.types.vpc_security_group_membership_list


class ReplicationInstance(TypedDict, closed=True):
    replication_instance_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The replication instance identifier is a required parameter. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>myrepinstance</code> </p>"""
    replication_instance_class: NotRequired[
        "capo_database_migration_service.types.replication_instance_class.ReplicationInstanceClass"
    ]
    """<p>The compute and memory capacity of the replication instance as defined for the specified replication instance class. It is a required parameter, although a default value is pre-selected in the DMS console.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth"> Selecting the right DMS replication instance for your migration</a>. </p>"""
    replication_instance_status: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The status of the replication instance. The possible return values include:</p> <ul> <li> <p> <code>"available"</code> </p> </li> <li> <p> <code>"creating"</code> </p> </li> <li> <p> <code>"deleted"</code> </p> </li> <li> <p> <code>"deleting"</code> </p> </li> <li> <p> <code>"failed"</code> </p> </li> <li> <p> <code>"modifying"</code> </p> </li> <li> <p> <code>"upgrading"</code> </p> </li> <li> <p> <code>"rebooting"</code> </p> </li> <li> <p> <code>"resetting-master-credentials"</code> </p> </li> <li> <p> <code>"storage-full"</code> </p> </li> <li> <p> <code>"incompatible-credentials"</code> </p> </li> <li> <p> <code>"incompatible-network"</code> </p> </li> <li> <p> <code>"maintenance"</code> </p> </li> </ul>"""
    allocated_storage: "capo_database_migration_service.types.integer.Integer"
    """<p>The amount of storage (in gigabytes) that is allocated for the replication instance.</p>"""
    instance_create_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the replication instance was created.</p>"""
    vpc_security_groups: NotRequired[
        "capo_database_migration_service.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>The VPC security group for the instance.</p>"""
    availability_zone: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Availability Zone for the instance.</p>"""
    replication_subnet_group: NotRequired[
        "capo_database_migration_service.types.replication_subnet_group.ReplicationSubnetGroup"
    ]
    """<p>The subnet group for the replication instance.</p>"""
    preferred_maintenance_window: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The maintenance window times for the replication instance. Any pending upgrades to the replication instance are performed during this time.</p>"""
    pending_modified_values: NotRequired[
        "capo_database_migration_service.types.replication_pending_modified_values.ReplicationPendingModifiedValues"
    ]
    """<p>The pending modification values.</p>"""
    multi_az: "capo_database_migration_service.types.boolean.Boolean"
    """<p> Specifies whether the replication instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the Multi-AZ parameter is set to <code>true</code>. </p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The engine version number of the replication instance.</p> <p>If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.</p> <p>When modifying a major engine version of an instance, also set <code>AllowMajorVersionUpgrade</code> to <code>true</code>.</p>"""
    auto_minor_version_upgrade: "capo_database_migration_service.types.boolean.Boolean"
    """<p>Boolean value indicating if minor version upgrades will be automatically applied to the instance.</p>"""
    kms_key_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An KMS key identifier that is used to encrypt the data on the replication instance.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    replication_instance_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    replication_instance_public_ip_address: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The public IP address of the replication instance.</p>"""
    replication_instance_private_ip_address: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The private IP address of the replication instance.</p>"""
    replication_instance_public_ip_addresses: NotRequired[
        "capo_database_migration_service.types.replication_instance_public_ip_address_list.ReplicationInstancePublicIpAddressList"
    ]
    """<p>One or more public IP addresses for the replication instance.</p>"""
    replication_instance_private_ip_addresses: NotRequired[
        "capo_database_migration_service.types.replication_instance_private_ip_address_list.ReplicationInstancePrivateIpAddressList"
    ]
    """<p>One or more private IP addresses for the replication instance.</p>"""
    replication_instance_ipv6_addresses: NotRequired[
        "capo_database_migration_service.types.replication_instance_ipv6_address_list.ReplicationInstanceIpv6AddressList"
    ]
    """<p>One or more IPv6 addresses for the replication instance.</p>"""
    publicly_accessible: "capo_database_migration_service.types.boolean.Boolean"
    """<p> Specifies the accessibility options for the replication instance. A value of <code>true</code> represents an instance with a public IP address. A value of <code>false</code> represents an instance with a private IP address. The default value is <code>true</code>. </p>"""
    secondary_availability_zone: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Availability Zone of the standby replication instance in a Multi-AZ deployment.</p>"""
    free_until: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p> The expiration date of the free replication instance that is part of the Free DMS program. </p>"""
    dns_name_servers: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The DNS name servers supported for the replication instance to access your on-premise source or target database.</p>"""
    network_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>"""
    kerberos_authentication_settings: NotRequired[
        "capo_database_migration_service.types.kerberos_authentication_settings.KerberosAuthenticationSettings"
    ]
    """<p>Specifies the settings required for kerberos authentication when replicating an instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationInstance) -> dict:
    out: dict = {}
    if "replication_instance_identifier" in value:
        out["ReplicationInstanceIdentifier"] = value["replication_instance_identifier"]
    if "replication_instance_class" in value:
        out["ReplicationInstanceClass"] = value["replication_instance_class"]
    if "replication_instance_status" in value:
        out["ReplicationInstanceStatus"] = value["replication_instance_status"]
    out["AllocatedStorage"] = value.get("allocated_storage", 0)
    if "instance_create_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["InstanceCreateTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["instance_create_time"]
            )
        )
    if "vpc_security_groups" in value:
        import capo_database_migration_service.types.vpc_security_group_membership_list

        out["VpcSecurityGroups"] = (
            capo_database_migration_service.types.vpc_security_group_membership_list.serialize_aws_json_1_1(
                value["vpc_security_groups"]
            )
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "replication_subnet_group" in value:
        import capo_database_migration_service.types.replication_subnet_group

        out["ReplicationSubnetGroup"] = (
            capo_database_migration_service.types.replication_subnet_group.serialize_aws_json_1_1(
                value["replication_subnet_group"]
            )
        )
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "pending_modified_values" in value:
        import capo_database_migration_service.types.replication_pending_modified_values

        out["PendingModifiedValues"] = (
            capo_database_migration_service.types.replication_pending_modified_values.serialize_aws_json_1_1(
                value["pending_modified_values"]
            )
        )
    out["MultiAZ"] = value.get("multi_az", False)
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    out["AutoMinorVersionUpgrade"] = value.get("auto_minor_version_upgrade", False)
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "replication_instance_public_ip_address" in value:
        out["ReplicationInstancePublicIpAddress"] = value[
            "replication_instance_public_ip_address"
        ]
    if "replication_instance_private_ip_address" in value:
        out["ReplicationInstancePrivateIpAddress"] = value[
            "replication_instance_private_ip_address"
        ]
    if "replication_instance_public_ip_addresses" in value:
        import capo_database_migration_service.types.replication_instance_public_ip_address_list

        out["ReplicationInstancePublicIpAddresses"] = (
            capo_database_migration_service.types.replication_instance_public_ip_address_list.serialize_aws_json_1_1(
                value["replication_instance_public_ip_addresses"]
            )
        )
    if "replication_instance_private_ip_addresses" in value:
        import capo_database_migration_service.types.replication_instance_private_ip_address_list

        out["ReplicationInstancePrivateIpAddresses"] = (
            capo_database_migration_service.types.replication_instance_private_ip_address_list.serialize_aws_json_1_1(
                value["replication_instance_private_ip_addresses"]
            )
        )
    if "replication_instance_ipv6_addresses" in value:
        import capo_database_migration_service.types.replication_instance_ipv6_address_list

        out["ReplicationInstanceIpv6Addresses"] = (
            capo_database_migration_service.types.replication_instance_ipv6_address_list.serialize_aws_json_1_1(
                value["replication_instance_ipv6_addresses"]
            )
        )
    out["PubliclyAccessible"] = value.get("publicly_accessible", False)
    if "secondary_availability_zone" in value:
        out["SecondaryAvailabilityZone"] = value["secondary_availability_zone"]
    if "free_until" in value:
        import capo_database_migration_service.types.t_stamp

        out["FreeUntil"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["free_until"]
            )
        )
    if "dns_name_servers" in value:
        out["DnsNameServers"] = value["dns_name_servers"]
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


def deserialize_aws_json_1_1(data: dict) -> ReplicationInstance:
    out: ReplicationInstance = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceIdentifier") is not None:
        out["replication_instance_identifier"] = data["ReplicationInstanceIdentifier"]
    if data.get("ReplicationInstanceClass") is not None:
        out["replication_instance_class"] = data["ReplicationInstanceClass"]
    if data.get("ReplicationInstanceStatus") is not None:
        out["replication_instance_status"] = data["ReplicationInstanceStatus"]
    if data.get("AllocatedStorage") is not None:
        out["allocated_storage"] = data["AllocatedStorage"]
    else:
        out["allocated_storage"] = 0
    if data.get("InstanceCreateTime") is not None:
        import capo_database_migration_service.types.t_stamp

        out["instance_create_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["InstanceCreateTime"]
            )
        )
    if data.get("VpcSecurityGroups") is not None:
        import capo_database_migration_service.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            capo_database_migration_service.types.vpc_security_group_membership_list.deserialize_aws_json_1_1(
                data["VpcSecurityGroups"]
            )
        )
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("ReplicationSubnetGroup") is not None:
        import capo_database_migration_service.types.replication_subnet_group

        out["replication_subnet_group"] = (
            capo_database_migration_service.types.replication_subnet_group.deserialize_aws_json_1_1(
                data["ReplicationSubnetGroup"]
            )
        )
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("PendingModifiedValues") is not None:
        import capo_database_migration_service.types.replication_pending_modified_values

        out["pending_modified_values"] = (
            capo_database_migration_service.types.replication_pending_modified_values.deserialize_aws_json_1_1(
                data["PendingModifiedValues"]
            )
        )
    if data.get("MultiAZ") is not None:
        out["multi_az"] = data["MultiAZ"]
    else:
        out["multi_az"] = False
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("AutoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    else:
        out["auto_minor_version_upgrade"] = False
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if data.get("ReplicationInstancePublicIpAddress") is not None:
        out["replication_instance_public_ip_address"] = data[
            "ReplicationInstancePublicIpAddress"
        ]
    if data.get("ReplicationInstancePrivateIpAddress") is not None:
        out["replication_instance_private_ip_address"] = data[
            "ReplicationInstancePrivateIpAddress"
        ]
    if data.get("ReplicationInstancePublicIpAddresses") is not None:
        import capo_database_migration_service.types.replication_instance_public_ip_address_list

        out["replication_instance_public_ip_addresses"] = (
            capo_database_migration_service.types.replication_instance_public_ip_address_list.deserialize_aws_json_1_1(
                data["ReplicationInstancePublicIpAddresses"]
            )
        )
    if data.get("ReplicationInstancePrivateIpAddresses") is not None:
        import capo_database_migration_service.types.replication_instance_private_ip_address_list

        out["replication_instance_private_ip_addresses"] = (
            capo_database_migration_service.types.replication_instance_private_ip_address_list.deserialize_aws_json_1_1(
                data["ReplicationInstancePrivateIpAddresses"]
            )
        )
    if data.get("ReplicationInstanceIpv6Addresses") is not None:
        import capo_database_migration_service.types.replication_instance_ipv6_address_list

        out["replication_instance_ipv6_addresses"] = (
            capo_database_migration_service.types.replication_instance_ipv6_address_list.deserialize_aws_json_1_1(
                data["ReplicationInstanceIpv6Addresses"]
            )
        )
    if data.get("PubliclyAccessible") is not None:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    else:
        out["publicly_accessible"] = False
    if data.get("SecondaryAvailabilityZone") is not None:
        out["secondary_availability_zone"] = data["SecondaryAvailabilityZone"]
    if data.get("FreeUntil") is not None:
        import capo_database_migration_service.types.t_stamp

        out["free_until"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FreeUntil"]
            )
        )
    if data.get("DnsNameServers") is not None:
        out["dns_name_servers"] = data["DnsNameServers"]
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
