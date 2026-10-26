"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ServerSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_license_manager_user_subscriptions.errors import (
    DeserializationError,
    SerializationError,
)
from capo_license_manager_user_subscriptions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.rds_sal_settings


class _ServerSettings_RdsSalSettings(TypedDict, closed=True):
    RdsSalSettings: (
        "capo_license_manager_user_subscriptions.types.rds_sal_settings.RdsSalSettings"
    )


ServerSettings: TypeAlias = _ServerSettings_RdsSalSettings | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ServerSettings) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ServerSettings: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RdsSalSettings" in value:
        import capo_license_manager_user_subscriptions.types.rds_sal_settings

        return {
            "RdsSalSettings": capo_license_manager_user_subscriptions.types.rds_sal_settings.serialize_json(
                value["RdsSalSettings"]
            )
        }
    else:
        raise SerializationError("ServerSettings: no variant present")


def deserialize_json(data: dict) -> ServerSettings:
    if data.get("RdsSalSettings") is not None:
        import capo_license_manager_user_subscriptions.types.rds_sal_settings

        return {
            "RdsSalSettings": capo_license_manager_user_subscriptions.types.rds_sal_settings.deserialize_json(
                data["RdsSalSettings"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ServerSettings: no recognized variant key")
