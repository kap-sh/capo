"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetFreeTrialInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.free_trial_account_info_list
    import capo_inspector2.types.free_trial_info_error_list


class BatchGetFreeTrialInfoResponse(TypedDict, closed=True):
    accounts: (
        "capo_inspector2.types.free_trial_account_info_list.FreeTrialAccountInfoList"
    )
    """<p>An array of objects that provide Amazon Inspector free trial details for each of the requested accounts. </p>"""
    failed_accounts: (
        "capo_inspector2.types.free_trial_info_error_list.FreeTrialInfoErrorList"
    )
    """<p>An array of objects detailing any accounts that free trial data could not be returned for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFreeTrialInfoResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.free_trial_account_info_list

    out["accounts"] = capo_inspector2.types.free_trial_account_info_list.serialize_json(
        value["accounts"]
    )
    import capo_inspector2.types.free_trial_info_error_list

    out["failedAccounts"] = (
        capo_inspector2.types.free_trial_info_error_list.serialize_json(
            value["failed_accounts"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFreeTrialInfoResponse:
    out: BatchGetFreeTrialInfoResponse = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_inspector2.types.free_trial_account_info_list

        out["accounts"] = (
            capo_inspector2.types.free_trial_account_info_list.deserialize_json(
                data["accounts"]
            )
        )
    else:
        out["accounts"] = []
    if data.get("failedAccounts") is not None:
        import capo_inspector2.types.free_trial_info_error_list

        out["failed_accounts"] = (
            capo_inspector2.types.free_trial_info_error_list.deserialize_json(
                data["failedAccounts"]
            )
        )
    else:
        out["failed_accounts"] = []
    return out
