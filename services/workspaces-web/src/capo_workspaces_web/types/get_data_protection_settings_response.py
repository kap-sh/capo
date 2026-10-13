"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.data_protection_settings


class GetDataProtectionSettingsResponse(TypedDict, closed=True):
    data_protection_settings: NotRequired[
        "capo_workspaces_web.types.data_protection_settings.DataProtectionSettings"
    ]
    """<p>The data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    if "data_protection_settings" in value:
        import capo_workspaces_web.types.data_protection_settings

        out["dataProtectionSettings"] = (
            capo_workspaces_web.types.data_protection_settings.serialize_json(
                value["data_protection_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataProtectionSettingsResponse:
    out: GetDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataProtectionSettings") is not None:
        import capo_workspaces_web.types.data_protection_settings

        out["data_protection_settings"] = (
            capo_workspaces_web.types.data_protection_settings.deserialize_json(
                data["dataProtectionSettings"]
            )
        )
    return out


def redact_sensitive(value: GetDataProtectionSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_protection_settings" in value:
        import capo_workspaces_web.types.data_protection_settings

        out["data_protection_settings"] = (
            capo_workspaces_web.types.data_protection_settings.redact_sensitive(
                value["data_protection_settings"]
            )
        )
    return out
