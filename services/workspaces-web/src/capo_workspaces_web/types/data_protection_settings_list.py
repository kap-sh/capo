"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DataProtectionSettingsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.data_protection_settings_summary

DataProtectionSettingsList: TypeAlias = list[
    "capo_workspaces_web.types.data_protection_settings_summary.DataProtectionSettingsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProtectionSettingsList) -> list:
    import capo_workspaces_web.types.data_protection_settings_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.data_protection_settings_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataProtectionSettingsList:
    import capo_workspaces_web.types.data_protection_settings_summary

    out: DataProtectionSettingsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_web.types.data_protection_settings_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DataProtectionSettingsList) -> list[Any]:
    import capo_workspaces_web.types.data_protection_settings_summary

    return [
        capo_workspaces_web.types.data_protection_settings_summary.redact_sensitive(
            item
        )
        for item in value
    ]
