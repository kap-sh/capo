"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Namespace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.db_user
    import capo_redshift_serverless.types.iam_role_arn_list
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.log_export_list
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.namespace_status
    import capo_redshift_serverless.types.s3_table_publish_status


class Namespace(TypedDict, closed=True):
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) associated with a namespace.</p>"""
    namespace_id: NotRequired["str"]
    """<p>The unique identifier of a namespace.</p>"""
    namespace_name: NotRequired[
        "capo_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide.</p>"""
    admin_username: NotRequired["capo_redshift_serverless.types.db_user.DbUser"]
    """<p>The username of the administrator for the first database created in the namespace.</p>"""
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
    """<p>The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.</p>"""
    status: NotRequired[
        "capo_redshift_serverless.types.namespace_status.NamespaceStatus"
    ]
    """<p>The status of the namespace.</p>"""
    creation_date: NotRequired["datetime.datetime"]
    """<p>The date of when the namespace was created.</p>"""
    admin_password_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.</p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>"""
    lakehouse_registration_status: NotRequired["str"]
    """<p>The status of the lakehouse registration for the namespace. Indicates whether the namespace is successfully registered with Amazon Redshift federated permissions.</p>"""
    catalog_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Glue Data Catalog associated with the namespace enabled with Amazon Redshift federated permissions.</p>"""
    s3_table_publish_status: NotRequired[
        "capo_redshift_serverless.types.s3_table_publish_status.S3TablePublishStatus"
    ]
    """<p>The current Amazon S3 Tables log-publishing status for the namespace. Not returned when S3 Tables publishing has never been configured for the namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Namespace) -> dict:
    out: dict = {}
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
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
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date" in value:
        import capo_redshift_serverless._protocol.serialize

        out["creationDate"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["creation_date"]
            )
        )
    if "admin_password_secret_arn" in value:
        out["adminPasswordSecretArn"] = value["admin_password_secret_arn"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    if "lakehouse_registration_status" in value:
        out["lakehouseRegistrationStatus"] = value["lakehouse_registration_status"]
    if "catalog_arn" in value:
        out["catalogArn"] = value["catalog_arn"]
    if "s3_table_publish_status" in value:
        import capo_redshift_serverless.types.s3_table_publish_status

        out["s3TablePublishStatus"] = (
            capo_redshift_serverless.types.s3_table_publish_status.serialize_aws_json_1_1(
                value["s3_table_publish_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Namespace:
    out: Namespace = {}  # type: ignore[typeddict-item]
    if data.get("namespaceArn") is not None:
        out["namespace_arn"] = data["namespaceArn"]
    if data.get("namespaceId") is not None:
        out["namespace_id"] = data["namespaceId"]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("adminUsername") is not None:
        out["admin_username"] = data["adminUsername"]
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("creationDate") is not None:
        import datetime

        out["creation_date"] = datetime.datetime.fromisoformat(
            data["creationDate"].replace("Z", "+00:00")
        )
    if data.get("adminPasswordSecretArn") is not None:
        out["admin_password_secret_arn"] = data["adminPasswordSecretArn"]
    if data.get("adminPasswordSecretKmsKeyId") is not None:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    if data.get("lakehouseRegistrationStatus") is not None:
        out["lakehouse_registration_status"] = data["lakehouseRegistrationStatus"]
    if data.get("catalogArn") is not None:
        out["catalog_arn"] = data["catalogArn"]
    if data.get("s3TablePublishStatus") is not None:
        import capo_redshift_serverless.types.s3_table_publish_status

        out["s3_table_publish_status"] = (
            capo_redshift_serverless.types.s3_table_publish_status.deserialize_aws_json_1_1(
                data["s3TablePublishStatus"]
            )
        )
    return out
