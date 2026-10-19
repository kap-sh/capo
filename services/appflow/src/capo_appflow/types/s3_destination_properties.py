"""Generated from Smithy shape ``com.amazonaws.appflow#S3DestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.bucket_name
    import capo_appflow.types.bucket_prefix
    import capo_appflow.types.s3_output_format_config


class S3DestinationProperties(TypedDict, closed=True):
    bucket_name: "capo_appflow.types.bucket_name.BucketName"
    """<p> The Amazon S3 bucket name in which Amazon AppFlow places the transferred data. </p>"""
    bucket_prefix: NotRequired["capo_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the destination bucket in which Amazon AppFlow places the files. </p>"""
    s3_output_format_config: NotRequired[
        "capo_appflow.types.s3_output_format_config.S3OutputFormatConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationProperties) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "s3_output_format_config" in value:
        import capo_appflow.types.s3_output_format_config

        out["s3OutputFormatConfig"] = (
            capo_appflow.types.s3_output_format_config.serialize_json(
                value["s3_output_format_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DestinationProperties:
    out: S3DestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("bucketPrefix") is not None:
        out["bucket_prefix"] = data["bucketPrefix"]
    if data.get("s3OutputFormatConfig") is not None:
        import capo_appflow.types.s3_output_format_config

        out["s3_output_format_config"] = (
            capo_appflow.types.s3_output_format_config.deserialize_json(
                data["s3OutputFormatConfig"]
            )
        )
    return out
