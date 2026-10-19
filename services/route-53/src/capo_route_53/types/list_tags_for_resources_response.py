"""Generated from Smithy shape ``com.amazonaws.route53#ListTagsForResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_tag_set_list


class ListTagsForResourcesResponse(TypedDict, closed=True):
    resource_tag_sets: "capo_route_53.types.resource_tag_set_list.ResourceTagSetList"
    """<p>A list of <code>ResourceTagSet</code>s containing tags associated with the specified resources.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTagsForResourcesResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.resource_tag_set_list

    capo_route_53.types.resource_tag_set_list.serialize_xml(
        value["resource_tag_sets"], el, "ResourceTagSets"
    )


def deserialize_xml(el: Element) -> ListTagsForResourcesResponse:
    out: ListTagsForResourcesResponse = {}  # type: ignore[typeddict-item]
    child_resource_tag_sets = el.find("ResourceTagSets")
    if child_resource_tag_sets is not None:
        import capo_route_53.types.resource_tag_set_list

        out["resource_tag_sets"] = (
            capo_route_53.types.resource_tag_set_list.deserialize_xml(
                child_resource_tag_sets
            )
        )
    else:
        out["resource_tag_sets"] = []
    return out
