"""Generated from Smithy shape ``com.amazonaws.route53#ChangeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.change_status
    import capo_route_53.types.resource_description
    import capo_route_53.types.resource_id
    import capo_route_53.types.time_stamp


class ChangeInfo(TypedDict, closed=True):
    id: "capo_route_53.types.resource_id.ResourceId"
    """<p>This element contains an ID that you use when performing a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html">GetChange</a> action to get detailed information about the change.</p>"""
    status: "capo_route_53.types.change_status.ChangeStatus"
    """<p>The current state of the request. <code>PENDING</code> indicates that this request has not yet been applied to all Amazon Route 53 DNS servers.</p>"""
    submitted_at: "capo_route_53.types.time_stamp.TimeStamp"
    """<p>The date and time that the change request was submitted in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> and Coordinated Universal Time (UTC). For example, the value <code>2017-03-27T17:48:16.751Z</code> represents March 27, 2017 at 17:48:16.751 UTC.</p>"""
    comment: NotRequired["capo_route_53.types.resource_description.ResourceDescription"]
    """<p>A comment you can provide.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ChangeInfo, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_route_53.types.change_status

    capo_route_53.types.change_status.serialize_xml(value["status"], el, "Status")
    import capo_route_53.types.time_stamp

    capo_route_53.types.time_stamp.serialize_xml(
        value["submitted_at"], el, "SubmittedAt"
    )
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> ChangeInfo:
    out: ChangeInfo = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("ChangeInfo.id required")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_route_53.types.change_status

        out["status"] = capo_route_53.types.change_status.deserialize_xml(child_status)
    else:
        raise DeserializationError("ChangeInfo.status required")
    child_submitted_at = el.find("SubmittedAt")
    if child_submitted_at is not None:
        import capo_route_53.types.time_stamp

        out["submitted_at"] = capo_route_53.types.time_stamp.deserialize_xml(
            child_submitted_at
        )
    else:
        raise DeserializationError("ChangeInfo.submitted_at required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
