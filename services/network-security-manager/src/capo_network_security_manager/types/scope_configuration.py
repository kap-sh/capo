"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_filter
    import capo_network_security_manager.types.resource_scope_map


class ScopeConfiguration(TypedDict, closed=True):
    account_filter: NotRequired[
        "capo_network_security_manager.types.account_filter.AccountFilter"
    ]
    """<p>The account filter that determines which accounts are in scope. When set, exactly one of <code>includeAll</code>, <code>include</code>, or <code>exclude</code> is set.</p> <p>Organization administrators must include an account filter in every scope configuration. Single-account administrators must omit it: a scope without an account filter applies only to the administrator's own account. The presence of an account filter is fixed when the scope is created: an update can't add an account filter to a scope that was created without one, or remove the account filter from a scope that was created with one.</p>"""
    resource_scopes: (
        "capo_network_security_manager.types.resource_scope_map.ResourceScopeMap"
    )
    """<p>The resource-level scoping configuration, keyed by resource type, that defines which resources within the selected accounts are in scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeConfiguration) -> dict:
    out: dict = {}
    if "account_filter" in value:
        import capo_network_security_manager.types.account_filter

        out["accountFilter"] = (
            capo_network_security_manager.types.account_filter.serialize_json(
                value["account_filter"]
            )
        )
    import capo_network_security_manager.types.resource_scope_map

    out["resourceScopes"] = (
        capo_network_security_manager.types.resource_scope_map.serialize_json(
            value["resource_scopes"]
        )
    )
    return out


def deserialize_json(data: dict) -> ScopeConfiguration:
    out: ScopeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accountFilter") is not None:
        import capo_network_security_manager.types.account_filter

        out["account_filter"] = (
            capo_network_security_manager.types.account_filter.deserialize_json(
                data["accountFilter"]
            )
        )
    if data.get("resourceScopes") is not None:
        import capo_network_security_manager.types.resource_scope_map

        out["resource_scopes"] = (
            capo_network_security_manager.types.resource_scope_map.deserialize_json(
                data["resourceScopes"]
            )
        )
    else:
        raise DeserializationError("ScopeConfiguration.resource_scopes required")
    return out
