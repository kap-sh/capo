"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ScheduleItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_discovery.types.bounded_string


class ScheduleItem(TypedDict, closed=True):
    charge_date: "datetime.datetime"
    """<p>The date when the payment is due.</p>"""
    charge_amount: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The amount to be charged on the charge date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleItem) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types._prelude.timestamp

    out["chargeDate"] = (
        capo_marketplace_discovery.types._prelude.timestamp.serialize_json(
            value["charge_date"]
        )
    )
    out["chargeAmount"] = value["charge_amount"]
    return out


def deserialize_json(data: dict) -> ScheduleItem:
    out: ScheduleItem = {}  # type: ignore[typeddict-item]
    if data.get("chargeDate") is not None:
        import capo_marketplace_discovery.types._prelude.timestamp

        out["charge_date"] = (
            capo_marketplace_discovery.types._prelude.timestamp.deserialize_json(
                data["chargeDate"]
            )
        )
    else:
        import datetime

        out["charge_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("chargeAmount") is not None:
        out["charge_amount"] = data["chargeAmount"]
    else:
        out["charge_amount"] = ""
    return out
