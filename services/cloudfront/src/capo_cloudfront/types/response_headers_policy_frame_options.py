"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyFrameOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.frame_options_list


class ResponseHeadersPolicyFrameOptions(TypedDict, closed=True):
    override: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>X-Frame-Options</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""
    frame_option: "capo_cloudfront.types.frame_options_list.FrameOptionsList"
    """<p>The value of the <code>X-Frame-Options</code> HTTP response header. Valid values are <code>DENY</code> and <code>SAMEORIGIN</code>.</p> <p>For more information about these values, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options">X-Frame-Options</a> in the MDN Web Docs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyFrameOptions, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"
    import capo_cloudfront.types.frame_options_list

    capo_cloudfront.types.frame_options_list.serialize_xml(
        value["frame_option"], el, "FrameOption"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyFrameOptions:
    out: ResponseHeadersPolicyFrameOptions = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyFrameOptions.override required"
        )
    child_frame_option = el.find("FrameOption")
    if child_frame_option is not None:
        import capo_cloudfront.types.frame_options_list

        out["frame_option"] = capo_cloudfront.types.frame_options_list.deserialize_xml(
            child_frame_option
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyFrameOptions.frame_option required"
        )
    return out
