"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentScheduleEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.charge_percentage
    import capo_marketplace_agreement.types.offset_duration


class PaymentScheduleEntry(TypedDict, closed=True):
    charge_date_offset: NotRequired[
        "capo_marketplace_agreement.types.offset_duration.OffsetDuration"
    ]
    """<p>The time between the start date of the renewed agreement and the date this installment is charged. The duration is represented in the ISO 8601 format in either whole months or whole days (for example, <code>P1M</code> for 1 month or <code>P30D</code> for 30 days). All installments in a schedule use the same unit.</p>"""
    charge_percentage: NotRequired[
        "capo_marketplace_agreement.types.charge_percentage.ChargePercentage"
    ]
    """<p>The percentage of the total contract value of the renewed agreement that is charged in this installment. Valid values range from <code>0.01</code> to <code>100.00</code>, with up to two decimal places.</p>"""
    day_of_month: NotRequired["int"]
    """<p>The day of the month on which this installment is charged, from <code>1</code> to <code>31</code>. Use this field to anchor the charge to a specific calendar day within the month identified by <code>ChargeDateOffset</code>. This field is supported only when <code>ChargeDateOffset</code> is expressed in months.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentScheduleEntry) -> dict:
    out: dict = {}
    if "charge_date_offset" in value:
        out["chargeDateOffset"] = value["charge_date_offset"]
    if "charge_percentage" in value:
        out["chargePercentage"] = value["charge_percentage"]
    if "day_of_month" in value:
        out["dayOfMonth"] = value["day_of_month"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PaymentScheduleEntry:
    out: PaymentScheduleEntry = {}  # type: ignore[typeddict-item]
    if data.get("chargeDateOffset") is not None:
        out["charge_date_offset"] = data["chargeDateOffset"]
    if data.get("chargePercentage") is not None:
        out["charge_percentage"] = data["chargePercentage"]
    if data.get("dayOfMonth") is not None:
        out["day_of_month"] = data["dayOfMonth"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentScheduleEntry) -> dict:
    out: dict = {}
    if "charge_date_offset" in value:
        out["chargeDateOffset"] = value["charge_date_offset"]
    if "charge_percentage" in value:
        out["chargePercentage"] = value["charge_percentage"]
    if "day_of_month" in value:
        out["dayOfMonth"] = value["day_of_month"]
    return out


def deserialize_cbor(data: dict) -> PaymentScheduleEntry:
    out: PaymentScheduleEntry = {}  # type: ignore[typeddict-item]
    if data.get("chargeDateOffset") is not None:
        out["charge_date_offset"] = data["chargeDateOffset"]
    if data.get("chargePercentage") is not None:
        out["charge_percentage"] = data["chargePercentage"]
    if data.get("dayOfMonth") is not None:
        out["day_of_month"] = data["dayOfMonth"]
    return out
