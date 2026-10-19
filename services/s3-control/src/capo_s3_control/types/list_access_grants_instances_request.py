"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessGrantsInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.continuation_token
    import capo_s3_control.types.max_results


class ListAccessGrantsInstancesRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants Instances</code> request in order to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access grants that you would like returned in the <code>List Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListAccessGrantsInstancesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListAccessGrantsInstancesRequest:
    out: ListAccessGrantsInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
