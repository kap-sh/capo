"""Generated from Smithy shape ``com.amazonaws.s3#Delete``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_identifier_list
    import capo_s3.types.quiet


class Delete(TypedDict, closed=True):
    objects: "capo_s3.types.object_identifier_list.ObjectIdentifierList"
    """<p>The object to delete.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, an object that's composed entirely of whitespace characters is not supported by the <code>DeleteObjects</code> API operation. The request will receive a <code>400 Bad Request</code> error and none of the objects in the request will be deleted.</p> </note>"""
    quiet: NotRequired["capo_s3.types.quiet.Quiet"]
    """<p>Element to enable quiet mode for the request. When you add this element, you must set its value to <code>true</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Delete, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.object_identifier_list

    capo_s3.types.object_identifier_list.serialize_xml_flat(
        value["objects"], el, "Object"
    )
    if "quiet" in value:
        SubElement(el, "Quiet").text = "true" if value["quiet"] else "false"


def deserialize_xml(el: Element) -> Delete:
    out: Delete = {}  # type: ignore[typeddict-item]
    if el.find("Object") is not None:
        import capo_s3.types.object_identifier_list

        out["objects"] = capo_s3.types.object_identifier_list.deserialize_xml_flat(
            el, "Object"
        )
    else:
        out["objects"] = []
    child_quiet = el.find("Quiet")
    if child_quiet is not None:
        out["quiet"] = (child_quiet.text or "").lower() == "true"
    return out
