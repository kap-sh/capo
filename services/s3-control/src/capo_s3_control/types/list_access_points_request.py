"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.data_source_id
    import capo_s3_control.types.data_source_type
    import capo_s3_control.types.max_results
    import capo_s3_control.types.non_empty_max_length1024_string


class ListAccessPointsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the account that owns the specified access points.</p>"""
    bucket: NotRequired["capo_s3_control.types.bucket_name.BucketName"]
    """<p>The name of the bucket whose associated access points you want to list.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>"""
    next_token: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>A continuation token. If a previous call to <code>ListAccessPoints</code> returned a continuation token in the <code>NextToken</code> field, then providing that value here causes Amazon S3 to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access points that you want to include in the list. If the specified bucket has more than this number of access points, then the response will include a continuation token in the <code>NextToken</code> field that you can use to retrieve the next page of access points.</p>"""
    data_source_id: NotRequired["capo_s3_control.types.data_source_id.DataSourceId"]
    """<p>The unique identifier for the data source of the access point.</p>"""
    data_source_type: NotRequired[
        "capo_s3_control.types.data_source_type.DataSourceType"
    ]
    """<p>The type of the data source that the access point is attached to. Returns only access points attached to S3 buckets by default. To return all access points specify <code>DataSourceType</code> as <code>ALL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListAccessPointsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListAccessPointsRequest:
    out: ListAccessPointsRequest = {}  # type: ignore[typeddict-item]
    return out
