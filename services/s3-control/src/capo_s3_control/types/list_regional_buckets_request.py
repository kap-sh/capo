"""Generated from Smithy shape ``com.amazonaws.s3control#ListRegionalBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.max_results
    import capo_s3_control.types.non_empty_max_length64_string
    import capo_s3_control.types.non_empty_max_length1024_string


class ListRegionalBucketsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Outposts bucket.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p></p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p></p>"""
    outpost_id: NotRequired[
        "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
    ]
    """<p>The ID of the Outposts resource.</p> <note> <p>This ID is required by Amazon S3 on Outposts buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: ListRegionalBucketsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListRegionalBucketsRequest:
    out: ListRegionalBucketsRequest = {}  # type: ignore[typeddict-item]
    return out
