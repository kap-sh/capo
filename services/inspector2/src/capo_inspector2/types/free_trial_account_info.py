"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialAccountInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.free_trial_info_list
    import capo_inspector2.types.metering_account_id


class FreeTrialAccountInfo(TypedDict, closed=True):
    account_id: "capo_inspector2.types.metering_account_id.MeteringAccountId"
    """<p>The account associated with the Amazon Inspector free trial information.</p>"""
    free_trial_info: "capo_inspector2.types.free_trial_info_list.FreeTrialInfoList"
    """<p>Contains information about the Amazon Inspector free trial for an account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialAccountInfo) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_inspector2.types.free_trial_info_list

    out["freeTrialInfo"] = capo_inspector2.types.free_trial_info_list.serialize_json(
        value["free_trial_info"]
    )
    return out


def deserialize_json(data: dict) -> FreeTrialAccountInfo:
    out: FreeTrialAccountInfo = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("freeTrialInfo") is not None:
        import capo_inspector2.types.free_trial_info_list

        out["free_trial_info"] = (
            capo_inspector2.types.free_trial_info_list.deserialize_json(
                data["freeTrialInfo"]
            )
        )
    else:
        out["free_trial_info"] = []
    return out
