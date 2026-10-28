"""Generated from Smithy shape ``com.amazonaws.accountaccess#PrincipalFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError
from capo_account_access.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access.types.identity_center_principal_filter


class PrincipalFilterIdentityCenterMember(TypedDict, closed=True):
    identityCenter: "capo_account_access.types.identity_center_principal_filter.IdentityCenterPrincipalFilter"


PrincipalFilter: TypeAlias = PrincipalFilterIdentityCenterMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrincipalFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "identityCenter" in value:
        import capo_account_access.types.identity_center_principal_filter

        return {
            "identityCenter": capo_account_access.types.identity_center_principal_filter.serialize_json(
                value["identityCenter"]
            )
        }
    else:
        raise SerializationError("PrincipalFilter: no variant present")


def deserialize_json(data: dict) -> PrincipalFilter:
    if data.get("identityCenter") is not None:
        import capo_account_access.types.identity_center_principal_filter

        return {
            "identityCenter": capo_account_access.types.identity_center_principal_filter.deserialize_json(
                data["identityCenter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PrincipalFilter: no recognized variant key")
