"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ComputeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.string_list


class ComputeConfig(TypedDict, closed=True):
    availability_zone: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Availability Zone where the DMS Serverless replication using this configuration will run. The default value is a random, system-chosen Availability Zone in the configuration's Amazon Web Services Region, for example, <code>"us-west-2"</code>. You can't set this parameter if the <code>MultiAZ</code> parameter is set to <code>true</code>.</p>"""
    dns_name_servers: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A list of custom DNS name servers supported for the DMS Serverless replication to access your source or target database. This list overrides the default name servers supported by the DMS Serverless replication. You can specify a comma-separated list of internet addresses for up to four DNS name servers. For example: <code>"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"</code> </p>"""
    kms_key_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An Key Management Service (KMS) key Amazon Resource Name (ARN) that is used to encrypt the data during DMS Serverless replication.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    max_capacity_units: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the maximum value of the DMS capacity units (DCUs) for which a given DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the maximum value that you can specify for DMS Serverless is 384. The <code>MaxCapacityUnits</code> parameter is the only DCU parameter you are required to specify.</p>"""
    min_capacity_units: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the minimum value of the DMS capacity units (DCUs) for which a given DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the minimum DCU value that you can specify for DMS Serverless is 1. If you don't set this value, DMS sets this parameter to the minimum DCU value allowed, 1. If there is no current source activity, DMS scales down your replication until it reaches the value specified in <code>MinCapacityUnits</code>.</p>"""
    multi_az: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DMS Serverless replication is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the <code>MultiAZ</code> parameter is set to <code>true</code>.</p>"""
    preferred_maintenance_window: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The weekly time range during which system maintenance can occur for the DMS Serverless replication, in Universal Coordinated Time (UTC). The format is <code>ddd:hh24:mi-ddd:hh24:mi</code>.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time per Amazon Web Services Region. This maintenance occurs on a random day of the week. Valid values for days of the week include <code>Mon</code>, <code>Tue</code>, <code>Wed</code>, <code>Thu</code>, <code>Fri</code>, <code>Sat</code>, and <code>Sun</code>.</p> <p>Constraints include a minimum 30-minute window.</p>"""
    replication_subnet_group_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Specifies a subnet group identifier to associate with the DMS Serverless replication.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_database_migration_service.types.string_list.StringList"
    ]
    """<p>Specifies the virtual private cloud (VPC) security group to use with the DMS Serverless replication. The VPC security group must work with the VPC containing the replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeConfig) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "dns_name_servers" in value:
        out["DnsNameServers"] = value["dns_name_servers"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "max_capacity_units" in value:
        out["MaxCapacityUnits"] = value["max_capacity_units"]
    if "min_capacity_units" in value:
        out["MinCapacityUnits"] = value["min_capacity_units"]
    if "multi_az" in value:
        out["MultiAZ"] = value["multi_az"]
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "replication_subnet_group_id" in value:
        out["ReplicationSubnetGroupId"] = value["replication_subnet_group_id"]
    if "vpc_security_group_ids" in value:
        import capo_database_migration_service.types.string_list

        out["VpcSecurityGroupIds"] = (
            capo_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["vpc_security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeConfig:
    out: ComputeConfig = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("DnsNameServers") is not None:
        out["dns_name_servers"] = data["DnsNameServers"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("MaxCapacityUnits") is not None:
        out["max_capacity_units"] = data["MaxCapacityUnits"]
    if data.get("MinCapacityUnits") is not None:
        out["min_capacity_units"] = data["MinCapacityUnits"]
    if data.get("MultiAZ") is not None:
        out["multi_az"] = data["MultiAZ"]
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("ReplicationSubnetGroupId") is not None:
        out["replication_subnet_group_id"] = data["ReplicationSubnetGroupId"]
    if data.get("VpcSecurityGroupIds") is not None:
        import capo_database_migration_service.types.string_list

        out["vpc_security_group_ids"] = (
            capo_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["VpcSecurityGroupIds"]
            )
        )
    return out
