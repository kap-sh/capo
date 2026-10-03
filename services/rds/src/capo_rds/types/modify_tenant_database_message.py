"""Generated from Smithy shape ``com.amazonaws.rds#ModifyTenantDatabaseMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.sensitive_string
    import capo_rds.types.string


class ModifyTenantDatabaseMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the DB instance that contains the tenant database that you are modifying. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB instance.</p> </li> </ul>"""
    tenant_db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied name of the tenant database that you want to modify. This parameter isn’t case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing tenant database.</p> </li> </ul>"""
    master_user_password: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>The new password for the master user of the specified tenant database in your DB instance.</p> <note> <p>Amazon RDS operations never return the password, so this action provides a way to regain access to a tenant database user if the password is lost. This includes restoring privileges that might have been accidentally revoked.</p> </note> <p>Constraints:</p> <ul> <li> <p>Can include any printable ASCII character except <code>/</code>, <code>"</code> (double quote), <code>@</code>, <code>&amp;</code> (ampersand), and <code>'</code> (single quote).</p> </li> </ul> <p>Length constraints:</p> <ul> <li> <p>Must contain between 8 and 30 characters. </p> </li> </ul>"""
    new_tenant_db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The new name of the tenant database when renaming a tenant database. This parameter isn’t case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Can't be the string null or any other reserved word.</p> </li> <li> <p>Can't be longer than 8 characters.</p> </li> </ul>"""
    manage_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to manage the master user password with Amazon Web Services Secrets Manager.</p> <p>If the tenant database doesn't manage the master user password with Amazon Web Services Secrets Manager, you can turn on this management. In this case, you can't specify <code>MasterUserPassword</code>.</p> <p>If the tenant database already manages the master user password with Amazon Web Services Secrets Manager, and you specify that the master user password is not managed with Amazon Web Services Secrets Manager, then you must specify <code>MasterUserPassword</code>. In this case, Amazon RDS deletes the secret and uses the new password for the master user specified by <code>MasterUserPassword</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>Can't manage the master user password with Amazon Web Services Secrets Manager if <code>MasterUserPassword</code> is specified.</p> </li> </ul>"""
    rotate_master_user_password: NotRequired[
        "capo_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to rotate the secret managed by Amazon Web Services Secrets Manager for the master user password.</p> <p>This setting is valid only if the master user password is managed by RDS in Amazon Web Services Secrets Manager for the DB instance. The secret value contains the updated password.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html">Password management with Amazon Web Services Secrets Manager</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Constraints:</p> <ul> <li> <p>You must apply the change immediately when rotating the master user password.</p> </li> </ul>"""
    master_user_secret_kms_key_id: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier to encrypt a secret that is automatically generated and managed in Amazon Web Services Secrets Manager.</p> <p>This setting is valid only if both of the following conditions are met:</p> <ul> <li> <p>The tenant database doesn't manage the master user password in Amazon Web Services Secrets Manager.</p> <p>If the tenant database already manages the master user password in Amazon Web Services Secrets Manager, you can't change the KMS key used to encrypt the secret.</p> </li> <li> <p>You're turning on <code>ManageMasterUserPassword</code> to manage the master user password in Amazon Web Services Secrets Manager.</p> <p>If you're turning on <code>ManageMasterUserPassword</code> and don't specify <code>MasterUserSecretKmsKeyId</code>, then the <code>aws/secretsmanager</code> KMS key is used to encrypt the secret. If the secret is in a different Amazon Web Services account, then you can't use the <code>aws/secretsmanager</code> KMS key to encrypt the secret, and you must use a self-managed KMS key.</p> </li> </ul> <p>The Amazon Web Services KMS key identifier is any of the following:</p> <ul> <li> <p>Key ARN</p> </li> <li> <p>Key ID</p> </li> <li> <p>Alias ARN</p> </li> <li> <p>Alias name for the KMS key</p> </li> </ul> <p>To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>A default KMS key exists for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTenantDatabaseMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "tenant_db_name" in value:
        pairs.append((f"{key_prefix}TenantDBName", str(value["tenant_db_name"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "new_tenant_db_name" in value:
        pairs.append((f"{key_prefix}NewTenantDBName", str(value["new_tenant_db_name"])))
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


def deserialize_query(el: Element) -> ModifyTenantDatabaseMessage:
    out: ModifyTenantDatabaseMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_tenant_db_name = el.find("TenantDBName")
    if child_tenant_db_name is not None:
        out["tenant_db_name"] = str(child_tenant_db_name.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_new_tenant_db_name = el.find("NewTenantDBName")
    if child_new_tenant_db_name is not None:
        out["new_tenant_db_name"] = str(child_new_tenant_db_name.text or "")
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
    return out
