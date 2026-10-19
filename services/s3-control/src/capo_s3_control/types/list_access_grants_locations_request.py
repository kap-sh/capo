"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessGrantsLocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.continuation_token
    import capo_s3_control.types.max_results
    import capo_s3_control.types.s3_prefix


class ListAccessGrantsLocationsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants Locations</code> request in order to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access grants that you would like returned in the <code>List Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>"""
    location_scope: NotRequired["capo_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 path to the location that you are registering. The location scope can be the default S3 location <code>s3://</code>, the S3 path to a bucket <code>s3://<bucket></code>, or the S3 path to a bucket and prefix <code>s3://<bucket>/<prefix></code>. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the <code>engineering/</code> prefix or object key names that start with the <code>marketing/campaigns/</code> prefix.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListAccessGrantsLocationsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListAccessGrantsLocationsRequest:
    out: ListAccessGrantsLocationsRequest = {}  # type: ignore[typeddict-item]
    return out
