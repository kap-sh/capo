"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListUserSettingsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.user_settings_list


class ListUserSettingsResponse(TypedDict, closed=True):
    user_settings: NotRequired[
        "capo_workspaces_web.types.user_settings_list.UserSettingsList"
    ]
    """<p>The user settings.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserSettingsResponse) -> dict:
    out: dict = {}
    if "user_settings" in value:
        import capo_workspaces_web.types.user_settings_list

        out["userSettings"] = (
            capo_workspaces_web.types.user_settings_list.serialize_json(
                value["user_settings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserSettingsResponse:
    out: ListUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("userSettings") is not None:
        import capo_workspaces_web.types.user_settings_list

        out["user_settings"] = (
            capo_workspaces_web.types.user_settings_list.deserialize_json(
                data["userSettings"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListUserSettingsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_settings" in value:
        import capo_workspaces_web.types.user_settings_list

        out["user_settings"] = (
            capo_workspaces_web.types.user_settings_list.redact_sensitive(
                value["user_settings"]
            )
        )
    return out
