"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControlSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control_origin_types
    import capo_cloudfront.types.origin_access_control_signing_behaviors
    import capo_cloudfront.types.origin_access_control_signing_protocols
    import capo_cloudfront.types.string


class OriginAccessControlSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique identifier of the origin access control.</p>"""
    description: "capo_cloudfront.types.string.string"
    """<p>A description of the origin access control.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A unique name that identifies the origin access control.</p>"""
    signing_protocol: "capo_cloudfront.types.origin_access_control_signing_protocols.OriginAccessControlSigningProtocols"
    """<p>The signing protocol of the origin access control. The signing protocol determines how CloudFront signs (authenticates) requests. The only valid values are <code>sigv4</code> and <code>sigv4a</code>.</p>"""
    signing_behavior: "capo_cloudfront.types.origin_access_control_signing_behaviors.OriginAccessControlSigningBehaviors"
    """<p>A value that specifies which requests CloudFront signs (adds authentication information to). This field can have one of the following values:</p> <ul> <li> <p> <code>never</code> – CloudFront doesn't sign any origin requests.</p> </li> <li> <p> <code>always</code> – CloudFront signs all origin requests, overwriting the <code>Authorization</code> header from the viewer request if necessary.</p> </li> <li> <p> <code>no-override</code> – If the viewer request doesn't contain the <code>Authorization</code> header, CloudFront signs the origin request. If the viewer request contains the <code>Authorization</code> header, CloudFront doesn't sign the origin request, but instead passes along the <code>Authorization</code> header that it received in the viewer request.</p> </li> <li> <p> <code>always-amz-auth</code> – CloudFront signs all origin requests with Amazon authentication headers, and forwards the viewer's <code>Authorization</code> header to the origin if one is present. This value is only valid with Lambda-Web origins.</p> </li> </ul>"""
    origin_access_control_origin_type: "capo_cloudfront.types.origin_access_control_origin_types.OriginAccessControlOriginTypes"
    """<p>The type of origin that this origin access control is for.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginAccessControlSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Description").text = str(value["description"])
    SubElement(el, "Name").text = str(value["name"])
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


def deserialize_xml(el: Element) -> OriginAccessControlSummary:
    out: OriginAccessControlSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("OriginAccessControlSummary.id required")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    else:
        raise DeserializationError("OriginAccessControlSummary.description required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("OriginAccessControlSummary.name required")
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
            "OriginAccessControlSummary.signing_protocol required"
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
            "OriginAccessControlSummary.signing_behavior required"
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
            "OriginAccessControlSummary.origin_access_control_origin_type required"
        )
    return out
