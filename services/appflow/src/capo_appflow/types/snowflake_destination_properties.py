"""Generated from Smithy shape ``com.amazonaws.appflow#SnowflakeDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.bucket_name
    import capo_appflow.types.bucket_prefix
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.object


class SnowflakeDestinationProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Snowflake flow destination. </p>"""
    intermediate_bucket_name: "capo_appflow.types.bucket_name.BucketName"
    """<p> The intermediate bucket that Amazon AppFlow uses when moving data into Snowflake. </p>"""
    bucket_prefix: NotRequired["capo_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the destination bucket in which Amazon AppFlow places the files. </p>"""
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    """<p> The settings that determine how Amazon AppFlow handles an error when placing data in the Snowflake destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. <code>ErrorHandlingConfig</code> is a part of the destination connector details. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    out["intermediateBucketName"] = value["intermediate_bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "error_handling_config" in value:
        import capo_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            capo_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnowflakeDestinationProperties:
    out: SnowflakeDestinationProperties = {}  # type: ignore[typeddict-item]
    if data.get("object") is not None:
        out["object"] = data["object"]
    else:
        out["object"] = ""
    if data.get("intermediateBucketName") is not None:
        out["intermediate_bucket_name"] = data["intermediateBucketName"]
    else:
        out["intermediate_bucket_name"] = ""
    if data.get("bucketPrefix") is not None:
        out["bucket_prefix"] = data["bucketPrefix"]
    if data.get("errorHandlingConfig") is not None:
        import capo_appflow.types.error_handling_config

        out["error_handling_config"] = (
            capo_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    return out
