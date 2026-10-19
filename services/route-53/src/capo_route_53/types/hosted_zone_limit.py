"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.hosted_zone_limit_type
    import capo_route_53.types.limit_value


class HostedZoneLimit(TypedDict, closed=True):
    type: "capo_route_53.types.hosted_zone_limit_type.HostedZoneLimitType"
    """<p>The limit that you requested. Valid values include the following:</p> <ul> <li> <p> <b>MAX_RRSETS_BY_ZONE</b>: The maximum number of records that you can create in the specified hosted zone.</p> </li> <li> <p> <b>MAX_VPCS_ASSOCIATED_BY_ZONE</b>: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.</p> </li> </ul>"""
    value: "capo_route_53.types.limit_value.LimitValue"
    """<p>The current value for the limit that is specified by <code>Type</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneLimit, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.hosted_zone_limit_type

    capo_route_53.types.hosted_zone_limit_type.serialize_xml(value["type"], el, "Type")
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> HostedZoneLimit:
    out: HostedZoneLimit = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_route_53.types.hosted_zone_limit_type

        out["type"] = capo_route_53.types.hosted_zone_limit_type.deserialize_xml(
            child_type
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_route_53.types.hosted_zone_limit_type.HostedZoneLimitType", ""
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    else:
        out["value"] = 0
    return out
