"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsForObjectLambdaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.max_results
    import capo_s3_control.types.non_empty_max_length1024_string


class ListAccessPointsForObjectLambdaRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified Object Lambda Access Point.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>If the list has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>The maximum number of access points that you want to include in the list. The response may contain fewer access points but will never contain more. If there are more than this number of access points, then the response will include a continuation token in the <code>NextToken</code> field that you can use to retrieve the next page of access points.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListAccessPointsForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListAccessPointsForObjectLambdaRequest:
    out: ListAccessPointsForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
    return out
