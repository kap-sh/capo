"""Generated from Smithy shape ``com.amazonaws.s3#Bucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_name
    import capo_s3.types.bucket_region
    import capo_s3.types.creation_date
    import capo_s3.types.s3_regional_or_s3_express_bucket_arn_string


class Bucket(TypedDict, closed=True):
    name: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The name of the bucket.</p>"""
    creation_date: NotRequired["capo_s3.types.creation_date.CreationDate"]
    """<p>Date the bucket was created. This date can change when making changes to your bucket, such as editing its bucket policy.</p>"""
    bucket_region: NotRequired["capo_s3.types.bucket_region.BucketRegion"]
    """<p> <code>BucketRegion</code> indicates the Amazon Web Services region where the bucket is located. If the request contains at least one valid parameter, it is included in the response.</p>"""
    bucket_arn: NotRequired[
        "capo_s3.types.s3_regional_or_s3_express_bucket_arn_string.S3RegionalOrS3ExpressBucketArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify Amazon Web Services resources across all of Amazon Web Services.</p> <note> <p>This parameter is only supported for S3 directory buckets. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html">Using tags with directory buckets</a>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: Bucket, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "creation_date" in value:
        import capo_s3.types.creation_date

        capo_s3.types.creation_date.serialize_xml(
            value["creation_date"], el, "CreationDate"
        )
    if "bucket_region" in value:
        SubElement(el, "BucketRegion").text = str(value["bucket_region"])
    if "bucket_arn" in value:
        SubElement(el, "BucketArn").text = str(value["bucket_arn"])


def deserialize_xml(el: Element) -> Bucket:
    out: Bucket = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import capo_s3.types.creation_date

        out["creation_date"] = capo_s3.types.creation_date.deserialize_xml(
            child_creation_date
        )
    child_bucket_region = el.find("BucketRegion")
    if child_bucket_region is not None:
        out["bucket_region"] = str(child_bucket_region.text or "")
    child_bucket_arn = el.find("BucketArn")
    if child_bucket_arn is not None:
        out["bucket_arn"] = str(child_bucket_arn.text or "")
    return out
