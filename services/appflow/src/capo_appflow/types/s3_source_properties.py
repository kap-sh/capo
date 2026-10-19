"""Generated from Smithy shape ``com.amazonaws.appflow#S3SourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.bucket_name
    import capo_appflow.types.bucket_prefix
    import capo_appflow.types.s3_input_format_config


class S3SourceProperties(TypedDict, closed=True):
    bucket_name: "capo_appflow.types.bucket_name.BucketName"
    """<p> The Amazon S3 bucket name where the source files are stored. </p>"""
    bucket_prefix: NotRequired["capo_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the Amazon S3 bucket in which the source files are stored. </p>"""
    s3_input_format_config: NotRequired[
        "capo_appflow.types.s3_input_format_config.S3InputFormatConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: S3SourceProperties) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "s3_input_format_config" in value:
        import capo_appflow.types.s3_input_format_config

        out["s3InputFormatConfig"] = (
            capo_appflow.types.s3_input_format_config.serialize_json(
                value["s3_input_format_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3SourceProperties:
    out: S3SourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("bucketPrefix") is not None:
        out["bucket_prefix"] = data["bucketPrefix"]
    if data.get("s3InputFormatConfig") is not None:
        import capo_appflow.types.s3_input_format_config

        out["s3_input_format_config"] = (
            capo_appflow.types.s3_input_format_config.deserialize_json(
                data["s3InputFormatConfig"]
            )
        )
    return out
