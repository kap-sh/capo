"""Generated from Smithy shape ``com.amazonaws.s3#CreateBucketOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.location
    import capo_s3.types.s3_regional_or_s3_express_bucket_arn_string


class CreateBucketOutput(TypedDict, closed=True):
    location: NotRequired["capo_s3.types.location.Location"]
    """<p>A forward slash followed by the name of the bucket for all account regional namespace buckets and all global general purpose buckets created in us-east-1. For example, <code>/amzn-s3-demo-bucket</code>. For global general purpose buckets created in other Amazon Web Services Regions, the Location field is the global endpoint URL. For example, <code>http://amzn-s3-demo-bucket.s3.amazonaws.com/</code>.</p>"""
    bucket_arn: NotRequired[
        "capo_s3.types.s3_regional_or_s3_express_bucket_arn_string.S3RegionalOrS3ExpressBucketArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify Amazon Web Services resources across all of Amazon Web Services.</p> <note> <p>This parameter is only supported for S3 directory buckets. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html">Using tags with directory buckets</a>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateBucketOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> CreateBucketOutput:
    out: CreateBucketOutput = {}  # type: ignore[typeddict-item]
    return out
