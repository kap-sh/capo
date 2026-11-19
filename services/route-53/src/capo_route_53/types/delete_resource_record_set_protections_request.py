"""Generated from Smithy shape ``com.amazonaws.route53#DeleteResourceRecordSetProtectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_id
    import capo_route_53.types.resource_record_set_protection_key_batch


class DeleteResourceRecordSetProtectionsRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that contains the protections that you want to delete.</p>"""
    protections: "capo_route_53.types.resource_record_set_protection_key_batch.ResourceRecordSetProtectionKeyBatch"
    """<p>The name and type of each protection to delete. The list must contain at least one entry and can contain up to 100 entries. Each name and type can appear only once in the list.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteResourceRecordSetProtectionsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.resource_record_set_protection_key_batch

    capo_route_53.types.resource_record_set_protection_key_batch.serialize_xml(
        value["protections"], el, "Protections"
    )


def deserialize_xml(el: Element) -> DeleteResourceRecordSetProtectionsRequest:
    out: DeleteResourceRecordSetProtectionsRequest = {}  # type: ignore[typeddict-item]
    child_protections = el.find("Protections")
    if child_protections is not None:
        import capo_route_53.types.resource_record_set_protection_key_batch

        out["protections"] = (
            capo_route_53.types.resource_record_set_protection_key_batch.deserialize_xml(
                child_protections
            )
        )
    else:
        out["protections"] = []
    return out
