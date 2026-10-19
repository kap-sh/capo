"""Generated from Smithy shape ``com.amazonaws.cloudfront#StagingDistributionDnsNames``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.staging_distribution_dns_name_list


class StagingDistributionDnsNames(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of CloudFront domain names in your staging distribution.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.staging_distribution_dns_name_list.StagingDistributionDnsNameList"
    ]
    """<p>The CloudFront domain name of the staging distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StagingDistributionDnsNames, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.staging_distribution_dns_name_list

        capo_cloudfront.types.staging_distribution_dns_name_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> StagingDistributionDnsNames:
    out: StagingDistributionDnsNames = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.staging_distribution_dns_name_list

        out["items"] = (
            capo_cloudfront.types.staging_distribution_dns_name_list.deserialize_xml(
                child_items
            )
        )
    return out
