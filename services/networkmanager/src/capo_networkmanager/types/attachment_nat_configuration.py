"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentNatConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.boxed_boolean
    import capo_networkmanager.types.nat_gateway_support_state
    import capo_networkmanager.types.nat_rule_list


class AttachmentNatConfiguration(TypedDict, closed=True):
    attachment_id: NotRequired["capo_networkmanager.types.attachment_id.AttachmentId"]
    """<p>The ID of the attachment.</p>"""
    nat_gateway_support: NotRequired[
        "capo_networkmanager.types.nat_gateway_support_state.NatGatewaySupportState"
    ]
    """<p>The state of NAT gateway support on the attachment.</p>"""
    nat_system_route_support: NotRequired[
        "capo_networkmanager.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates whether the core network installs system routes for the NAT CIDR blocks of the attachment's NAT rules.</p>"""
    nat_gateway_rules: NotRequired[
        "capo_networkmanager.types.nat_rule_list.NatRuleList"
    ]
    """<p>The NAT rules of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentNatConfiguration) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "nat_gateway_support" in value:
        import capo_networkmanager.types.nat_gateway_support_state

        out["NatGatewaySupport"] = (
            capo_networkmanager.types.nat_gateway_support_state.serialize_json(
                value["nat_gateway_support"]
            )
        )
    if "nat_system_route_support" in value:
        out["NatSystemRouteSupport"] = value["nat_system_route_support"]
    if "nat_gateway_rules" in value:
        import capo_networkmanager.types.nat_rule_list

        out["NatGatewayRules"] = capo_networkmanager.types.nat_rule_list.serialize_json(
            value["nat_gateway_rules"]
        )
    return out


def deserialize_json(data: dict) -> AttachmentNatConfiguration:
    out: AttachmentNatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("NatGatewaySupport") is not None:
        import capo_networkmanager.types.nat_gateway_support_state

        out["nat_gateway_support"] = (
            capo_networkmanager.types.nat_gateway_support_state.deserialize_json(
                data["NatGatewaySupport"]
            )
        )
    if data.get("NatSystemRouteSupport") is not None:
        out["nat_system_route_support"] = data["NatSystemRouteSupport"]
    if data.get("NatGatewayRules") is not None:
        import capo_networkmanager.types.nat_rule_list

        out["nat_gateway_rules"] = (
            capo_networkmanager.types.nat_rule_list.deserialize_json(
                data["NatGatewayRules"]
            )
        )
    return out
