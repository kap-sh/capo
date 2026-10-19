"""Generated from Smithy shape ``com.amazonaws.account#GetGovCloudAccountInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.aws_account_state


class GetGovCloudAccountInformationResponse(TypedDict, closed=True):
    gov_cloud_account_id: "capo_account.types.account_id.AccountId"
    """<p>The 12-digit account ID number of the linked GovCloud account.</p>"""
    account_state: "capo_account.types.aws_account_state.AwsAccountState"
    """<p>The account state of the linked GovCloud account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGovCloudAccountInformationResponse) -> dict:
    out: dict = {}
    out["GovCloudAccountId"] = value["gov_cloud_account_id"]
    out["AccountState"] = value["account_state"]
    return out


def deserialize_json(data: dict) -> GetGovCloudAccountInformationResponse:
    out: GetGovCloudAccountInformationResponse = {}  # type: ignore[typeddict-item]
    if data.get("GovCloudAccountId") is not None:
        out["gov_cloud_account_id"] = data["GovCloudAccountId"]
    else:
        out["gov_cloud_account_id"] = ""
    if data.get("AccountState") is not None:
        out["account_state"] = data["AccountState"]
    else:
        out["account_state"] = ""
    return out
