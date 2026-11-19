"""Generated from Smithy shape ``com.amazonaws.route53#CreateResourceRecordSetProtectionsResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class CreateResourceRecordSetProtectionsResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: CreateResourceRecordSetProtectionsResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> CreateResourceRecordSetProtectionsResponse:
    out: CreateResourceRecordSetProtectionsResponse = {}  # type: ignore[typeddict-item]
    return out
