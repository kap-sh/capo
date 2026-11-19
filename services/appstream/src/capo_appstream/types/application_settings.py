"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.boolean
    import capo_appstream.types.settings_group


class ApplicationSettings(TypedDict, closed=True):
    enabled: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Enables or disables persistent application settings for users during their streaming sessions. </p>"""
    settings_group: NotRequired["capo_appstream.types.settings_group.SettingsGroup"]
    """<p>The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple stacks by specifying the same settings group for each stack. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSettings) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSettings:
    out: ApplicationSettings = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SettingsGroup") is not None:
        out["settings_group"] = data["SettingsGroup"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationSettings) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    return out


def deserialize_cbor(data: dict) -> ApplicationSettings:
    out: ApplicationSettings = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SettingsGroup") is not None:
        out["settings_group"] = data["SettingsGroup"]
    return out
