"""Generated from Smithy shape ``com.amazonaws.s3#Grantee``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.display_name
    import capo_s3.types.email_address
    import capo_s3.types.id
    import capo_s3.types.type
    import capo_s3.types.uri


class Grantee(TypedDict, closed=True):
    display_name: NotRequired["capo_s3.types.display_name.DisplayName"]
    """<p></p>"""
    email_address: NotRequired["capo_s3.types.email_address.EmailAddress"]
    """<p></p>"""
    id: NotRequired["capo_s3.types.id.ID"]
    """<p>The canonical user ID of the grantee.</p>"""
    uri: NotRequired["capo_s3.types.uri.URI"]
    """<p>URI of the grantee group.</p>"""
    type: "capo_s3.types.type.Type"
    """<p>Type of grantee</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Grantee, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "display_name" in value:
        SubElement(el, "DisplayName").text = str(value["display_name"])
    if "email_address" in value:
        SubElement(el, "EmailAddress").text = str(value["email_address"])
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])
    if "uri" in value:
        SubElement(el, "URI").text = str(value["uri"])
    import capo_s3.types.type

    el.set("xsi:type", capo_s3.types.type.to_xml_text(value["type"]))


def deserialize_xml(el: Element) -> Grantee:
    out: Grantee = {}  # type: ignore[typeddict-item]
    child_display_name = el.find("DisplayName")
    if child_display_name is not None:
        out["display_name"] = str(child_display_name.text or "")
    child_email_address = el.find("EmailAddress")
    if child_email_address is not None:
        out["email_address"] = str(child_email_address.text or "")
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_uri = el.find("URI")
    if child_uri is not None:
        out["uri"] = str(child_uri.text or "")
    attr_type = el.get("type")
    if attr_type is not None:
        import capo_s3.types.type

        out["type"] = capo_s3.types.type.from_xml_text(attr_type)
    else:
        import typing

        out["type"] = typing.cast("capo_s3.types.type.Type", "")
    return out
