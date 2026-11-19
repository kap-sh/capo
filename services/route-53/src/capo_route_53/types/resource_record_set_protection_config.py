"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetProtectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.resource_description
    import capo_route_53.types.rr_type


class ResourceRecordSetProtectionConfig(TypedDict, closed=True):
    record_name: "capo_route_53.types.dns_name.DNSName"
    """<p>The name of the resource record sets to protect, for example, <code>www.example.com</code>. The name must be the name of the hosted zone or a subdomain of it.</p>"""
    record_type: "capo_route_53.types.rr_type.RRType"
    """<p>The DNS record type of the resource record sets to protect. You can't protect records of type <code>DNAME</code> or of the DNSSEC record types that Route 53 manages.</p>"""
    comment: NotRequired["capo_route_53.types.resource_description.ResourceDescription"]
    """<p>An optional comment about the protection, for example, the reason that the resource record sets are protected. The comment can be up to 256 characters long. If you don't specify a comment, the protection doesn't have a comment. When Route 53 rejects a <code>ChangeResourceRecordSets</code> request because of this protection, the error message includes the comment, so don't include sensitive information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResourceRecordSetProtectionConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "RecordName").text = str(value["record_name"])
    import capo_route_53.types.rr_type

    capo_route_53.types.rr_type.serialize_xml(value["record_type"], el, "RecordType")
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> ResourceRecordSetProtectionConfig:
    out: ResourceRecordSetProtectionConfig = {}  # type: ignore[typeddict-item]
    child_record_name = el.find("RecordName")
    if child_record_name is not None:
        out["record_name"] = str(child_record_name.text or "")
    else:
        out["record_name"] = ""
    child_record_type = el.find("RecordType")
    if child_record_type is not None:
        import capo_route_53.types.rr_type

        out["record_type"] = capo_route_53.types.rr_type.deserialize_xml(
            child_record_type
        )
    else:
        import typing

        out["record_type"] = typing.cast("capo_route_53.types.rr_type.RRType", "")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
