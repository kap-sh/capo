"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateMlflowTrackingServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.account_id
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.mlflow_version
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.tracking_server_name
    import capo_sagemaker.types.tracking_server_size
    import capo_sagemaker.types.weekly_maintenance_window_start


class CreateMlflowTrackingServerRequest(TypedDict, closed=True):
    tracking_server_name: NotRequired[
        "capo_sagemaker.types.tracking_server_name.TrackingServerName"
    ]
    """<p>A unique string identifying the tracking server name. This string is part of the tracking server ARN.</p>"""
    artifact_store_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI for a general purpose bucket to use as the MLflow Tracking Server artifact store.</p>"""
    tracking_server_size: NotRequired[
        "capo_sagemaker.types.tracking_server_size.TrackingServerSize"
    ]
    """<p>The size of the tracking server you want to create. You can choose between <code>"Small"</code>, <code>"Medium"</code>, and <code>"Large"</code>. The default MLflow Tracking Server configuration size is <code>"Small"</code>. You can choose a size depending on the projected use of the tracking server such as the volume of data logged, number of users, and frequency of use. </p> <p>We recommend using a small tracking server for teams of up to 25 users, a medium tracking server for teams of up to 50 users, and a large tracking server for teams of up to 100 users. </p>"""
    mlflow_version: NotRequired["capo_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>The version of MLflow that the tracking server uses. To see which MLflow versions are available to use, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html#mlflow-create-tracking-server-how-it-works">How it works</a>.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) for an IAM role in your account that the MLflow Tracking Server uses to access the artifact store in Amazon S3. The role should have <code>AmazonS3FullAccess</code> permissions. For more information on IAM permissions for tracking server creation, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server-iam.html">Set up IAM permissions for MLflow</a>.</p>"""
    automatic_model_registration: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Whether to enable or disable automatic registration of new MLflow models to the SageMaker Model Registry. To enable automatic model registration, set this value to <code>True</code>. To disable automatic model registration, set this value to <code>False</code>. If not specified, <code>AutomaticModelRegistration</code> defaults to <code>False</code>.</p>"""
    weekly_maintenance_window_start: NotRequired[
        "capo_sagemaker.types.weekly_maintenance_window_start.WeeklyMaintenanceWindowStart"
    ]
    """<p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: TUE:03:30.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags consisting of key-value pairs used to manage metadata for the tracking server.</p>"""
    s3_bucket_owner_account_id: NotRequired["capo_sagemaker.types.account_id.AccountId"]
    """<p>Expected Amazon Web Services account ID that owns the Amazon S3 bucket for artifact storage. Defaults to caller's account ID if not provided.</p>"""
    s3_bucket_owner_verification: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Enable Amazon S3 Ownership checks when interacting with Amazon S3 buckets from a SageMaker Managed MLflow Tracking Server. Defaults to <code>True</code> if not provided. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMlflowTrackingServerRequest) -> dict:
    out: dict = {}
    if "tracking_server_name" in value:
        out["TrackingServerName"] = value["tracking_server_name"]
    if "artifact_store_uri" in value:
        out["ArtifactStoreUri"] = value["artifact_store_uri"]
    if "tracking_server_size" in value:
        import capo_sagemaker.types.tracking_server_size

        out["TrackingServerSize"] = (
            capo_sagemaker.types.tracking_server_size.serialize_aws_json_1_1(
                value["tracking_server_size"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "automatic_model_registration" in value:
        out["AutomaticModelRegistration"] = value["automatic_model_registration"]
    if "weekly_maintenance_window_start" in value:
        out["WeeklyMaintenanceWindowStart"] = value["weekly_maintenance_window_start"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "s3_bucket_owner_account_id" in value:
        out["S3BucketOwnerAccountId"] = value["s3_bucket_owner_account_id"]
    if "s3_bucket_owner_verification" in value:
        out["S3BucketOwnerVerification"] = value["s3_bucket_owner_verification"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMlflowTrackingServerRequest:
    out: CreateMlflowTrackingServerRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrackingServerName") is not None:
        out["tracking_server_name"] = data["TrackingServerName"]
    if data.get("ArtifactStoreUri") is not None:
        out["artifact_store_uri"] = data["ArtifactStoreUri"]
    if data.get("TrackingServerSize") is not None:
        import capo_sagemaker.types.tracking_server_size

        out["tracking_server_size"] = (
            capo_sagemaker.types.tracking_server_size.deserialize_aws_json_1_1(
                data["TrackingServerSize"]
            )
        )
    if data.get("MlflowVersion") is not None:
        out["mlflow_version"] = data["MlflowVersion"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("AutomaticModelRegistration") is not None:
        out["automatic_model_registration"] = data["AutomaticModelRegistration"]
    if data.get("WeeklyMaintenanceWindowStart") is not None:
        out["weekly_maintenance_window_start"] = data["WeeklyMaintenanceWindowStart"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("S3BucketOwnerAccountId") is not None:
        out["s3_bucket_owner_account_id"] = data["S3BucketOwnerAccountId"]
    if data.get("S3BucketOwnerVerification") is not None:
        out["s3_bucket_owner_verification"] = data["S3BucketOwnerVerification"]
    return out
