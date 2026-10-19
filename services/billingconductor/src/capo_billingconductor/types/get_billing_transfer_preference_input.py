"""Generated from Smithy shape ``com.amazonaws.billingconductor#GetBillingTransferPreferenceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.responsibility_transfer_arn


class GetBillingTransferPreferenceInput(TypedDict, closed=True):
    responsibility_transfer_arn: "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    """<p>The Amazon Resource Name (ARN) of the billing transfer whose preference you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBillingTransferPreferenceInput) -> dict:
    out: dict = {}
    out["ResponsibilityTransferArn"] = value["responsibility_transfer_arn"]
    return out


def deserialize_json(data: dict) -> GetBillingTransferPreferenceInput:
    out: GetBillingTransferPreferenceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResponsibilityTransferArn") is not None:
        out["responsibility_transfer_arn"] = data["ResponsibilityTransferArn"]
    else:
        out["responsibility_transfer_arn"] = ""
    return out
