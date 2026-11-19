"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachmentOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.dynamic_routing_value
    import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode
    import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_status


class TransitGatewayPeeringAttachmentOptions(TypedDict, closed=True):
    dynamic_routing: NotRequired[
        "capo_ec2.types.dynamic_routing_value.DynamicRoutingValue"
    ]
    """<p>Describes whether dynamic routing is enabled or disabled for the transit gateway peering attachment.</p>"""
    requester_allow_multipath_resilience: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the requester allows multipath resilience for the transit gateway peering attachment.</p>"""
    requester_multipath_resilience_mode: NotRequired[
        "capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode.TransitGatewayPeeringAttachmentMultipathResilienceMode"
    ]
    """<p>The multipath resilience mode for the requester. This value is present only when the requester allows multipath resilience.</p>"""
    accepter_allow_multipath_resilience: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the accepter allows multipath resilience for the transit gateway peering attachment.</p>"""
    accepter_multipath_resilience_mode: NotRequired[
        "capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode.TransitGatewayPeeringAttachmentMultipathResilienceMode"
    ]
    """<p>The multipath resilience mode for the accepter. This value is present only when the accepter allows multipath resilience.</p>"""
    multipath_resilience_status: NotRequired[
        "capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_status.TransitGatewayPeeringAttachmentMultipathResilienceStatus"
    ]
    """<p>The multipath resilience status of the transit gateway peering attachment. The possible values are:</p> <ul> <li> <p> <code>enabled</code> – Both the requester and the accepter allow multipath resilience.</p> </li> <li> <p> <code>pending</code> – Either the requester or the accepter allows multipath resilience, but not both.</p> </li> <li> <p> <code>disabled</code> – Neither the requester nor the accepter allows multipath resilience.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPeeringAttachmentOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dynamic_routing" in value:
        import capo_ec2.types.dynamic_routing_value

        capo_ec2.types.dynamic_routing_value.serialize_ec2_query(
            value["dynamic_routing"], pairs, f"{key_prefix}DynamicRouting"
        )
    if "requester_allow_multipath_resilience" in value:
        pairs.append(
            (
                f"{key_prefix}RequesterAllowMultipathResilience",
                "true" if value["requester_allow_multipath_resilience"] else "false",
            )
        )
    if "requester_multipath_resilience_mode" in value:
        import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode

        capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode.serialize_ec2_query(
            value["requester_multipath_resilience_mode"],
            pairs,
            f"{key_prefix}RequesterMultipathResilienceMode",
        )
    if "accepter_allow_multipath_resilience" in value:
        pairs.append(
            (
                f"{key_prefix}AccepterAllowMultipathResilience",
                "true" if value["accepter_allow_multipath_resilience"] else "false",
            )
        )
    if "accepter_multipath_resilience_mode" in value:
        import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode

        capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode.serialize_ec2_query(
            value["accepter_multipath_resilience_mode"],
            pairs,
            f"{key_prefix}AccepterMultipathResilienceMode",
        )
    if "multipath_resilience_status" in value:
        import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_status

        capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_status.serialize_ec2_query(
            value["multipath_resilience_status"],
            pairs,
            f"{key_prefix}MultipathResilienceStatus",
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPeeringAttachmentOptions:
    out: TransitGatewayPeeringAttachmentOptions = {}  # type: ignore[typeddict-item]
    child_dynamic_routing = el.find("dynamicRouting")
    if child_dynamic_routing is not None:
        import capo_ec2.types.dynamic_routing_value

        out["dynamic_routing"] = (
            capo_ec2.types.dynamic_routing_value.deserialize_ec2_query(
                child_dynamic_routing
            )
        )
    child_requester_allow_multipath_resilience = el.find(
        "requesterAllowMultipathResilience"
    )
    if child_requester_allow_multipath_resilience is not None:
        out["requester_allow_multipath_resilience"] = (
            child_requester_allow_multipath_resilience.text or ""
        ).lower() == "true"
    child_requester_multipath_resilience_mode = el.find(
        "requesterMultipathResilienceMode"
    )
    if child_requester_multipath_resilience_mode is not None:
        import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode

        out["requester_multipath_resilience_mode"] = (
            capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode.deserialize_ec2_query(
                child_requester_multipath_resilience_mode
            )
        )
    child_accepter_allow_multipath_resilience = el.find(
        "accepterAllowMultipathResilience"
    )
    if child_accepter_allow_multipath_resilience is not None:
        out["accepter_allow_multipath_resilience"] = (
            child_accepter_allow_multipath_resilience.text or ""
        ).lower() == "true"
    child_accepter_multipath_resilience_mode = el.find(
        "accepterMultipathResilienceMode"
    )
    if child_accepter_multipath_resilience_mode is not None:
        import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode

        out["accepter_multipath_resilience_mode"] = (
            capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_mode.deserialize_ec2_query(
                child_accepter_multipath_resilience_mode
            )
        )
    child_multipath_resilience_status = el.find("multipathResilienceStatus")
    if child_multipath_resilience_status is not None:
        import capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_status

        out["multipath_resilience_status"] = (
            capo_ec2.types.transit_gateway_peering_attachment_multipath_resilience_status.deserialize_ec2_query(
                child_multipath_resilience_status
            )
        )
    return out
