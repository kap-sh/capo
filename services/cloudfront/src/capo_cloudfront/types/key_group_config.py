"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyGroupConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.public_key_id_list
    import capo_cloudfront.types.string


class KeyGroupConfig(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>A name to identify the key group.</p>"""
    items: "capo_cloudfront.types.public_key_id_list.PublicKeyIdList"
    """<p>A list of the identifiers of the public keys in the key group.</p>"""
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A comment to describe the key group. The comment cannot be longer than 128 characters.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyGroupConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.public_key_id_list

    capo_cloudfront.types.public_key_id_list.serialize_xml(value["items"], el, "Items")
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> KeyGroupConfig:
    out: KeyGroupConfig = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.public_key_id_list

        out["items"] = capo_cloudfront.types.public_key_id_list.deserialize_xml(
            child_items
        )
    else:
        out["items"] = []
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
