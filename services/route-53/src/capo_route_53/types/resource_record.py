"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.r_data


class ResourceRecord(TypedDict, closed=True):
    value: "capo_route_53.types.r_data.RData"
    """<p>The current or new DNS record value, not to exceed 4,000 characters. In the case of a <code>DELETE</code> action, if the current value does not match the actual value, an error is returned. For descriptions about how to format <code>Value</code> for different record types, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html">Supported DNS Resource Record Types</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>You can specify more than one value for all record types except <code>CNAME</code> and <code>SOA</code>. </p> <note> <p>If you're creating an alias resource record set, omit <code>Value</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: ResourceRecord, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> ResourceRecord:
    out: ResourceRecord = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("ResourceRecord.value required")
    return out
