"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IdentityProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_license_manager_user_subscriptions.errors import (
    DeserializationError,
    SerializationError,
)
from capo_license_manager_user_subscriptions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.active_directory_identity_provider


class _IdentityProvider_ActiveDirectoryIdentityProvider(TypedDict, closed=True):
    ActiveDirectoryIdentityProvider: "capo_license_manager_user_subscriptions.types.active_directory_identity_provider.ActiveDirectoryIdentityProvider"


IdentityProvider: TypeAlias = (
    _IdentityProvider_ActiveDirectoryIdentityProvider | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProvider) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IdentityProvider: cannot serialize unknown variant {value.name!r}"
        )
    elif "ActiveDirectoryIdentityProvider" in value:
        import capo_license_manager_user_subscriptions.types.active_directory_identity_provider

        return {
            "ActiveDirectoryIdentityProvider": capo_license_manager_user_subscriptions.types.active_directory_identity_provider.serialize_json(
                value["ActiveDirectoryIdentityProvider"]
            )
        }
    else:
        raise SerializationError("IdentityProvider: no variant present")


def deserialize_json(data: dict) -> IdentityProvider:
    if data.get("ActiveDirectoryIdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.active_directory_identity_provider

        return {
            "ActiveDirectoryIdentityProvider": capo_license_manager_user_subscriptions.types.active_directory_identity_provider.deserialize_json(
                data["ActiveDirectoryIdentityProvider"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IdentityProvider: no recognized variant key")
