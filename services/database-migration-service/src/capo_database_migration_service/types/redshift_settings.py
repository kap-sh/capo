"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RedshiftSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.encryption_mode_value
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string


class RedshiftSettings(TypedDict, closed=True):
    accept_any_date: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose <code>true</code> or <code>false</code> (the default).</p> <p>This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field. </p>"""
    after_connect_script: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.</p>"""
    bucket_folder: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster. </p> <p>For full load mode, DMS converts source records into .csv files and loads them to the <i>BucketFolder/TableID</i> path. DMS uses the Redshift <code>COPY</code> command to upload the .csv files to the target table. The files are deleted once the <code>COPY</code> operation has finished. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html">COPY</a> in the <i>Amazon Redshift Database Developer Guide</i>.</p> <p>For change-data-capture (CDC) mode, DMS creates a <i>NetChanges</i> table, and loads the .csv files to this <i>BucketFolder/NetChangesTableID</i> path.</p>"""
    bucket_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.</p>"""
    case_sensitive_names: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If Amazon Redshift is configured to support case sensitive schema names, set <code>CaseSensitiveNames</code> to <code>true</code>. The default is <code>false</code>.</p>"""
    comp_update: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If you set <code>CompUpdate</code> to <code>true</code> Amazon Redshift applies automatic compression if the table is empty. This applies even if the table columns already have encodings other than <code>RAW</code>. If you set <code>CompUpdate</code> to <code>false</code>, automatic compression is disabled and existing column encodings aren't changed. The default is <code>true</code>.</p>"""
    connection_timeout: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.</p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the Amazon Redshift data warehouse (service) that you are working with.</p>"""
    date_format: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The date format that you are using. Valid values are <code>auto</code> (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using <code>auto</code> recognizes most strings, even some that aren't supported when you use a date format string. </p> <p>If your date and time values use formats different from each other, set this to <code>auto</code>. </p>"""
    empty_as_null: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies whether DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of <code>true</code> sets empty CHAR and VARCHAR fields to null. The default is <code>false</code>.</p>"""
    encryption_mode: NotRequired[
        "capo_database_migration_service.types.encryption_mode_value.EncryptionModeValue"
    ]
    """<p>The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either <code>SSE_S3</code> (the default) or <code>SSE_KMS</code>. </p> <note> <p>For the <code>ModifyEndpoint</code> operation, you can change the existing value of the <code>EncryptionMode</code> parameter from <code>SSE_KMS</code> to <code>SSE_S3</code>. But you can’t change the existing value from <code>SSE_S3</code> to <code>SSE_KMS</code>.</p> </note> <p>To use <code>SSE_S3</code>, create an Identity and Access Management (IAM) role with a policy that allows <code>"arn:aws:s3:::*"</code> to use the following actions: <code>"s3:PutObject", "s3:ListBucket"</code> </p>"""
    explicit_ids: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>This setting is only valid for a full-load migration task. Set <code>ExplicitIds</code> to <code>true</code> to have tables with <code>IDENTITY</code> columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is <code>false</code>.</p>"""
    file_transfer_upload_streams: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.</p> <p>The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html">Multipart upload overview</a>. </p> <p> <code>FileTransferUploadStreams</code> accepts a value from 1 through 64. It defaults to 10.</p>"""
    load_timeout: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of time to wait (in seconds) before timing out of operations performed by DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.</p>"""
    max_file_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).</p>"""
    password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>The password for the user named in the <code>username</code> property.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port number for Amazon Redshift. The default value is 5439.</p>"""
    remove_quotes: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose <code>true</code> to remove quotation marks. The default is <code>false</code>.</p>"""
    replace_invalid_chars: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A list of characters that you want to replace. Use with <code>ReplaceChars</code>.</p>"""
    replace_chars: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A value that specifies to replaces the invalid characters specified in <code>ReplaceInvalidChars</code>, substituting the specified characters instead. The default is <code>"?"</code>.</p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the Amazon Redshift cluster you are using.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service. The role must allow the <code>iam:PassRole</code> action.</p>"""
    server_side_encryption_kms_key_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The KMS key ID. If you are using <code>SSE_KMS</code> for the <code>EncryptionMode</code>, provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.</p>"""
    time_format: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The time format that you want to use. Valid values are <code>auto</code> (case-sensitive), <code>'timeformat_string'</code>, <code>'epochsecs'</code>, or <code>'epochmillisecs'</code>. It defaults to 10. Using <code>auto</code> recognizes most strings, even some that aren't supported when you use a time format string. </p> <p>If your date and time values use formats different from each other, set this parameter to <code>auto</code>. </p>"""
    trim_blanks: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose <code>true</code> to remove unneeded white space. The default is <code>false</code>.</p>"""
    truncate_columns: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose <code>true</code> to truncate data. The default is <code>false</code>.</p>"""
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An Amazon Redshift user name for a registered user.</p>"""
    write_buffer_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the Amazon Redshift endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the Amazon Redshift endpoint connection details.</p>"""
    map_boolean_as_boolean: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When true, lets Redshift migrate the boolean type as boolean. By default, Redshift migrates booleans as <code>varchar(1)</code>. You must set this setting on both the source and target endpoints for it to take effect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftSettings) -> dict:
    out: dict = {}
    if "accept_any_date" in value:
        out["AcceptAnyDate"] = value["accept_any_date"]
    if "after_connect_script" in value:
        out["AfterConnectScript"] = value["after_connect_script"]
    if "bucket_folder" in value:
        out["BucketFolder"] = value["bucket_folder"]
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "case_sensitive_names" in value:
        out["CaseSensitiveNames"] = value["case_sensitive_names"]
    if "comp_update" in value:
        out["CompUpdate"] = value["comp_update"]
    if "connection_timeout" in value:
        out["ConnectionTimeout"] = value["connection_timeout"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "date_format" in value:
        out["DateFormat"] = value["date_format"]
    if "empty_as_null" in value:
        out["EmptyAsNull"] = value["empty_as_null"]
    if "encryption_mode" in value:
        import capo_database_migration_service.types.encryption_mode_value

        out["EncryptionMode"] = (
            capo_database_migration_service.types.encryption_mode_value.serialize_aws_json_1_1(
                value["encryption_mode"]
            )
        )
    if "explicit_ids" in value:
        out["ExplicitIds"] = value["explicit_ids"]
    if "file_transfer_upload_streams" in value:
        out["FileTransferUploadStreams"] = value["file_transfer_upload_streams"]
    if "load_timeout" in value:
        out["LoadTimeout"] = value["load_timeout"]
    if "max_file_size" in value:
        out["MaxFileSize"] = value["max_file_size"]
    if "password" in value:
        out["Password"] = value["password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "remove_quotes" in value:
        out["RemoveQuotes"] = value["remove_quotes"]
    if "replace_invalid_chars" in value:
        out["ReplaceInvalidChars"] = value["replace_invalid_chars"]
    if "replace_chars" in value:
        out["ReplaceChars"] = value["replace_chars"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "server_side_encryption_kms_key_id" in value:
        out["ServerSideEncryptionKmsKeyId"] = value["server_side_encryption_kms_key_id"]
    if "time_format" in value:
        out["TimeFormat"] = value["time_format"]
    if "trim_blanks" in value:
        out["TrimBlanks"] = value["trim_blanks"]
    if "truncate_columns" in value:
        out["TruncateColumns"] = value["truncate_columns"]
    if "username" in value:
        out["Username"] = value["username"]
    if "write_buffer_size" in value:
        out["WriteBufferSize"] = value["write_buffer_size"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "map_boolean_as_boolean" in value:
        out["MapBooleanAsBoolean"] = value["map_boolean_as_boolean"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftSettings:
    out: RedshiftSettings = {}  # type: ignore[typeddict-item]
    if data.get("AcceptAnyDate") is not None:
        out["accept_any_date"] = data["AcceptAnyDate"]
    if data.get("AfterConnectScript") is not None:
        out["after_connect_script"] = data["AfterConnectScript"]
    if data.get("BucketFolder") is not None:
        out["bucket_folder"] = data["BucketFolder"]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    if data.get("CaseSensitiveNames") is not None:
        out["case_sensitive_names"] = data["CaseSensitiveNames"]
    if data.get("CompUpdate") is not None:
        out["comp_update"] = data["CompUpdate"]
    if data.get("ConnectionTimeout") is not None:
        out["connection_timeout"] = data["ConnectionTimeout"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("DateFormat") is not None:
        out["date_format"] = data["DateFormat"]
    if data.get("EmptyAsNull") is not None:
        out["empty_as_null"] = data["EmptyAsNull"]
    if data.get("EncryptionMode") is not None:
        import capo_database_migration_service.types.encryption_mode_value

        out["encryption_mode"] = (
            capo_database_migration_service.types.encryption_mode_value.deserialize_aws_json_1_1(
                data["EncryptionMode"]
            )
        )
    if data.get("ExplicitIds") is not None:
        out["explicit_ids"] = data["ExplicitIds"]
    if data.get("FileTransferUploadStreams") is not None:
        out["file_transfer_upload_streams"] = data["FileTransferUploadStreams"]
    if data.get("LoadTimeout") is not None:
        out["load_timeout"] = data["LoadTimeout"]
    if data.get("MaxFileSize") is not None:
        out["max_file_size"] = data["MaxFileSize"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("RemoveQuotes") is not None:
        out["remove_quotes"] = data["RemoveQuotes"]
    if data.get("ReplaceInvalidChars") is not None:
        out["replace_invalid_chars"] = data["ReplaceInvalidChars"]
    if data.get("ReplaceChars") is not None:
        out["replace_chars"] = data["ReplaceChars"]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("ServerSideEncryptionKmsKeyId") is not None:
        out["server_side_encryption_kms_key_id"] = data["ServerSideEncryptionKmsKeyId"]
    if data.get("TimeFormat") is not None:
        out["time_format"] = data["TimeFormat"]
    if data.get("TrimBlanks") is not None:
        out["trim_blanks"] = data["TrimBlanks"]
    if data.get("TruncateColumns") is not None:
        out["truncate_columns"] = data["TruncateColumns"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("WriteBufferSize") is not None:
        out["write_buffer_size"] = data["WriteBufferSize"]
    if data.get("SecretsManagerAccessRoleArn") is not None:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if data.get("SecretsManagerSecretId") is not None:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if data.get("MapBooleanAsBoolean") is not None:
        out["map_boolean_as_boolean"] = data["MapBooleanAsBoolean"]
    return out
