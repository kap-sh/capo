"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_cluster_associated_roles
    import capo_securityhub.types.aws_rds_db_cluster_members
    import capo_securityhub.types.aws_rds_db_cluster_option_group_memberships
    import capo_securityhub.types.aws_rds_db_domain_memberships
    import capo_securityhub.types.aws_rds_db_instance_vpc_security_groups
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsRdsDbClusterDetails(TypedDict, closed=True):
    allocated_storage: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>For all database engines except Aurora, specifies the allocated storage size in gibibytes (GiB).</p>"""
    availability_zones: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>A list of Availability Zones (AZs) where instances in the DB cluster can be created.</p>"""
    backup_retention_period: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of days for which automated backups are retained.</p>"""
    database_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the database.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current status of this DB cluster.</p>"""
    endpoint: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The connection endpoint for the primary instance of the DB cluster.</p>"""
    reader_endpoint: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reader endpoint for the DB cluster.</p>"""
    custom_endpoints: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>A list of custom endpoints for the DB cluster.</p>"""
    multi_az: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB cluster has instances in multiple Availability Zones.</p>"""
    engine: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the database engine to use for this DB cluster. Valid values are as follows:</p> <ul> <li> <p> <code>aurora</code> </p> </li> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> </ul>"""
    engine_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version number of the database engine to use.</p>"""
    port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The port number on which the DB instances in the DB cluster accept connections.</p>"""
    master_username: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the master user for the DB cluster.</p>"""
    preferred_backup_window: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The range of time each day when automated backups are created, if automated backups are enabled.</p> <p>Uses the format <code>HH:MM-HH:MM</code>. For example, <code>04:52-05:22</code>.</p>"""
    preferred_maintenance_window: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p>Uses the format <code><day>:HH:MM-<day>:HH:MM</code>.</p> <p>For the day values, use <code>mon</code>|<code>tue</code>|<code>wed</code>|<code>thu</code>|<code>fri</code>|<code>sat</code>|<code>sun</code>.</p> <p>For example, <code>sun:09:32-sun:10:02</code>.</p>"""
    read_replica_identifiers: NotRequired[
        "capo_securityhub.types.string_list.StringList"
    ]
    """<p>The identifiers of the read replicas that are associated with this DB cluster.</p>"""
    vpc_security_groups: NotRequired[
        "capo_securityhub.types.aws_rds_db_instance_vpc_security_groups.AwsRdsDbInstanceVpcSecurityGroups"
    ]
    """<p>A list of VPC security groups that the DB cluster belongs to.</p>"""
    hosted_zone_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the identifier that Amazon Route 53 assigns when you create a hosted zone.</p>"""
    storage_encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB cluster is encrypted.</p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the KMS master key that is used to encrypt the database instances in the DB cluster.</p>"""
    db_cluster_resource_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the DB cluster. The identifier must be unique within each Amazon Web Services Region and is immutable.</p>"""
    associated_roles: NotRequired[
        "capo_securityhub.types.aws_rds_db_cluster_associated_roles.AwsRdsDbClusterAssociatedRoles"
    ]
    """<p>A list of the IAM roles that are associated with the DB cluster.</p>"""
    cluster_create_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when the DB cluster was created, in Universal Coordinated Time (UTC).</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    enabled_cloud_watch_logs_exports: NotRequired[
        "capo_securityhub.types.string_list.StringList"
    ]
    """<p>A list of log types that this DB cluster is configured to export to CloudWatch Logs.</p>"""
    engine_mode: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The database engine mode of the DB cluster.Valid values are as follows:</p> <ul> <li> <p> <code>global</code> </p> </li> <li> <p> <code>multimaster</code> </p> </li> <li> <p> <code>parallelquery</code> </p> </li> <li> <p> <code>provisioned</code> </p> </li> <li> <p> <code>serverless</code> </p> </li> </ul>"""
    deletion_protection: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB cluster has deletion protection enabled.</p>"""
    http_endpoint_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the HTTP endpoint for an Aurora Serverless DB cluster is enabled.</p>"""
    activity_stream_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the database activity stream. Valid values are as follows:</p> <ul> <li> <p> <code>started</code> </p> </li> <li> <p> <code>starting</code> </p> </li> <li> <p> <code>stopped</code> </p> </li> <li> <p> <code>stopping</code> </p> </li> </ul>"""
    copy_tags_to_snapshot: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether tags are copied from the DB cluster to snapshots of the DB cluster.</p>"""
    cross_account_clone: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB cluster is a clone of a DB cluster owned by a different Amazon Web Services account.</p>"""
    domain_memberships: NotRequired[
        "capo_securityhub.types.aws_rds_db_domain_memberships.AwsRdsDbDomainMemberships"
    ]
    """<p>The Active Directory domain membership records that are associated with the DB cluster.</p>"""
    db_cluster_parameter_group: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the DB cluster parameter group for the DB cluster.</p>"""
    db_subnet_group: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The subnet group that is associated with the DB cluster, including the name, description, and subnets in the subnet group.</p>"""
    db_cluster_option_group_memberships: NotRequired[
        "capo_securityhub.types.aws_rds_db_cluster_option_group_memberships.AwsRdsDbClusterOptionGroupMemberships"
    ]
    """<p>The list of option group memberships for this DB cluster.</p>"""
    db_cluster_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The DB cluster identifier that the user assigned to the cluster. This identifier is the unique key that identifies a DB cluster.</p>"""
    db_cluster_members: NotRequired[
        "capo_securityhub.types.aws_rds_db_cluster_members.AwsRdsDbClusterMembers"
    ]
    """<p>The list of instances that make up the DB cluster.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether the mapping of IAM accounts to database accounts is enabled.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates if minor version upgrades are automatically applied to the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterDetails) -> dict:
    out: dict = {}
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "availability_zones" in value:
        import capo_securityhub.types.string_list

        out["AvailabilityZones"] = capo_securityhub.types.string_list.serialize_json(
            value["availability_zones"]
        )
    if "backup_retention_period" in value:
        out["BackupRetentionPeriod"] = value["backup_retention_period"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "reader_endpoint" in value:
        out["ReaderEndpoint"] = value["reader_endpoint"]
    if "custom_endpoints" in value:
        import capo_securityhub.types.string_list

        out["CustomEndpoints"] = capo_securityhub.types.string_list.serialize_json(
            value["custom_endpoints"]
        )
    if "multi_az" in value:
        out["MultiAz"] = value["multi_az"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "port" in value:
        out["Port"] = value["port"]
    if "master_username" in value:
        out["MasterUsername"] = value["master_username"]
    if "preferred_backup_window" in value:
        out["PreferredBackupWindow"] = value["preferred_backup_window"]
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "read_replica_identifiers" in value:
        import capo_securityhub.types.string_list

        out["ReadReplicaIdentifiers"] = (
            capo_securityhub.types.string_list.serialize_json(
                value["read_replica_identifiers"]
            )
        )
    if "vpc_security_groups" in value:
        import capo_securityhub.types.aws_rds_db_instance_vpc_security_groups

        out["VpcSecurityGroups"] = (
            capo_securityhub.types.aws_rds_db_instance_vpc_security_groups.serialize_json(
                value["vpc_security_groups"]
            )
        )
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    if "storage_encrypted" in value:
        out["StorageEncrypted"] = value["storage_encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "db_cluster_resource_id" in value:
        out["DbClusterResourceId"] = value["db_cluster_resource_id"]
    if "associated_roles" in value:
        import capo_securityhub.types.aws_rds_db_cluster_associated_roles

        out["AssociatedRoles"] = (
            capo_securityhub.types.aws_rds_db_cluster_associated_roles.serialize_json(
                value["associated_roles"]
            )
        )
    if "cluster_create_time" in value:
        out["ClusterCreateTime"] = value["cluster_create_time"]
    if "enabled_cloud_watch_logs_exports" in value:
        import capo_securityhub.types.string_list

        out["EnabledCloudWatchLogsExports"] = (
            capo_securityhub.types.string_list.serialize_json(
                value["enabled_cloud_watch_logs_exports"]
            )
        )
    if "engine_mode" in value:
        out["EngineMode"] = value["engine_mode"]
    if "deletion_protection" in value:
        out["DeletionProtection"] = value["deletion_protection"]
    if "http_endpoint_enabled" in value:
        out["HttpEndpointEnabled"] = value["http_endpoint_enabled"]
    if "activity_stream_status" in value:
        out["ActivityStreamStatus"] = value["activity_stream_status"]
    if "copy_tags_to_snapshot" in value:
        out["CopyTagsToSnapshot"] = value["copy_tags_to_snapshot"]
    if "cross_account_clone" in value:
        out["CrossAccountClone"] = value["cross_account_clone"]
    if "domain_memberships" in value:
        import capo_securityhub.types.aws_rds_db_domain_memberships

        out["DomainMemberships"] = (
            capo_securityhub.types.aws_rds_db_domain_memberships.serialize_json(
                value["domain_memberships"]
            )
        )
    if "db_cluster_parameter_group" in value:
        out["DbClusterParameterGroup"] = value["db_cluster_parameter_group"]
    if "db_subnet_group" in value:
        out["DbSubnetGroup"] = value["db_subnet_group"]
    if "db_cluster_option_group_memberships" in value:
        import capo_securityhub.types.aws_rds_db_cluster_option_group_memberships

        out["DbClusterOptionGroupMemberships"] = (
            capo_securityhub.types.aws_rds_db_cluster_option_group_memberships.serialize_json(
                value["db_cluster_option_group_memberships"]
            )
        )
    if "db_cluster_identifier" in value:
        out["DbClusterIdentifier"] = value["db_cluster_identifier"]
    if "db_cluster_members" in value:
        import capo_securityhub.types.aws_rds_db_cluster_members

        out["DbClusterMembers"] = (
            capo_securityhub.types.aws_rds_db_cluster_members.serialize_json(
                value["db_cluster_members"]
            )
        )
    if "iam_database_authentication_enabled" in value:
        out["IamDatabaseAuthenticationEnabled"] = value[
            "iam_database_authentication_enabled"
        ]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbClusterDetails:
    out: AwsRdsDbClusterDetails = {}  # type: ignore[typeddict-item]
    if data.get("AllocatedStorage") is not None:
        out["allocated_storage"] = data["AllocatedStorage"]
    if data.get("AvailabilityZones") is not None:
        import capo_securityhub.types.string_list

        out["availability_zones"] = capo_securityhub.types.string_list.deserialize_json(
            data["AvailabilityZones"]
        )
    if data.get("BackupRetentionPeriod") is not None:
        out["backup_retention_period"] = data["BackupRetentionPeriod"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Endpoint") is not None:
        out["endpoint"] = data["Endpoint"]
    if data.get("ReaderEndpoint") is not None:
        out["reader_endpoint"] = data["ReaderEndpoint"]
    if data.get("CustomEndpoints") is not None:
        import capo_securityhub.types.string_list

        out["custom_endpoints"] = capo_securityhub.types.string_list.deserialize_json(
            data["CustomEndpoints"]
        )
    if data.get("MultiAz") is not None:
        out["multi_az"] = data["MultiAz"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("MasterUsername") is not None:
        out["master_username"] = data["MasterUsername"]
    if data.get("PreferredBackupWindow") is not None:
        out["preferred_backup_window"] = data["PreferredBackupWindow"]
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("ReadReplicaIdentifiers") is not None:
        import capo_securityhub.types.string_list

        out["read_replica_identifiers"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["ReadReplicaIdentifiers"]
            )
        )
    if data.get("VpcSecurityGroups") is not None:
        import capo_securityhub.types.aws_rds_db_instance_vpc_security_groups

        out["vpc_security_groups"] = (
            capo_securityhub.types.aws_rds_db_instance_vpc_security_groups.deserialize_json(
                data["VpcSecurityGroups"]
            )
        )
    if data.get("HostedZoneId") is not None:
        out["hosted_zone_id"] = data["HostedZoneId"]
    if data.get("StorageEncrypted") is not None:
        out["storage_encrypted"] = data["StorageEncrypted"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("DbClusterResourceId") is not None:
        out["db_cluster_resource_id"] = data["DbClusterResourceId"]
    if data.get("AssociatedRoles") is not None:
        import capo_securityhub.types.aws_rds_db_cluster_associated_roles

        out["associated_roles"] = (
            capo_securityhub.types.aws_rds_db_cluster_associated_roles.deserialize_json(
                data["AssociatedRoles"]
            )
        )
    if data.get("ClusterCreateTime") is not None:
        out["cluster_create_time"] = data["ClusterCreateTime"]
    if data.get("EnabledCloudWatchLogsExports") is not None:
        import capo_securityhub.types.string_list

        out["enabled_cloud_watch_logs_exports"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["EnabledCloudWatchLogsExports"]
            )
        )
    if data.get("EngineMode") is not None:
        out["engine_mode"] = data["EngineMode"]
    if data.get("DeletionProtection") is not None:
        out["deletion_protection"] = data["DeletionProtection"]
    if data.get("HttpEndpointEnabled") is not None:
        out["http_endpoint_enabled"] = data["HttpEndpointEnabled"]
    if data.get("ActivityStreamStatus") is not None:
        out["activity_stream_status"] = data["ActivityStreamStatus"]
    if data.get("CopyTagsToSnapshot") is not None:
        out["copy_tags_to_snapshot"] = data["CopyTagsToSnapshot"]
    if data.get("CrossAccountClone") is not None:
        out["cross_account_clone"] = data["CrossAccountClone"]
    if data.get("DomainMemberships") is not None:
        import capo_securityhub.types.aws_rds_db_domain_memberships

        out["domain_memberships"] = (
            capo_securityhub.types.aws_rds_db_domain_memberships.deserialize_json(
                data["DomainMemberships"]
            )
        )
    if data.get("DbClusterParameterGroup") is not None:
        out["db_cluster_parameter_group"] = data["DbClusterParameterGroup"]
    if data.get("DbSubnetGroup") is not None:
        out["db_subnet_group"] = data["DbSubnetGroup"]
    if data.get("DbClusterOptionGroupMemberships") is not None:
        import capo_securityhub.types.aws_rds_db_cluster_option_group_memberships

        out["db_cluster_option_group_memberships"] = (
            capo_securityhub.types.aws_rds_db_cluster_option_group_memberships.deserialize_json(
                data["DbClusterOptionGroupMemberships"]
            )
        )
    if data.get("DbClusterIdentifier") is not None:
        out["db_cluster_identifier"] = data["DbClusterIdentifier"]
    if data.get("DbClusterMembers") is not None:
        import capo_securityhub.types.aws_rds_db_cluster_members

        out["db_cluster_members"] = (
            capo_securityhub.types.aws_rds_db_cluster_members.deserialize_json(
                data["DbClusterMembers"]
            )
        )
    if data.get("IamDatabaseAuthenticationEnabled") is not None:
        out["iam_database_authentication_enabled"] = data[
            "IamDatabaseAuthenticationEnabled"
        ]
    if data.get("AutoMinorVersionUpgrade") is not None:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    return out
