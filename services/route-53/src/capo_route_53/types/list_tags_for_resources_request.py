"""Generated from Smithy shape ``com.amazonaws.route53#ListTagsForResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.tag_resource_id_list
    import capo_route_53.types.tag_resource_type


class ListTagsForResourcesRequest(TypedDict, closed=True):
    resource_type: "capo_route_53.types.tag_resource_type.TagResourceType"
    """<p>The type of the resources.</p> <ul> <li> <p>The resource type for health checks is <code>healthcheck</code>.</p> </li> <li> <p>The resource type for hosted zones is <code>hostedzone</code>.</p> </li> </ul>"""
    resource_ids: "capo_route_53.types.tag_resource_id_list.TagResourceIdList"
    """<p>A complex type that contains the ResourceId element for each resource for which you want to get a list of tags.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTagsForResourcesRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.tag_resource_id_list

    capo_route_53.types.tag_resource_id_list.serialize_xml(
        value["resource_ids"], el, "ResourceIds"
    )


def deserialize_xml(el: Element) -> ListTagsForResourcesRequest:
    out: ListTagsForResourcesRequest = {}  # type: ignore[typeddict-item]
    child_resource_ids = el.find("ResourceIds")
    if child_resource_ids is not None:
        import capo_route_53.types.tag_resource_id_list

        out["resource_ids"] = capo_route_53.types.tag_resource_id_list.deserialize_xml(
            child_resource_ids
        )
    else:
        out["resource_ids"] = []
    return out
