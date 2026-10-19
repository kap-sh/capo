"""Generated from Smithy shape ``com.amazonaws.accountaccess#Principal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError
from capo_account_access.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access.types.identity_center_principal


class _Principal_identityCenter(TypedDict, closed=True):
    identityCenter: (
        "capo_account_access.types.identity_center_principal.IdentityCenterPrincipal"
    )


Principal: TypeAlias = _Principal_identityCenter | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Principal) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Principal: cannot serialize unknown variant {value.name!r}"
        )
    elif "identityCenter" in value:
        import capo_account_access.types.identity_center_principal

        return {
            "identityCenter": capo_account_access.types.identity_center_principal.serialize_json(
                value["identityCenter"]
            )
        }
    else:
        raise SerializationError("Principal: no variant present")


def deserialize_json(data: dict) -> Principal:
    if data.get("identityCenter") is not None:
        import capo_account_access.types.identity_center_principal

        return {
            "identityCenter": capo_account_access.types.identity_center_principal.deserialize_json(
                data["identityCenter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Principal: no recognized variant key")
