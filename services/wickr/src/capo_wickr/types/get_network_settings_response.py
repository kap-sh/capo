"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.settings_list


class GetNetworkSettingsResponse(TypedDict, closed=True):
    settings: "capo_wickr.types.settings_list.SettingsList"
    """<p>A list of network settings, where each setting includes a name, value, and type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkSettingsResponse) -> dict:
    out: dict = {}
    import capo_wickr.types.settings_list

    out["settings"] = capo_wickr.types.settings_list.serialize_json(value["settings"])
    return out


def deserialize_json(data: dict) -> GetNetworkSettingsResponse:
    out: GetNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_wickr.types.settings_list

        out["settings"] = capo_wickr.types.settings_list.deserialize_json(
            data["settings"]
        )
    else:
        out["settings"] = []
    return out
