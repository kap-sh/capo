"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByWebACLIdResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_list


class ListDistributionsByWebACLIdResult(TypedDict, closed=True):
    distribution_list: NotRequired[
        "capo_cloudfront.types.distribution_list.DistributionList"
    ]
    """<p>The <code>DistributionList</code> type.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByWebACLIdResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_list" in value:
        import capo_cloudfront.types.distribution_list

        capo_cloudfront.types.distribution_list.serialize_xml(
            value["distribution_list"], el, "DistributionList"
        )


def deserialize_xml(el: Element) -> ListDistributionsByWebACLIdResult:
    out: ListDistributionsByWebACLIdResult = {}  # type: ignore[typeddict-item]
    child_distribution_list = el.find("DistributionList")
    if child_distribution_list is not None:
        import capo_cloudfront.types.distribution_list

        out["distribution_list"] = (
            capo_cloudfront.types.distribution_list.deserialize_xml(
                child_distribution_list
            )
        )
    return out


def redact_sensitive(value: ListDistributionsByWebACLIdResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distribution_list" in value:
        import capo_cloudfront.types.distribution_list

        out["distribution_list"] = (
            capo_cloudfront.types.distribution_list.redact_sensitive(
                value["distribution_list"]
            )
        )
    return out
