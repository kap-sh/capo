"""Generated from Smithy shape ``com.amazonaws.evs#PutAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.account_setting_list


class PutAccountSettingsRequest(TypedDict, closed=True):
    settings: "capo_evs.types.account_setting_list.AccountSettingList"
    """<p>A list of regional account-level EVS settings to create or update. Only the settings included in this list are modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAccountSettingsRequest) -> dict:
    out: dict = {}
    import capo_evs.types.account_setting_list

    out["settings"] = capo_evs.types.account_setting_list.serialize_aws_json_1_0(
        value["settings"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAccountSettingsRequest:
    out: PutAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("settings") is not None:
        import capo_evs.types.account_setting_list

        out["settings"] = capo_evs.types.account_setting_list.deserialize_aws_json_1_0(
            data["settings"]
        )
    else:
        out["settings"] = []
    return out
