"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateNamespaceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.db_password
    import capo_redshift_serverless.types.db_user
    import capo_redshift_serverless.types.iam_role_arn_list
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.log_destination_type
    import capo_redshift_serverless.types.log_export_list
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.s3_table_action
    import capo_redshift_serverless.types.s3_table_granularity
    import capo_redshift_serverless.types.s3_table_name_list


class UpdateNamespaceRequest(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>"""
    admin_user_password: NotRequired[
        "capo_redshift_serverless.types.db_password.DbPassword"
    ]
    """<p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p> <p>If your admin user account is locked, this operation also unlocks your account and resets the failed-login counter. This option is available only when account lockout security is enabled for the namespace.</p>"""
    admin_username: NotRequired["capo_redshift_serverless.types.db_user.DbUser"]
    """<p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>"""
    default_iam_role_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>"""
    iam_roles: NotRequired[
        "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
    ]
    """<p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>"""
    log_exports: NotRequired[
        "capo_redshift_serverless.types.log_export_list.LogExportList"
    ]
    """<p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>"""
    manage_admin_password: NotRequired["bool"]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>"""
    log_destination_type: NotRequired[
        "capo_redshift_serverless.types.log_destination_type.LogDestinationType"
    ]
    """<p>The destination for the log data. Valid values are <code>s3table</code> and <code>cloudwatch</code>.</p> <p>Set this to <code>s3table</code> to manage Amazon S3 Tables system-table publishing for the namespace.</p>"""
    s3_table_action: NotRequired[
        "capo_redshift_serverless.types.s3_table_action.S3TableAction"
    ]
    """<p>Whether to enable or disable Amazon S3 Tables publishing. Valid values are <code>Enable</code> and <code>Disable</code>, matched case-insensitively.</p> <p>When omitted, defaults to <code>Enable</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>"""
    s3_table_names: NotRequired[
        "capo_redshift_serverless.types.s3_table_name_list.S3TableNameList"
    ]
    """<p>The system tables to publish (on enable) or to stop publishing (on disable). Each value is either a system table view name that begins with <code>sys_</code> or the keyword <code>all</code>.</p> <p>Omitting this parameter, passing an empty list, or including <code>all</code> each select every current and future system table. Each name must be 1-128 characters, and the list can contain up to 256 names.</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>"""
    s3_table_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The identifier of the Key Management Service key used to encrypt the published Amazon S3 Tables data. When omitted, the data is encrypted with SSE-S3 (Amazon S3 managed keys).</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>"""
    s3_table_granularity: NotRequired[
        "capo_redshift_serverless.types.s3_table_granularity.S3TableGranularity"
    ]
    """<p>The scope of the Amazon S3 Tables destination. Valid values are <code>namespace</code> and <code>account</code>, matched case-insensitively. <code>namespace</code> scopes the published tables to this namespace; <code>account</code> scopes them to the Amazon Web Services account.</p> <p>Required when enabling. Omitting this parameter or passing a blank value fails with <code>ValidationException</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNamespaceRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "admin_user_password" in value:
        out["adminUserPassword"] = value["admin_user_password"]
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "default_iam_role_arn" in value:
        out["defaultIamRoleArn"] = value["default_iam_role_arn"]
    if "iam_roles" in value:
        import capo_redshift_serverless.types.iam_role_arn_list

        out["iamRoles"] = (
            capo_redshift_serverless.types.iam_role_arn_list.serialize_aws_json_1_1(
                value["iam_roles"]
            )
        )
    if "log_exports" in value:
        import capo_redshift_serverless.types.log_export_list

        out["logExports"] = (
            capo_redshift_serverless.types.log_export_list.serialize_aws_json_1_1(
                value["log_exports"]
            )
        )
    if "manage_admin_password" in value:
        out["manageAdminPassword"] = value["manage_admin_password"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    if "log_destination_type" in value:
        out["logDestinationType"] = value["log_destination_type"]
    if "s3_table_action" in value:
        out["s3TableAction"] = value["s3_table_action"]
    if "s3_table_names" in value:
        import capo_redshift_serverless.types.s3_table_name_list

        out["s3TableNames"] = (
            capo_redshift_serverless.types.s3_table_name_list.serialize_aws_json_1_1(
                value["s3_table_names"]
            )
        )
    if "s3_table_kms_key_id" in value:
        out["s3TableKmsKeyId"] = value["s3_table_kms_key_id"]
    if "s3_table_granularity" in value:
        out["s3TableGranularity"] = value["s3_table_granularity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNamespaceRequest:
    out: UpdateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError("UpdateNamespaceRequest.namespace_name required")
    if data.get("adminUserPassword") is not None:
        out["admin_user_password"] = data["adminUserPassword"]
    if data.get("adminUsername") is not None:
        out["admin_username"] = data["adminUsername"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("defaultIamRoleArn") is not None:
        out["default_iam_role_arn"] = data["defaultIamRoleArn"]
    if data.get("iamRoles") is not None:
        import capo_redshift_serverless.types.iam_role_arn_list

        out["iam_roles"] = (
            capo_redshift_serverless.types.iam_role_arn_list.deserialize_aws_json_1_1(
                data["iamRoles"]
            )
        )
    if data.get("logExports") is not None:
        import capo_redshift_serverless.types.log_export_list

        out["log_exports"] = (
            capo_redshift_serverless.types.log_export_list.deserialize_aws_json_1_1(
                data["logExports"]
            )
        )
    if data.get("manageAdminPassword") is not None:
        out["manage_admin_password"] = data["manageAdminPassword"]
    if data.get("adminPasswordSecretKmsKeyId") is not None:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    if data.get("logDestinationType") is not None:
        out["log_destination_type"] = data["logDestinationType"]
    if data.get("s3TableAction") is not None:
        out["s3_table_action"] = data["s3TableAction"]
    if data.get("s3TableNames") is not None:
        import capo_redshift_serverless.types.s3_table_name_list

        out["s3_table_names"] = (
            capo_redshift_serverless.types.s3_table_name_list.deserialize_aws_json_1_1(
                data["s3TableNames"]
            )
        )
    if data.get("s3TableKmsKeyId") is not None:
        out["s3_table_kms_key_id"] = data["s3TableKmsKeyId"]
    if data.get("s3TableGranularity") is not None:
        out["s3_table_granularity"] = data["s3TableGranularity"]
    return out


def redact_sensitive(value: UpdateNamespaceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "admin_user_password" in value:
        out["admin_user_password"] = "*** Sensitive Data Redacted ***"
    if "admin_username" in value:
        out["admin_username"] = "*** Sensitive Data Redacted ***"
    return out
