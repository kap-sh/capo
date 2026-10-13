"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserSettingsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.user_settings_summary

UserSettingsList: TypeAlias = list[
    "capo_workspaces_web.types.user_settings_summary.UserSettingsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserSettingsList) -> list:
    import capo_workspaces_web.types.user_settings_summary

    out: list = []
    for item in value:
        out.append(capo_workspaces_web.types.user_settings_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserSettingsList:
    import capo_workspaces_web.types.user_settings_summary

    out: UserSettingsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_web.types.user_settings_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: UserSettingsList) -> list[Any]:
    import capo_workspaces_web.types.user_settings_summary

    return [
        capo_workspaces_web.types.user_settings_summary.redact_sensitive(item)
        for item in value
    ]
