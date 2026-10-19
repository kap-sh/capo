"""Generated from Smithy shape ``com.amazonaws.route53#ChangeBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.changes
    import capo_route_53.types.resource_description


class ChangeBatch(TypedDict, closed=True):
    comment: NotRequired["capo_route_53.types.resource_description.ResourceDescription"]
    """<p> <i>Optional:</i> Any comments you want to include about a change batch request.</p>"""
    changes: "capo_route_53.types.changes.Changes"
    """<p>Information about the changes to make to the record sets.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ChangeBatch, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    import capo_route_53.types.changes

    capo_route_53.types.changes.serialize_xml(value["changes"], el, "Changes")


def deserialize_xml(el: Element) -> ChangeBatch:
    out: ChangeBatch = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_changes = el.find("Changes")
    if child_changes is not None:
        import capo_route_53.types.changes

        out["changes"] = capo_route_53.types.changes.deserialize_xml(child_changes)
    else:
        out["changes"] = []
    return out
