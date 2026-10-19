"""Generated from Smithy shape ``com.amazonaws.codebuild#S3LogsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.bucket_owner_access
    import capo_codebuild.types.logs_config_status_type
    import capo_codebuild.types.string
    import capo_codebuild.types.wrapper_boolean


class S3LogsConfig(TypedDict, closed=True):
    status: "capo_codebuild.types.logs_config_status_type.LogsConfigStatusType"
    """<p>The current status of the S3 build logs. Valid values are:</p> <ul> <li> <p> <code>ENABLED</code>: S3 build logs are enabled for this build project.</p> </li> <li> <p> <code>DISABLED</code>: S3 build logs are not enabled for this build project.</p> </li> </ul>"""
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p> The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is <code>my-bucket</code>, and your path prefix is <code>build-log</code>, then acceptable formats are <code>my-bucket/build-log</code> or <code>arn:aws:s3:::my-bucket/build-log</code>. </p>"""
    encryption_disabled: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted. </p>"""
    bucket_owner_access: NotRequired[
        "capo_codebuild.types.bucket_owner_access.BucketOwnerAccess"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3LogsConfig) -> dict:
    out: dict = {}
    import capo_codebuild.types.logs_config_status_type

    out["status"] = capo_codebuild.types.logs_config_status_type.serialize_aws_json_1_1(
        value["status"]
    )
    if "location" in value:
        out["location"] = value["location"]
    if "encryption_disabled" in value:
        out["encryptionDisabled"] = value["encryption_disabled"]
    if "bucket_owner_access" in value:
        import capo_codebuild.types.bucket_owner_access

        out["bucketOwnerAccess"] = (
            capo_codebuild.types.bucket_owner_access.serialize_aws_json_1_1(
                value["bucket_owner_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3LogsConfig:
    out: S3LogsConfig = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codebuild.types.logs_config_status_type

        out["status"] = (
            capo_codebuild.types.logs_config_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_codebuild.types.logs_config_status_type.LogsConfigStatusType", ""
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("encryptionDisabled") is not None:
        out["encryption_disabled"] = data["encryptionDisabled"]
    if data.get("bucketOwnerAccess") is not None:
        import capo_codebuild.types.bucket_owner_access

        out["bucket_owner_access"] = (
            capo_codebuild.types.bucket_owner_access.deserialize_aws_json_1_1(
                data["bucketOwnerAccess"]
            )
        )
    return out
