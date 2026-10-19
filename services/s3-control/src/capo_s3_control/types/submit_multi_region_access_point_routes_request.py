"""Generated from Smithy shape ``com.amazonaws.s3control#SubmitMultiRegionAccessPointRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.multi_region_access_point_id
    import capo_s3_control.types.route_list


class SubmitMultiRegionAccessPointRoutesRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    mrap: "capo_s3_control.types.multi_region_access_point_id.MultiRegionAccessPointId"
    """<p>The Multi-Region Access Point ARN.</p>"""
    route_updates: "capo_s3_control.types.route_list.RouteList"
    """<p>The different routes that make up the new route configuration. Active routes return a value of <code>100</code>, and passive routes return a value of <code>0</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: SubmitMultiRegionAccessPointRoutesRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.route_list

    capo_s3_control.types.route_list.serialize_xml(
        value["route_updates"], el, "RouteUpdates"
    )


def deserialize_xml(el: Element) -> SubmitMultiRegionAccessPointRoutesRequest:
    out: SubmitMultiRegionAccessPointRoutesRequest = {}  # type: ignore[typeddict-item]
    child_route_updates = el.find("RouteUpdates")
    if child_route_updates is not None:
        import capo_s3_control.types.route_list

        out["route_updates"] = capo_s3_control.types.route_list.deserialize_xml(
            child_route_updates
        )
    else:
        out["route_updates"] = []
    return out
