"""Generated from Smithy shape ``com.amazonaws.accountaccess#EntitlementSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError
from capo_account_access.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access.types.principal_role_entitlement_summary


class _EntitlementSummary_principalRole(TypedDict, closed=True):
    principalRole: "capo_account_access.types.principal_role_entitlement_summary.PrincipalRoleEntitlementSummary"


EntitlementSummary: TypeAlias = _EntitlementSummary_principalRole | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementSummary) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EntitlementSummary: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "principalRole" in value:
        import capo_account_access.types.principal_role_entitlement_summary

        return {
            "principalRole": capo_account_access.types.principal_role_entitlement_summary.serialize_json(
                value["principalRole"]
            )
        }
    else:
        raise SerializationError("EntitlementSummary: no variant present")


def deserialize_json(data: dict) -> EntitlementSummary:
    if data.get("principalRole") is not None:
        import capo_account_access.types.principal_role_entitlement_summary

        return {
            "principalRole": capo_account_access.types.principal_role_entitlement_summary.deserialize_json(
                data["principalRole"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EntitlementSummary: no recognized variant key")
