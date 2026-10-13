"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistributionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_config


class CreateDistributionRequest(TypedDict, closed=True):
    distribution_config: "capo_cloudfront.types.distribution_config.DistributionConfig"
    """<p>The distribution's configuration information.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateDistributionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.distribution_config

    capo_cloudfront.types.distribution_config.serialize_xml(
        value["distribution_config"], el, "DistributionConfig"
    )


def deserialize_xml(el: Element) -> CreateDistributionRequest:
    out: CreateDistributionRequest = {}  # type: ignore[typeddict-item]
    child_distribution_config = el.find("DistributionConfig")
    if child_distribution_config is not None:
        import capo_cloudfront.types.distribution_config

        out["distribution_config"] = (
            capo_cloudfront.types.distribution_config.deserialize_xml(
                child_distribution_config
            )
        )
    else:
        raise DeserializationError(
            "CreateDistributionRequest.distribution_config required"
        )
    return out


def redact_sensitive(value: CreateDistributionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distribution_config" in value:
        import capo_cloudfront.types.distribution_config

        out["distribution_config"] = (
            capo_cloudfront.types.distribution_config.redact_sensitive(
                value["distribution_config"]
            )
        )
    return out
