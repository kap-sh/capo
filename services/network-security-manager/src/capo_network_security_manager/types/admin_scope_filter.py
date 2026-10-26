"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeFilter``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

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
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AdminScopeFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "includeAll" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AdminScopeFilter: no recognized variant key")


def redact_sensitive(value: AdminScopeFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "includeOnly" in value:
        import capo_network_security_manager.types.admin_scope_selection

        out["includeOnly"] = (
            capo_network_security_manager.types.admin_scope_selection.redact_sensitive(
                value["includeOnly"]
            )
        )
    if "excludeOnly" in value:
        import capo_network_security_manager.types.admin_scope_selection

        out["excludeOnly"] = (
            capo_network_security_manager.types.admin_scope_selection.redact_sensitive(
                value["excludeOnly"]
            )
        )
    return out
