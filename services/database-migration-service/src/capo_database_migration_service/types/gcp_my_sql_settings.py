"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#GcpMySQLSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.target_db_type


class GcpMySQLSettings(TypedDict, closed=True):
    after_connect_script: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Specifies a script to run immediately after DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails.</p> <p>For this parameter, provide the code of the script itself, not the name of a file containing the script. </p>"""
    clean_source_metadata_on_mismatch: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance. </p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Database name for the endpoint. For a MySQL source or target endpoint, don't explicitly specify the database using the <code>DatabaseName</code> request parameter on either the <code>CreateEndpoint</code> or <code>ModifyEndpoint</code> API call. Specifying <code>DatabaseName</code> when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task. </p>"""
    events_poll_interval: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds.</p> <p>Example: <code>eventsPollInterval=5;</code> </p> <p>In the example, DMS checks for changes in the binary logs every five seconds. </p>"""
    target_db_type: NotRequired[
        "capo_database_migration_service.types.target_db_type.TargetDbType"
    ]
    """<p>Specifies where to migrate source tables on the target, either to a single database or multiple databases.</p> <p>Example: <code>targetDbType=MULTIPLE_DATABASES</code> </p>"""
    max_file_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.</p> <p>Example: <code>maxFileSize=512</code> </p>"""
    parallel_load_threads: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.</p> <p>Example: <code>parallelLoadThreads=1</code> </p>"""
    password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>Endpoint connection password.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Endpoint TCP port.</p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The MySQL host name.</p>"""
    server_timezone: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the time zone for the source MySQL database.</p> <p>Example: <code>serverTimezone=US/Pacific;</code> </p> <p>Note: Do not enclose time zones in single quotes.</p>"""
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Endpoint connection user name.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret.</code> The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the MySQL endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager">Using secrets to access Database Migration Service resources</a> in the Database Migration Service User Guide. </p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the MySQL endpoint connection details. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GcpMySQLSettings) -> dict:
    out: dict = {}
    if "after_connect_script" in value:
        out["AfterConnectScript"] = value["after_connect_script"]
    if "clean_source_metadata_on_mismatch" in value:
        out["CleanSourceMetadataOnMismatch"] = value[
            "clean_source_metadata_on_mismatch"
        ]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "events_poll_interval" in value:
        out["EventsPollInterval"] = value["events_poll_interval"]
    if "target_db_type" in value:
        import capo_database_migration_service.types.target_db_type

        out["TargetDbType"] = (
            capo_database_migration_service.types.target_db_type.serialize_aws_json_1_1(
                value["target_db_type"]
            )
        )
    if "max_file_size" in value:
        out["MaxFileSize"] = value["max_file_size"]
    if "parallel_load_threads" in value:
        out["ParallelLoadThreads"] = value["parallel_load_threads"]
    if "password" in value:
        out["Password"] = value["password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "server_timezone" in value:
        out["ServerTimezone"] = value["server_timezone"]
    if "username" in value:
        out["Username"] = value["username"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GcpMySQLSettings:
    out: GcpMySQLSettings = {}  # type: ignore[typeddict-item]
    if data.get("AfterConnectScript") is not None:
        out["after_connect_script"] = data["AfterConnectScript"]
    if data.get("CleanSourceMetadataOnMismatch") is not None:
        out["clean_source_metadata_on_mismatch"] = data["CleanSourceMetadataOnMismatch"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("EventsPollInterval") is not None:
        out["events_poll_interval"] = data["EventsPollInterval"]
    if data.get("TargetDbType") is not None:
        import capo_database_migration_service.types.target_db_type

        out["target_db_type"] = (
            capo_database_migration_service.types.target_db_type.deserialize_aws_json_1_1(
                data["TargetDbType"]
            )
        )
    if data.get("MaxFileSize") is not None:
        out["max_file_size"] = data["MaxFileSize"]
    if data.get("ParallelLoadThreads") is not None:
        out["parallel_load_threads"] = data["ParallelLoadThreads"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("ServerTimezone") is not None:
        out["server_timezone"] = data["ServerTimezone"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("SecretsManagerAccessRoleArn") is not None:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if data.get("SecretsManagerSecretId") is not None:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    return out
