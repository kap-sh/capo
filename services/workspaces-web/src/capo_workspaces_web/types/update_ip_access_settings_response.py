"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.ip_access_settings


class UpdateIpAccessSettingsResponse(TypedDict, closed=True):
    ip_access_settings: "capo_workspaces_web.types.ip_access_settings.IpAccessSettings"
    """<p>The IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpAccessSettingsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.ip_access_settings

    out["ipAccessSettings"] = (
        capo_workspaces_web.types.ip_access_settings.serialize_json(
            value["ip_access_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIpAccessSettingsResponse:
    out: UpdateIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ipAccessSettings") is not None:
        import capo_workspaces_web.types.ip_access_settings

        out["ip_access_settings"] = (
            capo_workspaces_web.types.ip_access_settings.deserialize_json(
                data["ipAccessSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIpAccessSettingsResponse.ip_access_settings required"
        )
    return out


def redact_sensitive(value: UpdateIpAccessSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_access_settings" in value:
        import capo_workspaces_web.types.ip_access_settings

        out["ip_access_settings"] = (
            capo_workspaces_web.types.ip_access_settings.redact_sensitive(
                value["ip_access_settings"]
            )
        )
    return out
