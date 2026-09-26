"""Generated from Smithy shape ``com.amazonaws.accountaccess#PrincipalFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_account_access.types.identity_center_principal_filter


class _PrincipalFilter_identityCenter(TypedDict, closed=True):
    identityCenter: "capo_account_access.types.identity_center_principal_filter.IdentityCenterPrincipalFilter"


PrincipalFilter: TypeAlias = _PrincipalFilter_identityCenter


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalFilter) -> dict:
    if "identityCenter" in value:
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
        raise DeserializationError("PrincipalFilter: no recognized variant key")
