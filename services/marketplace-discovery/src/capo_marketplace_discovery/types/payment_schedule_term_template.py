"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PaymentScheduleTermTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.payment_schedule_entry_list


class PaymentScheduleTermTemplate(TypedDict, closed=True):
    schedule: "capo_marketplace_discovery.types.payment_schedule_entry_list.PaymentScheduleEntryList"
    """<p>An ordered list of installment entries for the renewal payment schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentScheduleTermTemplate) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.payment_schedule_entry_list

    out["schedule"] = (
        capo_marketplace_discovery.types.payment_schedule_entry_list.serialize_json(
            value["schedule"]
        )
    )
    return out


def deserialize_json(data: dict) -> PaymentScheduleTermTemplate:
    out: PaymentScheduleTermTemplate = {}  # type: ignore[typeddict-item]
    if data.get("schedule") is not None:
        import capo_marketplace_discovery.types.payment_schedule_entry_list

        out["schedule"] = (
            capo_marketplace_discovery.types.payment_schedule_entry_list.deserialize_json(
                data["schedule"]
            )
        )
    else:
        out["schedule"] = []
    return out
