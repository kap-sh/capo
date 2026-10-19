"""Generated from Smithy shape ``com.amazonaws.route53#ChangeCidrCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_collection_changes
    import capo_route_53.types.collection_version
    import capo_route_53.types.uuid


class ChangeCidrCollectionRequest(TypedDict, closed=True):
    id: "capo_route_53.types.uuid.UUID"
    """<p>The UUID of the CIDR collection to update.</p>"""
    collection_version: NotRequired[
        "capo_route_53.types.collection_version.CollectionVersion"
    ]
    """<p>A sequential counter that Amazon Route 53 sets to 1 when you create a collection and increments it by 1 each time you update the collection.</p> <p>We recommend that you use <code>ListCidrCollection</code> to get the current value of <code>CollectionVersion</code> for the collection that you want to update, and then include that value with the change request. This prevents Route 53 from overwriting an intervening update: </p> <ul> <li> <p>If the value in the request matches the value of <code>CollectionVersion</code> in the collection, Route 53 updates the collection.</p> </li> <li> <p>If the value of <code>CollectionVersion</code> in the collection is greater than the value in the request, the collection was changed after you got the version number. Route 53 does not update the collection, and it returns a <code>CidrCollectionVersionMismatch</code> error. </p> </li> </ul>"""
    changes: "capo_route_53.types.cidr_collection_changes.CidrCollectionChanges"
    """<p> Information about changes to a CIDR collection.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ChangeCidrCollectionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "collection_version" in value:
        SubElement(el, "CollectionVersion").text = str(value["collection_version"])
    import capo_route_53.types.cidr_collection_changes

    capo_route_53.types.cidr_collection_changes.serialize_xml(
        value["changes"], el, "Changes"
    )


def deserialize_xml(el: Element) -> ChangeCidrCollectionRequest:
    out: ChangeCidrCollectionRequest = {}  # type: ignore[typeddict-item]
    child_collection_version = el.find("CollectionVersion")
    if child_collection_version is not None:
        out["collection_version"] = int(child_collection_version.text or "")
    child_changes = el.find("Changes")
    if child_changes is not None:
        import capo_route_53.types.cidr_collection_changes

        out["changes"] = capo_route_53.types.cidr_collection_changes.deserialize_xml(
            child_changes
        )
    else:
        out["changes"] = []
    return out
