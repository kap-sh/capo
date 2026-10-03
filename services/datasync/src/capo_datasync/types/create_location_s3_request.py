"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationS3Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.s3_bucket_arn
    import capo_datasync.types.s3_config
    import capo_datasync.types.s3_storage_class
    import capo_datasync.types.s3_subdirectory


class CreateLocationS3Request(TypedDict, closed=True):
    subdirectory: NotRequired["capo_datasync.types.s3_subdirectory.S3Subdirectory"]
    """<p>Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).</p> <note> <p>DataSync can't transfer objects with a prefix that begins with a slash (<code>/</code>) or includes <code>//</code>, <code>/./</code>, or <code>/../</code> patterns. For example:</p> <ul> <li> <p> <code>/photos</code> </p> </li> <li> <p> <code>photos//2006/January</code> </p> </li> <li> <p> <code>photos/./2006/February</code> </p> </li> <li> <p> <code>photos/../2006/March</code> </p> </li> </ul> </note>"""
    s3_bucket_arn: "capo_datasync.types.s3_bucket_arn.S3BucketArn"
    """<p>Specifies the ARN of the S3 bucket that you want to use as a location. (When creating your DataSync task later, you specify whether this location is a transfer source or destination.) </p> <p>If your S3 bucket is located on an Outposts resource, you must specify an Amazon S3 access point. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">Managing data access with Amazon S3 access points</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    s3_storage_class: NotRequired["capo_datasync.types.s3_storage_class.S3StorageClass"]
    """<p>Specifies the storage class that you want your objects to use when Amazon S3 is a transfer destination.</p> <p>For buckets in Amazon Web Services Regions, the storage class defaults to <code>STANDARD</code>. For buckets on Outposts, the storage class defaults to <code>OUTPOSTS</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 transfers</a>.</p>"""
    s3_config: "capo_datasync.types.s3_config.S3Config"
    agent_arns: NotRequired["capo_datasync.types.agent_arn_list.AgentArnList"]
    """<p>(Amazon S3 on Outposts only) Specifies the Amazon Resource Name (ARN) of the DataSync agent on your Outpost.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html#outposts-agent">Deploy your DataSync agent on Outposts</a>.</p>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your transfer location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationS3Request) -> dict:
    out: dict = {}
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    out["S3BucketArn"] = value["s3_bucket_arn"]
    if "s3_storage_class" in value:
        import capo_datasync.types.s3_storage_class

        out["S3StorageClass"] = (
            capo_datasync.types.s3_storage_class.serialize_aws_json_1_1(
                value["s3_storage_class"]
            )
        )
    import capo_datasync.types.s3_config

    out["S3Config"] = capo_datasync.types.s3_config.serialize_aws_json_1_1(
        value["s3_config"]
    )
    if "agent_arns" in value:
        import capo_datasync.types.agent_arn_list

        out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
            value["agent_arns"]
        )
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationS3Request:
    out: CreateLocationS3Request = {}  # type: ignore[typeddict-item]
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("S3BucketArn") is not None:
        out["s3_bucket_arn"] = data["S3BucketArn"]
    else:
        raise DeserializationError("CreateLocationS3Request.s3_bucket_arn required")
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
    else:
        raise DeserializationError("CreateLocationS3Request.s3_config required")
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
