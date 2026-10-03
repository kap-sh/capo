"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.automation_mode
    import capo_rds.types.aws_backup_recovery_point_arn
    import capo_rds.types.boolean
    import capo_rds.types.boolean_optional
    import capo_rds.types.cloudwatch_logs_export_configuration
    import capo_rds.types.database_insights_mode
    import capo_rds.types.db_security_group_name_list
    import capo_rds.types.integer_optional
    import capo_rds.types.master_user_authentication_type
    import capo_rds.types.modify_additional_storage_volumes_list
    import capo_rds.types.processor_feature_list
    import capo_rds.types.replica_mode
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class ModifyDBInstanceMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of DB instance to modify. This value is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB instance.</p> </li> </ul>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The new amount of storage in gibibytes (GiB) to allocate for the DB instance.</p> <p>For RDS for Db2, MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL, the value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.</p> <p>For the valid values for allocated storage for each engine, see <code>CreateDBInstance</code>.</p> <p>Constraints:</p> <ul> <li> <p>When you increase the allocated storage for a DB instance that uses Provisioned IOPS (<code>gp3</code>, <code>io1</code>, or <code>io2</code> storage type), you must also specify the <code>Iops</code> parameter. You can use the current value for <code>Iops</code>.</p> </li> </ul>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The new compute and memory capacity of the DB instance, for example <code>db.m4.large</code>. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB Instance Class</a> in the <i>Amazon RDS User Guide</i> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html">Aurora DB instance classes</a> in the <i>Amazon Aurora User Guide</i>. For RDS Custom, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.instances">DB instance class support for RDS Custom for Oracle</a> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html#custom-reqs-limits.instancesMS"> DB instance class support for RDS Custom for SQL Server</a>.</p> <p>If you modify the DB instance class, an outage occurs during the change. The change is applied during the next maintenance window, unless you specify <code>ApplyImmediately</code> in your request. </p> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>If you are modifying the DB instance class and upgrading the engine version at the same time, the currently running engine version must be supported on the specified DB instance class. Otherwise, the operation returns an error. In this case, first run the operation to upgrade the engine version, and then run it again to modify the DB instance class.</p> </li> </ul>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The new DB subnet group for the DB instance. You can use this parameter to move your DB instance to a different VPC. If your DB instance isn't in a VPC, you can also use this parameter to move your DB instance into a VPC. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Non-VPC2VPC">Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Changing the subnet group causes an outage during the change. The change is applied during the next maintenance window, unless you enable <code>ApplyImmediately</code>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match existing DB subnet group.</p> </li> </ul> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    db_security_groups: NotRequired[
        "capo_rds.types.db_security_group_name_list.DBSecurityGroupNameList"
    ]
    """<p>A list of DB security groups to authorize on this DB instance. Changing this setting doesn't result in an outage and the change is asynchronously applied as soon as possible.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match existing DB security groups.</p> </li> </ul>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of Amazon EC2 VPC security groups to associate with this DB instance. This change is asynchronously applied as soon as possible.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora (The associated list of EC2 VPC security groups is managed by the DB cluster. For more information, see <code>ModifyDBCluster</code>.)</p> </li> <li> <p>RDS Custom</p> </li> </ul> <p>Constraints:</p> <ul> <li> <p>If supplied, must match existing VPC security group IDs.</p> </li> </ul>"""
    apply_immediately: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether the modifications in this request and any pending modifications are asynchronously applied as soon as possible, regardless of the <code>PreferredMaintenanceWindow</code> setting for the DB instance. By default, this parameter is disabled.</p> <p>If this parameter is disabled, changes to the DB instance are applied during the next maintenance window. Some parameter changes can cause an outage and are applied on the next call to <a>RebootDBInstance</a>, or the next failure reboot. Review the table of parameters in <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html">Modifying a DB Instance</a> in the <i>Amazon RDS User Guide</i> to see the impact of enabling or disabling <code>ApplyImmediately</code> for each modified parameter and to determine when the changes are applied.</p>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The new password for the master user.</p> <p>Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the <code>MasterUserPassword</code> element exists in the <code>PendingModifiedValues</code> element of the operation response.</p> <note> <p>Amazon RDS API operations never return the password, so this operation provides a way to regain access to a primary instance user if the password is lost. This includes restoring privileges that might have been accidentally revoked.</p> </note> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora</p> <p>The password for the master user is managed by the DB cluster. For more information, see <code>ModifyDBCluster</code>.</p> </li> <li> <p>RDS Custom</p> </li> <li> <p>RDS for Oracle CDBs in the multi-tenant configuration</p> <p>Specify the master password in <code>ModifyTenantDatabase</code> instead.</p> </li> </ul> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>ManageMasterUserPassword</code> is turned on.</p> </li> <li> <p>Can include any printable ASCII character except \"/\", \"\"\", or \"@\". For RDS for Oracle, can't include the \"&amp;\" (ampersand) or the \"'\" (single quotes) character.</p> </li> </ul> <p>Length Constraints:</p> <ul> <li> <p>RDS for Db2 - Must contain from 8 to 255 characters.</p> </li> <li> <p>RDS for MariaDB - Must contain from 8 to 41 characters.</p> </li> <li> <p>RDS for Microsoft SQL Server - Must contain from 8 to 128 characters.</p> </li> <li> <p>RDS for MySQL - Must contain from 8 to 41 characters.</p> </li> <li> <p>RDS for Oracle - Must contain from 8 to 30 characters.</p> </li> <li> <p>RDS for PostgreSQL - Must contain from 8 to 128 characters.</p> </li> </ul>"""
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group to apply to the DB instance.</p> <p>Changing this setting doesn't result in an outage. The parameter group name itself is changed immediately, but the actual parameter changes are not applied until you reboot the instance without failover. In this case, the DB instance isn't rebooted automatically, and the parameter changes aren't applied during the next maintenance window. However, if you modify dynamic parameters in the newly associated DB parameter group, these changes are applied immediately without a reboot.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>Must be in the same DB parameter group family as the DB instance.</p> </li> </ul>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain automated backups. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.</p> <note> <p>Enabling and disabling backups can result in a brief I/O suspension that lasts from a few seconds to a few minutes, depending on the size and class of your DB instance.</p> </note> <p>These changes are applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is enabled for this request. If you change the parameter from one non-zero value to another non-zero value, the change is asynchronously applied as soon as possible.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster. For more information, see <code>ModifyDBCluster</code>.</p> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 0 to 35.</p> </li> <li> <p>Can't be set to 0 if the DB instance is a source to read replicas.</p> </li> <li> <p>Can't be set to 0 for an RDS Custom for Oracle DB instance.</p> </li> </ul>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code> parameter. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible. The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow">Backup window</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster. For more information, see <code>ModifyDBCluster</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The weekly time range during which system maintenance can occur, which might result in an outage. Changing this parameter doesn't result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If there are pending actions that cause a reboot, and the maintenance window is changed to include the current time, then changing this parameter causes a reboot of the DB instance. If you change this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance">Amazon RDS Maintenance Window</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Default: Uses existing setting</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>ddd:hh24:mi-ddd:hh24:mi</code>.</p> </li> <li> <p>The day values must be <code>mon | tue | wed | thu | fri | sat | sun</code>. </p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred backup window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is a Multi-AZ deployment. Changing this parameter doesn't result in an outage. The change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is enabled for this request.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to upgrade to. Changing this parameter results in an outage and the change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is enabled for this request.</p> <p>For major version upgrades, if a nondefault DB parameter group is currently in use, a new DB parameter group in the DB parameter group family for the new engine version must be specified. The new DB parameter group can be the default for that DB parameter group family.</p> <p>If you specify only a major version, Amazon RDS updates the DB instance to the default minor version if the current minor version is lower. For information about valid engine versions, see <code>CreateDBInstance</code>, or call <code>DescribeDBEngineVersions</code>.</p> <p>If the instance that you're modifying is acting as a read replica, the engine version that you specify must be the same or higher than the version that the source DB instance or cluster is running.</p> <p>In RDS Custom for Oracle, this parameter is supported for read replicas only if they are in the <code>PATCH_DB_FAILURE</code> lifecycle.</p> <p>Constraints:</p> <ul> <li> <p>If you are upgrading the engine version and modifying the DB instance class at the same time, the currently running engine version must be supported on the specified DB instance class. Otherwise, the operation returns an error. In this case, first run the operation to upgrade the engine version, and then run it again to modify the DB instance class.</p> </li> </ul>"""
    allow_major_version_upgrade: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Specifies whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Constraints:</p> <ul> <li> <p>Major version upgrades must be allowed when specifying a value for the <code>EngineVersion</code> parameter that's a different major version than the DB instance's current version.</p> </li> </ul>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether minor version upgrades are applied automatically to the DB instance during the maintenance window. An outage occurs when all the following conditions are met:</p> <ul> <li> <p>The automatic upgrade is enabled for the maintenance window.</p> </li> <li> <p>A newer minor version is available.</p> </li> <li> <p>RDS has enabled automatic patching for the engine version.</p> </li> </ul> <p>If any of the preceding conditions isn't met, Amazon RDS applies the change as soon as possible and doesn't cause an outage.</p> <p>For an RDS Custom DB instance, don't enable this setting. Otherwise, the operation returns an error.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model for the DB instance.</p> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p> <p>Valid Values:</p> <ul> <li> <p>RDS for Db2 - <code>bring-your-own-license</code> </p> </li> <li> <p>RDS for MariaDB - <code>general-public-license</code> </p> </li> <li> <p>RDS for Microsoft SQL Server - <code>license-included | bring-your-own-media</code> </p> </li> <li> <p>RDS for MySQL - <code>general-public-license</code> </p> </li> <li> <p>RDS for Oracle - <code>bring-your-own-license | license-included</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql-license</code> </p> </li> </ul>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The new Provisioned IOPS (I/O operations per second) value for the RDS instance.</p> <p>Changing this setting doesn't result in an outage and the change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is enabled for this request. If you are migrating from Provisioned IOPS to standard storage, set this value to 0. The DB instance will require a reboot for the change in storage type to take effect.</p> <p>If you choose to migrate your DB instance from using standard storage to Provisioned IOPS (io1), or from Provisioned IOPS to standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a read replica for the instance, and creating a DB snapshot of the instance.</p> <p/> <p>Constraints:</p> <ul> <li> <p>For RDS for MariaDB, RDS for MySQL, RDS for Oracle, and RDS for PostgreSQL - The value supplied must be at least 10% greater than the current value. Values that are not at least 10% greater than the existing value are rounded up so that they are 10% greater than the current value.</p> </li> <li> <p>When you increase the Provisioned IOPS, you must also specify the <code>AllocatedStorage</code> parameter. You can use the current value for <code>AllocatedStorage</code>.</p> </li> </ul> <p>Default: Uses existing setting</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput value for the DB instance.</p> <p>This setting applies only to the <code>gp3</code> storage type.</p> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group to associate the DB instance with.</p> <p>Changing this parameter doesn't result in an outage, with one exception. If the parameter change results in an option group that enables OEM, it can cause a brief period, lasting less than a second, during which new connections are rejected but existing connections aren't interrupted.</p> <p>The change is applied during the next maintenance window unless the <code>ApplyImmediately</code> parameter is enabled for this request.</p> <p>Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance after it is associated with a DB instance.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    new_db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The new identifier for the DB instance when renaming a DB instance. When you change the DB instance identifier, an instance reboot occurs immediately if you enable <code>ApplyImmediately</code>, or will occur during the next maintenance window if you disable <code>ApplyImmediately</code>. This value is stored as a lowercase string.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type to associate with the DB instance.</p> <p>If you specify <code>io1</code>, <code>io2</code>, or <code>gp3</code> you must also include a value for the <code>Iops</code> parameter.</p> <p>If you choose to migrate your DB instance from using standard storage to gp2 (General Purpose SSD), gp3, or Provisioned IOPS (io1), or from these storage types to standard storage, the process can take time. The duration of the migration depends on several factors such as database load, storage size, storage type (standard or Provisioned IOPS), amount of IOPS provisioned (if any), and the number of prior scale storage operations. Typical migration times are under 24 hours, but the process can take up to several days in some cases. During the migration, the DB instance is available for use, but might experience performance degradation. While the migration takes place, nightly backups for the instance are suspended. No other Amazon RDS operations can take place for the instance, including modifying the instance, rebooting the instance, deleting the instance, creating a read replica for the instance, and creating a DB snapshot of the instance.</p> <p>Valid Values: <code>gp2 | gp3 | io1 | io2 | standard</code> </p> <p>Default: <code>io1</code>, if the <code>Iops</code> parameter is specified. Otherwise, <code>gp2</code>.</p>"""
    tde_credential_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN from the key store with which to associate the instance for TDE encryption.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    tde_credential_password: NotRequired[
        "capo_rds.types.sensitive_string.SensitiveString"
    ]
    """<p>The password for the given ARN from the key store in order to access the device.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the DB instance's server certificate.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to move the DB instance to. Specify <code>none</code> to remove the instance from its current domain. You must create the domain before this operation. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html"> Kerberos Authentication</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    domain_fqdn: NotRequired["capo_rds.types.string.String"]
    """<p>The fully qualified domain name (FQDN) of an Active Directory domain.</p> <p>Constraints:</p> <ul> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>mymanagedADtest.mymanagedAD.mydomain</code> </p>"""
    domain_ou: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory organizational unit for your DB instance to join.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the distinguished name format.</p> </li> </ul> <p>Example: <code>OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain</code> </p>"""
    domain_auth_secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the Secrets Manager secret with the credentials for the user joining the domain.</p> <p>Example: <code>arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456</code> </p>"""
    domain_dns_ips: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.</p> <p>Constraints:</p> <ul> <li> <p>Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.</p> </li> </ul> <p>Example: <code>123.124.125.126,234.235.236.237</code> </p>"""
    disable_domain: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to remove the DB instance from the Active Directory domain.</p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy all tags from the DB instance to snapshots of the DB instance. By default, tags aren't copied.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting. For more information, see <code>ModifyDBCluster</code>.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify <code>0</code>.</p> <p>If <code>MonitoringRoleArn</code> is specified, set <code>MonitoringInterval</code> to a value other than <code>0</code>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values: <code>0 | 1 | 5 | 10 | 15 | 30 | 60</code> </p> <p>Default: <code>0</code> </p>"""
    db_port_number: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the database accepts connections.</p> <p>The value of the <code>DBPortNumber</code> parameter must not match any of the port values specified for options in the option group for the DB instance.</p> <p>If you change the <code>DBPortNumber</code> value, your database restarts regardless of the value of the <code>ApplyImmediately</code> parameter.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values: <code>1150-65535</code> </p> <p>Default:</p> <ul> <li> <p>Amazon Aurora - <code>3306</code> </p> </li> <li> <p>RDS for Db2 - <code>50000</code> </p> </li> <li> <p>RDS for MariaDB - <code>3306</code> </p> </li> <li> <p>RDS for Microsoft SQL Server - <code>1433</code> </p> </li> <li> <p>RDS for MySQL - <code>3306</code> </p> </li> <li> <p>RDS for Oracle - <code>1521</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>5432</code> </p> </li> </ul> <p>Constraints:</p> <ul> <li> <p>For RDS for Microsoft SQL Server, the value can't be <code>1234</code>, <code>1434</code>, <code>3260</code>, <code>3343</code>, <code>3389</code>, <code>47001</code>, or <code>49152-49156</code>.</p> </li> </ul>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its Domain Name System (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB instance doesn't permit it.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p> <p> <code>PubliclyAccessible</code> only applies to DB instances in a VPC. The DB instance must be part of a public subnet and <code>PubliclyAccessible</code> must be enabled for it to be publicly accessible.</p> <p>Changes to the <code>PubliclyAccessible</code> parameter are applied immediately regardless of the value of the <code>ApplyImmediately</code> parameter.</p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html#USER_Monitoring.OS.IAMRole">To create an IAM role for Amazon RDS Enhanced Monitoring</a> in the <i>Amazon RDS User Guide.</i> </p> <p>If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, supply a <code>MonitoringRoleArn</code> value.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    promotion_tier: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance"> Fault Tolerance for an Aurora DB Cluster</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Default: <code>1</code> </p> <p>Valid Values: <code>0 - 15</code> </p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>This setting doesn't apply to Amazon Aurora. Mapping Amazon Web Services IAM accounts to database accounts is managed by the DB cluster.</p> <p>For more information about IAM database authentication, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication for MySQL and PostgreSQL</a> in the <i>Amazon RDS User Guide.</i> </p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>Specifies the mode of Database Insights to enable for the DB instance.</p> <note> <p>Aurora DB instances inherit this value from the DB cluster, so you can't change this value.</p> </note>"""
    enable_performance_insights: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable Performance Insights for the DB instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html">Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you don't specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p> <p>If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS returns an error.</p>"""
    cloudwatch_logs_export_configuration: NotRequired[
        "capo_rds.types.cloudwatch_logs_export_configuration.CloudwatchLogsExportConfiguration"
    ]
    """<p>The log types to be enabled for export to CloudWatch Logs for a specific DB instance.</p> <p>A change to the <code>CloudwatchLogsExportConfiguration</code> parameter is always applied to the DB instance immediately. Therefore, the <code>ApplyImmediately</code> parameter has no effect.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>The following values are valid for each DB engine:</p> <ul> <li> <p>Aurora MySQL - <code>audit | error | general | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>Aurora PostgreSQL - <code>postgresql | iam-db-auth-error</code> </p> </li> <li> <p>RDS for MySQL - <code>error | general | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql | upgrade | iam-db-auth-error</code> </p> </li> </ul> <p>For more information about exporting CloudWatch Logs for Amazon RDS, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch"> Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    use_default_processor_features: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance class of the DB instance uses its default processor features.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"> Deleting a DB Instance</a>.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see <code>ModifyDBCluster</code>. DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.</p> <p>For more information about this setting, including limitations that apply to it, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling"> Managing capacity automatically with Amazon RDS storage autoscaling</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    certificate_rotation_restart: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.</p> <p>By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.</p> <important> <p>Set this parameter only if you are <i>not</i> using SSL/TLS to connect to the DB instance.</p> </important> <p>If you are using SSL/TLS to connect to the DB instance, follow the appropriate instructions for your DB engine to rotate your SSL/TLS certificate:</p> <ul> <li> <p>For more information about rotating your SSL/TLS certificate for RDS DB engines, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html"> Rotating Your SSL/TLS Certificate.</a> in the <i>Amazon RDS User Guide.</i> </p> </li> <li> <p>For more information about rotating your SSL/TLS certificate for Aurora DB engines, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html"> Rotating Your SSL/TLS Certificate</a> in the <i>Amazon Aurora User Guide</i>.</p> </li> </ul> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    replica_mode: NotRequired["capo_rds.types.replica_mode.ReplicaMode"]
    """<p>The open mode of a replica database.</p> <p>This parameter is only supported for Db2 DB instances and Oracle DB instances.</p> <dl> <dt>Db2</dt> <dd> <p>Standby DB replicas are included in Db2 Advanced Edition (AE), Db2 Community Edition (CE), and Db2 Standard Edition (SE). The main use case for standby replicas is cross-Region disaster recovery. Because it doesn't accept user connections, a standby replica can't serve a read-only workload.</p> <p>You can create a combination of standby and read-only DB replicas for the same primary DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replication.html">Working with replicas for Amazon RDS for Db2</a> in the <i>Amazon RDS User Guide</i>.</p> <p>To create standby DB replicas for RDS for Db2, set this parameter to <code>mounted</code>.</p> </dd> <dt>Oracle</dt> <dd> <p>Mounted DB replicas are included in Oracle Database Enterprise Edition. The main use case for mounted replicas is cross-Region disaster recovery. The primary database doesn't use Active Data Guard to transmit information to the mounted replica. Because it doesn't accept user connections, a mounted replica can't serve a read-only workload.</p> <p>You can create a combination of mounted and read-only DB replicas for the same primary DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html">Working with read replicas for Amazon RDS for Oracle</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For RDS Custom, you must specify this parameter and set it to <code>mounted</code>. The value won't be set by default. After replica creation, you can manage the open mode manually.</p> </dd> </dl>"""
    automation_mode: NotRequired["capo_rds.types.automation_mode.AutomationMode"]
    """<p>The automation mode of the RDS Custom DB instance. If <code>full</code>, the DB instance automates monitoring and instance recovery. If <code>all paused</code>, the instance pauses automation for the duration set by <code>ResumeFullAutomationModeMinutes</code>.</p>"""
    resume_full_automation_mode_minutes: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of minutes to pause the automation. When the time period ends, RDS Custom resumes full automation.</p> <p>Default: <code>60</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be at least 60.</p> </li> <li> <p>Must be no more than 1,440.</p> </li> </ul>"""
    enable_customer_owned_ip: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.</p> <p>A <i>CoIP</i> provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about CoIPs, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing">Customer-owned IP addresses</a> in the <i>Amazon Web Services Outposts User Guide</i>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB instance. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid Values: <code>IPV4 | DUAL</code> </p>"""
    aws_backup_recovery_point_arn: NotRequired[
        "capo_rds.types.aws_backup_recovery_point_arn.AwsBackupRecoveryPointArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recovery point in Amazon Web Services Backup.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>If the DB instance doesn't manage the master user password with Amazon Web Services Secrets Manager, you can turn on this management. In this case, you can't specify <code>MasterUserPassword</code>.</p> <p>If the DB instance already manages the master user password with Amazon Web Services Secrets Manager, and you specify that the master user password is not managed with Amazon Web Services Secrets Manager, then you must specify <code>MasterUserPassword</code>. In this case, Amazon RDS deletes the secret and uses the new password for the master user specified by <code>MasterUserPassword</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p> </li> <li> <p>Can't specify for RDS for Oracle CDB instances in the multi-tenant configuration. Use <code>ModifyTenantDatabase</code> instead.</p> </li> <li> <p>Can't specify the parameters <code>ManageMasterUserPassword</code> and <code>MultiTenant</code> in the same operation.</p> </li> </ul>"""
    rotate_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance. The secret value contains the updated password.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>You must apply the change immediately when rotating the master user password.</p> </li> </ul>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if both of the following conditions are met:</p> <ul> <li> <p>The DB instance doesn't manage the master user password in Amazon Web Services Secrets Manager.</p> <p>If the DB instance already manages the master user password in Amazon Web Services Secrets Manager, you can't change the KMS key used to encrypt the secret.</p> </li> <li> <p>You are turning on <code>ManageMasterUserPassword</code> to manage the master user password in Amazon Web Services Secrets Manager.</p> <p>If you are turning on <code>ManageMasterUserPassword</code> and don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> </li> </ul> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    multi_tenant: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the to convert your DB instance from the single-tenant conﬁguration to the multi-tenant conﬁguration. This parameter is supported only for RDS for Oracle CDB instances.</p> <p>During the conversion, RDS creates an initial tenant database and associates the DB name, master user name, character set, and national character set metadata with this database. The tags associated with the instance also propagate to the initial tenant database. You can add more tenant databases to your DB instance by using the <code>CreateTenantDatabase</code> operation.</p> <important> <p>The conversion to the multi-tenant configuration is permanent and irreversible, so you can't later convert back to the single-tenant configuration. When you specify this parameter, you must also specify <code>ApplyImmediately</code>.</p> </important>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The target Oracle DB engine when you convert a non-CDB to a CDB. This intermediate step is necessary to upgrade an Oracle Database 19c non-CDB to an Oracle Database 21c CDB.</p> <p>Note the following requirements:</p> <ul> <li> <p>Make sure that you specify <code>oracle-ee-cdb</code> or <code>oracle-se2-cdb</code>.</p> </li> <li> <p>Make sure that your DB engine runs Oracle Database 19c with an April 2021 or later RU.</p> </li> </ul> <p>Note the following limitations:</p> <ul> <li> <p>You can't convert a CDB to a non-CDB.</p> </li> <li> <p>You can't convert a replica database.</p> </li> <li> <p>You can't convert a non-CDB to a CDB and upgrade the engine version in the same command.</p> </li> <li> <p>You can't convert the existing custom parameter or option group when it has options or parameters that are permanent or persistent. In this situation, the DB instance reverts to the default option and parameter group. To avoid reverting to the default, specify a new parameter group with <code>--db-parameter-group-name</code> and a new option group with <code>--option-group-name</code>.</p> </li> </ul>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.modify_additional_storage_volumes_list.ModifyAdditionalStorageVolumesList"
    ]
    """<p>A list of additional storage volumes to modify or delete for the DB instance. You can create up to 3 additional storage volumes. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.</p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB instance.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> </ul>"""
    master_user_authentication_type: NotRequired[
        "capo_rds.types.master_user_authentication_type.MasterUserAuthenticationType"
    ]
    """<p>Specifies the authentication type for the master user. With IAM master user authentication, you can change the master DB user to use IAM database authentication.</p> <p>You can specify one of the following values:</p> <ul> <li> <p> <code>password</code> - Use standard database authentication with a password.</p> </li> <li> <p> <code>iam-db-auth</code> - Use IAM database authentication for the master user.</p> </li> </ul> <p>This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB instance.</p> <p>This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the engine lifecycle support is managed by the DB cluster.</p> <p>You can use this setting to enroll your DB instance into Amazon RDS Extended Support or to opt out. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_security_groups" in value:
        import capo_rds.types.db_security_group_name_list

        capo_rds.types.db_security_group_name_list.serialize_query(
            value["db_security_groups"], pairs, f"{key_prefix}DBSecurityGroups"
        )
    if "vpc_security_group_ids" in value:
        import capo_rds.types.vpc_security_group_id_list

        capo_rds.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{key_prefix}ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
        )
    if "backup_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}BackupRetentionPeriod",
                str(value["backup_retention_period"]),
            )
        )
    if "preferred_backup_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredBackupWindow",
                str(value["preferred_backup_window"]),
            )
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "allow_major_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AllowMajorVersionUpgrade",
                "true" if value["allow_major_version_upgrade"] else "false",
            )
        )
    if "auto_minor_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AutoMinorVersionUpgrade",
                "true" if value["auto_minor_version_upgrade"] else "false",
            )
        )
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "new_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}NewDBInstanceIdentifier",
                str(value["new_db_instance_identifier"]),
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "tde_credential_arn" in value:
        pairs.append(
            (f"{key_prefix}TdeCredentialArn", str(value["tde_credential_arn"]))
        )
    if "tde_credential_password" in value:
        pairs.append(
            (
                f"{key_prefix}TdeCredentialPassword",
                str(value["tde_credential_password"]),
            )
        )
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "domain" in value:
        pairs.append((f"{key_prefix}Domain", str(value["domain"])))
    if "domain_fqdn" in value:
        pairs.append((f"{key_prefix}DomainFqdn", str(value["domain_fqdn"])))
    if "domain_ou" in value:
        pairs.append((f"{key_prefix}DomainOu", str(value["domain_ou"])))
    if "domain_auth_secret_arn" in value:
        pairs.append(
            (f"{key_prefix}DomainAuthSecretArn", str(value["domain_auth_secret_arn"]))
        )
    if "domain_dns_ips" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["domain_dns_ips"], pairs, f"{key_prefix}DomainDnsIps"
        )
    if "disable_domain" in value:
        pairs.append(
            (
                f"{key_prefix}DisableDomain",
                "true" if value["disable_domain"] else "false",
            )
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
    if "db_port_number" in value:
        pairs.append((f"{key_prefix}DBPortNumber", str(value["db_port_number"])))
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "monitoring_role_arn" in value:
        pairs.append(
            (f"{key_prefix}MonitoringRoleArn", str(value["monitoring_role_arn"]))
        )
    if "domain_iam_role_name" in value:
        pairs.append(
            (f"{key_prefix}DomainIAMRoleName", str(value["domain_iam_role_name"]))
        )
    if "promotion_tier" in value:
        pairs.append((f"{key_prefix}PromotionTier", str(value["promotion_tier"])))
    if "enable_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}EnableIAMDatabaseAuthentication",
                "true" if value["enable_iam_database_authentication"] else "false",
            )
        )
    if "database_insights_mode" in value:
        import capo_rds.types.database_insights_mode

        capo_rds.types.database_insights_mode.serialize_query(
            value["database_insights_mode"], pairs, f"{key_prefix}DatabaseInsightsMode"
        )
    if "enable_performance_insights" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePerformanceInsights",
                "true" if value["enable_performance_insights"] else "false",
            )
        )
    if "performance_insights_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsKMSKeyId",
                str(value["performance_insights_kms_key_id"]),
            )
        )
    if "performance_insights_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}PerformanceInsightsRetentionPeriod",
                str(value["performance_insights_retention_period"]),
            )
        )
    if "cloudwatch_logs_export_configuration" in value:
        import capo_rds.types.cloudwatch_logs_export_configuration

        capo_rds.types.cloudwatch_logs_export_configuration.serialize_query(
            value["cloudwatch_logs_export_configuration"],
            pairs,
            f"{key_prefix}CloudwatchLogsExportConfiguration",
        )
    if "processor_features" in value:
        import capo_rds.types.processor_feature_list

        capo_rds.types.processor_feature_list.serialize_query(
            value["processor_features"], pairs, f"{key_prefix}ProcessorFeatures"
        )
    if "use_default_processor_features" in value:
        pairs.append(
            (
                f"{key_prefix}UseDefaultProcessorFeatures",
                "true" if value["use_default_processor_features"] else "false",
            )
        )
    if "deletion_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeletionProtection",
                "true" if value["deletion_protection"] else "false",
            )
        )
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{key_prefix}MaxAllocatedStorage", str(value["max_allocated_storage"]))
        )
    if "certificate_rotation_restart" in value:
        pairs.append(
            (
                f"{key_prefix}CertificateRotationRestart",
                "true" if value["certificate_rotation_restart"] else "false",
            )
        )
    if "replica_mode" in value:
        import capo_rds.types.replica_mode

        capo_rds.types.replica_mode.serialize_query(
            value["replica_mode"], pairs, f"{key_prefix}ReplicaMode"
        )
    if "automation_mode" in value:
        import capo_rds.types.automation_mode

        capo_rds.types.automation_mode.serialize_query(
            value["automation_mode"], pairs, f"{key_prefix}AutomationMode"
        )
    if "resume_full_automation_mode_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}ResumeFullAutomationModeMinutes",
                str(value["resume_full_automation_mode_minutes"]),
            )
        )
    if "enable_customer_owned_ip" in value:
        pairs.append(
            (
                f"{key_prefix}EnableCustomerOwnedIp",
                "true" if value["enable_customer_owned_ip"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "aws_backup_recovery_point_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AwsBackupRecoveryPointArn",
                str(value["aws_backup_recovery_point_arn"]),
            )
        )
    if "manage_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}ManageMasterUserPassword",
                "true" if value["manage_master_user_password"] else "false",
            )
        )
    if "rotate_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}RotateMasterUserPassword",
                "true" if value["rotate_master_user_password"] else "false",
            )
        )
    if "master_user_secret_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}MasterUserSecretKmsKeyId",
                str(value["master_user_secret_kms_key_id"]),
            )
        )
    if "multi_tenant" in value:
        pairs.append(
            (f"{key_prefix}MultiTenant", "true" if value["multi_tenant"] else "false")
        )
    if "dedicated_log_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DedicatedLogVolume",
                "true" if value["dedicated_log_volume"] else "false",
            )
        )
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "additional_storage_volumes" in value:
        import capo_rds.types.modify_additional_storage_volumes_list

        capo_rds.types.modify_additional_storage_volumes_list.serialize_query(
            value["additional_storage_volumes"],
            pairs,
            f"{key_prefix}AdditionalStorageVolumes",
        )
    if "tag_specifications" in value:
        import capo_rds.types.tag_specification_list

        capo_rds.types.tag_specification_list.serialize_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "master_user_authentication_type" in value:
        import capo_rds.types.master_user_authentication_type

        capo_rds.types.master_user_authentication_type.serialize_query(
            value["master_user_authentication_type"],
            pairs,
            f"{key_prefix}MasterUserAuthenticationType",
        )
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )


def deserialize_query(el: Element) -> ModifyDBInstanceMessage:
    out: ModifyDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_db_security_groups = el.find("DBSecurityGroups")
    if child_db_security_groups is not None:
        import capo_rds.types.db_security_group_name_list

        out["db_security_groups"] = (
            capo_rds.types.db_security_group_name_list.deserialize_query(
                child_db_security_groups
            )
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_rds.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_rds.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_allow_major_version_upgrade = el.find("AllowMajorVersionUpgrade")
    if child_allow_major_version_upgrade is not None:
        out["allow_major_version_upgrade"] = (
            child_allow_major_version_upgrade.text or ""
        ).lower() == "true"
    child_auto_minor_version_upgrade = el.find("AutoMinorVersionUpgrade")
    if child_auto_minor_version_upgrade is not None:
        out["auto_minor_version_upgrade"] = (
            child_auto_minor_version_upgrade.text or ""
        ).lower() == "true"
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_new_db_instance_identifier = el.find("NewDBInstanceIdentifier")
    if child_new_db_instance_identifier is not None:
        out["new_db_instance_identifier"] = str(
            child_new_db_instance_identifier.text or ""
        )
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_tde_credential_password = el.find("TdeCredentialPassword")
    if child_tde_credential_password is not None:
        out["tde_credential_password"] = str(child_tde_credential_password.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_domain_fqdn = el.find("DomainFqdn")
    if child_domain_fqdn is not None:
        out["domain_fqdn"] = str(child_domain_fqdn.text or "")
    child_domain_ou = el.find("DomainOu")
    if child_domain_ou is not None:
        out["domain_ou"] = str(child_domain_ou.text or "")
    child_domain_auth_secret_arn = el.find("DomainAuthSecretArn")
    if child_domain_auth_secret_arn is not None:
        out["domain_auth_secret_arn"] = str(child_domain_auth_secret_arn.text or "")
    child_domain_dns_ips = el.find("DomainDnsIps")
    if child_domain_dns_ips is not None:
        import capo_rds.types.string_list

        out["domain_dns_ips"] = capo_rds.types.string_list.deserialize_query(
            child_domain_dns_ips
        )
    child_disable_domain = el.find("DisableDomain")
    if child_disable_domain is not None:
        out["disable_domain"] = (child_disable_domain.text or "").lower() == "true"
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_db_port_number = el.find("DBPortNumber")
    if child_db_port_number is not None:
        out["db_port_number"] = int(child_db_port_number.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
    child_domain_iam_role_name = el.find("DomainIAMRoleName")
    if child_domain_iam_role_name is not None:
        out["domain_iam_role_name"] = str(child_domain_iam_role_name.text or "")
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    child_enable_iam_database_authentication = el.find(
        "EnableIAMDatabaseAuthentication"
    )
    if child_enable_iam_database_authentication is not None:
        out["enable_iam_database_authentication"] = (
            child_enable_iam_database_authentication.text or ""
        ).lower() == "true"
    child_database_insights_mode = el.find("DatabaseInsightsMode")
    if child_database_insights_mode is not None:
        import capo_rds.types.database_insights_mode

        out["database_insights_mode"] = (
            capo_rds.types.database_insights_mode.deserialize_query(
                child_database_insights_mode
            )
        )
    child_enable_performance_insights = el.find("EnablePerformanceInsights")
    if child_enable_performance_insights is not None:
        out["enable_performance_insights"] = (
            child_enable_performance_insights.text or ""
        ).lower() == "true"
    child_performance_insights_kms_key_id = el.find("PerformanceInsightsKMSKeyId")
    if child_performance_insights_kms_key_id is not None:
        out["performance_insights_kms_key_id"] = str(
            child_performance_insights_kms_key_id.text or ""
        )
    child_performance_insights_retention_period = el.find(
        "PerformanceInsightsRetentionPeriod"
    )
    if child_performance_insights_retention_period is not None:
        out["performance_insights_retention_period"] = int(
            child_performance_insights_retention_period.text or ""
        )
    child_cloudwatch_logs_export_configuration = el.find(
        "CloudwatchLogsExportConfiguration"
    )
    if child_cloudwatch_logs_export_configuration is not None:
        import capo_rds.types.cloudwatch_logs_export_configuration

        out["cloudwatch_logs_export_configuration"] = (
            capo_rds.types.cloudwatch_logs_export_configuration.deserialize_query(
                child_cloudwatch_logs_export_configuration
            )
        )
    child_processor_features = el.find("ProcessorFeatures")
    if child_processor_features is not None:
        import capo_rds.types.processor_feature_list

        out["processor_features"] = (
            capo_rds.types.processor_feature_list.deserialize_query(
                child_processor_features
            )
        )
    child_use_default_processor_features = el.find("UseDefaultProcessorFeatures")
    if child_use_default_processor_features is not None:
        out["use_default_processor_features"] = (
            child_use_default_processor_features.text or ""
        ).lower() == "true"
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
    child_certificate_rotation_restart = el.find("CertificateRotationRestart")
    if child_certificate_rotation_restart is not None:
        out["certificate_rotation_restart"] = (
            child_certificate_rotation_restart.text or ""
        ).lower() == "true"
    child_replica_mode = el.find("ReplicaMode")
    if child_replica_mode is not None:
        import capo_rds.types.replica_mode

        out["replica_mode"] = capo_rds.types.replica_mode.deserialize_query(
            child_replica_mode
        )
    child_automation_mode = el.find("AutomationMode")
    if child_automation_mode is not None:
        import capo_rds.types.automation_mode

        out["automation_mode"] = capo_rds.types.automation_mode.deserialize_query(
            child_automation_mode
        )
    child_resume_full_automation_mode_minutes = el.find(
        "ResumeFullAutomationModeMinutes"
    )
    if child_resume_full_automation_mode_minutes is not None:
        out["resume_full_automation_mode_minutes"] = int(
            child_resume_full_automation_mode_minutes.text or ""
        )
    child_enable_customer_owned_ip = el.find("EnableCustomerOwnedIp")
    if child_enable_customer_owned_ip is not None:
        out["enable_customer_owned_ip"] = (
            child_enable_customer_owned_ip.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_aws_backup_recovery_point_arn = el.find("AwsBackupRecoveryPointArn")
    if child_aws_backup_recovery_point_arn is not None:
        out["aws_backup_recovery_point_arn"] = str(
            child_aws_backup_recovery_point_arn.text or ""
        )
    child_manage_master_user_password = el.find("ManageMasterUserPassword")
    if child_manage_master_user_password is not None:
        out["manage_master_user_password"] = (
            child_manage_master_user_password.text or ""
        ).lower() == "true"
    child_rotate_master_user_password = el.find("RotateMasterUserPassword")
    if child_rotate_master_user_password is not None:
        out["rotate_master_user_password"] = (
            child_rotate_master_user_password.text or ""
        ).lower() == "true"
    child_master_user_secret_kms_key_id = el.find("MasterUserSecretKmsKeyId")
    if child_master_user_secret_kms_key_id is not None:
        out["master_user_secret_kms_key_id"] = str(
            child_master_user_secret_kms_key_id.text or ""
        )
    child_multi_tenant = el.find("MultiTenant")
    if child_multi_tenant is not None:
        out["multi_tenant"] = (child_multi_tenant.text or "").lower() == "true"
    child_dedicated_log_volume = el.find("DedicatedLogVolume")
    if child_dedicated_log_volume is not None:
        out["dedicated_log_volume"] = (
            child_dedicated_log_volume.text or ""
        ).lower() == "true"
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.modify_additional_storage_volumes_list

        out["additional_storage_volumes"] = (
            capo_rds.types.modify_additional_storage_volumes_list.deserialize_query(
                child_additional_storage_volumes
            )
        )
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_rds.types.tag_specification_list

        out["tag_specifications"] = (
            capo_rds.types.tag_specification_list.deserialize_query(
                child_tag_specifications
            )
        )
    child_master_user_authentication_type = el.find("MasterUserAuthenticationType")
    if child_master_user_authentication_type is not None:
        import capo_rds.types.master_user_authentication_type

        out["master_user_authentication_type"] = (
            capo_rds.types.master_user_authentication_type.deserialize_query(
                child_master_user_authentication_type
            )
        )
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    return out
