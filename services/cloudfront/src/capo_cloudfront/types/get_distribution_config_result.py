"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetDistributionConfigResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_config
    import capo_cloudfront.types.string


class GetDistributionConfigResult(TypedDict, closed=True):
    distribution_config: NotRequired[
        "capo_cloudfront.types.distribution_config.DistributionConfig"
    ]
    """<p>The distribution's configuration information.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the configuration. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetDistributionConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "distribution_config" in value:
        import capo_cloudfront.types.distribution_config

        capo_cloudfront.types.distribution_config.serialize_xml(
            value["distribution_config"], el, "DistributionConfig"
        )


def deserialize_xml(el: Element) -> GetDistributionConfigResult:
    out: GetDistributionConfigResult = {}  # type: ignore[typeddict-item]
    child_distribution_config = el.find("DistributionConfig")
    if child_distribution_config is not None:
        import capo_cloudfront.types.distribution_config

        out["distribution_config"] = (
            capo_cloudfront.types.distribution_config.deserialize_xml(
                child_distribution_config
            )
        )
    return out


def redact_sensitive(value: GetDistributionConfigResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distribution_config" in value:
        import capo_cloudfront.types.distribution_config

        out["distribution_config"] = (
            capo_cloudfront.types.distribution_config.redact_sensitive(
                value["distribution_config"]
            )
        )
    return out
