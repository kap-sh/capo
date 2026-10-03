"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OracleDataProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.dms_ssl_mode_value
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class OracleDataProviderSettings(TypedDict, closed=True):
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the Oracle server.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the Oracle data provider.</p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database name on the Oracle data provider.</p>"""
    ssl_mode: NotRequired[
        "capo_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the Oracle data provider. The default value is <code>none</code>.</p>"""
    certificate_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""
    asm_server: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The address of your Oracle Automatic Storage Management (ASM) server. You can set this value from the <code>asm_server</code> value. You set <code>asm_server</code> as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration">Configuration for change data capture (CDC) on an Oracle source database</a>.</p>"""
    secrets_manager_oracle_asm_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the secret in Secrets Manager that contains the Oracle ASM connection details.</p> <p>Required only if your data provider uses the Oracle ASM server.</p>"""
    secrets_manager_oracle_asm_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the IAM role that provides access to the secret in Secrets Manager that contains the Oracle ASM connection details.</p>"""
    secrets_manager_security_db_encryption_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the secret in Secrets Manager that contains the transparent data encryption (TDE) password. DMS requires this password to access Oracle redo logs encrypted by TDE using Binary Reader.</p>"""
    secrets_manager_security_db_encryption_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the IAM role that provides access to the secret in Secrets Manager that contains the TDE password.</p>"""
    s3_path: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.</p>"""
    s3_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN for the role the application uses to access its Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OracleDataProviderSettings) -> dict:
    out: dict = {}
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "ssl_mode" in value:
        import capo_database_migration_service.types.dms_ssl_mode_value

        out["SslMode"] = (
            capo_database_migration_service.types.dms_ssl_mode_value.serialize_aws_json_1_1(
                value["ssl_mode"]
            )
        )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "asm_server" in value:
        out["AsmServer"] = value["asm_server"]
    if "secrets_manager_oracle_asm_secret_id" in value:
        out["SecretsManagerOracleAsmSecretId"] = value[
            "secrets_manager_oracle_asm_secret_id"
        ]
    if "secrets_manager_oracle_asm_access_role_arn" in value:
        out["SecretsManagerOracleAsmAccessRoleArn"] = value[
            "secrets_manager_oracle_asm_access_role_arn"
        ]
    if "secrets_manager_security_db_encryption_secret_id" in value:
        out["SecretsManagerSecurityDbEncryptionSecretId"] = value[
            "secrets_manager_security_db_encryption_secret_id"
        ]
    if "secrets_manager_security_db_encryption_access_role_arn" in value:
        out["SecretsManagerSecurityDbEncryptionAccessRoleArn"] = value[
            "secrets_manager_security_db_encryption_access_role_arn"
        ]
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    if "s3_access_role_arn" in value:
        out["S3AccessRoleArn"] = value["s3_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OracleDataProviderSettings:
    out: OracleDataProviderSettings = {}  # type: ignore[typeddict-item]
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("SslMode") is not None:
        import capo_database_migration_service.types.dms_ssl_mode_value

        out["ssl_mode"] = (
            capo_database_migration_service.types.dms_ssl_mode_value.deserialize_aws_json_1_1(
                data["SslMode"]
            )
        )
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("AsmServer") is not None:
        out["asm_server"] = data["AsmServer"]
    if data.get("SecretsManagerOracleAsmSecretId") is not None:
        out["secrets_manager_oracle_asm_secret_id"] = data[
            "SecretsManagerOracleAsmSecretId"
        ]
    if data.get("SecretsManagerOracleAsmAccessRoleArn") is not None:
        out["secrets_manager_oracle_asm_access_role_arn"] = data[
            "SecretsManagerOracleAsmAccessRoleArn"
        ]
    if data.get("SecretsManagerSecurityDbEncryptionSecretId") is not None:
        out["secrets_manager_security_db_encryption_secret_id"] = data[
            "SecretsManagerSecurityDbEncryptionSecretId"
        ]
    if data.get("SecretsManagerSecurityDbEncryptionAccessRoleArn") is not None:
        out["secrets_manager_security_db_encryption_access_role_arn"] = data[
            "SecretsManagerSecurityDbEncryptionAccessRoleArn"
        ]
    if data.get("S3Path") is not None:
        out["s3_path"] = data["S3Path"]
    if data.get("S3AccessRoleArn") is not None:
        out["s3_access_role_arn"] = data["S3AccessRoleArn"]
    return out
