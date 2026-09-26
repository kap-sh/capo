"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminFirewallTypeScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.firewall_type_list


class AdminFirewallTypeScope(TypedDict, closed=True):
    all_firewall_types_enabled: NotRequired["bool"]
    """<p>Specifies whether the administrator can manage all firewall types, except for third-party firewall types.</p>"""
    firewall_types: NotRequired[
        "capo_network_security_manager.types.firewall_type_list.FirewallTypeList"
    ]
    """<p>The list of firewall types that the administrator can manage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminFirewallTypeScope) -> dict:
    out: dict = {}
    if "all_firewall_types_enabled" in value:
        out["allFirewallTypesEnabled"] = value["all_firewall_types_enabled"]
    if "firewall_types" in value:
        import capo_network_security_manager.types.firewall_type_list

        out["firewallTypes"] = (
            capo_network_security_manager.types.firewall_type_list.serialize_json(
                value["firewall_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdminFirewallTypeScope:
    out: AdminFirewallTypeScope = {}  # type: ignore[typeddict-item]
    if data.get("allFirewallTypesEnabled") is not None:
        out["all_firewall_types_enabled"] = data["allFirewallTypesEnabled"]
    if data.get("firewallTypes") is not None:
        import capo_network_security_manager.types.firewall_type_list

        out["firewall_types"] = (
            capo_network_security_manager.types.firewall_type_list.deserialize_json(
                data["firewallTypes"]
            )
        )
    return out
