"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistributionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution
    import capo_cloudfront.types.string


class CreateDistributionResult(TypedDict, closed=True):
    distribution: NotRequired["capo_cloudfront.types.distribution.Distribution"]
    """<p>The distribution's information.</p>"""
    location: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The fully qualified URI of the new distribution resource just created.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the distribution created.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateDistributionResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "distribution" in value:
        import capo_cloudfront.types.distribution

        capo_cloudfront.types.distribution.serialize_xml(
            value["distribution"], el, "Distribution"
        )


def deserialize_xml(el: Element) -> CreateDistributionResult:
    out: CreateDistributionResult = {}  # type: ignore[typeddict-item]
    child_distribution = el.find("Distribution")
    if child_distribution is not None:
        import capo_cloudfront.types.distribution

        out["distribution"] = capo_cloudfront.types.distribution.deserialize_xml(
            child_distribution
        )
    return out


def redact_sensitive(value: CreateDistributionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distribution" in value:
        import capo_cloudfront.types.distribution

        out["distribution"] = capo_cloudfront.types.distribution.redact_sensitive(
            value["distribution"]
        )
    return out
