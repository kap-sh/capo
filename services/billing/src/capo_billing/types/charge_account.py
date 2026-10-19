"""Generated from Smithy shape ``com.amazonaws.billing#ChargeAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.account_id


class ChargeAccount(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The account ID.</p>"""
    charge_percentage: "str"
    """<p>The percentage of the total Support charge allocated to this account. This is 0.0 when supportAllocationMethod = Proportional.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChargeAccount) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["chargePercentage"] = value["charge_percentage"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ChargeAccount:
    out: ChargeAccount = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("chargePercentage") is not None:
        out["charge_percentage"] = data["chargePercentage"]
    else:
        out["charge_percentage"] = ""
    return out
