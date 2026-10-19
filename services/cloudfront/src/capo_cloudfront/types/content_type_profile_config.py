"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContentTypeProfileConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.content_type_profiles


class ContentTypeProfileConfig(TypedDict, closed=True):
    forward_when_content_type_is_unknown: "capo_cloudfront.types.boolean.boolean"
    """<p>The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.</p>"""
    content_type_profiles: NotRequired[
        "capo_cloudfront.types.content_type_profiles.ContentTypeProfiles"
    ]
    """<p>The configuration for a field-level encryption content type-profile.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ContentTypeProfileConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ForwardWhenContentTypeIsUnknown").text = (
        "true" if value["forward_when_content_type_is_unknown"] else "false"
    )
    if "content_type_profiles" in value:
        import capo_cloudfront.types.content_type_profiles

        capo_cloudfront.types.content_type_profiles.serialize_xml(
            value["content_type_profiles"], el, "ContentTypeProfiles"
        )


def deserialize_xml(el: Element) -> ContentTypeProfileConfig:
    out: ContentTypeProfileConfig = {}  # type: ignore[typeddict-item]
    child_forward_when_content_type_is_unknown = el.find(
        "ForwardWhenContentTypeIsUnknown"
    )
    if child_forward_when_content_type_is_unknown is not None:
        out["forward_when_content_type_is_unknown"] = (
            child_forward_when_content_type_is_unknown.text or ""
        ).lower() == "true"
    else:
        out["forward_when_content_type_is_unknown"] = False
    child_content_type_profiles = el.find("ContentTypeProfiles")
    if child_content_type_profiles is not None:
        import capo_cloudfront.types.content_type_profiles

        out["content_type_profiles"] = (
            capo_cloudfront.types.content_type_profiles.deserialize_xml(
                child_content_type_profiles
            )
        )
    return out
