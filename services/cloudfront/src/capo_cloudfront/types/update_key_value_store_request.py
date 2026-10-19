"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateKeyValueStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_value_store_comment
    import capo_cloudfront.types.key_value_store_name
    import capo_cloudfront.types.string


class UpdateKeyValueStoreRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName"
    """<p>The name of the key value store to update.</p>"""
    comment: "capo_cloudfront.types.key_value_store_comment.KeyValueStoreComment"
    """<p>The comment of the key value store to update.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The key value store to update, if a match occurs.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateKeyValueStoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> UpdateKeyValueStoreRequest:
    out: UpdateKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        out["comment"] = ""
    return out
