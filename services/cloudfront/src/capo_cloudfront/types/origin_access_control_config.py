"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control_origin_types
    import capo_cloudfront.types.origin_access_control_signing_behaviors
    import capo_cloudfront.types.origin_access_control_signing_protocols
    import capo_cloudfront.types.string


class OriginAccessControlConfig(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>A name to identify the origin access control. You can specify up to 64 characters.</p>"""
    description: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A description of the origin access control.</p>"""
    signing_protocol: "capo_cloudfront.types.origin_access_control_signing_protocols.OriginAccessControlSigningProtocols"
    """<p>The signing protocol of the origin access control, which determines how CloudFront signs (authenticates) requests. The only valid values are <code>sigv4</code> and <code>sigv4a</code>.</p>"""
    signing_behavior: "capo_cloudfront.types.origin_access_control_signing_behaviors.OriginAccessControlSigningBehaviors"
    """<p>Specifies which requests CloudFront signs (adds authentication information to). Specify <code>always</code> for the most common use case. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#oac-advanced-settings">origin access control advanced settings</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>This field can have one of the following values:</p> <ul> <li> <p> <code>always</code> – CloudFront signs all origin requests, overwriting the <code>Authorization</code> header from the viewer request if one exists.</p> </li> <li> <p> <code>never</code> – CloudFront doesn't sign any origin requests. This value turns off origin access control for all origins in all distributions that use this origin access control.</p> </li> <li> <p> <code>no-override</code> – If the viewer request doesn't contain the <code>Authorization</code> header, then CloudFront signs the origin request. If the viewer request contains the <code>Authorization</code> header, then CloudFront doesn't sign the origin request and instead passes along the <code>Authorization</code> header from the viewer request. <b>WARNING: To pass along the <code>Authorization</code> header from the viewer request, you <i>must</i> add the <code>Authorization</code> header to a <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html">cache policy</a> for all cache behaviors that use origins associated with this origin access control.</b> </p> </li> <li> <p> <code>always-amz-auth</code> – CloudFront signs all origin requests with Amazon authentication headers. If the viewer request contains the <code>Authorization</code> header, then CloudFront also forwards that header to the origin. This value is only valid with Lambda-Web origins. <b>WARNING: To forward the <code>Authorization</code> header from the viewer request, you <i>must</i> add the <code>Authorization</code> header to a <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html">cache policy</a> for all cache behaviors that use origins associated with this origin access control.</b> </p> </li> </ul>"""
    origin_access_control_origin_type: "capo_cloudfront.types.origin_access_control_origin_types.OriginAccessControlOriginTypes"
    """<p>The type of origin that this origin access control is for.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginAccessControlConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    if "description" in value:
        SubElement(el, "Description").text = str(value["description"])
    import capo_cloudfront.types.origin_access_control_signing_protocols

    capo_cloudfront.types.origin_access_control_signing_protocols.serialize_xml(
        value["signing_protocol"], el, "SigningProtocol"
    )
    import capo_cloudfront.types.origin_access_control_signing_behaviors

    capo_cloudfront.types.origin_access_control_signing_behaviors.serialize_xml(
        value["signing_behavior"], el, "SigningBehavior"
    )
    import capo_cloudfront.types.origin_access_control_origin_types

    capo_cloudfront.types.origin_access_control_origin_types.serialize_xml(
        value["origin_access_control_origin_type"], el, "OriginAccessControlOriginType"
    )


def deserialize_xml(el: Element) -> OriginAccessControlConfig:
    out: OriginAccessControlConfig = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("OriginAccessControlConfig.name required")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_signing_protocol = el.find("SigningProtocol")
    if child_signing_protocol is not None:
        import capo_cloudfront.types.origin_access_control_signing_protocols

        out["signing_protocol"] = (
            capo_cloudfront.types.origin_access_control_signing_protocols.deserialize_xml(
                child_signing_protocol
            )
        )
    else:
        raise DeserializationError(
            "OriginAccessControlConfig.signing_protocol required"
        )
    child_signing_behavior = el.find("SigningBehavior")
    if child_signing_behavior is not None:
        import capo_cloudfront.types.origin_access_control_signing_behaviors

        out["signing_behavior"] = (
            capo_cloudfront.types.origin_access_control_signing_behaviors.deserialize_xml(
                child_signing_behavior
            )
        )
    else:
        raise DeserializationError(
            "OriginAccessControlConfig.signing_behavior required"
        )
    child_origin_access_control_origin_type = el.find("OriginAccessControlOriginType")
    if child_origin_access_control_origin_type is not None:
        import capo_cloudfront.types.origin_access_control_origin_types

        out["origin_access_control_origin_type"] = (
            capo_cloudfront.types.origin_access_control_origin_types.deserialize_xml(
                child_origin_access_control_origin_type
            )
        )
    else:
        raise DeserializationError(
            "OriginAccessControlConfig.origin_access_control_origin_type required"
        )
    return out
