"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationS3Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.location_arn
    import capo_datasync.types.s3_config
    import capo_datasync.types.s3_storage_class
    import capo_datasync.types.s3_subdirectory


class UpdateLocationS3Request(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the Amazon S3 transfer location that you're updating.</p>"""
    subdirectory: NotRequired["capo_datasync.types.s3_subdirectory.S3Subdirectory"]
    """<p>Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).</p> <note> <p>DataSync can't transfer objects with a prefix that begins with a slash (<code>/</code>) or includes <code>//</code>, <code>/./</code>, or <code>/../</code> patterns. For example:</p> <ul> <li> <p> <code>/photos</code> </p> </li> <li> <p> <code>photos//2006/January</code> </p> </li> <li> <p> <code>photos/./2006/February</code> </p> </li> <li> <p> <code>photos/../2006/March</code> </p> </li> </ul> </note>"""
    s3_storage_class: NotRequired["capo_datasync.types.s3_storage_class.S3StorageClass"]
    """<p>Specifies the storage class that you want your objects to use when Amazon S3 is a transfer destination.</p> <p>For buckets in Amazon Web Services Regions, the storage class defaults to <code>STANDARD</code>. For buckets on Outposts, the storage class defaults to <code>OUTPOSTS</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 transfers</a>.</p>"""
    s3_config: NotRequired["capo_datasync.types.s3_config.S3Config"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationS3Request) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "s3_storage_class" in value:
        import capo_datasync.types.s3_storage_class

        out["S3StorageClass"] = (
            capo_datasync.types.s3_storage_class.serialize_aws_json_1_1(
                value["s3_storage_class"]
            )
        )
    if "s3_config" in value:
        import capo_datasync.types.s3_config

        out["S3Config"] = capo_datasync.types.s3_config.serialize_aws_json_1_1(
            value["s3_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationS3Request:
    out: UpdateLocationS3Request = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError("UpdateLocationS3Request.location_arn required")
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("S3StorageClass") is not None:
        import capo_datasync.types.s3_storage_class

        out["s3_storage_class"] = (
            capo_datasync.types.s3_storage_class.deserialize_aws_json_1_1(
                data["S3StorageClass"]
            )
        )
    if data.get("S3Config") is not None:
        import capo_datasync.types.s3_config

        out["s3_config"] = capo_datasync.types.s3_config.deserialize_aws_json_1_1(
            data["S3Config"]
        )
    return out
