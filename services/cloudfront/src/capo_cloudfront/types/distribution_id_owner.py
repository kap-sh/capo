"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionIdOwner``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DistributionIdOwner(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the distribution.</p>"""
    owner_account_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the Amazon Web Services account that owns the distribution. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionIdOwner, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "DistributionId").text = str(value["distribution_id"])
    SubElement(el, "OwnerAccountId").text = str(value["owner_account_id"])


def deserialize_xml(el: Element) -> DistributionIdOwner:
    out: DistributionIdOwner = {}  # type: ignore[typeddict-item]
    child_distribution_id = el.find("DistributionId")
    if child_distribution_id is not None:
        out["distribution_id"] = str(child_distribution_id.text or "")
    else:
        out["distribution_id"] = ""
    child_owner_account_id = el.find("OwnerAccountId")
    if child_owner_account_id is not None:
        out["owner_account_id"] = str(child_owner_account_id.text or "")
    else:
        out["owner_account_id"] = ""
    return out
