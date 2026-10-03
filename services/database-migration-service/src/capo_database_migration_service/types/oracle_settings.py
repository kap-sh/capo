"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OracleSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.char_length_semantics
    import capo_database_migration_service.types.integer_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.oracle_authentication_method
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string


class OracleSettings(TypedDict, closed=True):
    add_supplemental_logging: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to set up table-level supplemental logging for the Oracle database. This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task.</p> <p>If you use this option, you still need to enable database-level supplemental logging.</p>"""
    archived_log_dest_id: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the <code>AdditionalArchivedLogDestId</code> option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.</p>"""
    additional_archived_log_dest_id: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Set this attribute with <code>ArchivedLogDestId</code> in a primary/ standby setup. This attribute is useful in the case of a switchover. In this case, DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover.</p> <p>Although DMS supports the use of the Oracle <code>RESETLOGS</code> option to open the database, never use <code>RESETLOGS</code> unless necessary. For additional information about <code>RESETLOGS</code>, see <a href="https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B">RMAN Data Repair Concepts</a> in the <i>Oracle Database Backup and Recovery User's Guide</i>.</p>"""
    extra_archived_log_dest_ids: NotRequired[
        "capo_database_migration_service.types.integer_list.IntegerList"
    ]
    """<p>Specifies the IDs of one more destinations for one or more archived redo logs. These IDs are the values of the <code>dest_id</code> column in the <code>v$archived_log</code> view. Use this setting with the <code>archivedLogDestId</code> extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup. </p> <p>This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, DMS needs information about what destination to get archive redo logs from to read changes. DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings. </p> <p> <code>archivedLogDestId=1; ExtraArchivedLogDestIds=[2]</code> </p> <p>In a primary-to-multiple-standby setup, you might apply the following settings.</p> <p> <code>archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]</code> </p> <p>Although DMS supports the use of the Oracle <code>RESETLOGS</code> option to open the database, never use <code>RESETLOGS</code> unless it's necessary. For more information about <code>RESETLOGS</code>, see <a href="https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B"> RMAN Data Repair Concepts</a> in the <i>Oracle Database Backup and Recovery User's Guide</i>.</p>"""
    allow_select_nested_tables: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to <code>true</code> to enable replication of Oracle tables containing columns that are nested tables or defined types.</p>"""
    parallel_asm_read_threads: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the <code>readAheadBlocks</code> attribute.</p>"""
    read_ahead_blocks: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 1000 (the default) and 200,000 (the maximum).</p>"""
    access_alternate_directly: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to <code>false</code> in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.</p>"""
    use_alternate_folder_for_online: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to <code>true</code> in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to use any specified prefix replacement to access all online redo logs.</p>"""
    oracle_path_prefix: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the default Oracle root used to access the redo logs.</p>"""
    use_path_prefix: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the path prefix used to replace the default Oracle root to access the redo logs.</p>"""
    replace_path_prefix: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This setting tells DMS instance to replace the default Oracle root with the specified <code>usePathPrefix</code> setting to access the redo logs.</p>"""
    enable_homogenous_tablespace: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.</p>"""
    direct_path_no_log: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to <code>true</code>, this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.</p>"""
    archived_logs_only: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When this field is set to <code>True</code>, DMS only accesses the archived redo logs. If the archived redo logs are stored on Automatic Storage Management (ASM) only, the DMS user account needs to be granted ASM privileges.</p>"""
    asm_password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password. You can set this value from the <code> <i>asm_user_password</i> </code> value. You set this value as part of the comma-separated value that you set to the <code>Password</code> request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration">Configuration for change data capture (CDC) on an Oracle source database</a>.</p>"""
    asm_server: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>For an Oracle source endpoint, your ASM server address. You can set this value from the <code>asm_server</code> value. You set <code>asm_server</code> as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration">Configuration for change data capture (CDC) on an Oracle source database</a>.</p>"""
    asm_user: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>For an Oracle source endpoint, your ASM user name. You can set this value from the <code>asm_user</code> value. You set <code>asm_user</code> as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration">Configuration for change data capture (CDC) on an Oracle source database</a>.</p>"""
    char_length_semantics: NotRequired[
        "capo_database_migration_service.types.char_length_semantics.CharLengthSemantics"
    ]
    """<p>Specifies whether the length of a character column is in bytes or in characters. To indicate that the character column length is in characters, set this attribute to <code>CHAR</code>. Otherwise, the character column length is in bytes.</p> <p>Example: <code>charLengthSemantics=CHAR;</code> </p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Database name for the endpoint.</p>"""
    direct_path_parallel_load: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to <code>true</code>, this attribute specifies a parallel load when <code>useDirectPathFullLoad</code> is set to <code>Y</code>. This attribute also only applies when you use the DMS parallel load feature. Note that the target table cannot have any constraints or indexes.</p>"""
    fail_tasks_on_lob_truncation: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to <code>true</code>, this attribute causes a task to fail if the actual size of an LOB column is greater than the specified <code>LobMaxSize</code>.</p> <p>If a task is set to limited LOB mode and this option is set to <code>true</code>, the task fails instead of truncating the LOB data.</p>"""
    number_datatype_scale: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the number scale. You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10.</p> <p>Example: <code>numberDataTypeScale=12</code> </p>"""
    password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>Endpoint connection password.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Endpoint TCP port.</p>"""
    read_table_space_name: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to <code>true</code>, this attribute supports tablespace replication.</p>"""
    retry_interval: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the number of seconds that the system waits before resending a query.</p> <p>Example: <code>retryInterval=6;</code> </p>"""
    security_db_encryption: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>For an Oracle source endpoint, the transparent data encryption (TDE) password required by DMS to access Oracle redo logs encrypted by TDE using Binary Reader. It is also the <code> <i>TDE_Password</i> </code> part of the comma-separated value you set to the <code>Password</code> request parameter when you create the endpoint. The <code>SecurityDbEncryption</code> setting is related to this <code>SecurityDbEncryptionName</code> setting. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption"> Supported encryption methods for using Oracle as a source for DMS </a> in the <i>Database Migration Service User Guide</i>. </p>"""
    security_db_encryption_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE. The key value is the value of the <code>SecurityDbEncryption</code> setting. For more information on setting the key name value of <code>SecurityDbEncryptionName</code>, see the information and example for setting the <code>securityDbEncryptionName</code> extra connection attribute in <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption"> Supported encryption methods for using Oracle as a source for DMS </a> in the <i>Database Migration Service User Guide</i>.</p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Fully qualified domain name of the endpoint.</p> <p>For an Amazon RDS Oracle instance, this is the output of <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html">DescribeDBInstances</a>, in the <code> <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html">Endpoint</a>.Address</code> field.</p>"""
    spatial_data_option_to_geo_json_function_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Use this attribute to convert <code>SDO_GEOMETRY</code> to <code>GEOJSON</code> format. By default, DMS calls the <code>SDO2GEOJSON</code> custom function if present and accessible. Or you can create your own custom function that mimics the operation of <code>SDOGEOJSON</code> and set <code>SpatialDataOptionToGeoJsonFunctionName</code> to call it instead. </p>"""
    standby_delay_time: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Use this attribute to specify a time in minutes for the delay in standby sync. If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases.</p> <p>In DMS, you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.</p>"""
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Endpoint connection user name.</p>"""
    use_b_file: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to True to capture change data using the Binary Reader utility. Set <code>UseLogminerReader</code> to False to set this attribute to True. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC"> Using Oracle LogMiner or DMS Binary Reader for CDC</a>.</p>"""
    use_direct_path_full_load: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to True to have DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.</p>"""
    use_logminer_reader: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to True to capture change data using the Oracle LogMiner utility (the default). Set this attribute to False if you want to access the redo logs as a binary file. When you set <code>UseLogminerReader</code> to False, also set <code>UseBfile</code> to True. For more information on this setting and using Oracle ASM, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC"> Using Oracle LogMiner or DMS Binary Reader for CDC</a> in the <i>DMS User Guide</i>.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the Oracle endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the Oracle endpoint connection details.</p>"""
    secrets_manager_oracle_asm_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the <code>SecretsManagerOracleAsmSecret</code>. This <code>SecretsManagerOracleAsmSecret</code> has the secret value that allows access to the Oracle ASM of the endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerOracleAsmSecretId</code>. Or you can specify clear-text values for <code>AsmUser</code>, <code>AsmPassword</code>, and <code>AsmServerName</code>. You can't specify both. For more information on creating this <code>SecretsManagerOracleAsmSecret</code> and the <code>SecretsManagerOracleAsmAccessRoleArn</code> and <code>SecretsManagerOracleAsmSecretId</code> required to access it, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_oracle_asm_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the <code>SecretsManagerOracleAsmSecret</code> that contains the Oracle ASM connection details for the Oracle endpoint.</p>"""
    trim_space_in_char: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Use the <code>TrimSpaceInChar</code> source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is <code>true</code>.</p>"""
    convert_timestamp_with_zone_to_utc: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When true, converts timestamps with the <code>timezone</code> datatype to their UTC value.</p>"""
    open_transaction_window: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The timeframe in minutes to check for open transactions for a CDC-only task.</p> <p>You can specify an integer value between 0 (the default) and 240 (the maximum). </p> <note> <p>This parameter is only valid in DMS version 3.5.0 and later.</p> </note>"""
    authentication_method: NotRequired[
        "capo_database_migration_service.types.oracle_authentication_method.OracleAuthenticationMethod"
    ]
    """<p>Specifies the authentication method to be used with Oracle.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OracleSettings) -> dict:
    out: dict = {}
    if "add_supplemental_logging" in value:
        out["AddSupplementalLogging"] = value["add_supplemental_logging"]
    if "archived_log_dest_id" in value:
        out["ArchivedLogDestId"] = value["archived_log_dest_id"]
    if "additional_archived_log_dest_id" in value:
        out["AdditionalArchivedLogDestId"] = value["additional_archived_log_dest_id"]
    if "extra_archived_log_dest_ids" in value:
        import capo_database_migration_service.types.integer_list

        out["ExtraArchivedLogDestIds"] = (
            capo_database_migration_service.types.integer_list.serialize_aws_json_1_1(
                value["extra_archived_log_dest_ids"]
            )
        )
    if "allow_select_nested_tables" in value:
        out["AllowSelectNestedTables"] = value["allow_select_nested_tables"]
    if "parallel_asm_read_threads" in value:
        out["ParallelAsmReadThreads"] = value["parallel_asm_read_threads"]
    if "read_ahead_blocks" in value:
        out["ReadAheadBlocks"] = value["read_ahead_blocks"]
    if "access_alternate_directly" in value:
        out["AccessAlternateDirectly"] = value["access_alternate_directly"]
    if "use_alternate_folder_for_online" in value:
        out["UseAlternateFolderForOnline"] = value["use_alternate_folder_for_online"]
    if "oracle_path_prefix" in value:
        out["OraclePathPrefix"] = value["oracle_path_prefix"]
    if "use_path_prefix" in value:
        out["UsePathPrefix"] = value["use_path_prefix"]
    if "replace_path_prefix" in value:
        out["ReplacePathPrefix"] = value["replace_path_prefix"]
    if "enable_homogenous_tablespace" in value:
        out["EnableHomogenousTablespace"] = value["enable_homogenous_tablespace"]
    if "direct_path_no_log" in value:
        out["DirectPathNoLog"] = value["direct_path_no_log"]
    if "archived_logs_only" in value:
        out["ArchivedLogsOnly"] = value["archived_logs_only"]
    if "asm_password" in value:
        out["AsmPassword"] = value["asm_password"]
    if "asm_server" in value:
        out["AsmServer"] = value["asm_server"]
    if "asm_user" in value:
        out["AsmUser"] = value["asm_user"]
    if "char_length_semantics" in value:
        import capo_database_migration_service.types.char_length_semantics

        out["CharLengthSemantics"] = (
            capo_database_migration_service.types.char_length_semantics.serialize_aws_json_1_1(
                value["char_length_semantics"]
            )
        )
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "direct_path_parallel_load" in value:
        out["DirectPathParallelLoad"] = value["direct_path_parallel_load"]
    if "fail_tasks_on_lob_truncation" in value:
        out["FailTasksOnLobTruncation"] = value["fail_tasks_on_lob_truncation"]
    if "number_datatype_scale" in value:
        out["NumberDatatypeScale"] = value["number_datatype_scale"]
    if "password" in value:
        out["Password"] = value["password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "read_table_space_name" in value:
        out["ReadTableSpaceName"] = value["read_table_space_name"]
    if "retry_interval" in value:
        out["RetryInterval"] = value["retry_interval"]
    if "security_db_encryption" in value:
        out["SecurityDbEncryption"] = value["security_db_encryption"]
    if "security_db_encryption_name" in value:
        out["SecurityDbEncryptionName"] = value["security_db_encryption_name"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "spatial_data_option_to_geo_json_function_name" in value:
        out["SpatialDataOptionToGeoJsonFunctionName"] = value[
            "spatial_data_option_to_geo_json_function_name"
        ]
    if "standby_delay_time" in value:
        out["StandbyDelayTime"] = value["standby_delay_time"]
    if "username" in value:
        out["Username"] = value["username"]
    if "use_b_file" in value:
        out["UseBFile"] = value["use_b_file"]
    if "use_direct_path_full_load" in value:
        out["UseDirectPathFullLoad"] = value["use_direct_path_full_load"]
    if "use_logminer_reader" in value:
        out["UseLogminerReader"] = value["use_logminer_reader"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "secrets_manager_oracle_asm_access_role_arn" in value:
        out["SecretsManagerOracleAsmAccessRoleArn"] = value[
            "secrets_manager_oracle_asm_access_role_arn"
        ]
    if "secrets_manager_oracle_asm_secret_id" in value:
        out["SecretsManagerOracleAsmSecretId"] = value[
            "secrets_manager_oracle_asm_secret_id"
        ]
    if "trim_space_in_char" in value:
        out["TrimSpaceInChar"] = value["trim_space_in_char"]
    if "convert_timestamp_with_zone_to_utc" in value:
        out["ConvertTimestampWithZoneToUTC"] = value[
            "convert_timestamp_with_zone_to_utc"
        ]
    if "open_transaction_window" in value:
        out["OpenTransactionWindow"] = value["open_transaction_window"]
    if "authentication_method" in value:
        import capo_database_migration_service.types.oracle_authentication_method

        out["AuthenticationMethod"] = (
            capo_database_migration_service.types.oracle_authentication_method.serialize_aws_json_1_1(
                value["authentication_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OracleSettings:
    out: OracleSettings = {}  # type: ignore[typeddict-item]
    if data.get("AddSupplementalLogging") is not None:
        out["add_supplemental_logging"] = data["AddSupplementalLogging"]
    if data.get("ArchivedLogDestId") is not None:
        out["archived_log_dest_id"] = data["ArchivedLogDestId"]
    if data.get("AdditionalArchivedLogDestId") is not None:
        out["additional_archived_log_dest_id"] = data["AdditionalArchivedLogDestId"]
    if data.get("ExtraArchivedLogDestIds") is not None:
        import capo_database_migration_service.types.integer_list

        out["extra_archived_log_dest_ids"] = (
            capo_database_migration_service.types.integer_list.deserialize_aws_json_1_1(
                data["ExtraArchivedLogDestIds"]
            )
        )
    if data.get("AllowSelectNestedTables") is not None:
        out["allow_select_nested_tables"] = data["AllowSelectNestedTables"]
    if data.get("ParallelAsmReadThreads") is not None:
        out["parallel_asm_read_threads"] = data["ParallelAsmReadThreads"]
    if data.get("ReadAheadBlocks") is not None:
        out["read_ahead_blocks"] = data["ReadAheadBlocks"]
    if data.get("AccessAlternateDirectly") is not None:
        out["access_alternate_directly"] = data["AccessAlternateDirectly"]
    if data.get("UseAlternateFolderForOnline") is not None:
        out["use_alternate_folder_for_online"] = data["UseAlternateFolderForOnline"]
    if data.get("OraclePathPrefix") is not None:
        out["oracle_path_prefix"] = data["OraclePathPrefix"]
    if data.get("UsePathPrefix") is not None:
        out["use_path_prefix"] = data["UsePathPrefix"]
    if data.get("ReplacePathPrefix") is not None:
        out["replace_path_prefix"] = data["ReplacePathPrefix"]
    if data.get("EnableHomogenousTablespace") is not None:
        out["enable_homogenous_tablespace"] = data["EnableHomogenousTablespace"]
    if data.get("DirectPathNoLog") is not None:
        out["direct_path_no_log"] = data["DirectPathNoLog"]
    if data.get("ArchivedLogsOnly") is not None:
        out["archived_logs_only"] = data["ArchivedLogsOnly"]
    if data.get("AsmPassword") is not None:
        out["asm_password"] = data["AsmPassword"]
    if data.get("AsmServer") is not None:
        out["asm_server"] = data["AsmServer"]
    if data.get("AsmUser") is not None:
        out["asm_user"] = data["AsmUser"]
    if data.get("CharLengthSemantics") is not None:
        import capo_database_migration_service.types.char_length_semantics

        out["char_length_semantics"] = (
            capo_database_migration_service.types.char_length_semantics.deserialize_aws_json_1_1(
                data["CharLengthSemantics"]
            )
        )
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("DirectPathParallelLoad") is not None:
        out["direct_path_parallel_load"] = data["DirectPathParallelLoad"]
    if data.get("FailTasksOnLobTruncation") is not None:
        out["fail_tasks_on_lob_truncation"] = data["FailTasksOnLobTruncation"]
    if data.get("NumberDatatypeScale") is not None:
        out["number_datatype_scale"] = data["NumberDatatypeScale"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("ReadTableSpaceName") is not None:
        out["read_table_space_name"] = data["ReadTableSpaceName"]
    if data.get("RetryInterval") is not None:
        out["retry_interval"] = data["RetryInterval"]
    if data.get("SecurityDbEncryption") is not None:
        out["security_db_encryption"] = data["SecurityDbEncryption"]
    if data.get("SecurityDbEncryptionName") is not None:
        out["security_db_encryption_name"] = data["SecurityDbEncryptionName"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("SpatialDataOptionToGeoJsonFunctionName") is not None:
        out["spatial_data_option_to_geo_json_function_name"] = data[
            "SpatialDataOptionToGeoJsonFunctionName"
        ]
    if data.get("StandbyDelayTime") is not None:
        out["standby_delay_time"] = data["StandbyDelayTime"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("UseBFile") is not None:
        out["use_b_file"] = data["UseBFile"]
    if data.get("UseDirectPathFullLoad") is not None:
        out["use_direct_path_full_load"] = data["UseDirectPathFullLoad"]
    if data.get("UseLogminerReader") is not None:
        out["use_logminer_reader"] = data["UseLogminerReader"]
    if data.get("SecretsManagerAccessRoleArn") is not None:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if data.get("SecretsManagerSecretId") is not None:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if data.get("SecretsManagerOracleAsmAccessRoleArn") is not None:
        out["secrets_manager_oracle_asm_access_role_arn"] = data[
            "SecretsManagerOracleAsmAccessRoleArn"
        ]
    if data.get("SecretsManagerOracleAsmSecretId") is not None:
        out["secrets_manager_oracle_asm_secret_id"] = data[
            "SecretsManagerOracleAsmSecretId"
        ]
    if data.get("TrimSpaceInChar") is not None:
        out["trim_space_in_char"] = data["TrimSpaceInChar"]
    if data.get("ConvertTimestampWithZoneToUTC") is not None:
        out["convert_timestamp_with_zone_to_utc"] = data[
            "ConvertTimestampWithZoneToUTC"
        ]
    if data.get("OpenTransactionWindow") is not None:
        out["open_transaction_window"] = data["OpenTransactionWindow"]
    if data.get("AuthenticationMethod") is not None:
        import capo_database_migration_service.types.oracle_authentication_method

        out["authentication_method"] = (
            capo_database_migration_service.types.oracle_authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    return out
