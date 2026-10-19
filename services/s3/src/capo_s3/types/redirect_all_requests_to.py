"""Generated from Smithy shape ``com.amazonaws.s3#RedirectAllRequestsTo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.host_name
    import capo_s3.types.protocol


class RedirectAllRequestsTo(TypedDict, closed=True):
    host_name: "capo_s3.types.host_name.HostName"
    """<p>Name of the host where requests are redirected.</p>"""
    protocol: NotRequired["capo_s3.types.protocol.Protocol"]
    """<p>Protocol to use when redirecting requests. The default is the protocol that is used in the original request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RedirectAllRequestsTo, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostName").text = str(value["host_name"])
    if "protocol" in value:
        import capo_s3.types.protocol

        capo_s3.types.protocol.serialize_xml(value["protocol"], el, "Protocol")


def deserialize_xml(el: Element) -> RedirectAllRequestsTo:
    out: RedirectAllRequestsTo = {}  # type: ignore[typeddict-item]
    child_host_name = el.find("HostName")
    if child_host_name is not None:
        out["host_name"] = str(child_host_name.text or "")
    else:
        out["host_name"] = ""
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_s3.types.protocol

        out["protocol"] = capo_s3.types.protocol.deserialize_xml(child_protocol)
    return out
