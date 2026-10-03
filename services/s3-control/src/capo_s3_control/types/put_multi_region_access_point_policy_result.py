"""Generated from Smithy shape ``com.amazonaws.s3control#PutMultiRegionAccessPointPolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.async_request_token_arn


class PutMultiRegionAccessPointPolicyResult(TypedDict, closed=True):
    request_token_arn: NotRequired[
        "capo_s3_control.types.async_request_token_arn.AsyncRequestTokenARN"
    ]
    """<p>The request token associated with the request. You can use this token with <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html">DescribeMultiRegionAccessPointOperation</a> to determine the status of asynchronous requests.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutMultiRegionAccessPointPolicyResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "request_token_arn" in value:
        SubElement(el, "RequestTokenARN").text = str(value["request_token_arn"])


def deserialize_xml(el: Element) -> PutMultiRegionAccessPointPolicyResult:
    out: PutMultiRegionAccessPointPolicyResult = {}  # type: ignore[typeddict-item]
    child_request_token_arn = el.find("RequestTokenARN")
    if child_request_token_arn is not None:
        out["request_token_arn"] = str(child_request_token_arn.text or "")
    return out
