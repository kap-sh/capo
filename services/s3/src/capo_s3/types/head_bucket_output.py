"""Generated from Smithy shape ``com.amazonaws.s3#HeadBucketOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.access_point_alias
    import capo_s3.types.bucket_location_name
    import capo_s3.types.location_type
    import capo_s3.types.region
    import capo_s3.types.s3_regional_or_s3_express_bucket_arn_string


class HeadBucketOutput(TypedDict, closed=True):
    bucket_arn: NotRequired[
        "capo_s3.types.s3_regional_or_s3_express_bucket_arn_string.S3RegionalOrS3ExpressBucketArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify Amazon Web Services resources across all of Amazon Web Services.</p> <note> <p>This parameter is only supported for S3 directory buckets. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html">Using tags with directory buckets</a>.</p> </note>"""
    bucket_location_type: NotRequired["capo_s3.types.location_type.LocationType"]
    """<p>The type of location where the bucket is created.</p> <note> <p>This functionality is only supported by directory buckets.</p> </note>"""
    bucket_location_name: NotRequired[
        "capo_s3.types.bucket_location_name.BucketLocationName"
    ]
    """<p>The name of the location where the bucket will be created.</p> <p>For directory buckets, the Zone ID of the Availability Zone or the Local Zone where the bucket is created. An example Zone ID value for an Availability Zone is <code>usw2-az1</code>.</p> <note> <p>This functionality is only supported by directory buckets.</p> </note>"""
    bucket_region: NotRequired["capo_s3.types.region.Region"]
    """<p>The Region that the bucket is located.</p>"""
    access_point_alias: NotRequired["capo_s3.types.access_point_alias.AccessPointAlias"]
    """<p>Indicates whether the bucket name used in the request is an access point alias.</p> <note> <p>For directory buckets, the value of this field is <code>false</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: HeadBucketOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> HeadBucketOutput:
    out: HeadBucketOutput = {}  # type: ignore[typeddict-item]
    return out
