"""Generated from Smithy shape ``com.amazonaws.route53#ProtectionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.error_message
    import capo_route_53.types.protection_error_code
    import capo_route_53.types.rr_type


class ProtectionError(TypedDict, closed=True):
    record_name: "capo_route_53.types.dns_name.DNSName"
    """<p>The name in the failing entry.</p>"""
    record_type: "capo_route_53.types.rr_type.RRType"
    """<p>The record type in the failing entry.</p>"""
    code: "capo_route_53.types.protection_error_code.ProtectionErrorCode"
    """<p>The reason that the entry failed. Valid values include the following:</p> <ul> <li> <p> <code>InvalidInput</code> means that the entry isn't valid. For example, the name isn't a valid DNS name, the name isn't in the hosted zone, the record type can't be protected, or the same name and type appear more than once in the request.</p> </li> <li> <p> <code>ProtectionAlreadyExists</code> means that a protection already exists for the name and type.</p> </li> <li> <p> <code>ProtectionNotFound</code> means that no protection exists for the name and type.</p> </li> </ul>"""
    message: "capo_route_53.types.error_message.ErrorMessage"
    """<p>A message that explains why Route 53 couldn't process the entry.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ProtectionError, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "RecordName").text = str(value["record_name"])
    import capo_route_53.types.rr_type

    capo_route_53.types.rr_type.serialize_xml(value["record_type"], el, "RecordType")
    SubElement(el, "Code").text = str(value["code"])
    SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> ProtectionError:
    out: ProtectionError = {}  # type: ignore[typeddict-item]
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
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    else:
        out["code"] = ""
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        out["message"] = ""
    return out
