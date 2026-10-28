"""Generated from Smithy shape ``com.amazonaws.accountaccess#IdentitySource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError
from capo_account_access.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access.types.identity_center


class IdentitySourceIdentityCenterMember(TypedDict, closed=True):
    identityCenter: "capo_account_access.types.identity_center.IdentityCenter"


IdentitySource: TypeAlias = IdentitySourceIdentityCenterMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IdentitySource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "identityCenter" in value:
        import capo_account_access.types.identity_center

        return {
            "identityCenter": capo_account_access.types.identity_center.serialize_json(
                value["identityCenter"]
            )
        }
    else:
        raise SerializationError("IdentitySource: no variant present")


def deserialize_json(data: dict) -> IdentitySource:
    if data.get("identityCenter") is not None:
        import capo_account_access.types.identity_center

        return {
            "identityCenter": capo_account_access.types.identity_center.deserialize_json(
                data["identityCenter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IdentitySource: no recognized variant key")
