"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainConflict``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_resource_type
    import capo_cloudfront.types.string


class DomainConflict(TypedDict, closed=True):
    domain: "capo_cloudfront.types.string.string"
    """<p>The domain used to find existing conflicts for domain configurations.</p>"""
    resource_type: (
        "capo_cloudfront.types.distribution_resource_type.DistributionResourceType"
    )
    """<p>The CloudFront resource type that has a domain conflict.</p>"""
    resource_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the resource that has a domain conflict.</p>"""
    account_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the Amazon Web Services account for the domain conflict.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DomainConflict, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    import capo_cloudfront.types.distribution_resource_type

    capo_cloudfront.types.distribution_resource_type.serialize_xml(
        value["resource_type"], el, "ResourceType"
    )
    SubElement(el, "ResourceId").text = str(value["resource_id"])
    SubElement(el, "AccountId").text = str(value["account_id"])


def deserialize_xml(el: Element) -> DomainConflict:
    out: DomainConflict = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_cloudfront.types.distribution_resource_type

        out["resource_type"] = (
            capo_cloudfront.types.distribution_resource_type.deserialize_xml(
                child_resource_type
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_cloudfront.types.distribution_resource_type.DistributionResourceType",
            "",
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    else:
        out["resource_id"] = ""
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    else:
        out["account_id"] = ""
    return out
