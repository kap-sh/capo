"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetUserSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.user_settings


class GetUserSettingsResponse(TypedDict, closed=True):
    user_settings: NotRequired["capo_workspaces_web.types.user_settings.UserSettings"]
    """<p>The user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserSettingsResponse) -> dict:
    out: dict = {}
    if "user_settings" in value:
        import capo_workspaces_web.types.user_settings

        out["userSettings"] = capo_workspaces_web.types.user_settings.serialize_json(
            value["user_settings"]
        )
    return out


def deserialize_json(data: dict) -> GetUserSettingsResponse:
    out: GetUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("userSettings") is not None:
        import capo_workspaces_web.types.user_settings

        out["user_settings"] = capo_workspaces_web.types.user_settings.deserialize_json(
            data["userSettings"]
        )
    return out


def redact_sensitive(value: GetUserSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_settings" in value:
        import capo_workspaces_web.types.user_settings

        out["user_settings"] = capo_workspaces_web.types.user_settings.redact_sensitive(
            value["user_settings"]
        )
    return out
