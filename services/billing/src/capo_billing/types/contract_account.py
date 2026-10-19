"""Generated from Smithy shape ``com.amazonaws.billing#ContractAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.account_id


class ContractAccount(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The account ID.</p>"""
    is_gdn: "bool"
    """<p>When true, Support charges are calculated on charges before private discounts. When false, they are calculated after private discounts.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractAccount) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["isGdn"] = value["is_gdn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContractAccount:
    out: ContractAccount = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("isGdn") is not None:
        out["is_gdn"] = data["isGdn"]
    else:
        out["is_gdn"] = False
    return out
