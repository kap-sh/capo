"""Generated from Smithy shape ``com.amazonaws.cloudfront#WebAclCustomization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.customization_action_type
    import capo_cloudfront.types.string


class WebAclCustomization(TypedDict, closed=True):
    action: "capo_cloudfront.types.customization_action_type.CustomizationActionType"
    """<p>The action for the WAF web ACL customization. You can specify <code>override</code> to specify a separate WAF web ACL for the distribution tenant. If you specify <code>disable</code>, the distribution tenant won't have WAF web ACL protections and won't inherit from the multi-tenant distribution.</p>"""
    arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the WAF web ACL.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: WebAclCustomization, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.customization_action_type

    capo_cloudfront.types.customization_action_type.serialize_xml(
        value["action"], el, "Action"
    )
    if "arn" in value:
        SubElement(el, "Arn").text = str(value["arn"])


def deserialize_xml(el: Element) -> WebAclCustomization:
    out: WebAclCustomization = {}  # type: ignore[typeddict-item]
    child_action = el.find("Action")
    if child_action is not None:
        import capo_cloudfront.types.customization_action_type

        out["action"] = capo_cloudfront.types.customization_action_type.deserialize_xml(
            child_action
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_cloudfront.types.customization_action_type.CustomizationActionType",
            "",
        )
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
