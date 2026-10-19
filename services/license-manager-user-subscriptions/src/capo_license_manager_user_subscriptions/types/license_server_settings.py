"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseServerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.server_settings
    import capo_license_manager_user_subscriptions.types.server_type


class LicenseServerSettings(TypedDict, closed=True):
    server_type: "capo_license_manager_user_subscriptions.types.server_type.ServerType"
    """<p>The type of license server.</p>"""
    server_settings: (
        "capo_license_manager_user_subscriptions.types.server_settings.ServerSettings"
    )
    """<p>The <code>ServerSettings</code> resource contains the settings for your server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseServerSettings) -> dict:
    out: dict = {}
    out["ServerType"] = value["server_type"]
    import capo_license_manager_user_subscriptions.types.server_settings

    out["ServerSettings"] = (
        capo_license_manager_user_subscriptions.types.server_settings.serialize_json(
            value["server_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> LicenseServerSettings:
    out: LicenseServerSettings = {}  # type: ignore[typeddict-item]
    if data.get("ServerType") is not None:
        out["server_type"] = data["ServerType"]
    else:
        out["server_type"] = ""
    if data.get("ServerSettings") is not None:
        import capo_license_manager_user_subscriptions.types.server_settings

        out["server_settings"] = (
            capo_license_manager_user_subscriptions.types.server_settings.deserialize_json(
                data["ServerSettings"]
            )
        )
    else:
        import capo_license_manager_user_subscriptions.types._unknown

        out["server_settings"] = (
            capo_license_manager_user_subscriptions.types._unknown.UnknownUnionMember(
                ""
            )
        )
    return out
