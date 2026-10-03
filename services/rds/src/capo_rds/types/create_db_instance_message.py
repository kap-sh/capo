"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.additional_storage_volumes_list
    import capo_rds.types.boolean_optional
    import capo_rds.types.database_insights_mode
    import capo_rds.types.db_security_group_name_list
    import capo_rds.types.integer_optional
    import capo_rds.types.log_type_list
    import capo_rds.types.master_user_authentication_type
    import capo_rds.types.processor_feature_list
    import capo_rds.types.sensitive_string
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.tag_list
    import capo_rds.types.tag_specification_list
    import capo_rds.types.vpc_security_group_id_list


class CreateDBInstanceMessage(TypedDict, closed=True):
    db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The meaning of this parameter differs according to the database engine you use.</p> <dl> <dt>Amazon Aurora MySQL</dt> <dd> <p>The name of the database to create when the primary DB instance of the Aurora MySQL DB cluster is created. If this parameter isn't specified for an Aurora MySQL DB cluster, no database is created in the DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 alphanumeric characters.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).</p> </li> <li> <p>Can't be a word reserved by the database engine.</p> </li> </ul> </dd> <dt>Amazon Aurora PostgreSQL</dt> <dd> <p>The name of the database to create when the primary DB instance of the Aurora PostgreSQL DB cluster is created. A database named <code>postgres</code> is always created. If this parameter is specified, an additional database with this name is created.</p> <p>Constraints:</p> <ul> <li> <p>It must contain 1 to 63 alphanumeric characters.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0 to 9).</p> </li> <li> <p>Can't be a word reserved by the database engine.</p> </li> </ul> </dd> <dt>Amazon RDS Custom for Oracle</dt> <dd> <p>The Oracle System ID (SID) of the created RDS Custom DB instance. If you don't specify a value, the default value is <code>ORCL</code> for non-CDBs and <code>RDSCDB</code> for CDBs.</p> <p>Default: <code>ORCL</code> </p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 8 alphanumeric characters.</p> </li> <li> <p>Must contain a letter.</p> </li> <li> <p>Can't be a word reserved by the database engine.</p> </li> </ul> </dd> <dt>Amazon RDS Custom for SQL Server</dt> <dd> <p>Not applicable. Must be null.</p> </dd> <dt>RDS for Db2</dt> <dd> <p>The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance. In some cases, we recommend that you don't add a database name. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-db-instance-prereqs.html#db2-prereqs-additional-considerations">Additional considerations</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> </li> </ul> </dd> <dt>RDS for MariaDB</dt> <dd> <p>The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> </li> </ul> </dd> <dt>RDS for MySQL</dt> <dd> <p>The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> </li> </ul> </dd> <dt>RDS for Oracle</dt> <dd> <p>The Oracle System ID (SID) of the created DB instance. If you don't specify a value, the default value is <code>ORCL</code>. You can't specify the string <code>null</code>, or any other reserved word, for <code>DBName</code>.</p> <p>Default: <code>ORCL</code> </p> <p>Constraints:</p> <ul> <li> <p>Can't be longer than 8 characters.</p> </li> </ul> </dd> <dt>RDS for PostgreSQL</dt> <dd> <p>The name of the database to create when the DB instance is created. A database named <code>postgres</code> is always created. If this parameter is specified, an additional database with this name is created.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 63 letters, numbers, or underscores.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> </li> </ul> </dd> <dt>RDS for SQL Server</dt> <dd> <p>Not applicable. Must be null.</p> </dd> </dl>"""
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for this DB instance. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>mydbinstance</code> </p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage in gibibytes (GiB) to allocate for the DB instance.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. Aurora cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in an Aurora cluster volume.</p> <dl> <dt>Amazon RDS Custom</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp2, gp3): Must be an integer from 40 to 65536 for RDS Custom for Oracle, 16384 for RDS Custom for SQL Server.</p> </li> <li> <p>Provisioned IOPS storage (io1, io2): Must be an integer from 40 to 65536 for RDS Custom for Oracle, 16384 for RDS Custom for SQL Server.</p> </li> </ul> </dd> <dt>RDS for Db2</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp3): Must be an integer from 20 to 65536.</p> </li> <li> <p>Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.</p> </li> </ul> </dd> <dt>RDS for MariaDB</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.</p> </li> <li> <p>Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.</p> </li> <li> <p>Magnetic storage (standard): Must be an integer from 5 to 3072.</p> </li> </ul> </dd> <dt>RDS for MySQL</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.</p> </li> <li> <p>Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.</p> </li> <li> <p>Magnetic storage (standard): Must be an integer from 5 to 3072.</p> </li> </ul> </dd> <dt>RDS for Oracle</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.</p> </li> <li> <p>Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.</p> </li> <li> <p>Magnetic storage (standard): Must be an integer from 10 to 3072.</p> </li> </ul> </dd> <dt>RDS for PostgreSQL</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp2, gp3): Must be an integer from 20 to 65536.</p> </li> <li> <p>Provisioned IOPS storage (io1, io2): Must be an integer from 100 to 65536.</p> </li> <li> <p>Magnetic storage (standard): Must be an integer from 5 to 3072.</p> </li> </ul> </dd> <dt>RDS for SQL Server</dt> <dd> <p>Constraints to the amount of storage for each storage type are the following:</p> <ul> <li> <p>General Purpose (SSD) storage (gp2, gp3):</p> <ul> <li> <p>Enterprise and Standard editions: Must be an integer from 20 to 16384.</p> </li> <li> <p>Web and Express editions: Must be an integer from 20 to 16384.</p> </li> </ul> </li> <li> <p>Provisioned IOPS storage (io1, io2):</p> <ul> <li> <p>Enterprise and Standard editions: Must be an integer from 100 to 16384.</p> </li> <li> <p>Web and Express editions: Must be an integer from 100 to 16384.</p> </li> </ul> </li> <li> <p>Magnetic storage (standard):</p> <ul> <li> <p>Enterprise and Standard editions: Must be an integer from 20 to 1024.</p> </li> <li> <p>Web and Express editions: Must be an integer from 20 to 1024.</p> </li> </ul> </li> </ul> </dd> </dl>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The compute and memory capacity of the DB instance, for example <code>db.m5.large</code>. Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html">DB instance classes</a> in the <i>Amazon RDS User Guide</i> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html">Aurora DB instance classes</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine to use for this DB instance.</p> <p>Not every database engine is available in every Amazon Web Services Region.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> (for Aurora MySQL DB instances)</p> </li> <li> <p> <code>aurora-postgresql</code> (for Aurora PostgreSQL DB instances)</p> </li> <li> <p> <code>custom-oracle-ee</code> (for RDS Custom for Oracle DB instances)</p> </li> <li> <p> <code>custom-oracle-ee-cdb</code> (for RDS Custom for Oracle DB instances)</p> </li> <li> <p> <code>custom-oracle-se2</code> (for RDS Custom for Oracle DB instances)</p> </li> <li> <p> <code>custom-oracle-se2-cdb</code> (for RDS Custom for Oracle DB instances)</p> </li> <li> <p> <code>custom-sqlserver-ee</code> (for RDS Custom for SQL Server DB instances)</p> </li> <li> <p> <code>custom-sqlserver-se</code> (for RDS Custom for SQL Server DB instances)</p> </li> <li> <p> <code>custom-sqlserver-web</code> (for RDS Custom for SQL Server DB instances)</p> </li> <li> <p> <code>custom-sqlserver-dev</code> (for RDS Custom for SQL Server DB instances)</p> </li> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-ce</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-dev-ee</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    master_username: NotRequired["capo_rds.types.string.String"]
    """<p>The name for the master user.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The name for the master user is managed by the DB cluster.</p> <p>This setting is required for RDS DB instances.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 16 letters, numbers, or underscores.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> </li> </ul>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The password for the master user.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The password for the master user is managed by the DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be specified if <code>ManageMasterUserPassword</code> is turned on.</p> </li> <li> <p>Can include any printable ASCII character except \"/\", \"\"\", or \"@\". For RDS for Oracle, can't include the \"&amp;\" (ampersand) or the \"'\" (single quotes) character.</p> </li> </ul> <p>Length Constraints:</p> <ul> <li> <p>RDS for Db2 - Must contain from 8 to 255 characters.</p> </li> <li> <p>RDS for MariaDB - Must contain from 8 to 41 characters.</p> </li> <li> <p>RDS for Microsoft SQL Server - Must contain from 8 to 128 characters.</p> </li> <li> <p>RDS for MySQL - Must contain from 8 to 41 characters.</p> </li> <li> <p>RDS for Oracle - Must contain from 8 to 30 characters.</p> </li> <li> <p>RDS for PostgreSQL - Must contain from 8 to 128 characters.</p> </li> </ul>"""
    db_security_groups: NotRequired[
        "capo_rds.types.db_security_group_name_list.DBSecurityGroupNameList"
    ]
    """<p>A list of DB security groups to associate with this DB instance.</p> <p>This setting applies to the legacy EC2-Classic platform, which is no longer used to create new DB instances. Use the <code>VpcSecurityGroupIds</code> setting instead.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_rds.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of Amazon EC2 VPC security groups to associate with this DB instance.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The associated list of EC2 VPC security groups is managed by the DB cluster.</p> <p>Default: The default EC2 VPC security group for the DB subnet group's VPC.</p>"""
    availability_zone: NotRequired["capo_rds.types.string.String"]
    """<p>The Availability Zone (AZ) where the database will be created. For information on Amazon Web Services Regions and Availability Zones, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html">Regions and Availability Zones</a>.</p> <p>For Amazon Aurora, each Aurora DB cluster hosts copies of its storage in three separate Availability Zones. Specify one of these Availability Zones. Aurora automatically chooses an appropriate Availability Zone if you don't specify one.</p> <p>Default: A random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region.</p> <p>Constraints:</p> <ul> <li> <p>The <code>AvailabilityZone</code> parameter can't be specified if the DB instance is a Multi-AZ deployment.</p> </li> <li> <p>The specified Availability Zone must be in the same Amazon Web Services Region as the current endpoint.</p> </li> </ul> <p>Example: <code>us-east-1d</code> </p>"""
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>A DB subnet group to associate with this DB instance.</p> <p>Constraints:</p> <ul> <li> <p>Must match the name of an existing DB subnet group.</p> </li> </ul> <p>Example: <code>mydbsubnetgroup</code> </p>"""
    preferred_maintenance_window: NotRequired["capo_rds.types.string.String"]
    """<p>The time range each week during which system maintenance can occur. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#Concepts.DBMaintenance">Amazon RDS Maintenance Window</a> in the <i>Amazon RDS User Guide.</i> </p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>ddd:hh24:mi-ddd:hh24:mi</code>.</p> </li> <li> <p>The day values must be <code>mon | tue | wed | thu | fri | sat | sun</code>. </p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred backup window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    db_parameter_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB parameter group to associate with this DB instance. If you don't specify a value, then Amazon RDS uses the default DB parameter group for the specified DB engine and version.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    backup_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to <code>0</code> disables automated backups.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The retention period for automated backups is managed by the DB cluster.</p> <p>Default: <code>1</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be a value from 0 to 35.</p> </li> <li> <p>Can't be set to 0 if the DB instance is a source to read replicas.</p> </li> <li> <p>Can't be set to 0 for an RDS Custom for Oracle DB instance.</p> </li> </ul>"""
    preferred_backup_window: NotRequired["capo_rds.types.string.String"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow">Backup window</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The daily time range for creating automated backups is managed by the DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the format <code>hh24:mi-hh24:mi</code>.</p> </li> <li> <p>Must be in Universal Coordinated Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    port: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the database accepts connections.</p> <p>This setting doesn't apply to Aurora DB instances. The port number is managed by the cluster.</p> <p>Valid Values: <code>1150-65535</code> </p> <p>Default:</p> <ul> <li> <p>RDS for Db2 - <code>50000</code> </p> </li> <li> <p>RDS for MariaDB - <code>3306</code> </p> </li> <li> <p>RDS for Microsoft SQL Server - <code>1433</code> </p> </li> <li> <p>RDS for MySQL - <code>3306</code> </p> </li> <li> <p>RDS for Oracle - <code>1521</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>5432</code> </p> </li> </ul> <p>Constraints:</p> <ul> <li> <p>For RDS for Microsoft SQL Server, the value can't be <code>1234</code>, <code>1434</code>, <code>3260</code>, <code>3343</code>, <code>3389</code>, <code>47001</code>, or <code>49152-49156</code>.</p> </li> </ul>"""
    multi_az: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the DB instance is a Multi-AZ deployment.</p> <p>This setting doesn't apply to Amazon Aurora because the DB instance Availability Zones (AZs) are managed by the DB cluster.</p>"""
    engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The version number of the database engine to use.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The version number of the database engine the DB instance uses is managed by the DB cluster.</p> <p>For a list of valid engine versions, use the <code>DescribeDBEngineVersions</code> operation.</p> <p>The following are the database engines and links to information about the major and minor versions that are available with Amazon RDS. Not every database engine is available for every Amazon Web Services Region.</p> <dl> <dt>Amazon RDS Custom for Oracle</dt> <dd> <p>A custom engine version (CEV) that you have previously created. This setting is required for RDS Custom for Oracle. The CEV name has the following format: 19.<i>customized_string</i>. A valid CEV name is <code>19.my_cev1</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.html#custom-creating.create"> Creating an RDS Custom for Oracle DB instance</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>Amazon RDS Custom for SQL Server</dt> <dd> <p>See <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html">RDS Custom for SQL Server general requirements</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>RDS for Db2</dt> <dd> <p>For information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html#Db2.Concepts.VersionMgmt">Db2 on Amazon RDS versions</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>RDS for MariaDB</dt> <dd> <p>For information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt">MariaDB on Amazon RDS versions</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>RDS for Microsoft SQL Server</dt> <dd> <p>For information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport">Microsoft SQL Server versions on Amazon RDS</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>RDS for MySQL</dt> <dd> <p>For information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt">MySQL on Amazon RDS versions</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>RDS for Oracle</dt> <dd> <p>For information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.PatchComposition.html">Oracle Database Engine release notes</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> <dt>RDS for PostgreSQL</dt> <dd> <p>For information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts">Amazon RDS for PostgreSQL versions and extensions</a> in the <i>Amazon RDS User Guide</i>.</p> </dd> </dl>"""
    auto_minor_version_upgrade: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.</p> <p>If you create an RDS Custom DB instance, you must set <code>AutoMinorVersionUpgrade</code> to <code>false</code>.</p> <p>For more information about automatic minor version upgrades, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades">Automatically upgrading the minor engine version</a>.</p>"""
    license_model: NotRequired["capo_rds.types.string.String"]
    """<p>The license model information for this DB instance.</p> <note> <p>License models for RDS for Db2 require additional configuration. The bring your own license (BYOL) model requires a custom parameter group and an Amazon Web Services License Manager self-managed license. The Db2 license through Amazon Web Services Marketplace model requires an Amazon Web Services Marketplace subscription. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html">Amazon RDS for Db2 licensing options</a> in the <i>Amazon RDS User Guide</i>.</p> <p>The default for RDS for Db2 is <code>bring-your-own-license</code>.</p> </note> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p> <p>Valid Values:</p> <ul> <li> <p>RDS for Db2 - <code>bring-your-own-license | marketplace-license</code> </p> </li> <li> <p>RDS for MariaDB - <code>general-public-license</code> </p> </li> <li> <p>RDS for Microsoft SQL Server - <code>license-included | bring-your-own-media</code> </p> </li> <li> <p>RDS for MySQL - <code>general-public-license</code> </p> </li> <li> <p>RDS for Oracle - <code>bring-your-own-license | license-included</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql-license</code> </p> </li> </ul>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to initially allocate for the DB instance. For information about valid IOPS values, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html">Amazon RDS DB instance storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.</p> <p>Constraints:</p> <ul> <li> <p>For RDS for Db2, MariaDB, MySQL, Oracle, and PostgreSQL - Must be a multiple between .5 and 50 of the storage amount for the DB instance.</p> </li> <li> <p>For RDS for SQL Server - Must be a multiple between 1 and 50 of the storage amount for the DB instance.</p> </li> </ul>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput value, in mebibyte per second (MiBps), for the DB instance.</p> <p>This setting applies only to the <code>gp3</code> storage type.</p> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p>"""
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The option group to associate the DB instance with.</p> <p>Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group. Also, that option group can't be removed from a DB instance after it is associated with a DB instance.</p> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p>"""
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>For supported engines, the character set (<code>CharacterSet</code>) to associate the DB instance with.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora - The character set is managed by the DB cluster. For more information, see <code>CreateDBCluster</code>.</p> </li> <li> <p>RDS Custom - However, if you need to change the character set, you can change it on the database itself.</p> </li> </ul>"""
    nchar_character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the NCHAR character set for the Oracle DB instance.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    publicly_accessible: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance is publicly accessible.</p> <p>When the DB instance is publicly accessible and you connect from outside of the DB instance's virtual private cloud (VPC), its domain name system (DNS) endpoint resolves to the public IP address. When you connect from within the same VPC as the DB instance, the endpoint resolves to the private IP address. Access to the DB instance is controlled by its security group settings.</p> <p>When the DB instance isn't publicly accessible, it is an internal DB instance with a DNS name that resolves to a private IP address.</p> <p>The default behavior when <code>PubliclyAccessible</code> is not specified depends on whether a <code>DBSubnetGroup</code> is specified.</p> <p>If <code>DBSubnetGroup</code> isn't specified, <code>PubliclyAccessible</code> defaults to <code>false</code> for Aurora instances and <code>true</code> for non-Aurora instances.</p> <p>If <code>DBSubnetGroup</code> is specified, <code>PubliclyAccessible</code> defaults to <code>false</code> unless the value of <code>DBSubnetGroup</code> is <code>default</code>, in which case <code>PubliclyAccessible</code> defaults to <code>true</code>.</p> <p>If <code>PubliclyAccessible</code> is true and the VPC that the <code>DBSubnetGroup</code> is in doesn't have an internet gateway attached to it, Amazon RDS returns an error.</p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]
    """<p>Tags to assign to the DB instance.</p>"""
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the DB cluster that this DB instance will belong to.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type to associate with the DB instance.</p> <p>If you specify <code>io1</code>, <code>io2</code>, or <code>gp3</code>, you must also include a value for the <code>Iops</code> parameter.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.</p> <p>Valid Values: <code>gp2 | gp3 | io1 | io2 | standard</code> </p> <p>Default: <code>io1</code>, if the <code>Iops</code> parameter is specified. Otherwise, <code>gp3</code>.</p>"""
    tde_credential_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN from the key store with which to associate the instance for TDE encryption.</p> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p>"""
    tde_credential_password: NotRequired[
        "capo_rds.types.sensitive_string.SensitiveString"
    ]
    """<p>The password for the given ARN from the key store in order to access the device.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    storage_encrypted: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifes whether the DB instance is encrypted. By default, it isn't encrypted.</p> <p>For RDS Custom DB instances, either enable this setting or leave it unset. Otherwise, Amazon RDS reports an error.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The encryption for DB instances is managed by the DB cluster.</p>"""
    kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for an encrypted DB instance.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. The Amazon Web Services KMS key identifier is managed by the DB cluster. For more information, see <code>CreateDBCluster</code>.</p> <p>If <code>StorageEncrypted</code> is enabled, and you do not specify a value for the <code>KmsKeyId</code> parameter, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>For Amazon RDS Custom, a KMS key is required for DB instances. For most RDS engines, if you leave this parameter empty while enabling <code>StorageEncrypted</code>, the engine uses the default KMS key. However, RDS Custom doesn't use the default key when this parameter is empty. You must explicitly specify a key.</p>"""
    domain: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory directory ID to create the DB instance in. Currently, you can create only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances in an Active Directory Domain.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html"> Kerberos Authentication</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora (The domain is managed by the DB cluster.)</p> </li> <li> <p>RDS Custom</p> </li> </ul>"""
    domain_fqdn: NotRequired["capo_rds.types.string.String"]
    """<p>The fully qualified domain name (FQDN) of an Active Directory domain.</p> <p>Constraints:</p> <ul> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>mymanagedADtest.mymanagedAD.mydomain</code> </p>"""
    domain_ou: NotRequired["capo_rds.types.string.String"]
    """<p>The Active Directory organizational unit for your DB instance to join.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the distinguished name format.</p> </li> <li> <p>Can't be longer than 64 characters.</p> </li> </ul> <p>Example: <code>OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain</code> </p>"""
    domain_auth_secret_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the Secrets Manager secret with the credentials for the user joining the domain.</p> <p>Example: <code>arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456</code> </p>"""
    domain_dns_ips: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.</p> <p>Constraints:</p> <ul> <li> <p>Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.</p> </li> </ul> <p>Example: <code>123.124.125.126,234.235.236.237</code> </p>"""
    copy_tags_to_snapshot: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting.</p>"""
    monitoring_interval: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify <code>0</code>.</p> <p>If <code>MonitoringRoleArn</code> is specified, then you must set <code>MonitoringInterval</code> to a value other than <code>0</code>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values: <code>0 | 1 | 5 | 10 | 15 | 30 | 60</code> </p> <p>Default: <code>0</code> </p>"""
    monitoring_role_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling">Setting Up and Enabling Enhanced Monitoring</a> in the <i>Amazon RDS User Guide</i>.</p> <p>If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, then you must supply a <code>MonitoringRoleArn</code> value.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    domain_iam_role_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the IAM role to use when making API calls to the Directory Service.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora (The domain is managed by the DB cluster.)</p> </li> <li> <p>RDS Custom</p> </li> </ul>"""
    promotion_tier: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance"> Fault Tolerance for an Aurora DB Cluster</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Default: <code>1</code> </p> <p>Valid Values: <code>0 - 15</code> </p>"""
    timezone: NotRequired["capo_rds.types.string.String"]
    """<p>The time zone of the DB instance. The time zone parameter is currently supported only by <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-time-zone">RDS for Db2</a> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone">RDS for SQL Server</a>.</p>"""
    enable_iam_database_authentication: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"> IAM Database Authentication for MySQL and PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora (Mapping Amazon Web Services IAM accounts to database accounts is managed by the DB cluster.)</p> </li> <li> <p>RDS Custom</p> </li> </ul>"""
    database_insights_mode: NotRequired[
        "capo_rds.types.database_insights_mode.DatabaseInsightsMode"
    ]
    """<p>The mode of Database Insights to enable for the DB instance.</p> <note> <p>Aurora DB instances inherit this value from the DB cluster, so you can't change this value.</p> </note>"""
    enable_performance_insights: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable Performance Insights for the DB instance. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html">Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    performance_insights_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier for encryption of Performance Insights data.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <p>If you don't specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    performance_insights_retention_period: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days to retain Performance Insights data.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>Valid Values:</p> <ul> <li> <p> <code>7</code> </p> </li> <li> <p> <i>month</i> * 31, where <i>month</i> is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)</p> </li> <li> <p> <code>731</code> </p> </li> </ul> <p>Default: <code>7</code> days</p> <p>If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS returns an error.</p>"""
    enable_cloudwatch_logs_exports: NotRequired[
        "capo_rds.types.log_type_list.LogTypeList"
    ]
    """<p>The list of log types to enable for exporting to CloudWatch Logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch"> Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora (CloudWatch Logs exports are managed by the DB cluster.)</p> </li> <li> <p>RDS Custom</p> </li> </ul> <p>The following values are valid for each DB engine:</p> <ul> <li> <p>RDS for Db2 - <code>diag.log | notify.log | iam-db-auth-error</code> </p> </li> <li> <p>RDS for MariaDB - <code>audit | error | general | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>RDS for Microsoft SQL Server - <code>agent | error</code> </p> </li> <li> <p>RDS for MySQL - <code>audit | error | general | slowquery | iam-db-auth-error</code> </p> </li> <li> <p>RDS for Oracle - <code>alert | audit | listener | trace | oemagent</code> </p> </li> <li> <p>RDS for PostgreSQL - <code>postgresql | upgrade | iam-db-auth-error</code> </p> </li> </ul>"""
    processor_features: NotRequired[
        "capo_rds.types.processor_feature_list.ProcessorFeatureList"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p> <p>This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</p>"""
    deletion_protection: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection isn't enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html"> Deleting a DB Instance</a>.</p> <p>This setting doesn't apply to Amazon Aurora DB instances. You can enable or disable deletion protection for the DB cluster. For more information, see <code>CreateDBCluster</code>. DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.</p> <p>For more information about this setting, including limitations that apply to it, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling"> Managing capacity automatically with Amazon RDS storage autoscaling</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting doesn't apply to the following DB instances:</p> <ul> <li> <p>Amazon Aurora (Storage is managed by the DB cluster.)</p> </li> <li> <p>RDS Custom</p> </li> </ul>"""
    enable_customer_owned_ip: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable a customer-owned IP address (CoIP) for an RDS on Outposts DB instance.</p> <p>A <i>CoIP</i> provides local or external connectivity to resources in your Outpost subnets through your on-premises network. For some use cases, a CoIP can provide lower latency for connections to the DB instance from outside of its virtual private cloud (VPC) on your local network.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p> <p>For more information about CoIPs, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing">Customer-owned IP addresses</a> in the <i>Amazon Web Services Outposts User Guide</i>.</p>"""
    network_type: NotRequired["capo_rds.types.string.String"]
    """<p>The network type of the DB instance.</p> <p>The network type is determined by the <code>DBSubnetGroup</code> specified for the DB instance. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid Values: <code>IPV4 | DUAL</code> </p>"""
    backup_target: NotRequired["capo_rds.types.string.String"]
    """<p>The location for storing automated backups and manual snapshots.</p> <p>Valid Values:</p> <ul> <li> <p> <code>local</code> (Dedicated Local Zone)</p> </li> <li> <p> <code>outposts</code> (Amazon Web Services Outposts)</p> </li> <li> <p> <code>region</code> (Amazon Web Services Region)</p> </li> </ul> <p>Default: <code>region</code> </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Working with Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    custom_iam_instance_profile: NotRequired["capo_rds.types.string.String"]
    """<p>The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance.</p> <p>This setting is required for RDS Custom.</p> <p>Constraints:</p> <ul> <li> <p>The profile must exist in your account.</p> </li> <li> <p>The profile must have an IAM role that Amazon EC2 has permissions to assume.</p> </li> <li> <p>The instance profile name and the associated IAM role name must start with the prefix <code>AWSRDSCustom</code>.</p> </li> </ul> <p>For the list of permissions required for the IAM role, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc"> Configure IAM and your VPC</a> in the <i>Amazon RDS User Guide</i>.</p>"""
    db_system_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. In this context, the term "Oracle database instance" refers exclusively to the system global area (SGA) and Oracle background processes. If you don't specify a SID, the value defaults to <code>RDSCDB</code>. The Oracle SID is also the name of your CDB.</p>"""
    ca_certificate_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The CA certificate identifier to use for the DB instance's server certificate.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html">Using SSL/TLS to encrypt a connection to a DB instance</a> in the <i>Amazon RDS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"> Using SSL/TLS to encrypt a connection to a DB cluster</a> in the <i>Amazon Aurora User Guide</i>.</p>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p> </li> </ul>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If you don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a customer managed KMS key.</p> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""
    multi_tenant: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to use the multi-tenant configuration or the single-tenant configuration (default). This parameter only applies to RDS for Oracle container database (CDB) engines.</p> <p>Note the following restrictions: </p> <ul> <li> <p>The DB engine that you specify in the request must support the multi-tenant configuration. If you attempt to enable the multi-tenant configuration on a DB engine that doesn't support it, the request fails.</p> </li> <li> <p>If you specify the multi-tenant configuration when you create your DB instance, you can't later modify this DB instance to use the single-tenant configuration.</p> </li> </ul>"""
    dedicated_log_volume: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</p>"""
    engine_lifecycle_support: NotRequired["capo_rds.types.string.String"]
    """<p>The lifecycle type for this DB instance.</p> <note> <p>By default, this value is set to <code>open-source-rds-extended-support</code>, which enrolls your DB instance into Amazon RDS Extended Support. At the end of standard support, you can avoid charges for Extended Support by setting the value to <code>open-source-rds-extended-support-disabled</code>. In this case, creating the DB instance will fail if the DB major version is past its end of standard support date.</p> </note> <p>This setting applies only to RDS for MySQL and RDS for PostgreSQL. For Amazon Aurora DB instances, the engine lifecycle support is managed by the DB cluster.</p> <p>You can use this setting to enroll your DB instance into Amazon RDS Extended Support. With RDS Extended Support, you can run the selected major engine version on your DB instance past the end of standard support for that engine version. For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html">Amazon RDS Extended Support with Amazon RDS</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid Values: <code>open-source-rds-extended-support | open-source-rds-extended-support-disabled</code> </p> <p>Default: <code>open-source-rds-extended-support</code> </p>"""
    additional_storage_volumes: NotRequired[
        "capo_rds.types.additional_storage_volumes_list.AdditionalStorageVolumesList"
    ]
    """<p>A list of additional storage volumes to create for the DB instance. You can create up to three additional storage volumes using the names <code>rdsdbdata2</code>, <code>rdsdbdata3</code>, and <code>rdsdbdata4</code>. Additional storage volumes are supported for RDS for Oracle and RDS for SQL Server DB instances only.</p>"""
    tag_specifications: NotRequired[
        "capo_rds.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tags to assign to resources associated with the DB instance.</p> <p>Valid Values: </p> <ul> <li> <p> <code>auto-backup</code> - The DB instance's automated backup.</p> </li> </ul>"""
    master_user_authentication_type: NotRequired[
        "capo_rds.types.master_user_authentication_type.MasterUserAuthenticationType"
    ]
    """<p>Specifies the authentication type for the master user. With IAM master user authentication, you can configure the master DB user with IAM database authentication when you create a DB instance.</p> <p>You can specify one of the following values:</p> <ul> <li> <p> <code>password</code> - Use standard database authentication with a password.</p> </li> <li> <p> <code>iam-db-auth</code> - Use IAM database authentication for the master user.</p> </li> </ul> <p>This option is only valid for RDS for PostgreSQL and Aurora PostgreSQL engines.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
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
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
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
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
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
    if "character_set_name" in value:
        pairs.append(
            (f"{key_prefix}CharacterSetName", str(value["character_set_name"]))
        )
    if "nchar_character_set_name" in value:
        pairs.append(
            (
                f"{key_prefix}NcharCharacterSetName",
                str(value["nchar_character_set_name"]),
            )
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
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
    if "storage_encrypted" in value:
        pairs.append(
            (
                f"{key_prefix}StorageEncrypted",
                "true" if value["storage_encrypted"] else "false",
            )
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
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
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))
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
    if "enable_cloudwatch_logs_exports" in value:
        import capo_rds.types.log_type_list

        capo_rds.types.log_type_list.serialize_query(
            value["enable_cloudwatch_logs_exports"],
            pairs,
            f"{key_prefix}EnableCloudwatchLogsExports",
        )
    if "processor_features" in value:
        import capo_rds.types.processor_feature_list

        capo_rds.types.processor_feature_list.serialize_query(
            value["processor_features"], pairs, f"{key_prefix}ProcessorFeatures"
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
    if "enable_customer_owned_ip" in value:
        pairs.append(
            (
                f"{key_prefix}EnableCustomerOwnedIp",
                "true" if value["enable_customer_owned_ip"] else "false",
            )
        )
    if "network_type" in value:
        pairs.append((f"{key_prefix}NetworkType", str(value["network_type"])))
    if "backup_target" in value:
        pairs.append((f"{key_prefix}BackupTarget", str(value["backup_target"])))
    if "custom_iam_instance_profile" in value:
        pairs.append(
            (
                f"{key_prefix}CustomIamInstanceProfile",
                str(value["custom_iam_instance_profile"]),
            )
        )
    if "db_system_id" in value:
        pairs.append((f"{key_prefix}DBSystemId", str(value["db_system_id"])))
    if "ca_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}CACertificateIdentifier",
                str(value["ca_certificate_identifier"]),
            )
        )
    if "manage_master_user_password" in value:
        pairs.append(
            (
                f"{key_prefix}ManageMasterUserPassword",
                "true" if value["manage_master_user_password"] else "false",
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
    if "engine_lifecycle_support" in value:
        pairs.append(
            (
                f"{key_prefix}EngineLifecycleSupport",
                str(value["engine_lifecycle_support"]),
            )
        )
    if "additional_storage_volumes" in value:
        import capo_rds.types.additional_storage_volumes_list

        capo_rds.types.additional_storage_volumes_list.serialize_query(
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


def deserialize_query(el: Element) -> CreateDBInstanceMessage:
    out: CreateDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
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
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    child_backup_retention_period = el.find("BackupRetentionPeriod")
    if child_backup_retention_period is not None:
        out["backup_retention_period"] = int(child_backup_retention_period.text or "")
    child_preferred_backup_window = el.find("PreferredBackupWindow")
    if child_preferred_backup_window is not None:
        out["preferred_backup_window"] = str(child_preferred_backup_window.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
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
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_nchar_character_set_name = el.find("NcharCharacterSetName")
    if child_nchar_character_set_name is not None:
        out["nchar_character_set_name"] = str(child_nchar_character_set_name.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_tde_credential_arn = el.find("TdeCredentialArn")
    if child_tde_credential_arn is not None:
        out["tde_credential_arn"] = str(child_tde_credential_arn.text or "")
    child_tde_credential_password = el.find("TdeCredentialPassword")
    if child_tde_credential_password is not None:
        out["tde_credential_password"] = str(child_tde_credential_password.text or "")
    child_storage_encrypted = el.find("StorageEncrypted")
    if child_storage_encrypted is not None:
        out["storage_encrypted"] = (
            child_storage_encrypted.text or ""
        ).lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
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
    child_copy_tags_to_snapshot = el.find("CopyTagsToSnapshot")
    if child_copy_tags_to_snapshot is not None:
        out["copy_tags_to_snapshot"] = (
            child_copy_tags_to_snapshot.text or ""
        ).lower() == "true"
    child_monitoring_interval = el.find("MonitoringInterval")
    if child_monitoring_interval is not None:
        out["monitoring_interval"] = int(child_monitoring_interval.text or "")
    child_monitoring_role_arn = el.find("MonitoringRoleArn")
    if child_monitoring_role_arn is not None:
        out["monitoring_role_arn"] = str(child_monitoring_role_arn.text or "")
    child_domain_iam_role_name = el.find("DomainIAMRoleName")
    if child_domain_iam_role_name is not None:
        out["domain_iam_role_name"] = str(child_domain_iam_role_name.text or "")
    child_promotion_tier = el.find("PromotionTier")
    if child_promotion_tier is not None:
        out["promotion_tier"] = int(child_promotion_tier.text or "")
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
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
    child_enable_cloudwatch_logs_exports = el.find("EnableCloudwatchLogsExports")
    if child_enable_cloudwatch_logs_exports is not None:
        import capo_rds.types.log_type_list

        out["enable_cloudwatch_logs_exports"] = (
            capo_rds.types.log_type_list.deserialize_query(
                child_enable_cloudwatch_logs_exports
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
    child_deletion_protection = el.find("DeletionProtection")
    if child_deletion_protection is not None:
        out["deletion_protection"] = (
            child_deletion_protection.text or ""
        ).lower() == "true"
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
    child_enable_customer_owned_ip = el.find("EnableCustomerOwnedIp")
    if child_enable_customer_owned_ip is not None:
        out["enable_customer_owned_ip"] = (
            child_enable_customer_owned_ip.text or ""
        ).lower() == "true"
    child_network_type = el.find("NetworkType")
    if child_network_type is not None:
        out["network_type"] = str(child_network_type.text or "")
    child_backup_target = el.find("BackupTarget")
    if child_backup_target is not None:
        out["backup_target"] = str(child_backup_target.text or "")
    child_custom_iam_instance_profile = el.find("CustomIamInstanceProfile")
    if child_custom_iam_instance_profile is not None:
        out["custom_iam_instance_profile"] = str(
            child_custom_iam_instance_profile.text or ""
        )
    child_db_system_id = el.find("DBSystemId")
    if child_db_system_id is not None:
        out["db_system_id"] = str(child_db_system_id.text or "")
    child_ca_certificate_identifier = el.find("CACertificateIdentifier")
    if child_ca_certificate_identifier is not None:
        out["ca_certificate_identifier"] = str(
            child_ca_certificate_identifier.text or ""
        )
    child_manage_master_user_password = el.find("ManageMasterUserPassword")
    if child_manage_master_user_password is not None:
        out["manage_master_user_password"] = (
            child_manage_master_user_password.text or ""
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
    child_engine_lifecycle_support = el.find("EngineLifecycleSupport")
    if child_engine_lifecycle_support is not None:
        out["engine_lifecycle_support"] = str(child_engine_lifecycle_support.text or "")
    child_additional_storage_volumes = el.find("AdditionalStorageVolumes")
    if child_additional_storage_volumes is not None:
        import capo_rds.types.additional_storage_volumes_list

        out["additional_storage_volumes"] = (
            capo_rds.types.additional_storage_volumes_list.deserialize_query(
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
    return out
