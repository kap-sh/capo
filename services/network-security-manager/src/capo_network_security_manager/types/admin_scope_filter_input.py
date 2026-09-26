"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeFilterInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_scope_selection_input


class _AdminScopeFilterInput_includeAll(TypedDict, closed=True):
    includeAll: "None"


class _AdminScopeFilterInput_includeOnly(TypedDict, closed=True):
    includeOnly: "capo_network_security_manager.types.admin_scope_selection_input.AdminScopeSelectionInput"


class _AdminScopeFilterInput_excludeOnly(TypedDict, closed=True):
    excludeOnly: "capo_network_security_manager.types.admin_scope_selection_input.AdminScopeSelectionInput"


AdminScopeFilterInput: TypeAlias = (
    _AdminScopeFilterInput_includeAll
    | _AdminScopeFilterInput_includeOnly
    | _AdminScopeFilterInput_excludeOnly
)


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeFilterInput) -> dict:
    if "includeAll" in value:
        return {"includeAll": {}}
    elif "includeOnly" in value:
        import capo_network_security_manager.types.admin_scope_selection_input

        return {
            "includeOnly": capo_network_security_manager.types.admin_scope_selection_input.serialize_json(
                value["includeOnly"]
            )
        }
    elif "excludeOnly" in value:
        import capo_network_security_manager.types.admin_scope_selection_input

        return {
            "excludeOnly": capo_network_security_manager.types.admin_scope_selection_input.serialize_json(
                value["excludeOnly"]
            )
        }
    else:
        raise SerializationError("AdminScopeFilterInput: no variant present")


def deserialize_json(data: dict) -> AdminScopeFilterInput:
    if data.get("includeAll") is not None:
        return {"includeAll": None}
    elif data.get("includeOnly") is not None:
        import capo_network_security_manager.types.admin_scope_selection_input

        return {
            "includeOnly": capo_network_security_manager.types.admin_scope_selection_input.deserialize_json(
                data["includeOnly"]
            )
        }
    elif data.get("excludeOnly") is not None:
        import capo_network_security_manager.types.admin_scope_selection_input

        return {
            "excludeOnly": capo_network_security_manager.types.admin_scope_selection_input.deserialize_json(
                data["excludeOnly"]
            )
        }
    else:
        raise DeserializationError("AdminScopeFilterInput: no recognized variant key")
