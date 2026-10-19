"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeleteBillingGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_arn


class DeleteBillingGroupInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBillingGroupInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteBillingGroupInput:
    out: DeleteBillingGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
