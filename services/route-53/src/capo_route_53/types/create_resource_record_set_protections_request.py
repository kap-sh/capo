"""Generated from Smithy shape ``com.amazonaws.route53#CreateResourceRecordSetProtectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_id
    import capo_route_53.types.resource_record_set_protection_config_batch


class CreateResourceRecordSetProtectionsRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that contains the resource record sets that you want to protect.</p>"""
    protections: "capo_route_53.types.resource_record_set_protection_config_batch.ResourceRecordSetProtectionConfigBatch"
    """<p>The protections to create. Each entry specifies a resource record set name and type, and an optional comment. The list must contain at least one entry and can contain up to 100 entries. Each name and type can appear only once in the list.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateResourceRecordSetProtectionsRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.resource_record_set_protection_config_batch

    capo_route_53.types.resource_record_set_protection_config_batch.serialize_xml(
        value["protections"], el, "Protections"
    )


def deserialize_xml(el: Element) -> CreateResourceRecordSetProtectionsRequest:
    out: CreateResourceRecordSetProtectionsRequest = {}  # type: ignore[typeddict-item]
    child_protections = el.find("Protections")
    if child_protections is not None:
        import capo_route_53.types.resource_record_set_protection_config_batch

        out["protections"] = (
            capo_route_53.types.resource_record_set_protection_config_batch.deserialize_xml(
                child_protections
            )
        )
    else:
        out["protections"] = []
    return out
