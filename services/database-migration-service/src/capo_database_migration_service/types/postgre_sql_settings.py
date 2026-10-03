"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PostgreSQLSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.database_mode
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.long_varchar_mapping_type
    import capo_database_migration_service.types.plugin_name_value
    import capo_database_migration_service.types.postgre_sql_authentication_method
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string


class PostgreSQLSettings(TypedDict, closed=True):
    after_connect_script: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>For use with change data capture (CDC) only, this attribute has DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data.</p> <p>Example: <code>afterConnectScript=SET session_replication_role='replica'</code> </p>"""
    capture_ddls: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>To capture DDL events, DMS creates various artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts.</p> <p>The default value is <code>true</code>.</p> <p>If this value is set to <code>N</code>, you don't have to create tables or triggers on the source database.</p>"""
    max_file_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL.</p> <p>The default value is 32,768 KB (32 MB).</p> <p>Example: <code>maxFileSize=512</code> </p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Database name for the endpoint.</p>"""
    ddl_artifacts_schema: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The schema in which the operational DDL database artifacts are created.</p> <p>The default value is <code>public</code>.</p> <p>Example: <code>ddlArtifactsSchema=xyzddlschema;</code> </p>"""
    execute_timeout: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds.</p> <p>Example: <code>executeTimeout=100;</code> </p>"""
    fail_tasks_on_lob_truncation: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to <code>true</code>, this value causes a task to fail if the actual size of a LOB column is greater than the specified <code>LobMaxSize</code>.</p> <p>The default value is <code>false</code>.</p> <p>If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.</p>"""
    heartbeat_enable: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>The write-ahead log (WAL) heartbeat feature mimics a dummy transaction. By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps <code>restart_lsn</code> moving and prevents storage full scenarios.</p> <p>The default value is <code>false</code>.</p>"""
    heartbeat_schema: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Sets the schema in which the heartbeat artifacts are created.</p> <p>The default value is <code>public</code>.</p>"""
    heartbeat_frequency: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Sets the WAL heartbeat frequency (in minutes).</p> <p>The default value is 5 minutes.</p>"""
    password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>Endpoint connection password.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Endpoint TCP port. The default is 5432.</p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The host name of the endpoint database. </p> <p>For an Amazon RDS PostgreSQL instance, this is the output of <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html">DescribeDBInstances</a>, in the <code> <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html">Endpoint</a>.Address</code> field.</p> <p>For an Aurora PostgreSQL instance, this is the output of <a href="https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html">DescribeDBClusters</a>, in the <code>Endpoint</code> field.</p>"""
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Endpoint connection user name.</p>"""
    slot_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance. </p> <p>When used with the <code>CdcStartPosition</code> request parameter for the DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of <code>CdcStartPosition</code>. If the specified slot doesn't exist or the task doesn't have a valid <code>CdcStartPosition</code> setting, DMS raises an error.</p> <p>For more information about setting the <code>CdcStartPosition</code> request parameter, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native">Determining a CDC native start point</a> in the <i>Database Migration Service User Guide</i>. For more information about using <code>CdcStartPosition</code>, see <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html">CreateReplicationTask</a>, <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html">StartReplicationTask</a>, and <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html">ModifyReplicationTask</a>.</p>"""
    plugin_name: NotRequired[
        "capo_database_migration_service.types.plugin_name_value.PluginNameValue"
    ]
    """<p>Specifies the plugin to use to create a replication slot.</p> <p>The default value is <code>pglogical</code>.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the PostgreSQL endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the PostgreSQL endpoint connection details.</p>"""
    trim_space_in_char: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Use the <code>TrimSpaceInChar</code> source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is <code>true</code>.</p>"""
    map_boolean_as_boolean: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When true, lets PostgreSQL migrate the boolean type as boolean. By default, PostgreSQL migrates booleans as <code>varchar(5)</code>. You must set this setting on both the source and target endpoints for it to take effect.</p> <p>The default value is <code>false</code>.</p>"""
    map_jsonb_as_clob: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When true, DMS migrates JSONB values as CLOB.</p> <p>The default value is <code>false</code>.</p>"""
    map_long_varchar_as: NotRequired[
        "capo_database_migration_service.types.long_varchar_mapping_type.LongVarcharMappingType"
    ]
    """<p>Sets what datatype to map LONG values as.</p> <p>The default value is <code>wstring</code>.</p>"""
    database_mode: NotRequired[
        "capo_database_migration_service.types.database_mode.DatabaseMode"
    ]
    """<p>Specifies the default behavior of the replication's handling of PostgreSQL- compatible endpoints that require some additional configuration, such as Babelfish endpoints.</p>"""
    babelfish_database_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Babelfish for Aurora PostgreSQL database name for the endpoint.</p>"""
    disable_unicode_source_filter: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Disables the Unicode source filter with PostgreSQL, for values passed into the Selection rule filter on Source Endpoint column values. By default DMS performs source filter comparisons using a Unicode string which can cause look ups to ignore the indexes in the text columns and slow down migrations.</p> <p>Unicode support should only be disabled when using a selection rule filter is on a text column in the Source database that is indexed.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The IAM role arn you can use to authenticate the connection to your endpoint. Ensure to include <code>iam:PassRole</code> and <code>rds-db:connect</code> actions in permission policy.</p>"""
    authentication_method: NotRequired[
        "capo_database_migration_service.types.postgre_sql_authentication_method.PostgreSQLAuthenticationMethod"
    ]
    """<p>This attribute allows you to specify the authentication method as "iam auth".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostgreSQLSettings) -> dict:
    out: dict = {}
    if "after_connect_script" in value:
        out["AfterConnectScript"] = value["after_connect_script"]
    if "capture_ddls" in value:
        out["CaptureDdls"] = value["capture_ddls"]
    if "max_file_size" in value:
        out["MaxFileSize"] = value["max_file_size"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "ddl_artifacts_schema" in value:
        out["DdlArtifactsSchema"] = value["ddl_artifacts_schema"]
    if "execute_timeout" in value:
        out["ExecuteTimeout"] = value["execute_timeout"]
    if "fail_tasks_on_lob_truncation" in value:
        out["FailTasksOnLobTruncation"] = value["fail_tasks_on_lob_truncation"]
    if "heartbeat_enable" in value:
        out["HeartbeatEnable"] = value["heartbeat_enable"]
    if "heartbeat_schema" in value:
        out["HeartbeatSchema"] = value["heartbeat_schema"]
    if "heartbeat_frequency" in value:
        out["HeartbeatFrequency"] = value["heartbeat_frequency"]
    if "password" in value:
        out["Password"] = value["password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "username" in value:
        out["Username"] = value["username"]
    if "slot_name" in value:
        out["SlotName"] = value["slot_name"]
    if "plugin_name" in value:
        import capo_database_migration_service.types.plugin_name_value

        out["PluginName"] = (
            capo_database_migration_service.types.plugin_name_value.serialize_aws_json_1_1(
                value["plugin_name"]
            )
        )
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "trim_space_in_char" in value:
        out["TrimSpaceInChar"] = value["trim_space_in_char"]
    if "map_boolean_as_boolean" in value:
        out["MapBooleanAsBoolean"] = value["map_boolean_as_boolean"]
    if "map_jsonb_as_clob" in value:
        out["MapJsonbAsClob"] = value["map_jsonb_as_clob"]
    if "map_long_varchar_as" in value:
        import capo_database_migration_service.types.long_varchar_mapping_type

        out["MapLongVarcharAs"] = (
            capo_database_migration_service.types.long_varchar_mapping_type.serialize_aws_json_1_1(
                value["map_long_varchar_as"]
            )
        )
    if "database_mode" in value:
        import capo_database_migration_service.types.database_mode

        out["DatabaseMode"] = (
            capo_database_migration_service.types.database_mode.serialize_aws_json_1_1(
                value["database_mode"]
            )
        )
    if "babelfish_database_name" in value:
        out["BabelfishDatabaseName"] = value["babelfish_database_name"]
    if "disable_unicode_source_filter" in value:
        out["DisableUnicodeSourceFilter"] = value["disable_unicode_source_filter"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "authentication_method" in value:
        import capo_database_migration_service.types.postgre_sql_authentication_method

        out["AuthenticationMethod"] = (
            capo_database_migration_service.types.postgre_sql_authentication_method.serialize_aws_json_1_1(
                value["authentication_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PostgreSQLSettings:
    out: PostgreSQLSettings = {}  # type: ignore[typeddict-item]
    if data.get("AfterConnectScript") is not None:
        out["after_connect_script"] = data["AfterConnectScript"]
    if data.get("CaptureDdls") is not None:
        out["capture_ddls"] = data["CaptureDdls"]
    if data.get("MaxFileSize") is not None:
        out["max_file_size"] = data["MaxFileSize"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("DdlArtifactsSchema") is not None:
        out["ddl_artifacts_schema"] = data["DdlArtifactsSchema"]
    if data.get("ExecuteTimeout") is not None:
        out["execute_timeout"] = data["ExecuteTimeout"]
    if data.get("FailTasksOnLobTruncation") is not None:
        out["fail_tasks_on_lob_truncation"] = data["FailTasksOnLobTruncation"]
    if data.get("HeartbeatEnable") is not None:
        out["heartbeat_enable"] = data["HeartbeatEnable"]
    if data.get("HeartbeatSchema") is not None:
        out["heartbeat_schema"] = data["HeartbeatSchema"]
    if data.get("HeartbeatFrequency") is not None:
        out["heartbeat_frequency"] = data["HeartbeatFrequency"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("SlotName") is not None:
        out["slot_name"] = data["SlotName"]
    if data.get("PluginName") is not None:
        import capo_database_migration_service.types.plugin_name_value

        out["plugin_name"] = (
            capo_database_migration_service.types.plugin_name_value.deserialize_aws_json_1_1(
                data["PluginName"]
            )
        )
    if data.get("SecretsManagerAccessRoleArn") is not None:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if data.get("SecretsManagerSecretId") is not None:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if data.get("TrimSpaceInChar") is not None:
        out["trim_space_in_char"] = data["TrimSpaceInChar"]
    if data.get("MapBooleanAsBoolean") is not None:
        out["map_boolean_as_boolean"] = data["MapBooleanAsBoolean"]
    if data.get("MapJsonbAsClob") is not None:
        out["map_jsonb_as_clob"] = data["MapJsonbAsClob"]
    if data.get("MapLongVarcharAs") is not None:
        import capo_database_migration_service.types.long_varchar_mapping_type

        out["map_long_varchar_as"] = (
            capo_database_migration_service.types.long_varchar_mapping_type.deserialize_aws_json_1_1(
                data["MapLongVarcharAs"]
            )
        )
    if data.get("DatabaseMode") is not None:
        import capo_database_migration_service.types.database_mode

        out["database_mode"] = (
            capo_database_migration_service.types.database_mode.deserialize_aws_json_1_1(
                data["DatabaseMode"]
            )
        )
    if data.get("BabelfishDatabaseName") is not None:
        out["babelfish_database_name"] = data["BabelfishDatabaseName"]
    if data.get("DisableUnicodeSourceFilter") is not None:
        out["disable_unicode_source_filter"] = data["DisableUnicodeSourceFilter"]
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("AuthenticationMethod") is not None:
        import capo_database_migration_service.types.postgre_sql_authentication_method

        out["authentication_method"] = (
            capo_database_migration_service.types.postgre_sql_authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    return out
