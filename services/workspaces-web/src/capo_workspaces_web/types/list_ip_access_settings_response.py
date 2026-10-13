"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.ip_access_settings_list
    import capo_workspaces_web.types.pagination_token


class ListIpAccessSettingsResponse(TypedDict, closed=True):
    ip_access_settings: NotRequired[
        "capo_workspaces_web.types.ip_access_settings_list.IpAccessSettingsList"
    ]
    """<p>The IP access settings.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIpAccessSettingsResponse) -> dict:
    out: dict = {}
    if "ip_access_settings" in value:
        import capo_workspaces_web.types.ip_access_settings_list

        out["ipAccessSettings"] = (
            capo_workspaces_web.types.ip_access_settings_list.serialize_json(
                value["ip_access_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIpAccessSettingsResponse:
    out: ListIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ipAccessSettings") is not None:
        import capo_workspaces_web.types.ip_access_settings_list

        out["ip_access_settings"] = (
            capo_workspaces_web.types.ip_access_settings_list.deserialize_json(
                data["ipAccessSettings"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListIpAccessSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_access_settings" in value:
        import capo_workspaces_web.types.ip_access_settings_list

        out["ip_access_settings"] = (
            capo_workspaces_web.types.ip_access_settings_list.redact_sensitive(
                value["ip_access_settings"]
            )
        )
    return out
