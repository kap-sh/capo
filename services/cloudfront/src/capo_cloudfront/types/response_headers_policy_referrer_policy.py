"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyReferrerPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.referrer_policy_list


class ResponseHeadersPolicyReferrerPolicy(TypedDict, closed=True):
    override: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>Referrer-Policy</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""
    referrer_policy: "capo_cloudfront.types.referrer_policy_list.ReferrerPolicyList"
    """<p>The value of the <code>Referrer-Policy</code> HTTP response header. Valid values are:</p> <ul> <li> <p> <code>no-referrer</code> </p> </li> <li> <p> <code>no-referrer-when-downgrade</code> </p> </li> <li> <p> <code>origin</code> </p> </li> <li> <p> <code>origin-when-cross-origin</code> </p> </li> <li> <p> <code>same-origin</code> </p> </li> <li> <p> <code>strict-origin</code> </p> </li> <li> <p> <code>strict-origin-when-cross-origin</code> </p> </li> <li> <p> <code>unsafe-url</code> </p> </li> </ul> <p>For more information about these values, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy">Referrer-Policy</a> in the MDN Web Docs.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyReferrerPolicy, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"
    import capo_cloudfront.types.referrer_policy_list

    capo_cloudfront.types.referrer_policy_list.serialize_xml(
        value["referrer_policy"], el, "ReferrerPolicy"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyReferrerPolicy:
    out: ResponseHeadersPolicyReferrerPolicy = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyReferrerPolicy.override required"
        )
    child_referrer_policy = el.find("ReferrerPolicy")
    if child_referrer_policy is not None:
        import capo_cloudfront.types.referrer_policy_list

        out["referrer_policy"] = (
            capo_cloudfront.types.referrer_policy_list.deserialize_xml(
                child_referrer_policy
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicyReferrerPolicy.referrer_policy required"
        )
    return out
