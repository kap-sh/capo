"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateBrowserSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.browser_settings


class UpdateBrowserSettingsResponse(TypedDict, closed=True):
    browser_settings: "capo_workspaces_web.types.browser_settings.BrowserSettings"
    """<p>The browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrowserSettingsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.browser_settings

    out["browserSettings"] = capo_workspaces_web.types.browser_settings.serialize_json(
        value["browser_settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBrowserSettingsResponse:
    out: UpdateBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserSettings") is not None:
        import capo_workspaces_web.types.browser_settings

        out["browser_settings"] = (
            capo_workspaces_web.types.browser_settings.deserialize_json(
                data["browserSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateBrowserSettingsResponse.browser_settings required"
        )
    return out


def redact_sensitive(value: UpdateBrowserSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "browser_settings" in value:
        import capo_workspaces_web.types.browser_settings

        out["browser_settings"] = (
            capo_workspaces_web.types.browser_settings.redact_sensitive(
                value["browser_settings"]
            )
        )
    return out
