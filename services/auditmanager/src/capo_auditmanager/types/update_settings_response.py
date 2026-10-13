"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.settings


class UpdateSettingsResponse(TypedDict, closed=True):
    settings: NotRequired["capo_auditmanager.types.settings.Settings"]
    """<p> The current list of settings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSettingsResponse) -> dict:
    out: dict = {}
    if "settings" in value:
        import capo_auditmanager.types.settings

        out["settings"] = capo_auditmanager.types.settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSettingsResponse:
    out: UpdateSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_auditmanager.types.settings

        out["settings"] = capo_auditmanager.types.settings.deserialize_json(
            data["settings"]
        )
    return out


def redact_sensitive(value: UpdateSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "settings" in value:
        import capo_auditmanager.types.settings

        out["settings"] = capo_auditmanager.types.settings.redact_sensitive(
            value["settings"]
        )
    return out
