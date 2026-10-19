"""Generated from Smithy shape ``com.amazonaws.s3control#ListCallerAccessGrantsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.boolean
    import capo_s3_control.types.continuation_token
    import capo_s3_control.types.max_results
    import capo_s3_control.types.s3_prefix


class ListCallerAccessGrantsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    grant_scope: NotRequired["capo_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 path of the data that you would like to access. Must start with <code>s3://</code>. You can optionally pass only the beginning characters of a path, and S3 Access Grants will search for all applicable grants for the path fragment. </p>"""
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Caller Access Grants</code> request in order to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access grants that you would like returned in the <code>List Caller Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>"""
    allowed_by_application: NotRequired["capo_s3_control.types.boolean.Boolean"]
    """<p>If this optional parameter is passed in the request, a filter is applied to the results. The results will include only the access grants for the caller's Identity Center application or for any other applications (<code>ALL</code>).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListCallerAccessGrantsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListCallerAccessGrantsRequest:
    out: ListCallerAccessGrantsRequest = {}  # type: ignore[typeddict-item]
    return out
