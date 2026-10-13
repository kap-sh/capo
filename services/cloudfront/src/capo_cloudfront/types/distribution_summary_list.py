"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_summary

DistributionSummaryList: TypeAlias = list[
    "capo_cloudfront.types.distribution_summary.DistributionSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: DistributionSummaryList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.distribution_summary

        capo_cloudfront.types.distribution_summary.serialize_xml(
            item, el, "DistributionSummary"
        )


def deserialize_xml(el: Element) -> DistributionSummaryList:
    import capo_cloudfront.types.distribution_summary

    out: DistributionSummaryList = []
    for child in el.findall("DistributionSummary"):
        out.append(capo_cloudfront.types.distribution_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: DistributionSummaryList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.distribution_summary

        capo_cloudfront.types.distribution_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DistributionSummaryList:
    import capo_cloudfront.types.distribution_summary

    out: DistributionSummaryList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.distribution_summary.deserialize_xml(child))
    return out


def redact_sensitive(value: DistributionSummaryList) -> list[Any]:
    import capo_cloudfront.types.distribution_summary

    return [
        capo_cloudfront.types.distribution_summary.redact_sensitive(item)
        for item in value
    ]
