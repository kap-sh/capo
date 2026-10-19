"""Generated from Smithy shape ``com.amazonaws.s3control#ListMultiRegionAccessPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.max_results
    import capo_s3_control.types.non_empty_max_length1024_string


class ListMultiRegionAccessPointsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>Not currently used. Do not use this parameter.</p>"""
    max_results: NotRequired["capo_s3_control.types.max_results.MaxResults"]
    """<p>Not currently used. Do not use this parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListMultiRegionAccessPointsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListMultiRegionAccessPointsRequest:
    out: ListMultiRegionAccessPointsRequest = {}  # type: ignore[typeddict-item]
    return out
