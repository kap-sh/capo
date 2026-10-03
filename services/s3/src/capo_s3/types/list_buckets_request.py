"""Generated from Smithy shape ``com.amazonaws.s3#ListBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_region
    import capo_s3.types.max_buckets
    import capo_s3.types.prefix
    import capo_s3.types.token


class ListBucketsRequest(TypedDict, closed=True):
    max_buckets: NotRequired["capo_s3.types.max_buckets.MaxBuckets"]
    """<p>Maximum number of buckets to be returned in response. When the number is more than the count of buckets that are owned by an Amazon Web Services account, return all the buckets in response.</p>"""
    continuation_token: NotRequired["capo_s3.types.token.Token"]
    """<p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results. </p> <p>Length Constraints: Minimum length of 0. Maximum length of 1024.</p> <p>Required: No.</p> <note> <p>If you specify the <code>bucket-region</code>, <code>prefix</code>, or <code>continuation-token</code> query parameters without using <code>max-buckets</code> to set the maximum number of buckets returned in the response, Amazon S3 applies a default page size of 10,000 and provides a continuation token if there are more buckets.</p> </note>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>Limits the response to bucket names that begin with the specified bucket name prefix.</p>"""
    bucket_region: NotRequired["capo_s3.types.bucket_region.BucketRegion"]
    """<p>Limits the response to buckets that are located in the specified Amazon Web Services Region. The Amazon Web Services Region must be expressed according to the Amazon Web Services Region code, such as <code>us-west-2</code> for the US West (Oregon) Region. For a list of the valid values for all of the Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region">Regions and Endpoints</a>.</p> <note> <p>Requests made to a Regional endpoint that is different from the <code>bucket-region</code> parameter are not supported. For example, if you want to limit the response to your buckets in Region <code>us-west-2</code>, the request must be made to an endpoint in Region <code>us-west-2</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: ListBucketsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListBucketsRequest:
    out: ListBucketsRequest = {}  # type: ignore[typeddict-item]
    return out
