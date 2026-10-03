"""Generated from Smithy shape ``com.amazonaws.route53#ChangeResourceRecordSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.change_info


class ChangeResourceRecordSetsResponse(TypedDict, closed=True):
    change_info: "capo_route_53.types.change_info.ChangeInfo"
    """<p>A complex type that contains information about changes made to your hosted zone.</p> <p>This element contains an ID that you use when performing a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html">GetChange</a> action to get detailed information about the change.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ChangeResourceRecordSetsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.change_info

    capo_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )


def deserialize_xml(el: Element) -> ChangeResourceRecordSetsResponse:
    out: ChangeResourceRecordSetsResponse = {}  # type: ignore[typeddict-item]
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import capo_route_53.types.change_info

        out["change_info"] = capo_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError(
            "ChangeResourceRecordSetsResponse.change_info required"
        )
    return out
