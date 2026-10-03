"""Generated from Smithy shape ``com.amazonaws.s3control#GetMultiRegionAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.multi_region_access_point_name


class GetMultiRegionAccessPointRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName"
    """<p>The name of the Multi-Region Access Point whose configuration information you want to receive. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming">Rules for naming Amazon S3 Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMultiRegionAccessPointRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetMultiRegionAccessPointRequest:
    out: GetMultiRegionAccessPointRequest = {}  # type: ignore[typeddict-item]
    return out
