"""Generated from Smithy shape ``com.amazonaws.route53#DeleteResourceRecordSetProtectionsResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class DeleteResourceRecordSetProtectionsResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteResourceRecordSetProtectionsResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteResourceRecordSetProtectionsResponse:
    out: DeleteResourceRecordSetProtectionsResponse = {}  # type: ignore[typeddict-item]
    return out
