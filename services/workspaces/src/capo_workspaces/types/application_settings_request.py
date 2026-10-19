"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.application_settings_status_enum
    import capo_workspaces.types.settings_group


class ApplicationSettingsRequest(TypedDict, closed=True):
    status: "capo_workspaces.types.application_settings_status_enum.ApplicationSettingsStatusEnum"
    """<p>Enables or disables persistent application settings for users during their pool sessions.</p>"""
    settings_group: NotRequired["capo_workspaces.types.settings_group.SettingsGroup"]
    """<p>The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple pools by specifying the same settings group for each pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSettingsRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.application_settings_status_enum

    out["Status"] = (
        capo_workspaces.types.application_settings_status_enum.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSettingsRequest:
    out: ApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_workspaces.types.application_settings_status_enum

        out["status"] = (
            capo_workspaces.types.application_settings_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_workspaces.types.application_settings_status_enum.ApplicationSettingsStatusEnum",
            "",
        )
    if data.get("SettingsGroup") is not None:
        out["settings_group"] = data["SettingsGroup"]
    return out
