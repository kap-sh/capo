"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_list
    import capo_inspector2.types.failed_account_list


class EnableResponse(TypedDict, closed=True):
    accounts: "capo_inspector2.types.account_list.AccountList"
    """<p>Information on the accounts that have had Amazon Inspector scans successfully enabled. Details are provided for each account.</p>"""
    failed_accounts: NotRequired[
        "capo_inspector2.types.failed_account_list.FailedAccountList"
    ]
    """<p>Information on any accounts for which Amazon Inspector scans could not be enabled. Details are provided for each account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.account_list

    out["accounts"] = capo_inspector2.types.account_list.serialize_json(
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


def deserialize_json(data: dict) -> EnableResponse:
    out: EnableResponse = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_inspector2.types.account_list

        out["accounts"] = capo_inspector2.types.account_list.deserialize_json(
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
