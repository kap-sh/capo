"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentScheduleTermTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.payment_schedule_entry_list


class PaymentScheduleTermTemplate(TypedDict, closed=True):
    schedule: NotRequired[
        "capo_marketplace_agreement.types.payment_schedule_entry_list.PaymentScheduleEntryList"
    ]
    """<p>The installments that make up the payment schedule of the renewed agreement. The <code>ChargePercentage</code> values of all installments add up to <code>100</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentScheduleTermTemplate) -> dict:
    out: dict = {}
    if "schedule" in value:
        import capo_marketplace_agreement.types.payment_schedule_entry_list

        out["schedule"] = (
            capo_marketplace_agreement.types.payment_schedule_entry_list.serialize_aws_json_1_0(
                value["schedule"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PaymentScheduleTermTemplate:
    out: PaymentScheduleTermTemplate = {}  # type: ignore[typeddict-item]
    if data.get("schedule") is not None:
        import capo_marketplace_agreement.types.payment_schedule_entry_list

        out["schedule"] = (
            capo_marketplace_agreement.types.payment_schedule_entry_list.deserialize_aws_json_1_0(
                data["schedule"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentScheduleTermTemplate) -> dict:
    out: dict = {}
    if "schedule" in value:
        import capo_marketplace_agreement.types.payment_schedule_entry_list

        out["schedule"] = (
            capo_marketplace_agreement.types.payment_schedule_entry_list.serialize_cbor(
                value["schedule"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PaymentScheduleTermTemplate:
    out: PaymentScheduleTermTemplate = {}  # type: ignore[typeddict-item]
    if data.get("schedule") is not None:
        import capo_marketplace_agreement.types.payment_schedule_entry_list

        out["schedule"] = (
            capo_marketplace_agreement.types.payment_schedule_entry_list.deserialize_cbor(
                data["schedule"]
            )
        )
    return out
