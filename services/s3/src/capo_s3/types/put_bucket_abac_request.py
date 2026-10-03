"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketAbacRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.abac_status
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5


class PutBucketAbacRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the general purpose bucket.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The MD5 hash of the <code>PutBucketAbac</code> request body. </p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the general purpose bucket's owner. </p>"""
    abac_status: "capo_s3.types.abac_status.AbacStatus"
    """<p>The ABAC status of the general purpose bucket. When ABAC is enabled for the general purpose bucket, you can use tags to manage access to the general purpose buckets as well as for cost tracking purposes. When ABAC is disabled for the general purpose buckets, you can only use tags for cost tracking purposes. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html">Using tags with S3 general purpose buckets</a>. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketAbacRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.abac_status

    capo_s3.types.abac_status.serialize_xml(value["abac_status"], el, "AbacStatus")


def deserialize_xml(el: Element) -> PutBucketAbacRequest:
    out: PutBucketAbacRequest = {}  # type: ignore[typeddict-item]
    child_abac_status = el.find("AbacStatus")
    if child_abac_status is not None:
        import capo_s3.types.abac_status

        out["abac_status"] = capo_s3.types.abac_status.deserialize_xml(
            child_abac_status
        )
    else:
        raise DeserializationError("PutBucketAbacRequest.abac_status required")
    return out
