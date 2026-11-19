"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSetProtectionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.rr_type


class ResourceRecordSetProtectionKey(TypedDict, closed=True):
    record_name: "capo_route_53.types.dns_name.DNSName"
    """<p>The name of the protected resource record sets.</p>"""
    record_type: "capo_route_53.types.rr_type.RRType"
    """<p>The DNS record type of the protected resource record sets.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResourceRecordSetProtectionKey, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "RecordName").text = str(value["record_name"])
    import capo_route_53.types.rr_type

    capo_route_53.types.rr_type.serialize_xml(value["record_type"], el, "RecordType")


def deserialize_xml(el: Element) -> ResourceRecordSetProtectionKey:
    out: ResourceRecordSetProtectionKey = {}  # type: ignore[typeddict-item]
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
    return out
