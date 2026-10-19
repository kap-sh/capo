"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsForDirectoryBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.max_results
    import capo_s3_control.types.non_empty_max_length1024_string


class ListAccessPointsForDirectoryBucketsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID that owns the access points.</p>"""
    directory_bucket: NotRequired["capo_s3_control.types.bucket_name.BucketName"]
    """<p>The name of the directory bucket associated with the access points you want to list.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p> If <code>NextToken</code> is returned, there are more access points available than requested in the <code>maxResults</code> value. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access points that you would like returned in the <code>ListAccessPointsForDirectoryBuckets</code> response. If the directory bucket is associated with more than this number of access points, the results include the pagination token <code>NextToken</code>. Make another call using the <code>NextToken</code> to retrieve more results.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListAccessPointsForDirectoryBucketsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListAccessPointsForDirectoryBucketsRequest:
    out: ListAccessPointsForDirectoryBucketsRequest = {}  # type: ignore[typeddict-item]
    return out
