"""Generated from Smithy shape ``com.amazonaws.neptune#DBInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean
    import capo_neptune.types.boolean_optional
    import capo_neptune.types.db_instance_status_info_list
    import capo_neptune.types.db_parameter_group_status_list
    import capo_neptune.types.db_security_group_membership_list
    import capo_neptune.types.db_subnet_group
    import capo_neptune.types.domain_membership_list
    import capo_neptune.types.endpoint
    import capo_neptune.types.integer
    import capo_neptune.types.integer_optional
    import capo_neptune.types.log_type_list
    import capo_neptune.types.option_group_membership_list
    import capo_neptune.types.pending_modified_values
    import capo_neptune.types.read_replica_db_cluster_identifier_list
    import capo_neptune.types.read_replica_db_instance_identifier_list
    import capo_neptune.types.string
    import capo_neptune.types.t_stamp
    import capo_neptune.types.vpc_security_group_membership_list


class DBInstance(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>Contains a user-supplied database identifier. This identifier is the unique key that identifies a DB instance.</p>"""
    db_instance_class: NotRequired["capo_neptune.types.string.String"]
    """<p>Contains the name of the compute and memory capacity class of the DB instance.</p>"""
    engine: NotRequired["capo_neptune.types.string.String"]
    """<p>Provides the name of the database engine to be used for this DB instance.</p>"""
    db_instance_status: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the current state of this database.</p>"""
    master_username: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    db_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The database name.</p>"""
    endpoint: NotRequired["capo_neptune.types.endpoint.Endpoint"]
    """<p>Specifies the connection endpoint.</p>"""
    allocated_storage: NotRequired["capo_neptune.types.integer.Integer"]
    """<p>Not supported by Neptune.</p>"""
    instance_create_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p>Provides the date and time the DB instance was created.</p>"""
    preferred_backup_window: NotRequired["capo_neptune.types.string.String"]
    """<p> Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.</p>"""
    backup_retention_period: NotRequired["capo_neptune.types.integer.Integer"]
    """<p>Specifies the number of days for which automatic DB snapshots are retained.</p>"""
    db_security_groups: NotRequired[
        "capo_neptune.types.db_security_group_membership_list.DBSecurityGroupMembershipList"
    ]
    """<p> Provides List of DB security group elements containing only <code>DBSecurityGroup.Name</code> and <code>DBSecurityGroup.Status</code> subelements.</p>"""
    vpc_security_groups: NotRequired[
        "capo_neptune.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>Provides a list of VPC security group elements that the DB instance belongs to.</p>"""
    db_parameter_groups: NotRequired[
        "capo_neptune.types.db_parameter_group_status_list.DBParameterGroupStatusList"
    ]
    """<p>Provides the list of DB parameter groups applied to this DB instance.</p>"""
    availability_zone: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the name of the Availability Zone the DB instance is located in.</p>"""
    db_subnet_group: NotRequired["capo_neptune.types.db_subnet_group.DBSubnetGroup"]
    """<p>Specifies information on the subnet group associated with the DB instance, including the name, description, and subnets in the subnet group.</p>"""
    preferred_maintenance_window: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>"""
    pending_modified_values: NotRequired[
        "capo_neptune.types.pending_modified_values.PendingModifiedValues"
    ]
    """<p>Specifies that changes to the DB instance are pending. This element is only included when changes are pending. Specific changes are identified by subelements.</p>"""
    latest_restorable_time: NotRequired["capo_neptune.types.t_stamp.TStamp"]
    """<p>Specifies the latest time to which a database can be restored with point-in-time restore.</p>"""
    multi_az: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Specifies if the DB instance is a Multi-AZ deployment.</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>Indicates the database engine version.</p>"""
    auto_minor_version_upgrade: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates that minor version patches are applied automatically.</p>"""
    read_replica_source_db_instance_identifier: NotRequired[
        "capo_neptune.types.string.String"
    ]
    """<p>Contains the identifier of the source DB instance if this DB instance is a Read Replica.</p>"""
    read_replica_db_instance_identifiers: NotRequired[
        "capo_neptune.types.read_replica_db_instance_identifier_list.ReadReplicaDBInstanceIdentifierList"
    ]
    """<p>Contains one or more identifiers of the Read Replicas associated with this DB instance.</p>"""
    read_replica_db_cluster_identifiers: NotRequired[
        "capo_neptune.types.read_replica_db_cluster_identifier_list.ReadReplicaDBClusterIdentifierList"
    ]
    """<p>Contains one or more identifiers of DB clusters that are Read Replicas of this DB instance.</p>"""
    license_model: NotRequired["capo_neptune.types.string.String"]
    """<p>License model information for this DB instance.</p>"""
    iops: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>Specifies the Provisioned IOPS (I/O operations per second) value.</p>"""
    option_group_memberships: NotRequired[
        "capo_neptune.types.option_group_membership_list.OptionGroupMembershipList"
    ]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    character_set_name: NotRequired["capo_neptune.types.string.String"]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    secondary_availability_zone: NotRequired["capo_neptune.types.string.String"]
    """<p>If present, specifies the name of the secondary Availability Zone for a DB instance with multi-AZ support.</p>"""
    publicly_accessible: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB cluster doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p>"""
    status_infos: NotRequired[
        "capo_neptune.types.db_instance_status_info_list.DBInstanceStatusInfoList"
    ]
    """<p>The status of a Read Replica. If the instance is not a Read Replica, this is blank.</p>"""
    storage_type: NotRequired["capo_neptune.types.string.String"]
    """<p>Specifies the storage type associated with the DB instance.</p>"""
    tde_credential_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The ARN from the key store with which the instance is associated for TDE encryption.</p>"""
    db_instance_port: NotRequired["capo_neptune.types.integer.Integer"]
    """<p>Specifies the port that the DB instance listens on. If the DB instance is part of a DB cluster, this can be a different port than the DB cluster port.</p>"""
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.</p>"""
    storage_encrypted: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Not supported: The encryption for DB instances is managed by the DB cluster.</p>"""
    kms_key_id: NotRequired["capo_neptune.types.string.String"]
    """<p> Not supported: The encryption for DB instances is managed by the DB cluster.</p>"""
    dbi_resource_id: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Region-unique, immutable identifier for the DB instance. This identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS key for the DB instance is accessed.</p>"""
    ca_certificate_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier of the CA certificate for this DB instance.</p>"""
    domain_memberships: NotRequired[
        "capo_neptune.types.domain_membership_list.DomainMembershipList"
    ]
    """<p>Not supported</p>"""
    copy_tags_to_snapshot: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Specifies whether tags are copied from the DB instance to snapshots of the DB instance.</p>"""
    monitoring_interval: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.</p>"""
    enhanced_monitoring_resource_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log stream that receives the Enhanced Monitoring metrics data for the DB instance.</p>"""
    monitoring_role_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The ARN for the IAM role that permits Neptune to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.</p>"""
    promotion_tier: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>A value that specifies the order in which a Read Replica is promoted to the primary instance after a failure of the existing primary instance. </p>"""
    db_instance_arn: NotRequired["capo_neptune.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB instance.</p>"""
    timezone: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "capo_neptune.types.boolean.Boolean"
    ]
    """<p>True if Amazon Identity and Access Management (IAM) authentication is enabled, and otherwise false.</p>"""
    performance_insights_enabled: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    performance_insights_kms_key_id: NotRequired["capo_neptune.types.string.String"]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    enabled_cloudwatch_logs_exports: NotRequired[
        "capo_neptune.types.log_type_list.LogTypeList"
    ]
    """<p>A list of log types that this DB instance is configured to export to CloudWatch Logs.</p>"""
    deletion_protection: NotRequired[
        "capo_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether or not the DB instance has deletion protection enabled. The instance can't be deleted when deletion protection is enabled. See <a href="https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-instances-delete.html">Deleting a DB Instance</a>.</p>"""
    network_type: NotRequired["capo_neptune.types.string.String"]
    """<p>The network type of the DB instance. Inherited from the DB cluster.</p> <p>Valid Values: <code>IPV4</code>, <code>DUAL</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "db_instance_status" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceStatus", str(value["db_instance_status"]))
        )
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "endpoint" in value:
        import capo_neptune.types.endpoint

        capo_neptune.types.endpoint.serialize_query(
            value["endpoint"], pairs, f"{key_prefix}Endpoint"
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "instance_create_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["instance_create_time"], pairs, f"{key_prefix}InstanceCreateTime"
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "db_security_groups" in value:
        import capo_neptune.types.db_security_group_membership_list

        capo_neptune.types.db_security_group_membership_list.serialize_query(
            value["db_security_groups"], pairs, f"{key_prefix}DBSecurityGroups"
        )
    if "vpc_security_groups" in value:
        import capo_neptune.types.vpc_security_group_membership_list

        capo_neptune.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_groups"], pairs, f"{key_prefix}VpcSecurityGroups"
        )
    if "db_parameter_groups" in value:
        import capo_neptune.types.db_parameter_group_status_list

        capo_neptune.types.db_parameter_group_status_list.serialize_query(
            value["db_parameter_groups"], pairs, f"{key_prefix}DBParameterGroups"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "db_subnet_group" in value:
        import capo_neptune.types.db_subnet_group

        capo_neptune.types.db_subnet_group.serialize_query(
            value["db_subnet_group"], pairs, f"{key_prefix}DBSubnetGroup"
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "pending_modified_values" in value:
        import capo_neptune.types.pending_modified_values

        capo_neptune.types.pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "latest_restorable_time" in value:
        import capo_neptune.types.t_stamp

        capo_neptune.types.t_stamp.serialize_query(
            value["latest_restorable_time"], pairs, f"{key_prefix}LatestRestorableTime"
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "read_replica_source_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}ReadReplicaSourceDBInstanceIdentifier",
                str(value["read_replica_source_db_instance_identifier"]),
            )
        )
    if "read_replica_db_instance_identifiers" in value:
        import capo_neptune.types.read_replica_db_instance_identifier_list

        capo_neptune.types.read_replica_db_instance_identifier_list.serialize_query(
            value["read_replica_db_instance_identifiers"],
            pairs,
            f"{key_prefix}ReadReplicaDBInstanceIdentifiers",
        )
    if "read_replica_db_cluster_identifiers" in value:
        import capo_neptune.types.read_replica_db_cluster_identifier_list

        capo_neptune.types.read_replica_db_cluster_identifier_list.serialize_query(
            value["read_replica_db_cluster_identifiers"],
            pairs,
            f"{key_prefix}ReadReplicaDBClusterIdentifiers",
        )
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "option_group_memberships" in value:
        import capo_neptune.types.option_group_membership_list

        capo_neptune.types.option_group_membership_list.serialize_query(
            value["option_group_memberships"],
            pairs,
            f"{key_prefix}OptionGroupMemberships",
        )
    if "character_set_name" in value:
        pairs.append(
            (f"{key_prefix}CharacterSetName", str(value["character_set_name"]))
        )
    if "secondary_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryAvailabilityZone",
                str(value["secondary_availability_zone"]),
            )
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "status_infos" in value:
        import capo_neptune.types.db_instance_status_info_list

        capo_neptune.types.db_instance_status_info_list.serialize_query(
            value["status_infos"], pairs, f"{key_prefix}StatusInfos"
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "tde_credential_arn" in value:
        pairs.append(
            (f"{key_prefix}TdeCredentialArn", str(value["tde_credential_arn"]))
        )
    if "db_instance_port" in value:
        pairs.append((f"{key_prefix}DbInstancePort", str(value["db_instance_port"])))
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "dbi_resource_id" in value:
        pairs.append((f"{key_prefix}DbiResourceId", str(value["dbi_resource_id"])))
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "domain_memberships" in value:
        import capo_neptune.types.domain_membership_list

        capo_neptune.types.domain_membership_list.serialize_query(
            value["domain_memberships"], pairs, f"{key_prefix}DomainMemberships"
        )
    if "copy_tags_to_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}CopyTagsToSnapshot",
                "true" if value["copy_tags_to_snapshot"] else "false",
            )
        )
    if "monitoring_interval" in value:
        pairs.append(
            (f"{key_prefix}MonitoringInterval", str(value["monitoring_interval"]))
        )
    if "enhanced_monitoring_resource_arn" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedMonitoringResourceArn",
                str(value["enhanced_monitoring_resource_arn"]),
            )
        )
    if "monitoring_role_arn" in value:
        pairs.append(
            (f"{key_prefix}MonitoringRoleArn", str(value["monitoring_role_arn"]))
        )
    if "promotion_tier" in value:
        pairs.append((f"{key_prefix}PromotionTier", str(value["promotion_tier"])))
    if "db_instance_arn" in value:
        pairs.append((f"{key_prefix}DBInstanceArn", str(value["db_instance_arn"])))
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))
    if "iam_database_authentication_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}IAMDatabaseAuthenticationEnabled",
                "true" if value["iam_database_authentication_enabled"] else "false",
            )
        )
    if "performance_insights_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsEnabled",
                "true" if value["performance_insights_enabled"] else "false",
            )
        )
    if "performance_insights_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsKMSKeyId",
                str(value["performance_insights_kms_key_id"]),
            )
        )
    if "enabled_cloudwatch_logs_exports" in value:
        import capo_neptune.types.log_type_list

        capo_neptune.types.log_type_list.serialize_query(
            value["enabled_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnabledCloudwatchLogsExports",
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))


def deserialize_query(el: Element) -> DBInstance:
    out: DBInstance = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_db_instance_status = el.find("DBInstanceStatus")
    if child_db_instance_status is not None:
        out["db_instance_status"] = str(child_db_instance_status.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        import capo_neptune.types.endpoint

        out["endpoint"] = capo_neptune.types.endpoint.deserialize_query(child_endpoint)
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_instance_create_time = el.find("InstanceCreateTime")
    if child_instance_create_time is not None:
        import capo_neptune.types.t_stamp

        out["instance_create_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_instance_create_time
        )
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_db_security_groups = el.find("DBSecurityGroups")
    if child_db_security_groups is not None:
        import capo_neptune.types.db_security_group_membership_list

        out["db_security_groups"] = (
            capo_neptune.types.db_security_group_membership_list.deserialize_query(
                child_db_security_groups
            )
        )
    child_vpc_security_groups = el.find("VpcSecurityGroups")
    if child_vpc_security_groups is not None:
        import capo_neptune.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            capo_neptune.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_groups
            )
        )
    child_db_parameter_groups = el.find("DBParameterGroups")
    if child_db_parameter_groups is not None:
        import capo_neptune.types.db_parameter_group_status_list

        out["db_parameter_groups"] = (
            capo_neptune.types.db_parameter_group_status_list.deserialize_query(
                child_db_parameter_groups
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        import capo_neptune.types.db_subnet_group

        out["db_subnet_group"] = capo_neptune.types.db_subnet_group.deserialize_query(
            child_db_subnet_group
        )
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_neptune.types.pending_modified_values

        out["pending_modified_values"] = (
            capo_neptune.types.pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_latest_restorable_time = el.find("LatestRestorableTime")
    if child_latest_restorable_time is not None:
        import capo_neptune.types.t_stamp

        out["latest_restorable_time"] = capo_neptune.types.t_stamp.deserialize_query(
            child_latest_restorable_time
        )
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_read_replica_source_db_instance_identifier = el.find(
        "ReadReplicaSourceDBInstanceIdentifier"
    )
    if child_read_replica_source_db_instance_identifier is not None:
        out["read_replica_source_db_instance_identifier"] = str(
            child_read_replica_source_db_instance_identifier.text or ""
        )
    child_read_replica_db_instance_identifiers = el.find(
        "ReadReplicaDBInstanceIdentifiers"
    )
    if child_read_replica_db_instance_identifiers is not None:
        import capo_neptune.types.read_replica_db_instance_identifier_list

        out["read_replica_db_instance_identifiers"] = (
            capo_neptune.types.read_replica_db_instance_identifier_list.deserialize_query(
                child_read_replica_db_instance_identifiers
            )
        )
    child_read_replica_db_cluster_identifiers = el.find(
        "ReadReplicaDBClusterIdentifiers"
    )
    if child_read_replica_db_cluster_identifiers is not None:
        import capo_neptune.types.read_replica_db_cluster_identifier_list

        out["read_replica_db_cluster_identifiers"] = (
            capo_neptune.types.read_replica_db_cluster_identifier_list.deserialize_query(
                child_read_replica_db_cluster_identifiers
            )
        )
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_option_group_memberships = el.find("OptionGroupMemberships")
    if child_option_group_memberships is not None:
        import capo_neptune.types.option_group_membership_list

        out["option_group_memberships"] = (
            capo_neptune.types.option_group_membership_list.deserialize_query(
                child_option_group_memberships
            )
        )
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_secondary_availability_zone = el.find("SecondaryAvailabilityZone")
    if child_secondary_availability_zone is not None:
        out["secondary_availability_zone"] = str(
            child_secondary_availability_zone.text or ""
        )
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_status_infos = el.find("StatusInfos")
    if child_status_infos is not None:
        import capo_neptune.types.db_instance_status_info_list

        out["status_infos"] = (
            capo_neptune.types.db_instance_status_info_list.deserialize_query(
                child_status_infos
            )
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_db_instance_port = el.find("DbInstancePort")
    if child_db_instance_port is not None:
        out["db_instance_port"] = int(child_db_instance_port.text or "")
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_dbi_resource_id = el.find("DbiResourceId")
    if child_dbi_resource_id is not None:
        out["dbi_resource_id"] = str(child_dbi_resource_id.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_domain_memberships = el.find("DomainMemberships")
    if child_domain_memberships is not None:
        import capo_neptune.types.domain_membership_list

        out["domain_memberships"] = (
            capo_neptune.types.domain_membership_list.deserialize_query(
                child_domain_memberships
            )
        )
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_enhanced_monitoring_resource_arn = el.find("EnhancedMonitoringResourceArn")
    if child_enhanced_monitoring_resource_arn is not None:
        out["enhanced_monitoring_resource_arn"] = str(
            child_enhanced_monitoring_resource_arn.text or ""
        )
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    child_db_instance_arn = el.find("DBInstanceArn")
    if child_db_instance_arn is not None:
        out["db_instance_arn"] = str(child_db_instance_arn.text or "")
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
    child_iam_database_authentication_enabled = el.find(
        "IAMDatabaseAuthenticationEnabled"
    )
    if child_iam_database_authentication_enabled is not None:
        out["iam_database_authentication_enabled"] = (
            child_iam_database_authentication_enabled.text or ""
        ).lower() == "true"
    child_performance_insights_enabled = el.find("PerformanceInsightsEnabled")
    if child_performance_insights_enabled is not None:
        out["performance_insights_enabled"] = (
            child_performance_insights_enabled.text or ""
        ).lower() == "true"
    child_performance_insights_kms_key_id = el.find("PerformanceInsightsKMSKeyId")
    if child_performance_insights_kms_key_id is not None:
        out["performance_insights_kms_key_id"] = str(
            child_performance_insights_kms_key_id.text or ""
        )
    child_enabled_cloudwatch_logs_exports = el.find("EnabledCloudwatchLogsExports")
    if child_enabled_cloudwatch_logs_exports is not None:
        import capo_neptune.types.log_type_list

        out["enabled_cloudwatch_logs_exports"] = (
            capo_neptune.types.log_type_list.deserialize_query(
                child_enabled_cloudwatch_logs_exports
            )
        )
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    return out
