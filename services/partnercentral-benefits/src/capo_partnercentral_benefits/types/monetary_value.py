"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#MonetaryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.currency_code


class MonetaryValue(TypedDict, closed=True):
    amount: "str"
    """<p>The numeric amount of the monetary value.</p>"""
    currency_code: "capo_partnercentral_benefits.types.currency_code.CurrencyCode"
    """<p>The ISO 4217 currency code (e.g., USD, EUR) for the monetary amount.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonetaryValue) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import capo_partnercentral_benefits.types.currency_code

    out["CurrencyCode"] = (
        capo_partnercentral_benefits.types.currency_code.serialize_aws_json_1_0(
            value["currency_code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonetaryValue:
    out: MonetaryValue = {}  # type: ignore[typeddict-item]
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("CurrencyCode") is not None:
        import capo_partnercentral_benefits.types.currency_code

        out["currency_code"] = (
            capo_partnercentral_benefits.types.currency_code.deserialize_aws_json_1_0(
                data["CurrencyCode"]
            )
        )
    else:
        import typing

        out["currency_code"] = typing.cast(
            "capo_partnercentral_benefits.types.currency_code.CurrencyCode", ""
        )
    return out
