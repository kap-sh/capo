"""Generated from Smithy shape ``com.amazonaws.route53#TestDNSAnswerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.dnsr_code
    import capo_route_53.types.nameserver
    import capo_route_53.types.record_data
    import capo_route_53.types.rr_type
    import capo_route_53.types.transport_protocol


class TestDNSAnswerResponse(TypedDict, closed=True):
    nameserver: "capo_route_53.types.nameserver.Nameserver"
    """<p>The Amazon Route 53 name server used to respond to the request.</p>"""
    record_name: "capo_route_53.types.dns_name.DNSName"
    """<p>The name of the resource record set that you submitted a request for.</p>"""
    record_type: "capo_route_53.types.rr_type.RRType"
    """<p>The type of the resource record set that you submitted a request for.</p>"""
    record_data: "capo_route_53.types.record_data.RecordData"
    """<p>A list that contains values that Amazon Route 53 returned for this resource record set.</p>"""
    response_code: "capo_route_53.types.dnsr_code.DNSRCode"
    """<p>A code that indicates whether the request is valid or not. The most common response code is <code>NOERROR</code>, meaning that the request is valid. If the response is not valid, Amazon Route 53 returns a response code that describes the error. For a list of possible response codes, see <a href="http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6">DNS RCODES</a> on the IANA website. </p>"""
    protocol: "capo_route_53.types.transport_protocol.TransportProtocol"
    """<p>The protocol that Amazon Route 53 used to respond to the request, either <code>UDP</code> or <code>TCP</code>. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: TestDNSAnswerResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Nameserver").text = str(value["nameserver"])
    SubElement(el, "RecordName").text = str(value["record_name"])
    import capo_route_53.types.rr_type

    capo_route_53.types.rr_type.serialize_xml(value["record_type"], el, "RecordType")
    import capo_route_53.types.record_data

    capo_route_53.types.record_data.serialize_xml(
        value["record_data"], el, "RecordData"
    )
    SubElement(el, "ResponseCode").text = str(value["response_code"])
    SubElement(el, "Protocol").text = str(value["protocol"])


def deserialize_xml(el: Element) -> TestDNSAnswerResponse:
    out: TestDNSAnswerResponse = {}  # type: ignore[typeddict-item]
    child_nameserver = el.find("Nameserver")
    if child_nameserver is not None:
        out["nameserver"] = str(child_nameserver.text or "")
    else:
        raise DeserializationError("TestDNSAnswerResponse.nameserver required")
    child_record_name = el.find("RecordName")
    if child_record_name is not None:
        out["record_name"] = str(child_record_name.text or "")
    else:
        raise DeserializationError("TestDNSAnswerResponse.record_name required")
    child_record_type = el.find("RecordType")
    if child_record_type is not None:
        import capo_route_53.types.rr_type

        out["record_type"] = capo_route_53.types.rr_type.deserialize_xml(
            child_record_type
        )
    else:
        raise DeserializationError("TestDNSAnswerResponse.record_type required")
    child_record_data = el.find("RecordData")
    if child_record_data is not None:
        import capo_route_53.types.record_data

        out["record_data"] = capo_route_53.types.record_data.deserialize_xml(
            child_record_data
        )
    else:
        raise DeserializationError("TestDNSAnswerResponse.record_data required")
    child_response_code = el.find("ResponseCode")
    if child_response_code is not None:
        out["response_code"] = str(child_response_code.text or "")
    else:
        raise DeserializationError("TestDNSAnswerResponse.response_code required")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    else:
        raise DeserializationError("TestDNSAnswerResponse.protocol required")
    return out
