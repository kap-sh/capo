"""Generated from Smithy shape ``com.amazonaws.route53#CidrCollectionChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_collection_change_action
    import capo_route_53.types.cidr_list
    import capo_route_53.types.cidr_location_name_default_not_allowed


class CidrCollectionChange(TypedDict, closed=True):
    location_name: "capo_route_53.types.cidr_location_name_default_not_allowed.CidrLocationNameDefaultNotAllowed"
    """<p>Name of the location that is associated with the CIDR collection.</p>"""
    action: (
        "capo_route_53.types.cidr_collection_change_action.CidrCollectionChangeAction"
    )
    """<p>CIDR collection change action. </p>"""
    cidr_list: "capo_route_53.types.cidr_list.CidrList"
    """<p>List of CIDR blocks.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CidrCollectionChange, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "LocationName").text = str(value["location_name"])
    import capo_route_53.types.cidr_collection_change_action

    capo_route_53.types.cidr_collection_change_action.serialize_xml(
        value["action"], el, "Action"
    )
    import capo_route_53.types.cidr_list

    capo_route_53.types.cidr_list.serialize_xml(value["cidr_list"], el, "CidrList")


def deserialize_xml(el: Element) -> CidrCollectionChange:
    out: CidrCollectionChange = {}  # type: ignore[typeddict-item]
    child_location_name = el.find("LocationName")
    if child_location_name is not None:
        out["location_name"] = str(child_location_name.text or "")
    else:
        out["location_name"] = ""
    child_action = el.find("Action")
    if child_action is not None:
        import capo_route_53.types.cidr_collection_change_action

        out["action"] = (
            capo_route_53.types.cidr_collection_change_action.deserialize_xml(
                child_action
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_route_53.types.cidr_collection_change_action.CidrCollectionChangeAction",
            "",
        )
    child_cidr_list = el.find("CidrList")
    if child_cidr_list is not None:
        import capo_route_53.types.cidr_list

        out["cidr_list"] = capo_route_53.types.cidr_list.deserialize_xml(
            child_cidr_list
        )
    else:
        out["cidr_list"] = []
    return out
