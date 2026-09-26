"""Generated from Smithy shape ``com.amazonaws.accountaccess#IdentitySourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_account_access.types.identity_center_details


class _IdentitySourceDetails_identityCenter(TypedDict, closed=True):
    identityCenter: (
        "capo_account_access.types.identity_center_details.IdentityCenterDetails"
    )


IdentitySourceDetails: TypeAlias = _IdentitySourceDetails_identityCenter


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceDetails) -> dict:
    if "identityCenter" in value:
        import capo_account_access.types.identity_center_details

        return {
            "identityCenter": capo_account_access.types.identity_center_details.serialize_json(
                value["identityCenter"]
            )
        }
    else:
        raise SerializationError("IdentitySourceDetails: no variant present")


def deserialize_json(data: dict) -> IdentitySourceDetails:
    if data.get("identityCenter") is not None:
        import capo_account_access.types.identity_center_details

        return {
            "identityCenter": capo_account_access.types.identity_center_details.deserialize_json(
                data["identityCenter"]
            )
        }
    else:
        raise DeserializationError("IdentitySourceDetails: no recognized variant key")
