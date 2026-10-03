"""Generated from Smithy shape ``com.amazonaws.appflow#RedshiftConnectorProfileProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.bucket_name
    import capo_appflow.types.bucket_prefix
    import capo_appflow.types.cluster_identifier
    import capo_appflow.types.data_api_role_arn
    import capo_appflow.types.database_name
    import capo_appflow.types.database_url
    import capo_appflow.types.role_arn
    import capo_appflow.types.workgroup_name


class RedshiftConnectorProfileProperties(TypedDict, closed=True):
    database_url: NotRequired["capo_appflow.types.database_url.DatabaseUrl"]
    """<p> The JDBC URL of the Amazon Redshift cluster. </p>"""
    bucket_name: "capo_appflow.types.bucket_name.BucketName"
    """<p> A name for the associated Amazon S3 bucket. </p>"""
    bucket_prefix: NotRequired["capo_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the destination bucket in which Amazon AppFlow places the files. </p>"""
    role_arn: "capo_appflow.types.role_arn.RoleArn"
    """<p> The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3. For more information, and for the polices that you attach to this role, see <a href="https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3">Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3</a>.</p>"""
    data_api_role_arn: NotRequired[
        "capo_appflow.types.data_api_role_arn.DataApiRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API. For more information, and for the polices that you attach to this role, see <a href="https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift">Allow Amazon AppFlow to access Amazon Redshift databases with the Data API</a>.</p>"""
    is_redshift_serverless: "capo_appflow.types.boolean.Boolean"
    """<p>Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.</p>"""
    cluster_identifier: NotRequired[
        "capo_appflow.types.cluster_identifier.ClusterIdentifier"
    ]
    """<p>The unique ID that's assigned to an Amazon Redshift cluster.</p>"""
    workgroup_name: NotRequired["capo_appflow.types.workgroup_name.WorkgroupName"]
    """<p>The name of an Amazon Redshift workgroup.</p>"""
    database_name: NotRequired["capo_appflow.types.database_name.DatabaseName"]
    """<p>The name of an Amazon Redshift database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConnectorProfileProperties) -> dict:
    out: dict = {}
    if "database_url" in value:
        out["databaseUrl"] = value["database_url"]
    out["bucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    out["roleArn"] = value["role_arn"]
    if "data_api_role_arn" in value:
        out["dataApiRoleArn"] = value["data_api_role_arn"]
    out["isRedshiftServerless"] = value.get("is_redshift_serverless", False)
    if "cluster_identifier" in value:
        out["clusterIdentifier"] = value["cluster_identifier"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> RedshiftConnectorProfileProperties:
    out: RedshiftConnectorProfileProperties = {}  # type: ignore[typeddict-item]
    if data.get("databaseUrl") is not None:
        out["database_url"] = data["databaseUrl"]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError(
            "RedshiftConnectorProfileProperties.bucket_name required"
        )
    if data.get("bucketPrefix") is not None:
        out["bucket_prefix"] = data["bucketPrefix"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "RedshiftConnectorProfileProperties.role_arn required"
        )
    if data.get("dataApiRoleArn") is not None:
        out["data_api_role_arn"] = data["dataApiRoleArn"]
    if data.get("isRedshiftServerless") is not None:
        out["is_redshift_serverless"] = data["isRedshiftServerless"]
    else:
        out["is_redshift_serverless"] = False
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    return out
