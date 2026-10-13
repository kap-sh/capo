"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateDistributionWithTagsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.distribution_config_with_tags


class CreateDistributionWithTagsRequest(TypedDict, closed=True):
    distribution_config_with_tags: (
        "capo_cloudfront.types.distribution_config_with_tags.DistributionConfigWithTags"
    )
    """<p>The distribution's configuration information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateDistributionWithTagsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.distribution_config_with_tags

    capo_cloudfront.types.distribution_config_with_tags.serialize_xml(
        value["distribution_config_with_tags"], el, "DistributionConfigWithTags"
    )


def deserialize_xml(el: Element) -> CreateDistributionWithTagsRequest:
    out: CreateDistributionWithTagsRequest = {}  # type: ignore[typeddict-item]
    child_distribution_config_with_tags = el.find("DistributionConfigWithTags")
    if child_distribution_config_with_tags is not None:
        import capo_cloudfront.types.distribution_config_with_tags

        out["distribution_config_with_tags"] = (
            capo_cloudfront.types.distribution_config_with_tags.deserialize_xml(
                child_distribution_config_with_tags
            )
        )
    else:
        raise DeserializationError(
            "CreateDistributionWithTagsRequest.distribution_config_with_tags required"
        )
    return out


def redact_sensitive(value: CreateDistributionWithTagsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distribution_config_with_tags" in value:
        import capo_cloudfront.types.distribution_config_with_tags

        out["distribution_config_with_tags"] = (
            capo_cloudfront.types.distribution_config_with_tags.redact_sensitive(
                value["distribution_config_with_tags"]
            )
        )
    return out
