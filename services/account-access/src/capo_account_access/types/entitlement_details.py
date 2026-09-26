"""Generated from Smithy shape ``com.amazonaws.accountaccess#EntitlementDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_account_access.types.principal_role_entitlement_details


class _EntitlementDetails_principalRole(TypedDict, closed=True):
    principalRole: "capo_account_access.types.principal_role_entitlement_details.PrincipalRoleEntitlementDetails"


EntitlementDetails: TypeAlias = _EntitlementDetails_principalRole


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementDetails) -> dict:
    if "principalRole" in value:
        import capo_account_access.types.principal_role_entitlement_details

        return {
            "principalRole": capo_account_access.types.principal_role_entitlement_details.serialize_json(
                value["principalRole"]
            )
        }
    else:
        raise SerializationError("EntitlementDetails: no variant present")


def deserialize_json(data: dict) -> EntitlementDetails:
    if data.get("principalRole") is not None:
        import capo_account_access.types.principal_role_entitlement_details

        return {
            "principalRole": capo_account_access.types.principal_role_entitlement_details.deserialize_json(
                data["principalRole"]
            )
        }
    else:
        raise DeserializationError("EntitlementDetails: no recognized variant key")
