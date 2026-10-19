"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateNamespaceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.db_password
    import capo_redshift_serverless.types.db_user
    import capo_redshift_serverless.types.iam_role_arn_list
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.log_export_list
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.redshift_idc_application_arn
    import capo_redshift_serverless.types.tag_list


class CreateNamespaceRequest(TypedDict, closed=True):
    namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace.</p>"""
    admin_username: NotRequired["capo_redshift_serverless.types.db_user.DbUser"]
    """<p>The username of the administrator for the first database created in the namespace.</p>"""
    admin_user_password: NotRequired[
        "capo_redshift_serverless.types.db_password.DbPassword"
    ]
    """<p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>"""
    db_name: NotRequired["str"]
    """<p>The name of the first database created in the namespace.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>"""
    default_iam_role_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>"""
    iam_roles: NotRequired[
        "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
    ]
    """<p>A list of IAM roles to associate with the namespace.</p>"""
    log_exports: NotRequired[
        "capo_redshift_serverless.types.log_export_list.LogExportList"
    ]
    """<p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>"""
    tags: NotRequired["capo_redshift_serverless.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""
    manage_admin_password: NotRequired["bool"]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>"""
    redshift_idc_application_arn: NotRequired[
        "capo_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
    ]
    """<p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamespaceRequest) -> dict:
    out: dict = {}
    out["namespaceName"] = value["namespace_name"]
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
    if "admin_user_password" in value:
        out["adminUserPassword"] = value["admin_user_password"]
    if "db_name" in value:
        out["dbName"] = value["db_name"]
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
    if "tags" in value:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "manage_admin_password" in value:
        out["manageAdminPassword"] = value["manage_admin_password"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    if "redshift_idc_application_arn" in value:
        out["redshiftIdcApplicationArn"] = value["redshift_idc_application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamespaceRequest:
    out: CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    else:
        out["namespace_name"] = ""
    if data.get("adminUsername") is not None:
        out["admin_username"] = data["adminUsername"]
    if data.get("adminUserPassword") is not None:
        out["admin_user_password"] = data["adminUserPassword"]
    if data.get("dbName") is not None:
        out["db_name"] = data["dbName"]
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
    if data.get("tags") is not None:
        import capo_redshift_serverless.types.tag_list

        out["tags"] = capo_redshift_serverless.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("manageAdminPassword") is not None:
        out["manage_admin_password"] = data["manageAdminPassword"]
    if data.get("adminPasswordSecretKmsKeyId") is not None:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    if data.get("redshiftIdcApplicationArn") is not None:
        out["redshift_idc_application_arn"] = data["redshiftIdcApplicationArn"]
    return out


def redact_sensitive(value: CreateNamespaceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "admin_username" in value:
        out["admin_username"] = "*** Sensitive Data Redacted ***"
    if "admin_user_password" in value:
        out["admin_user_password"] = "*** Sensitive Data Redacted ***"
    return out
