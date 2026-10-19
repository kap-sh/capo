"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#VariablePaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.currency_code
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class VariablePaymentTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "capo_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    max_total_charge_amount: (
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    )
    """<p>The maximum total amount that can be charged under this term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariablePaymentTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    out["maxTotalChargeAmount"] = value["max_total_charge_amount"]
    return out


def deserialize_json(data: dict) -> VariablePaymentTerm:
    out: VariablePaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_marketplace_discovery.types.term_type.TermType", ""
        )
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    else:
        out["currency_code"] = ""
    if data.get("maxTotalChargeAmount") is not None:
        out["max_total_charge_amount"] = data["maxTotalChargeAmount"]
    else:
        out["max_total_charge_amount"] = ""
    return out
