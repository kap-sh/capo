"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.kerberos_authentication_settings
    import capo_database_migration_service.types.replication_instance_class
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.vpc_security_group_id_list


class ModifyReplicationInstanceMessage(TypedDict, closed=True):
    replication_instance_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    allocated_storage: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of storage (in gigabytes) to be allocated for the replication instance.</p>"""
    apply_immediately: "capo_database_migration_service.types.boolean.Boolean"
    """<p>Indicates whether the changes should be applied immediately or during the next maintenance window.</p>"""
    replication_instance_class: NotRequired[
        "capo_database_migration_service.types.replication_instance_class.ReplicationInstanceClass"
    ]
    """<p>The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to <code>"dms.c4.large"</code>.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth"> Selecting the right DMS replication instance for your migration</a>. </p>"""
    vpc_security_group_ids: NotRequired[
        "capo_database_migration_service.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p> Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance. </p>"""
    preferred_maintenance_window: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.</p> <p>Default: Uses existing setting</p> <p>Format: ddd:hh24:mi-ddd:hh24:mi</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Must be at least 30 minutes</p>"""
    multi_az: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p> Specifies whether the replication instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the Multi-AZ parameter is set to <code>true</code>. </p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The engine version number of the replication instance.</p> <p>When modifying a major engine version of an instance, also set <code>AllowMajorVersionUpgrade</code> to <code>true</code>.</p>"""
    allow_major_version_upgrade: "capo_database_migration_service.types.boolean.Boolean"
    """<p>Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.</p> <p>This parameter must be set to <code>true</code> when specifying a value for the <code>EngineVersion</code> parameter that is a different major version than the replication instance's current version.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates that minor version upgrades are applied automatically to the replication instance during the maintenance window. Changing this parameter doesn't result in an outage, except in the case described following. The change is asynchronously applied as soon as possible. </p> <p>An outage does result if these factors apply: </p> <ul> <li> <p>This parameter is set to <code>true</code> during the maintenance window.</p> </li> <li> <p>A newer minor version is available. </p> </li> <li> <p>DMS has enabled automatic patching for the given engine version. </p> </li> </ul>"""
    replication_instance_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The replication instance identifier. This parameter is stored as a lowercase string.</p>"""
    network_type: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>"""
    kerberos_authentication_settings: NotRequired[
        "capo_database_migration_service.types.kerberos_authentication_settings.KerberosAuthenticationSettings"
    ]
    """<p>Specifies the settings required for kerberos authentication when modifying a replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationInstanceMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    out["ApplyImmediately"] = value.get("apply_immediately", False)
    if "replication_instance_class" in value:
        out["ReplicationInstanceClass"] = value["replication_instance_class"]
    if "vpc_security_group_ids" in value:
        import capo_database_migration_service.types.vpc_security_group_id_list

        out["VpcSecurityGroupIds"] = (
            capo_database_migration_service.types.vpc_security_group_id_list.serialize_aws_json_1_1(
                value["vpc_security_group_ids"]
            )
        )
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "multi_az" in value:
        out["MultiAZ"] = value["multi_az"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    out["AllowMajorVersionUpgrade"] = value.get("allow_major_version_upgrade", False)
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "replication_instance_identifier" in value:
        out["ReplicationInstanceIdentifier"] = value["replication_instance_identifier"]
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


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationInstanceMessage:
    out: ModifyReplicationInstanceMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "ModifyReplicationInstanceMessage.replication_instance_arn required"
        )
    if data.get("AllocatedStorage") is not None:
        out["allocated_storage"] = data["AllocatedStorage"]
    if data.get("ApplyImmediately") is not None:
        out["apply_immediately"] = data["ApplyImmediately"]
    else:
        out["apply_immediately"] = False
    if data.get("ReplicationInstanceClass") is not None:
        out["replication_instance_class"] = data["ReplicationInstanceClass"]
    if data.get("VpcSecurityGroupIds") is not None:
        import capo_database_migration_service.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_database_migration_service.types.vpc_security_group_id_list.deserialize_aws_json_1_1(
                data["VpcSecurityGroupIds"]
            )
        )
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("MultiAZ") is not None:
        out["multi_az"] = data["MultiAZ"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("AllowMajorVersionUpgrade") is not None:
        out["allow_major_version_upgrade"] = data["AllowMajorVersionUpgrade"]
    else:
        out["allow_major_version_upgrade"] = False
    if data.get("AutoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if data.get("ReplicationInstanceIdentifier") is not None:
        out["replication_instance_identifier"] = data["ReplicationInstanceIdentifier"]
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
