"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.settings


class GetSettingsResponse(TypedDict, closed=True):
    settings: NotRequired["capo_auditmanager.types.settings.Settings"]
    """<p> The settings object that holds all supported Audit Manager settings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSettingsResponse) -> dict:
    out: dict = {}
    if "settings" in value:
        import capo_auditmanager.types.settings

        out["settings"] = capo_auditmanager.types.settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> GetSettingsResponse:
    out: GetSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_auditmanager.types.settings

        out["settings"] = capo_auditmanager.types.settings.deserialize_json(
            data["settings"]
        )
    return out


def redact_sensitive(value: GetSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "settings" in value:
        import capo_auditmanager.types.settings

        out["settings"] = capo_auditmanager.types.settings.redact_sensitive(
            value["settings"]
        )
    return out
