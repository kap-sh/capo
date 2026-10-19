"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PaymentScheduleEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string


class PaymentScheduleEntry(TypedDict, closed=True):
    charge_date_offset: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The relative offset from the renewal agreement start date when this installment is due, represented in ISO 8601 duration format (for example, P1M or P30D).</p>"""
    charge_percentage: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The percentage of the increased Total Contract Value (TCV) to charge in this installment. All entries in a schedule sum to 100.00.</p>"""
    day_of_month: NotRequired["int"]
    """<p>The optional calendar day of month on which the charge occurs. When absent, the charge day is derived from <code>chargeDateOffset</code>. For months with fewer days than the specified day, the charge occurs on the last day of the month. For example, if <code>dayOfMonth</code> is 31, the charge in April occurs on April 30.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentScheduleEntry) -> dict:
    out: dict = {}
    out["chargeDateOffset"] = value["charge_date_offset"]
    out["chargePercentage"] = value["charge_percentage"]
    if "day_of_month" in value:
        out["dayOfMonth"] = value["day_of_month"]
    return out


def deserialize_json(data: dict) -> PaymentScheduleEntry:
    out: PaymentScheduleEntry = {}  # type: ignore[typeddict-item]
    if data.get("chargeDateOffset") is not None:
        out["charge_date_offset"] = data["chargeDateOffset"]
    else:
        out["charge_date_offset"] = ""
    if data.get("chargePercentage") is not None:
        out["charge_percentage"] = data["chargePercentage"]
    else:
        out["charge_percentage"] = ""
    if data.get("dayOfMonth") is not None:
        out["day_of_month"] = data["dayOfMonth"]
    return out
