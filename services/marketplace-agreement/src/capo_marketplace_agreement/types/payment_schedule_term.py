"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentScheduleTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.schedule_list
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class PaymentScheduleTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Type of the term.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in the term. </p>"""
    schedule: NotRequired["capo_marketplace_agreement.types.schedule_list.ScheduleList"]
    """<p>List of the payment schedule where each element defines one installment of payment. It contains the information necessary for calculating the price.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentScheduleTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "schedule" in value:
        import capo_marketplace_agreement.types.schedule_list

        out["schedule"] = (
            capo_marketplace_agreement.types.schedule_list.serialize_aws_json_1_0(
                value["schedule"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PaymentScheduleTerm:
    out: PaymentScheduleTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("schedule") is not None:
        import capo_marketplace_agreement.types.schedule_list

        out["schedule"] = (
            capo_marketplace_agreement.types.schedule_list.deserialize_aws_json_1_0(
                data["schedule"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentScheduleTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "schedule" in value:
        import capo_marketplace_agreement.types.schedule_list

        out["schedule"] = capo_marketplace_agreement.types.schedule_list.serialize_cbor(
            value["schedule"]
        )
    return out


def deserialize_cbor(data: dict) -> PaymentScheduleTerm:
    out: PaymentScheduleTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("schedule") is not None:
        import capo_marketplace_agreement.types.schedule_list

        out["schedule"] = (
            capo_marketplace_agreement.types.schedule_list.deserialize_cbor(
                data["schedule"]
            )
        )
    return out
