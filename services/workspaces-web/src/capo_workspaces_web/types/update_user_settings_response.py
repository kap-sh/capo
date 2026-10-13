"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateUserSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.user_settings


class UpdateUserSettingsResponse(TypedDict, closed=True):
    user_settings: "capo_workspaces_web.types.user_settings.UserSettings"
    """<p>The user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserSettingsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.user_settings

    out["userSettings"] = capo_workspaces_web.types.user_settings.serialize_json(
        value["user_settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserSettingsResponse:
    out: UpdateUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("userSettings") is not None:
        import capo_workspaces_web.types.user_settings

        out["user_settings"] = capo_workspaces_web.types.user_settings.deserialize_json(
            data["userSettings"]
        )
    else:
        raise DeserializationError("UpdateUserSettingsResponse.user_settings required")
    return out


def redact_sensitive(value: UpdateUserSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_settings" in value:
        import capo_workspaces_web.types.user_settings

        out["user_settings"] = capo_workspaces_web.types.user_settings.redact_sensitive(
            value["user_settings"]
        )
    return out
