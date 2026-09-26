"""Generated from Smithy shape ``com.amazonaws.accountaccess#IdentitySource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_account_access.types.identity_center


class _IdentitySource_identityCenter(TypedDict, closed=True):
    identityCenter: "capo_account_access.types.identity_center.IdentityCenter"


IdentitySource: TypeAlias = _IdentitySource_identityCenter


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySource) -> dict:
    if "identityCenter" in value:
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
        raise DeserializationError("IdentitySource: no recognized variant key")
