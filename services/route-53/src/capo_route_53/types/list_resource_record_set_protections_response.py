"""Generated from Smithy shape ``com.amazonaws.route53#ListResourceRecordSetProtectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.pagination_token
    import capo_route_53.types.resource_record_set_protections


class ListResourceRecordSetProtectionsResponse(TypedDict, closed=True):
    resource_record_set_protections: "capo_route_53.types.resource_record_set_protections.ResourceRecordSetProtections"
    """<p>The protections in the hosted zone. The list is empty if the hosted zone has no protections.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>If there are more protections to list, a token that you can specify in the <code>NextToken</code> parameter of another request to get the next page of results. If there are no more protections to list, the response doesn't include <code>NextToken</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListResourceRecordSetProtectionsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.resource_record_set_protections

    capo_route_53.types.resource_record_set_protections.serialize_xml(
        value["resource_record_set_protections"], el, "ResourceRecordSetProtections"
    )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListResourceRecordSetProtectionsResponse:
    out: ListResourceRecordSetProtectionsResponse = {}  # type: ignore[typeddict-item]
    child_resource_record_set_protections = el.find("ResourceRecordSetProtections")
    if child_resource_record_set_protections is not None:
        import capo_route_53.types.resource_record_set_protections

        out["resource_record_set_protections"] = (
            capo_route_53.types.resource_record_set_protections.deserialize_xml(
                child_resource_record_set_protections
            )
        )
    else:
        out["resource_record_set_protections"] = []
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
