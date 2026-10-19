"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateAccountsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id_list
    import capo_billingconductor.types.billing_group_arn


class AssociateAccountsInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>"""
    account_ids: "capo_billingconductor.types.account_id_list.AccountIdList"
    """<p> The associating array of account IDs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAccountsInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_billingconductor.types.account_id_list

    out["AccountIds"] = capo_billingconductor.types.account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> AssociateAccountsInput:
    out: AssociateAccountsInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AccountIds") is not None:
        import capo_billingconductor.types.account_id_list

        out["account_ids"] = (
            capo_billingconductor.types.account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        out["account_ids"] = []
    return out
