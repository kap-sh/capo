"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AdminScopeFilterInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.admin_scope_selection_input


class AdminScopeFilterInputIncludeAllMember(TypedDict, closed=True):
    includeAll: "None"


class AdminScopeFilterInputIncludeOnlyMember(TypedDict, closed=True):
    includeOnly: "capo_network_security_manager.types.admin_scope_selection_input.AdminScopeSelectionInput"


class AdminScopeFilterInputExcludeOnlyMember(TypedDict, closed=True):
    excludeOnly: "capo_network_security_manager.types.admin_scope_selection_input.AdminScopeSelectionInput"


AdminScopeFilterInput: TypeAlias = (
    AdminScopeFilterInputIncludeAllMember
    | AdminScopeFilterInputIncludeOnlyMember
    | AdminScopeFilterInputExcludeOnlyMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AdminScopeFilterInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AdminScopeFilterInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "includeAll" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AdminScopeFilterInput: no recognized variant key")
