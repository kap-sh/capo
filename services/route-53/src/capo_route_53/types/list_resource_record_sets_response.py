"""Generated from Smithy shape ``com.amazonaws.route53#ListResourceRecordSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.page_truncated
    import capo_route_53.types.resource_record_set_identifier
    import capo_route_53.types.resource_record_sets
    import capo_route_53.types.rr_type


class ListResourceRecordSetsResponse(TypedDict, closed=True):
    resource_record_sets: "capo_route_53.types.resource_record_sets.ResourceRecordSets"
    """<p>Information about multiple resource record sets.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether more resource record sets remain to be listed. If your results were truncated, you can make a follow-up pagination request by using the <code>NextRecordName</code> element.</p>"""
    next_record_name: NotRequired["capo_route_53.types.dns_name.DNSName"]
    """<p>If the results were truncated, the name of the next record in the list.</p> <p>This element is present only if <code>IsTruncated</code> is true. </p>"""
    next_record_type: NotRequired["capo_route_53.types.rr_type.RRType"]
    """<p>If the results were truncated, the type of the next record in the list.</p> <p>This element is present only if <code>IsTruncated</code> is true. </p>"""
    next_record_identifier: NotRequired[
        "capo_route_53.types.resource_record_set_identifier.ResourceRecordSetIdentifier"
    ]
    """<p> <i>Resource record sets that have a routing policy other than simple:</i> If results were truncated for a given DNS name and type, the value of <code>SetIdentifier</code> for the next resource record set that has the current DNS name and type.</p> <p>For information about routing policies, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html">Choosing a Routing Policy</a> in the <i>Amazon Route 53 Developer Guide</i>.</p>"""
    max_items: "int"
    """<p>The maximum number of records you requested.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListResourceRecordSetsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.resource_record_sets

    capo_route_53.types.resource_record_sets.serialize_xml(
        value["resource_record_sets"], el, "ResourceRecordSets"
    )
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    if "next_record_name" in value:
        SubElement(el, "NextRecordName").text = str(value["next_record_name"])
    if "next_record_type" in value:
        import capo_route_53.types.rr_type

        capo_route_53.types.rr_type.serialize_xml(
            value["next_record_type"], el, "NextRecordType"
        )
    if "next_record_identifier" in value:
        SubElement(el, "NextRecordIdentifier").text = str(
            value["next_record_identifier"]
        )
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListResourceRecordSetsResponse:
    out: ListResourceRecordSetsResponse = {}  # type: ignore[typeddict-item]
    child_resource_record_sets = el.find("ResourceRecordSets")
    if child_resource_record_sets is not None:
        import capo_route_53.types.resource_record_sets

        out["resource_record_sets"] = (
            capo_route_53.types.resource_record_sets.deserialize_xml(
                child_resource_record_sets
            )
        )
    else:
        raise DeserializationError(
            "ListResourceRecordSetsResponse.resource_record_sets required"
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_next_record_name = el.find("NextRecordName")
    if child_next_record_name is not None:
        out["next_record_name"] = str(child_next_record_name.text or "")
    child_next_record_type = el.find("NextRecordType")
    if child_next_record_type is not None:
        import capo_route_53.types.rr_type

        out["next_record_type"] = capo_route_53.types.rr_type.deserialize_xml(
            child_next_record_type
        )
    child_next_record_identifier = el.find("NextRecordIdentifier")
    if child_next_record_identifier is not None:
        out["next_record_identifier"] = str(child_next_record_identifier.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("ListResourceRecordSetsResponse.max_items required")
    return out
