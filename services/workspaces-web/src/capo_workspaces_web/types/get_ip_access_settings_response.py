"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.ip_access_settings


class GetIpAccessSettingsResponse(TypedDict, closed=True):
    ip_access_settings: NotRequired[
        "capo_workspaces_web.types.ip_access_settings.IpAccessSettings"
    ]
    """<p>The IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIpAccessSettingsResponse) -> dict:
    out: dict = {}
    if "ip_access_settings" in value:
        import capo_workspaces_web.types.ip_access_settings

        out["ipAccessSettings"] = (
            capo_workspaces_web.types.ip_access_settings.serialize_json(
                value["ip_access_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIpAccessSettingsResponse:
    out: GetIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ipAccessSettings") is not None:
        import capo_workspaces_web.types.ip_access_settings

        out["ip_access_settings"] = (
            capo_workspaces_web.types.ip_access_settings.deserialize_json(
                data["ipAccessSettings"]
            )
        )
    return out


def redact_sensitive(value: GetIpAccessSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_access_settings" in value:
        import capo_workspaces_web.types.ip_access_settings

        out["ip_access_settings"] = (
            capo_workspaces_web.types.ip_access_settings.redact_sensitive(
                value["ip_access_settings"]
            )
        )
    return out
