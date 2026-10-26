"""Generated from Smithy shape ``com.amazonaws.accountaccess#Entitlement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError
from capo_account_access.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access.types.principal_role_entitlement


class _Entitlement_principalRole(TypedDict, closed=True):
    principalRole: (
        "capo_account_access.types.principal_role_entitlement.PrincipalRoleEntitlement"
    )


Entitlement: TypeAlias = _Entitlement_principalRole | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Entitlement) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Entitlement: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "principalRole" in value:
        import capo_account_access.types.principal_role_entitlement

        return {
            "principalRole": capo_account_access.types.principal_role_entitlement.serialize_json(
                value["principalRole"]
            )
        }
    else:
        raise SerializationError("Entitlement: no variant present")


def deserialize_json(data: dict) -> Entitlement:
    if data.get("principalRole") is not None:
        import capo_account_access.types.principal_role_entitlement

        return {
            "principalRole": capo_account_access.types.principal_role_entitlement.deserialize_json(
                data["principalRole"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Entitlement: no recognized variant key")
