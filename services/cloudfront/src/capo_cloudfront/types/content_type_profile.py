"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContentTypeProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.format
    import capo_cloudfront.types.string


class ContentTypeProfile(TypedDict, closed=True):
    format: "capo_cloudfront.types.format.Format"
    """<p>The format for a field-level encryption content type-profile mapping.</p>"""
    profile_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The profile ID for a field-level encryption content type-profile mapping.</p>"""
    content_type: "capo_cloudfront.types.string.string"
    """<p>The content type for a field-level encryption content type-profile mapping.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ContentTypeProfile, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.format

    capo_cloudfront.types.format.serialize_xml(value["format"], el, "Format")
    if "profile_id" in value:
        SubElement(el, "ProfileId").text = str(value["profile_id"])
    SubElement(el, "ContentType").text = str(value["content_type"])


def deserialize_xml(el: Element) -> ContentTypeProfile:
    out: ContentTypeProfile = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import capo_cloudfront.types.format

        out["format"] = capo_cloudfront.types.format.deserialize_xml(child_format)
    else:
        import typing

        out["format"] = typing.cast("capo_cloudfront.types.format.Format", "")
    child_profile_id = el.find("ProfileId")
    if child_profile_id is not None:
        out["profile_id"] = str(child_profile_id.text or "")
    child_content_type = el.find("ContentType")
    if child_content_type is not None:
        out["content_type"] = str(child_content_type.text or "")
    else:
        out["content_type"] = ""
    return out
