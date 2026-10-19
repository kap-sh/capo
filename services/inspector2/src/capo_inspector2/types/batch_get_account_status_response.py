"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetAccountStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_state_list
    import capo_inspector2.types.failed_account_list


class BatchGetAccountStatusResponse(TypedDict, closed=True):
    accounts: "capo_inspector2.types.account_state_list.AccountStateList"
    """<p>An array of objects that provide details on the status of Amazon Inspector for each of the requested accounts.</p>"""
    failed_accounts: NotRequired[
        "capo_inspector2.types.failed_account_list.FailedAccountList"
    ]
    """<p>An array of objects detailing any accounts that failed to enable Amazon Inspector and why.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAccountStatusResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.account_state_list

    out["accounts"] = capo_inspector2.types.account_state_list.serialize_json(
        value["accounts"]
    )
    if "failed_accounts" in value:
        import capo_inspector2.types.failed_account_list

        out["failedAccounts"] = (
            capo_inspector2.types.failed_account_list.serialize_json(
                value["failed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAccountStatusResponse:
    out: BatchGetAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_inspector2.types.account_state_list

        out["accounts"] = capo_inspector2.types.account_state_list.deserialize_json(
            data["accounts"]
        )
    else:
        out["accounts"] = []
    if data.get("failedAccounts") is not None:
        import capo_inspector2.types.failed_account_list

        out["failed_accounts"] = (
            capo_inspector2.types.failed_account_list.deserialize_json(
                data["failedAccounts"]
            )
        )
    return out
