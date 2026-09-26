"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_firewall_type_scope
    import capo_network_security_manager.types.admin_scope_filter


class AdminScope(TypedDict, closed=True):
    scope_filter: NotRequired[
        "capo_network_security_manager.types.admin_scope_filter.AdminScopeFilter"
    ]
    """<p>The filter that determines which accounts and organizational units are in the administrator's scope.</p>"""
    firewall_type_scope: NotRequired[
        "capo_network_security_manager.types.admin_firewall_type_scope.AdminFirewallTypeScope"
    ]
    """<p>The firewall types that the administrator can create and manage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminScope) -> dict:
    out: dict = {}
    if "scope_filter" in value:
        import capo_network_security_manager.types.admin_scope_filter

        out["scopeFilter"] = (
            capo_network_security_manager.types.admin_scope_filter.serialize_json(
                value["scope_filter"]
            )
        )
    if "firewall_type_scope" in value:
        import capo_network_security_manager.types.admin_firewall_type_scope

        out["firewallTypeScope"] = (
            capo_network_security_manager.types.admin_firewall_type_scope.serialize_json(
                value["firewall_type_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdminScope:
    out: AdminScope = {}  # type: ignore[typeddict-item]
    if data.get("scopeFilter") is not None:
        import capo_network_security_manager.types.admin_scope_filter

        out["scope_filter"] = (
            capo_network_security_manager.types.admin_scope_filter.deserialize_json(
                data["scopeFilter"]
            )
        )
    if data.get("firewallTypeScope") is not None:
        import capo_network_security_manager.types.admin_firewall_type_scope

        out["firewall_type_scope"] = (
            capo_network_security_manager.types.admin_firewall_type_scope.deserialize_json(
                data["firewallTypeScope"]
            )
        )
    return out
