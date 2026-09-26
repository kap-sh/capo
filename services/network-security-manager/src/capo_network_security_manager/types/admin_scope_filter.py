"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_scope_selection


class _AdminScopeFilter_includeAll(TypedDict, closed=True):
    includeAll: "None"


class _AdminScopeFilter_includeOnly(TypedDict, closed=True):
    includeOnly: (
        "capo_network_security_manager.types.admin_scope_selection.AdminScopeSelection"
    )


class _AdminScopeFilter_excludeOnly(TypedDict, closed=True):
    excludeOnly: (
        "capo_network_security_manager.types.admin_scope_selection.AdminScopeSelection"
    )


AdminScopeFilter: TypeAlias = (
    _AdminScopeFilter_includeAll
    | _AdminScopeFilter_includeOnly
    | _AdminScopeFilter_excludeOnly
)


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeFilter) -> dict:
    if "includeAll" in value:
        return {"includeAll": {}}
    elif "includeOnly" in value:
        import capo_network_security_manager.types.admin_scope_selection

        return {
            "includeOnly": capo_network_security_manager.types.admin_scope_selection.serialize_json(
                value["includeOnly"]
            )
        }
    elif "excludeOnly" in value:
        import capo_network_security_manager.types.admin_scope_selection

        return {
            "excludeOnly": capo_network_security_manager.types.admin_scope_selection.serialize_json(
                value["excludeOnly"]
            )
        }
    else:
        raise SerializationError("AdminScopeFilter: no variant present")


def deserialize_json(data: dict) -> AdminScopeFilter:
    if data.get("includeAll") is not None:
        return {"includeAll": None}
    elif data.get("includeOnly") is not None:
        import capo_network_security_manager.types.admin_scope_selection

        return {
            "includeOnly": capo_network_security_manager.types.admin_scope_selection.deserialize_json(
                data["includeOnly"]
            )
        }
    elif data.get("excludeOnly") is not None:
        import capo_network_security_manager.types.admin_scope_selection

        return {
            "excludeOnly": capo_network_security_manager.types.admin_scope_selection.deserialize_json(
                data["excludeOnly"]
            )
        }
    else:
        raise DeserializationError("AdminScopeFilter: no recognized variant key")
