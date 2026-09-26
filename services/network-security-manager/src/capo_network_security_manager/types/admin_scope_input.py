"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_firewall_type_scope
    import capo_network_security_manager.types.admin_scope_filter_input


class AdminScopeInput(TypedDict, closed=True):
    scope_filter: NotRequired[
        "capo_network_security_manager.types.admin_scope_filter_input.AdminScopeFilterInput"
    ]
    """<p>The filter that determines which accounts and organizational units are in the administrator's scope.</p>"""
    firewall_type_scope: NotRequired[
        "capo_network_security_manager.types.admin_firewall_type_scope.AdminFirewallTypeScope"
    ]
    """<p>The firewall types that the administrator can create and manage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeInput) -> dict:
    out: dict = {}
    if "scope_filter" in value:
        import capo_network_security_manager.types.admin_scope_filter_input

        out["scopeFilter"] = (
            capo_network_security_manager.types.admin_scope_filter_input.serialize_json(
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


def deserialize_json(data: dict) -> AdminScopeInput:
    out: AdminScopeInput = {}  # type: ignore[typeddict-item]
    if data.get("scopeFilter") is not None:
        import capo_network_security_manager.types.admin_scope_filter_input

        out["scope_filter"] = (
            capo_network_security_manager.types.admin_scope_filter_input.deserialize_json(
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
